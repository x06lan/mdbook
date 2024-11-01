# hw0

[compiler HW0.pdf](../../assets/pdf/compiler_HW0.pdf)

```haskell
(*print_endline "Hello, World!"*)
let width=32;;
let height=16;;

(* Exercise 1 *)

(* Exercise 1.a*)
let rec  fact n= 
    if n<=1 then 
        1
    else 
        n*fact(n-1);;

let p_w= "1.a fact(5)="^ string_of_int (fact(5) );;
print_endline p_w;;


(* Exercise 1.b*)

let rec nb_bit_pos n= 
    if n=0 then 
        0
    else if (n land 1 = 1) then 
        1 + nb_bit_pos( n lsr 1)
    else 
        nb_bit_pos( n lsr 1);;

let p_w= "1.b nb_bit_pos(5)="  ^ string_of_int (nb_bit_pos(5) );;
print_endline p_w;;

(* Exercise 2*)

let fibo n= 
    let rec aux n a b=
        if n=0 then
            a
        else
            aux (n-1) b (a+b)
    in
    aux n 0 1


let p_w= "2.  fibo(6)="^ string_of_int (fibo(6));;
print_endline p_w;;

(* Exercise 3 *)
(* Exercise 3.a *)

let palindrome  m =
    let len=String.length m  in
    let vaild= ref true in
    for i = 0 to (len lsr 1) do
        if String.get m i <> String.get m (len-1-i) then
            vaild:=false
    done;
    !vaild

let p_w= "3.a palindrome('aba')="^ string_of_bool (palindrome("aba")) ;;
print_endline p_w;;

(* Exercise 3.b*)

let compare  m1 m2 =
    let len1=String.length m1 in
    let len2=String.length m2 in

    let rec check i= 
        if (i < len1) && (i < len2 )then

            let c1 =String.get m1 i in
            let c2 =String.get m2 i in

            if c1 = c2 then
                check(i+1)
            else if c1 < c2 then
                true
            else
                false

        else if len1 == len2 && i == len1 then
            false
        else if i < len1 then
            false
        else 
            true
    in
    check 0


let p_w= "3.b compare('ab','abc')="^ string_of_bool (compare "ab" "abc") ;;
print_endline p_w;;

(* Exercise 3.c *)

let factor m1 m2 =
    let len1=String.length m1 in
    let len2=String.length m2 in
    
    let vaild =ref  false in
    for i = 0 to len2-len1 do
        let sub=String.sub m2 i len1 in
        if sub = m1 then 
            vaild:=true
    done;
    !vaild

let p_w= "3.c factor('ab','abc')="^ string_of_bool (factor "ac" "abcdfg") ;;
print_endline p_w;;


(* Exercise 4 *)

let string_of_list l = "[" ^ (String.concat "," (List.map string_of_int l)) ^ "]"

let slice l start stop =
  let rec aux i acc = function
    | [] -> List.rev acc  (* If list is empty, return the reversed accumulator *)
    | hd :: tl ->
        if i >= stop then List.rev acc  (* Stop when index reaches 'stop' *)
        else if i >= start then aux (i + 1) (hd :: acc) tl  (* Add element to accumulator if within slice *)
        else aux (i + 1) acc tl  (* Continue without adding element *)
  in
  aux 0 [] l
let split l =
    let len = (List.length l) in
    let mid = len lsr 1
   in
    (slice l 0 mid, slice l mid len)

let merge l1 l2 = 
    let rec aux acc = function
        | (h1::t1,h2::t2) ->
            if h1 < h2 then
                aux (h1::acc) (t1,h2::t2)
            else 
                aux (h2::acc) (h1::t1,t2)
        | (h1::t1,[]) -> aux (h1::acc) (t1,[])
        | ([],h2::t2) -> aux (h2::acc) ([],t2)
        | ([],[]) -> List.rev acc
    in
    aux [] (l1,l2)

let rec sort ll=
    if List.length ll <=1  then
        ll
    else
        let l,r =split ll in
        let sl,sr=sort(l),sort(r) in
        merge sl sr




let () =
    let test_list = [1; 4; 3; 2; 5] in
    let l,r =split test_list in 
    let p_w1= "4.  split" ^ string_of_list (test_list) ^"=" ^ string_of_list (l) ^ ","^ string_of_list (r) in
    let p_w2= "4.  merge" ^ string_of_list (l) ^ ","^ string_of_list (r) ^ "=" ^string_of_list ( merge l r)in
    let p_w3= "4.  sort" ^ string_of_list (test_list) ^"=" ^ string_of_list (sort test_list) in
    print_endline p_w1;
    print_endline p_w2;
    print_endline p_w3

(* Exercise 5.a *)

let pow m = m * m
let square_sum m =
    List.fold_left (+) 0 (List.map pow m)
let () =
    let test_list = [1; 2; 3] in
    let p_w = "5.a square_sum = " ^ string_of_int (square_sum test_list) in
    print_endline p_w

(* Exercise 5.b *)

let find_opt x l =
    let rec aux i = function
        | [] -> None
        | hd :: tl -> 
            if hd = x then 
                Some i 
            else 
                aux (i + 1) tl  (* Check if head equals x, otherwise recurse *)
    in
    aux 0 l
let find_opt x l=
    let (return ,_) =List.fold_left (
            fun (out,i) v -> 
                if v=x && out ==None then 
                    (Some i,i+1)
                else 
                    (None,i+1)
        )(None,0) l  in
    return

let unwrap = function
  | Some c -> string_of_int c
  | None -> "Not found"

let () =
    let test_list = [1; 2; 3; 2] in
    let result = find_opt 2 test_list in
    let p_w = "5.b find_opt 2," ^ string_of_list test_list ^ " = " ^ unwrap result in
    print_endline p_w

(* Exercise 6 *)

let rev l =
  let rec rev_append acc l =
    match l with
    | [] -> acc
    | h :: t -> rev_append (h :: acc) t
  in
  rev_append [] l

let map f l =
  let rec aux acc l =
    match l with
    | [] -> List.rev acc  (* Reverse the accumulator before returning *)
    | h :: t -> aux (f h :: acc) t
  in
  aux [] l

let () =
    (*
    let test_list = List.init 1000001 (fun i -> i) in
    let r1= rev test_list in
    let r2= map (fun x -> x*2)test_list in
    *)
    let p_w1 = "6.  rev ..."  in
    let p_w2 = "6.  map ..."  in
    print_endline p_w1;
    print_endline p_w2

(* Exercise 7 *)
type 'a seq =
    | Elt of 'a
    | Seq of 'a seq * 'a seq



let (@@) x y = Seq(x, y)

let rec hd x = 
    match x with
    | Elt s -> s
    | Seq(s1,s2) -> hd s1


let rec tl l= 
  let rec aux find ll = 
    match ll with
    | Elt s -> raise (Failure "you entered an empty list")
    | Seq (Elt s, Elt s1) -> 
        if find then
            (false,Elt s1)
        else
            (false, Seq (Elt s, Elt s1))
    | Seq (Elt s, s1) -> 
        if find then
            (false,s1)
        else
            (false, Seq (Elt s, s1))
    | Seq (s1, Elt s) -> 
        let find',ll=aux find s1 in
        if find'=false then
            (false,Seq (ll, Elt s) )
        else
            (false,Seq (s1, Elt s) )
    | Seq (x1, x2 )->
        let find',ll=aux find x1 in
        if find'=false then
            (false,Seq (ll,x2) )
        else
            (false,Seq (x1, x2 ))
  in
  let _,ll=aux true l in
  ll





let rec mem v =function 
    | Elt s -> s=v
    | Seq(s1,s2) -> ((mem v s1) ||  (mem v s2))

let rec rev =function 
    | Elt s -> Elt s
    | Seq(s1,s2) -> Seq((rev s2),(rev s1))

let rec map f = function
  | Elt s -> Elt (f s)  (* Apply f to the single element *)
  | Seq (s1, s2) -> Seq (map f s1, map f s2)  (* Recursively map over both sub-sequences *)

let rec fold_left f acc = function
  | Elt s -> f acc s  (* Apply f to the accumulator and the single element *)
  | Seq (s1, s2) -> 
      let acc' = fold_left f acc s1 in  (* Fold over the first sub-sequence *)
      fold_left f acc' s2  (* Fold over the second sub-sequence *)

let rec fold_right f seq acc =
  match seq with
  | Elt s -> f s acc  (* Apply f to the single element and the accumulator *)
  | Seq (s1, s2) -> fold_right f s1 (fold_right f s2 acc)  (* Fold over both sub-sequences *)

let seq2list seq =
  let rec aux acc = function
    | Elt s -> s :: acc
    | Seq (s1, s2) -> aux (aux acc s1) s2
  in
  List.rev (aux [] seq)
let find_opt x l=
    let (return ,_) =fold_left (
            fun (out,i) v -> 
                match out with 
                | None ->
                    if v=x then
                        (Some i,i+1)
                    else 
                        (None,i+1)
                | Some k ->
                    (out,i+1)
        )(None,0) l  in
    return
let nth x l=
    
    let (return ,_) =fold_left (
            fun (out,i) v -> 
                match out with 
                | None ->
                    if i=x then
                        (Some v,i+1)
                    else 
                        (None,i+1)
                | Some k ->
                    (out,i+1)
        )(None,0) l  in

    match return  with 
    | None -> raise (Failure "out of range")
    | Some v -> v

(*
let print_of_something = function
    | Int s -> string_of_int s
    | Elt s -> string_of_list [s]
    | Seq (s1,s2)-> string_of_list (seq2list s1) ^ string_of_list (seq2list s2)
*)




let () =
    let test_seq =
        Seq(Seq (Elt 1,Elt 2),Seq (Seq (Elt 3,Elt 4),Elt 5)) in
    let test_list= seq2list test_seq in

    let p_w1 = "7.  hd "  ^ string_of_list test_list  ^"=" ^ string_of_int (hd test_seq) in
    let p_w2 = "7.  tl "  ^ string_of_list test_list  ^"=" ^ string_of_list (seq2list (tl test_seq)) in
    let p_w3 = "7.  mem"  ^ string_of_list test_list  ^"=" ^ string_of_bool(mem 5 test_seq) in
    let p_w4 = "7.  rev"  ^ string_of_list test_list  ^"=" ^ string_of_list (seq2list ( rev test_seq)) in
    let p_w5 = "7.  map"  ^ string_of_list test_list  ^"=" ^ string_of_list (seq2list ( map (fun x -> x *2 )test_seq)) in
    let p_w6 = "7.  fold_right"  ^ string_of_list test_list  ^"=" ^ string_of_int( fold_left (+) 0 test_seq  ) in
    let p_w7 = "7.  find_opt "  ^ string_of_int  3 ^ string_of_list test_list  ^"=" ^ (unwrap( find_opt 3 test_seq  ) )in
    let p_w8 = "7.  nth "  ^ string_of_int  3 ^ string_of_list test_list  ^"=" ^ (string_of_int( nth 3 test_seq  ) )in
    print_endline p_w1;
    print_endline p_w2;
    print_endline p_w3;
    print_endline p_w4;
    print_endline p_w5;
    print_endline p_w6;
    print_endline p_w7;
    print_endline p_w8
```