# hw2
[compiler HW2.pdf](../../assets/pdf/compiler_HW2.pdf)

```haskell
open Ast
open Format

(* Exception raised to signal a runtime error *)
exception Error of string
let error s = raise (Error s)

(* Values of Mini-Python.

   Two main differences wrt Python:

   - We use here machine integers (OCaml type `int`) while Python
     integers are arbitrary-precision integers (we could use an OCaml
     library for big integers, such as zarith, but we opt for simplicity
     here).

   - What Python calls a ``list'' is a resizeable array. In Mini-Python,
     there is no way to modify the length, so a mere OCaml array can be used.
*)
type value =
  | Vnone
  | Vbool of bool
  | Vint of int
  | Vstring of string
  | Vlist of value array

(* Print a value on standard output *)
let rec print_value = function
  | Vnone -> printf "None"
  | Vbool true -> printf "True"
  | Vbool false -> printf "False"
  | Vint n -> printf "%d" n
  | Vstring s -> printf "%s" s
  | Vlist a ->
    let n = Array.length a in
    printf "[";
    for i = 0 to n-1 do print_value a.(i); if i < n-1 then printf ", " done;
    printf "]"

(* Boolean interpretation of a value

   In Python, any value can be used as a Boolean: None, the integer 0,
   the empty string, and the empty list are all considered to be
   False, and any other value to be True.
*)
let is_false v = match v with 
  | Vnone
  | Vbool false
  | Vstring ""
  | Vlist [||] -> true
  | Vint n -> n = 0
  | _ -> false

let is_true v = not (is_false v)

(* We only have global functions in Mini-Python *)

let functions = (Hashtbl.create 16 : (string, ident list * stmt) Hashtbl.t)

(* The following exception is used to interpret `return` *)

exception Return of value

(* Local variables (function parameters and local variables introduced
   by assignments) are stored in a hash table that is passed to the
   following OCaml functions as parameter `ctx`. *)

type ctx = (string, value) Hashtbl.t

(* Interpreting an expression (returns a value) *)
let compare op n1 n2 = match n1 , n2 with 
    | int ,_->
        match op with
        | Beq -> n1 = n2
        | Bneq -> n1 <> n2
        | Blt -> n1 < n2
        | Ble -> n1 <= n2
        | Bgt -> n1 > n2
        | Bge -> n1 >= n2
        | _ -> raise (Error "unsupported operand types")
let rec expr ctx = function
  | Ecst Cnone ->
      Vnone
  | Ecst (Cbool b) ->
      Vbool(b)
  | Ecst (Cstring s) ->
      Vstring s
  | Ecst (Cint n) ->
      Vint (Int64.to_int n)
  (* arithmetic *)
  | Ebinop (Badd | Bsub | Bmul | Bdiv | Bmod |
            Beq | Bneq | Blt | Ble | Bgt | Bge as op, e1, e2) ->
      let v1 = expr ctx e1 in
      let v2 = expr ctx e2 in
      begin match op, v1, v2 with
        (* int *)
        | Badd, Vint n1, Vint n2 -> Vint (n1 + n2)
        | Bsub, Vint n1, Vint n2 -> Vint (n1 - n2)
        | Bmul, Vint n1, Vint n2 -> Vint (n1 * n2)
        | Bdiv, Vint n1, Vint n2 -> Vint (n1 / n2)
        | Bmod, Vint n1, Vint n2 -> Vint (n1 mod n2)

        (* string *)
        | Badd, Vstring n1, Vstring n2 -> Vstring (String.cat n1 n2)

        (* bool *)
        | Beq, _, _  -> Vbool (compare Beq v1 v2)
        | Bneq, _, _  -> Vbool (compare Bneq v1 v2)
        | Blt, _, _  -> Vbool (compare Blt v1 v2)
        | Ble, _, _  -> Vbool (compare Ble v1 v2)
        | Bgt, _, _  -> Vbool (compare Bgt v1 v2)
        | Bge, _, _  -> Vbool (compare Bge v1 v2)
        (*
        | Badd, Vlist l1, Vlist l2 ->
            assert false (* TODO (question 5) *)
        *)
        | _ -> error "unsupported operand types"
      end
  | Eunop (Uneg, e1) ->
    Vint ( match expr ctx e1 with
      | Vint v -> - v
      | _ -> error "unsupported operand type")
  (* Boolean *)
  | Ebinop (Band, e1, e2) -> 
      let v1 = expr ctx e1 in
      if is_true v1 
        then expr ctx e2 
      else v1

  | Ebinop (Bor, e1, e2) ->
      let v1 = expr ctx e1 in
      if is_true v1 
        then v1
      else 
        expr ctx e2
  | Eunop (Unot, e1) ->
    Vbool ( match expr ctx e1 with
      | Vbool b -> not b
      | _ -> error "unsupported operand type in 'not'")
  | Eident {id} ->
    Hashtbl.find ctx id
  (* function call *)
  | Ecall ({id="len"}, [e1]) ->
      begin match expr ctx e1 with
        | Vstring s -> Vint (String.length s)
        | Vlist l -> Vint (Array.length l)
        | _ -> error "this value has no 'len'" end
  | Ecall ({id="list"}, [Ecall ({id="range"}, [e1])]) ->
    let n = expr ctx e1 in
    Vlist (match n with
      | Vint n -> Array.init n (fun i -> Vint i)
      | _ -> error "unsupported operand type in 'list'")
  | Ecall ({id=f}, el) ->
      if not (Hashtbl.mem functions f) then error ("unbound function " ^ f);
      let args, body = Hashtbl.find functions f in
      if List.length args <> List.length el then error "bad arity";
      let ctx' = Hashtbl.create 16 in
      List.iter2 (fun {id=x} e -> Hashtbl.add ctx' x (expr ctx e)) args el;
      begin try stmt ctx' body; Vnone with Return v -> v end
  | Elist el ->
      Vlist (Array.of_list (List.map (expr ctx) el))
  | Eget (e1, e2) ->
    match expr ctx e2 with
    | Vint i -> 
      begin match expr ctx e1 with
        | Vlist l -> 
          if i < 0 || i >= Array.length l then error "index out of bounds"
          else l.(i)
        | _ -> error "list expected" end
    | _ -> error "integer expected"

(* Interpreting a statement
   returns nothing but may raise exception `Return` *)
  
and expr_int ctx e = match expr ctx e with
  | Vbool false -> 0
  | Vbool true -> 1
  | Vint n -> n
  | _ -> error "integer expected"

and stmt ctx = function
  | Seval e ->
      ignore (expr ctx e)
  | Sprint e ->
      print_value (expr ctx e); printf "@."
  | Sblock bl ->
      block ctx bl
  | Sif (e, s1, s2) ->
    if  is_true(expr ctx e) then
        stmt ctx s1
    else 
        stmt ctx s2
  | Sassign ({id}, e1) ->
      Hashtbl.replace ctx id (expr ctx e1)
  | Sreturn e ->
      raise (Return (expr ctx e))
  | Sfor ({id=x}, e, s) ->
      begin match expr ctx e with
      | Vlist l ->
        Array.iter (fun v -> Hashtbl.replace ctx x v; stmt ctx s) l
      | _ -> error "list expected" end
  | Sset (e1, e2, e3) ->
      match expr ctx e1 with
      | Vlist l -> 
        let index= expr_int ctx e2 in
         l.(index)<- expr ctx e3
      | _ -> error "list expected"

(* Interpreting a block (a sequence of statements) *)

and block ctx = function
  | [] -> ()
  | s :: sl -> stmt ctx s; block ctx sl

(* Interpreting a file
   - `dl` is a list of function definitions (see type `def` in ast.ml)
   - `s` is a statement (the toplevel code)
*)

let file (dl, s) =
  List.iter
    (fun (f,args,body) -> Hashtbl.add functions f.id (args, body)) dl;
  stmt (Hashtbl.create 16) s

```