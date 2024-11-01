# hw3


[compiler HW3.pdf](../../assets/pdf/compiler_HW3.pdf)

## run.sh

```bash
ocaml HW3.ml
dot -Tpdf autom2.dot > autom.pdf && firefox autom.pdf 
ocamlopt a.ml lexer.ml && ./a.out
```
## hw3
```haskell

type ichar = char * int
type regexp =
| Epsilon
| Character of ichar
| Union of regexp * regexp
| Concat of regexp * regexp
| Star of regexp

(*
Exercise 1: Nullity of a regular expression
val null : regexp -> bool
*)
let rec null a  = 
    match a with 
    | Epsilon -> 
        true
    | Character (c,v) -> 
        false
    | Union  (r1,r2) ->
        null(r1) || null(r2)
    | Concat (r1,r2) ->
        null(r1) && null(r2)
    | Star  r1 -> 
        true



let () =
    let a = Character ('a', 0) in

    assert (not (null a));
    assert (null (Star a));
    assert (null (Concat (Epsilon, Star Epsilon)));
    assert (null (Union (Epsilon, a)));
    assert (not (null (Concat (a, Star a))))

let () = print_endline "🎉✅ Exercise 1: tests passed successfully!"

(*
Exercise 2: The first and the last
*)
module Cset = Set.Make(struct type t = ichar let compare = Stdlib.compare end)

(*
val first : regexp -> Cset.t
*)

let rec first r =
  match r with
  | Epsilon -> Cset.empty  (* Epsilon has no characters *)
  | Character c -> Cset.singleton c  (* The character itself is the first *)
  | Union (r1, r2) -> Cset.union (first r1) (first r2)
  | Concat (r1, r2) -> if null r1 then Cset.union (first r1) (first r2)
                       else first r1
  | Star r1 -> first r1  (* Star can repeat, but first is just the first of the repeated expression *)


(*
val last : regexp -> Cset.t
*)

let rec last r =
  match r with
  | Epsilon -> Cset.empty  (* Epsilon has no characters *)
  | Character c -> Cset.singleton c  (* The character itself is the first *)
  | Union (r1, r2) -> Cset.union (last r1) (last r2)
  | Concat (r1, r2) -> if null r2 then Cset.union (last r1) (last r2)
                       else last r2
  | Star r1 -> last  r1  (* Star can repeat, but first is just the first of the repeated expression *)



let () =
    let ca = ('a', 0) and cb = ('b', 0) in
    let a = Character ca and b = Character cb in
    let ab = Concat (a, b) in
    let eq = Cset.equal in
    assert (eq (first a) (Cset.singleton ca));
    assert (eq (first ab) (Cset.singleton ca));
    assert (eq (first (Star ab)) (Cset.singleton ca));
    assert (eq (last b) (Cset.singleton cb));
    assert (eq (last ab) (Cset.singleton cb));
    assert (Cset.cardinal (first (Union (a, b))) = 2);
    assert (Cset.cardinal (first (Concat (Star a, b))) = 2);
    assert (Cset.cardinal (last (Concat (a, Star b))) = 2)


let () = print_endline "🎉✅ Exercise 2: tests passed successfully!"
(*
Exercise 3: The follow
*)

let print x = 
    match x with 
    |  (c,v)  -> print_endline (Char.escaped c ^ " " ^ string_of_int v)
let print_set pre x = 
    (* Cset.iter (fun (c,v) -> print_string (Char.escaped c ^ " " ^ string_of_int v ^ "\n")) x *)
    print_endline pre;
    Cset.iter (fun (c,v) -> print_string ( pre ^ " " ^ Char.escaped c ^ " " ^ string_of_int v ^ "\n")) x
    (* let ()=print_string  "\n" *)

(* val follow : ichar -> regexp -> Cset.t *)
let rec follow ic r =
    match r with
    | Epsilon -> 
        Cset.empty  (* Epsilon has no characters *)
    | Character (c,v) -> 
        Cset.empty

    | Union (r1, r2) -> 
        Cset.union (follow ic r1) (follow ic r2)
    | Concat (r1, r2) -> 
        let x=  last(r1) in
        if Cset.mem ic x then
            Cset.union (Cset.union (follow ic r1 ) (follow ic r2 )) (first r2 )
        else
            Cset.union (follow ic r1 ) (follow ic r2 )
    | Star r1 -> 
        let x=  last(r1) in
        if Cset.mem ic x then
            Cset.union (follow ic r1 ) (first r1 )
        else
            follow ic r1
        


let () =
    let ca = ('a', 0) and cb = ('b', 0) in
    let a = Character ca and b = Character cb in
    let ab = Concat (a, b) in
    assert (Cset.equal (follow ca ab) (Cset.singleton cb));
    assert (Cset.is_empty (follow cb ab));
    let r = Star (Union (a, b)) in
    assert (Cset.cardinal (follow ca r) = 2);
    assert (Cset.cardinal (follow cb r) = 2);
    let r2 = Star (Concat (a, Star b)) in
    assert (Cset.cardinal (follow cb r2) = 2);
    let r3 = Concat (Star a, b) in
    assert (Cset.cardinal (follow ca r3) = 2)

let () = print_endline "🎉✅ Exercise 3: tests passed successfully!"

(* Exercise 4: Construction of the automaton *)

type state = Cset.t (* a state is a set of characters *)
module Cmap = Map.Make(Char) (* dictionary whose keys are characters *)
module Smap = Map.Make(Cset) (* dictionary whose keys are states *)
type autom = {
    start : state;
    trans : state Cmap.t Smap.t (* state dictionary -> (character dictionary ->state) *)
}
(* cmap[c]=state *)
(* smap[state]=cmap *)
let map1= Cmap.add 'a' Cset.empty Cmap.empty
let map2= Smap.add Cset.empty map1 Smap.empty




(* val next_state : regexp -> Cset.t -> char -> Cset.t *)
(* val next_state : regexp -> state -> char -> state *)
let rec next_state r s c =
    (* Combine the first sets of states reachable from s via character c
       according to the transitions defined by r. *)
    
    let reachable_states = 
        Cset.fold (fun (ch, v) acc -> 
            (* print_endline (Char.escaped ch ^ " " ^ string_of_int v ^ " " ^ Char.escaped c); *)
            if ch = c then 
                (* let ()= print_set "follow" (follow (ch, v) r) in *)
                (* let f=(follow (ch, v) r) in *)
                Cset.union acc (follow (ch, v) r)
            else 
                acc
        ) s Cset.empty
    in
    reachable_states
let eof = ('#', -1)

(* val make_dfa : regexp -> autom *)
let make_dfa (r:regexp) =
    let r = Concat (r,  Character eof) in
    (* let k = Epsilon in *)
    (* let r = Concat (r,k  ) in *)
    let trans = ref Smap.empty in

    let rec transitions q =
        
        let find_all_next_state = 
            Cset.fold (fun (c, v) map ->
                let q' = next_state r q c in
                Cmap.add c q' map
            ) q Cmap.empty
        in
        trans := Smap.add q find_all_next_state !trans;

        (* Process the newly added states in transitions map *)
        Cmap.iter (fun c q' -> 
            (* the state that not find yet *)
            if not (Smap.mem q' !trans) then
                transitions q'
        )  find_all_next_state;
    in

    let q0 = first r in
    
    transitions q0;
    { start = q0; trans = !trans }
    

let fprint_state fmt q =
    Cset.iter (fun (c,i) ->
    if c = '#' then Format.fprintf fmt "# " else Format.fprintf fmt "%c%i " c i) q
let fprint_transition fmt q c q' =
    Format.fprintf fmt "\"%a\" -> \"%a\" [label=\"%c\"];@\n"
    fprint_state q
    fprint_state q'
    c
let fprint_autom fmt a =
    Format.fprintf fmt "digraph A {@\n";
    Format.fprintf fmt " @[\"%a\" [ shape = \"rect\"];@\n" fprint_state a.start;
    Smap.iter
        (fun q t -> Cmap.iter (fun c q' -> fprint_transition fmt q c q') t)
    a.trans;
    Format.fprintf fmt "@]@\n}@."
let save_autom file a =
    let ch = open_out file in
    Format.fprintf (Format.formatter_of_out_channel ch) "%a" fprint_autom a;
    close_out ch

let () = print_endline "🎉✅ Exercise 4: tests passed successfully!"

(* Exercise 5: Word recognition *)

(* val recognize : autom -> string -> bool *)
let recognize (a:autom) (s:string) =
    (* let str_with_eof = s ^ "#" in *)
    let str_with_eof = s  in
    let final_state,accpet = String.fold_left (fun (q,accpet) c ->
        if Cset.is_empty q then
            (* accpet or out of trans *)
            (q,accpet)
        else
            let cmap = Smap.find q a.trans in
            if Cmap.mem c cmap  then
                let q' = Cmap.find c cmap in
                (* let () = print_endline (Char.escaped c) in
                let () = print_set "final" q' in
                let _ =print_endline (string_of_bool( Cset.is_empty q' ))in *)
                (q', Cset.mem eof q')
            else
                (*out of trans *)
                (Cset.empty,false)

    ) (a.start,Cset.mem eof a.start) str_with_eof in
    accpet




(* (a|b)*a(a|b) *)
let r = Concat (Star (Union (Character ('a', 1), Character ('b', 1))),
    Concat (Character ('a', 2),
    Union (Character ('a', 3), Character ('b', 2))))


let a = make_dfa r
let () = save_autom "autom.dot" a

(* positive test *)
let () = assert (recognize a "aa")
let () = assert (recognize a "ab")
let () = assert (recognize a "abababaab")
let () = assert (recognize a "babababab")
let () = assert (recognize a (String.make 1000 'b' ^ "ab"))

(* neg test *)
let () = assert (not (recognize a ""))
let () = assert (not (recognize a "a"))
let () = assert (not (recognize a "b"))
let () = assert (not (recognize a "ba"))
let () = assert (not (recognize a "aba"))
let () = assert (not (recognize a "abababaaba"))



let r = Star (Union (Star (Character ('a', 1)),
    Concat (Character ('b', 1),
    Concat (Star (Character ('a',2)),
    Character ('b', 2)))))
let a = make_dfa r
let () = save_autom "autom2.dot" a

let () = assert (recognize a "")
let () = assert (recognize a "bb")
let () = assert (recognize a "aaa")
let () = assert (recognize a "aaabbaaababaaa")
let () = assert (recognize a "bbbbbbbbbbbbbb")
let () = assert (recognize a "bbbbabbbbabbbabbb")

let () = assert (not (recognize a "b"))
let () = assert (not (recognize a "ba"))
let () = assert (not (recognize a "ab"))
let () = assert (not (recognize a "aaabbaaaaabaaa"))
let () = assert (not (recognize a "bbbbbbbbbbbbb"))
let () = assert (not (recognize a "bbbbabbbbabbbabbbb"))

let () = print_endline "🎉✅ Exercise 5: tests passed successfully!"

(* Exercise 6: Generating a lexical analyzer *)


type buffer = { text: string; mutable current: int; mutable last: int }
let next_char b =
    if b.current = String.length b.text then raise End_of_file;
    let c = b.text.[b.current] in
    b.current <- b.current + 1;
    c

type gen_state={ 
    id: int ;
    trans:state Cmap.t Smap.t;
}

(* val generate: string -> autom -> unit *)
let generate (filename: string) (a: autom) =
    let channel = open_out filename in
    try
        let state_id = ref Smap.empty in
        let count = ref 0 in
        
        (* Write formatted content to the file *)
        Printf.fprintf channel "%s" "type buffer = { text: string; mutable current: int; mutable last: int }\n";
        Printf.fprintf channel "%s" "let next_char b =
    if b.current = String.length b.text then raise End_of_file;
    let c = b.text.[b.current] in
    b.current <- b.current + 1;
    c\n";

        let update_state_id (q : state) =
            if not (Smap.mem q !state_id) then (
                state_id := Smap.add q !count !state_id;
                count := !count + 1;
            );
            Smap.find q !state_id
        in
        let gen_state = Smap.fold (fun k v s -> 
            let i=update_state_id k in
            (* first state *)
            let prefix_string = Format.asprintf (if i = 0 then "let rec state%i b =\n" else "and state%i b =\n") i in

            (* accept state *)
            let accept = Cset.mem eof k in
            (* let prefix_string =if accept then prefix_string ^ "  print_endline ((string_of_int b.last)^(string_of_int b.current));\n" else prefix_string in *)
        

            if accept then
                let prefix_string =if accept then prefix_string ^ "  b.last <- b.current;\n" else prefix_string in
            
                let s'=s^(prefix_string)^"\n"in
                s'
            else

                let prefix_string = prefix_string ^ "  let c = next_char b in\n" in
                let prefix_string = prefix_string ^ "  match c with \n" in

                let match_string = Cmap.fold (fun c q s' -> 
                        
                    let q_id = update_state_id q in
                        let s'' = Format.asprintf "  | '%c' -> state%i b\n" c q_id in
                        s' ^ s''
                ) v "" in
                let match_string = match_string ^ "  | _ -> raise (Failure \"undefine key in state\")\n" in

                let state_string=prefix_string ^ match_string in
                let s'=s^(state_string)^"\n"in
                s'

        ) a.trans "" in
        let start_string =  Format.asprintf "let start = state%i\n" (Smap.find a.start !state_id)in
        let gen_state = gen_state ^ start_string in

        Printf.fprintf channel "%s" gen_state;

        close_out channel
    with e ->
        (* Ensure the file is closed if an error occurs *)
        close_out_noerr channel;
        raise e
    





(* a*b *)
let r3 = Concat (
        Star (Character ('a', 1)),
        Character ('b', 1)
    )
let a = make_dfa r3
let () = save_autom "autom2.dot" a
let () = generate "a.ml" a

let () = print_endline "🎉✅ Exercise 6: tests passed successfully!"

```

## lexer.ml
```haskell
(* type buffer = { text: string; mutable current: int; mutable last: int } *)
type buffer = A.buffer
let () =
  let str = "abbaaab" in
  (* let (b: ref A.buffer) = ref { text = str; current = 0; last = -1 } in *)
  let (b: A.buffer) = { text = str; current = 0; last = -1 } in
  let flag = ref true in
  let start = A.start in

  while !flag do
    try 
      let last = if b.last = -1 then 0 else b.last in
      let () = start b in
      (* print_endline ( "last: "^(string_of_int b.last) ^" current: "^(string_of_int b.current)); *)
       if b.last != -1 then 
        (* print_endline ( (string_of_int last) ^" "^(string_of_int b.last)); *)
          let ac_string=String.sub b.text (last) (b.last-last) in
          print_endline ("---> "^ac_string)
        ;

    with e ->
      print_endline (Printexc.to_string e);
      match Printexc.to_string e with
      | "Failure \"undefine key in state\"" -> flag := false
      | "End_of_file" -> flag := false
      | _ -> ()
  done
```