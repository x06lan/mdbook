# hw1

[formal_language_HW1.pdf](../../assets/pdf/formal_language_HW1.pdf)

# 1.a

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q1
    node [shape=plaintext] s;
    s [label=""];

    node [shape = circle];

    s  -> q0 [ label = "start" ];
    q0 -> q0 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q2 [ label = "0" ];
    q2 -> q2 [ label = "1" ];
    q2 -> q1 [ label = "0" ];
    q1 -> q0 [ label = "1" ];
}
```

# 1.b

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q0,q1,q2;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q0 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q0 [ label = "0" ];
    q1 -> q2 [ label = "1" ];
    q2 -> q2 [ label = "1" ];
    q2 -> q3 [ label = "0" ];
    q3 -> q3 [ label = "0,1" ];

}
```

# 1.c

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q0,q1;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q1 [ label = "1" ];
    q0 -> q2 [ label = "0" ];
    q1 -> q0 [ label = "0,1" ];
    q2 -> q2 [ label = "0,1" ];

}
```

# 1.d

```dot process
digraph finite_state_machine {
    rankdir=LR;
    layout=dot;
    size="100,100"


    node [shape = doublecircle]; q20,q21,q22;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q00 [ label = "start" ];
    q00 -> q10 [ label = "1" ];//1 0
    q10 -> q20 [ label = "1" ];//2 0
    q20 -> q20 [ label = "1" ];

    q00 -> q01 [ label = "0" ];//0 1
    q01 -> q02 [ label = "0" ];//0 2


    q10 -> q11 [ label = "0" ];//1 1
    q01 -> q11 [ label = "1" ];

    q20 -> q21 [ label = "0" ];//2 1
    q11 -> q21 [ label = "1" ];
    q21 -> q21 [ label = "1" ];


    q02 -> q12 [ label = "1" ];//1 2
    q11 -> q12 [ label = "0" ];

    q21 -> q22 [ label = "0" ];//2 2
    q12 -> q22 [ label = "1" ];
    q22 -> q22 [ label = "1" ];

    q20 -> qn [ label = "0" ];
    q21 -> qn [ label = "0" ];
    q22 -> qn [ label = "0" ];

    qn -> qn [ label = "0,1" ];
}
```

# 1.e

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q0;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q0 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q1 [ label = "0,1" ];

}
```

# 2.a

$$
\begin{aligned}
Q_1&=a Q_2 \cup b Q_1 =b^*aQ_2\\
Q_2&=a Q_2 \cup b Q_0= a^*bQ_0\\
\\
Q_0&=b Q_1 \cup aQ_0 \cup \epsilon\\
&=a^*bQ_1 \cup \epsilon\\
&=a^*b(b^*aQ_2) \cup \epsilon\\
&=a^*bb^*a(a^*bQ_0) \cup \epsilon\\
&=a^*b^+a^+bQ_0 \cup \epsilon\\
&=(a^*b^+a^+b)^* \cup \epsilon\\
&=(a^*b^+a^+b)^*\\
\end{aligned}
% R=(a^* b^+a^+b)^\ast \cup \epsilon
$$

# 2.b

$$
R=((a^*\cup b)b (bb)^*a )^*
$$

# 3.a

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q2;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q0 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q1 [ label = "1" ];
    q1 -> q2 [ label = "0" ];
    q2 -> q1 [ label = "1" ];
    q2 -> q0 [ label = "0" ];

}
```

# 3.b

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="10,10"

    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q0 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q1 [ label = "1" ];
    q1 -> q2 [ label = "0" ];
    q2 -> q0 [ label = "0" ];
    q2 -> q3 [ label = "1" ];
    q3 -> q2 [ label = "0" ];

    node [shape = doublecircle]; q4;
    q3 -> q4 [ label = "1" ];
    q4 -> q4 [ label = "0,1" ];

}
```

# 3.c

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="15,15"

    node [shape = circle];
    node [shape=plaintext] s;
    s [label=""];
    node [shape = doublecircle]; q3,q5;
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q1 [ label = "ϵ" ];
    q0 -> q2 [ label = "ϵ" ];

    q1 -> q3 [ label = "1" ];
    q1 -> q1 [ label = "0" ];
    q3 -> q1 [ label = "1" ];
    q3 -> q3 [ label = "0" ];

    q2 -> q4 [ label = "0"]
    q2 -> q2 [ label = "1"]
    q4 -> q5 [ label = "0"]
    q4 -> q4 [ label = "1"]
    q5 -> q6 [ label = "0,1"]
    q6 -> q6 [ label = "0,1"]


}
```

# 3.d

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q1,q2;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q2 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q1 [ label = "0,1" ];
    q2 -> q2 [ label = "0" ];
    q2 -> q3 [ label = "1" ];
    q3 -> q2 [ label = "0" ];

}
```

# 3.e

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q0,q3,q4;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q2 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q2 [ label = "0" ];
    q1 -> q3 [ label = "1" ];
    q3 -> q2 [ label = "0" ];
    q3 -> q4 [ label = "1" ];
    q4 -> q2 [ label = "0" ];
    q4 -> q3 [ label = "1" ];

}
```

# 4.a

$$
R=(0^* 1^+ )^3\Sigma^*
$$

[ref](https://chat.openai.com/share/9d8e1c78-f6ec-47b3-957c-38226e5fa2df)

# 4.b

$$
R=(1^+ 0 1^+ 0 1^*)\cup(1^* 0 1^+ 0 1^+)\cup(11^+ 01^*01^*)\cup(1^*01^*011^+)\cup(011^+0)
$$

# 4.c

$$
R=( 1 \circ  \Sigma )^*
$$

# 5

If $L$ is regular, then $\min(L)$ is also regular because $\min(L)$ is $L$ but remove the final state that be passing though another final state.

**for example**

$$
L=(ab\cup abc\cup abcd \cup ac )
$$

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q2,q3,q4,q5;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q1 [ label = "a" ];
    q1 -> q2 [ label = "b" ];
    q1 -> q5 [ label = "c" ];
    q2 -> q3 [ label = "c" ];
    q3 -> q4 [ label = "d" ];
}
```

$$
min(L)=(ab\cup ac )
$$

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q2,q5;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q1 [ label = "a" ];
    q1 -> q2 [ label = "b" ];
    q1 -> q5 [ label = "c" ];
}
```

# 6.a

$$
\begin{aligned}
L^*&=\bigcup_{i \in \N}L^i\\
L^{**}&=(\bigcup_{i \in \N}L^i)^*\\
&=\bigcup_{j \in \N}(\bigcup_{i \in \N}L^i)^j\\
&=\bigcup_{j \in \N}\bigcup_{i \in \N}L^{ij}\\
&=\bigcup_{ij \in \N}L^{ij}\\
&=L^*\\
\end{aligned}
$$

$$
\begin{aligned}
L^*L^*&=(L^+\cup \epsilon)(L^+\cup \epsilon)\\
&=LL^+\cup  L^+ \cup \epsilon\\
&=L^*
\end{aligned}
$$

# 6.b

$$
A \text{ is a finite language, then it contains a finite number of strings }a_0,a_1,\cdots,a_n\\
\text{The language }\{a_i\} \text{ consisting of a single literal string }a_i\text{ is regular }\\
\text{The union of a finite number of regular languages is also regular.}\\
\text{Therefore } A=a_0,a_1,\cdots,a_n \text{ is regular}
$$

[ref](https://cs.stackexchange.com/questions/104322/why-is-every-finite-language-a-%E2%8A%86-%CE%A3-regular)

# 6.c

$$
A \subseteq B\\
A=\{a^nb^n|n\in \N_0\}\\
B=\{(a\cup b)^n|n\in \N_0\}\\
$$

# 6.d

$$
B \subseteq A\\
A=\{a^nb^n|n\in \N_0\}\\
B=\{w|w=ab \}\\
$$

# 6.e

$$

L^{(\frac{1}{3})}=\{w|w^3\in L\}\\
$$

$$
L^{(\frac{1}{3})} \text{ mean all the solution that in } L \text{ that can divide to 3 exact same part}\\


$$

# 6.f
$$
L^{(3)}=\{w^3|w\in L\}\\
% \text{since } L \text{ is regular so is } L^3.\text{(regular closure)}
\text{If }L=\{ab^*,b\}\\
L^{(3)}=\{(ab^*)^3,bbb\}=\{ab^*ab^*ab^*,bbb\}\\ \\
w^3=\underbrace{w}_{x} \ \ \underbrace{w}_{y} \ \ \underbrace{w}_{z} \\
\text{By pumping lemma}\\
|y|\geq 1\\
|xy| \leq p\\
(\forall k  \geq  0)(xy^kz \in L )\\
\text{But }xy^0z=ww \notin L \\
\text{Therefor this is not regular languages}
$$

[ref (Formal definition)](https://en.wikipedia.org/wiki/Regular_language)

# 6.g

If $L$ is regular language then it can convert to DFA.

Divide a DFA to $k$ equeal part still are DFA which make it still regular.

# 6.h

$$
L^{\frac{1}{\infty}}=L^{1} \cap L^{\frac{1}{2}} \cdots  \cap L^{\frac{1}{\infty}}\\
\text{since } L\text{ is regular so is the }L^{\frac{1}{n}}\\
 L^{\infty}\text{ are regular because it is interest of } L^{\frac{1}{n}}\\
$$

# 6.i

$$

\sqrt{L} =\bigcup_{k\leq 1} L^{\frac{1}{k}}\\
\sqrt{L}\text{ is regular by union closure}
$$

# 6.j
not regular
<!-- $$
L^{\infty}=L^{1} \cup L^{2} \cdots  \cup L^{\infty}\\
\text{since } L\text{ is regular so is the }L^{n}\\
 L^{\infty}\text{ are regular because it is union of } L^n\\
$$ -->

# 7.a

$$
L=\{wcw| w\in \{a,b\}^*\}
$$

$$
wcw=(a\cup b)^i c(a\cup b)^i\\
(a\cup b)^i c(a\cup b)^j=\underbrace{(a\cup b)^{p-i}}_{x} \ \ \underbrace{(a\cup b)^{i}}_{y} \ \ \underbrace{c(a\cup b)^{p}}_{z} \text{ and }i>0\\
\text{By pumping lemma}\\
|y|\geq 1\\
|xy| \leq p\\
(\forall k  \geq  0)(xy^kz \in L )\\
\text{But }xy^0z=(a\cup b)^{p-i}c(a\cup b)^p \notin L \\
\text{Therefor this is not regular languages}


$$

# 7.b

$$
L=\{xy| x,y\in \{a,b\}^* \text{ and } |x|=|y|\}
$$

$$
xy=\{a,b\}^p\{a,b\}^p\\
x \text{ and } y \text{ is regular languages }\\
w\text{ is regular languages by closure of concatenate} 
$$

# 7.c

$$
L = \{a^n | n \text{ is a prime number}\}
$$

$$
a^p=\underbrace{a^{p-j-i}}_x \underbrace{a^i}_y  \underbrace{a^{j}}_z\\
|y|\geq 1 \\
|xy| \leq p\\
(\forall k  \geq  0)(xy^k z \in L )\\
\text{But }xy^0z=a^{p-j-i}a^{j}=a^{p-i}\notin L \\
\text{Therefor this is not regular languages}
$$

# 7.d

$$
L = \{a^mb^n | gcd(m, n) = 17\}
$$

$$
j,k\in \N \text{ and }gcd(j,k)=1 \\
\text{ then }a^mb^n=a^{17j}b^{17k}\\
a^mb^n=\underbrace{a^{17j-i}}_x \underbrace{a^i}_y  \underbrace{b^{17k}}_z\\
|y|\geq 1 \\
|xy| \leq p\\
(\forall k  \geq  0)(xy^kz \in L )\\
\text{But }xy^0z=a^{17j-i}b^{17k}\notin L \\
\text{Therefor this is not regular languages}
$$
# 8.a

$$
% \begin{aligned}
% \begin{split}
\text{Base case } \\
i=0 ,Q^{0}_r=\{ q_0\}\\
\text{ This is trivially true since the only path of length 0 is the path that starts and ends at }q_0 \\


\text{Inductive Step}\\
% We aim to show that Qk+1rQk+1r​ represents the set of all reachable states from q0q0​ using paths of length k+1k+1.

\text{Assume that for some }k\geq 0, Q^k_r \text{ is the set of all reachable states from } q_0 \text{ using paths of length }k.\\


\text{By definition, }Q^{k+1}_r​ \text{ includes all states that can be reached from states in } Q^k_r  \text{ by a single transition.}\\ \\

\text{By repeat }  Q^{k+1}_r​  \rightarrow Q^{k}_r \text{ until }k=0\\ 
\text{We prove }​ (\forall i\geq 0) (Q^i_r\text{​ is the set of all reachable states from }q_0\text{​ using paths of length } i)

% \end{split}
% \end{aligned}
$$
# 8.b
```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q0
    node [shape=plaintext] s;
    s [label=""];

    node [shape = circle];

    s  -> q0 [ label = "start" ];
    q0 -> q1 [ label = "0,1" ];
    q1 -> q2 [ label = "0,1" ];
    q2 -> q0 [ label = "0,1" ];
    
}
```
# 8.c
$$
\text{Base case } \\
Q^{0}_r=\{q_0\}\\
\text{Inductive Step}\\
q_0 = Q^0_r\text{ by definition}\\
\text{Assume } (\forall i \geq 0) (q_0\in Q^i_r)\\
Q^{i+1}_r=Q^i_r \cup  \{ q\in Q | \exist p \in Q^i_r, \exist a \in \Sigma ,q = \delta (p,a)\}\\
\text{We can see it will repeat }  Q^{i+1}_r​  \cup  Q^{i}_r \text{ until }i=0 \text{ which will union }q_0\\ 

\text{Then } (\forall i \geq 0) (q_0\in Q^i_r)\\

$$
# 8.d

$M$ is DFA by definition

$M_r$ is base on $M$ but modify $\delta$ function and remove some state and final state. So it still a DFA

# 8.e

<!-- $M$ is DFA by definition,$M_r$ is $M$ but remove all the state that cant reach by start state -->
$$
Q_r=\text{the state that can reach by init state}\\
F\cap Q_r= \text{only remain the final state can be reach by init state}\\
\text{since the state cant be reach by init state remove it will not change the language}\\

$$

# 9.a

Each symbols need 2 state to record is even or odd state and additional one state for init state; total 2n+1 state.

```dot process
digraph finite_state_machine {
    rankdir=LR;
    size="10,10"

    node [shape = doublecircle]; Q1_1,Q2_1, Q3_1 ,Qn_1;
    node [shape=plaintext] s;
    s [label=""];

    node [shape = circle];

    s  -> Q0 [ label = "start" ];
    Q0 -> Q1_1 [ label = "a1" ];
    Q0 -> Q2_1 [ label = "a2" ];
    Q0 -> Q3_1 [ label = "a3" ];
    Q0 -> Qn_1 [ label = "an" ];


    Q1_1 -> Q1_2 [ label = "a1" ];
    Q1_2 -> Q1_1 [ label = "a1" ];

    Q2_1 -> Q2_2 [ label = "a2" ];
    Q2_2 -> Q2_1 [ label = "a2" ];

    Q3_1 -> Q3_2 [ label = "a3" ];
    Q3_2 -> Q3_1 [ label = "a3" ];

    Qn_1 -> Qn_2 [ label = "an" ];
    Qn_2 -> Qn_1 [ label = "an" ];



}
```

# 9.b

Because DFA each state have determine result to next state by input. We need to know all symbols is even or odd in one state.
So each symbols have two possible (even or odd) lead to $2^n$ state

# 9.c

# 10.a
## prove $M_1 \rightarrow M_3 $ are morphism
$$
h(q_{(0,1)})=q_{(0,2)}\\
\text{}
(\forall q\in Q_1,\forall a\in \Sigma)(h(\delta_1(q,a)) =\delta_2(h(q),a))\\

$$


$$
M_1 \rightarrow M_2\\
(\forall q\in Q_1,\forall a\in \Sigma)f(\delta_1(q,a)) =\delta_2(f(q),a)\\
M_2 \rightarrow M_3\\
(\forall q\in Q_2,\forall a\in \Sigma)g(\delta_2(q,a)) =\delta_3(g(q),a)\\
M_1 \rightarrow M_3\\
\begin{aligned}
(\forall q\in Q_1,\forall a\in \Sigma)&g(f(\delta_1(q,a))) =\delta_3(g(f(q)),a)\\
(\forall q\in Q_1,\forall a\in \Sigma)&g(\delta_2(f(q),a)) =\delta_3(g(f(q)),a)\\
(\forall q\in Q_2,\forall a\in \Sigma)&g(\delta_2(q,a)) =\delta_3(g(q),a)\\
\end{aligned}\\
M_1 \rightarrow M_3 \text{ are morphism}
% \\ \text{} \\
% g(\delta_2(f(q),a))=\delta_3(g(f(q)),a)\\

% \circ 
% (\forall q\in Q_2,\forall a\in \Sigma)(g(\delta_2(q,a)) =\delta_3(g(q),a))\\
% (\forall q\in Q_1,\forall a\in \Sigma)(g(\delta_2(f(q),a)) =\delta_3(g(f(q)),a))\\
% \begin{aligned}
% \delta_1(q_{(n,1)},a)&=h^{-1}(\delta_2(h(q_{(n,1)}),a))\\
% &=\delta_2(q_{(n,2)},a)\\
% \end{aligned}
$$

## F-map
$$
f(F_1)\subseteq F_2 (f \text{ is F-map})\\
g(F_2)\subseteq F_3 (g \text{ is F-map})\\
{}\\
\text{Therefore }g(f(F_1))\subseteq F_3\\ 
g\circ f \text{ is F-map too.}
$$
## B-map
$$
\begin{aligned}
f^{-1}(F_2)&\subseteq F_1 &(f \text{ is B-map})\\
% F_2&\subseteq f(F_1) &(f \text{ is B-map})\\
g^{-1}(F_3)&\subseteq F_2 &(g \text{ is B-map})\\
% F_3&\subseteq g(F_2) &(g \text{ is B-map})\\
\end{aligned}
{}\\
\text{Therefore }f^{-1}(g^{-1}(F_3))\subseteq F_1\\ 
g\circ f \text{ is B-map too.}
$$
# 10.b




$$

% h(\delta_1(q,w_1)) =\delta_2(h(q),w_1)\\
\text{}\\

\begin{aligned}
% h(\delta_1(\delta_1(q,w_1),w_2))&=\delta_2(\delta_2(h(q),w_1),w_2)\\
\hat{\delta}_2(h(q),w_n)&=h(\hat{\delta}_1(q,w_n))\\
\delta_2(\hat{\delta}_2(h(q),w_{n-1}),a)&=h(\delta_1(\hat{\delta}_1(q,w_{n-1}),a))\\
\delta_2(\hat{\delta}_2(h(q),w_{n-1}),a)&=\delta_2(h(\hat{\delta}_1(q,w_{n-1})),a)\\
\hat{\delta}_2(h(q),w_{n-1})&=h(\hat{\delta}_1(q,w_{n-1}))\\
\end{aligned}\\

\text{By repeat this until } |w|=1 \text{ make }\hat{\delta}_2(q,w)=\delta_2(q,w)\\
% h(\delta_1(q,w_1)) =\delta_2(h(q),w_1)\\

\text{}\\
\text{We prove that }
(\forall q\in Q_1,\forall w\in \Sigma^{*})(h(\hat{\delta}_1(q,w)) =\hat{\delta}_2(h(q),w))\\
$$

# 10.c
<!-- $$
{\footnotesize
\begin{CD}
     q_{(n,1)} @>a>> \delta_1(q_{(n,1)},a)\\
     @VhVV @. \\
     h(q_{(n,1)})=q_{(n,2)} @>a>> \delta_2(h(q_{(n,1)}),a)
\end{CD}
}\\
\Huge{\Downarrow}\\
{\footnotesize
\begin{CD}
     q_{(n,1)} @>a>> \delta_1(q_{(n,1)},a)\\
     @VhVV @VhVV \\
     h(q_{(n,1)})=q_{(n,2)} @>a>> \delta_2(h(q_{(n,1)}),a)=h(\delta_1(q_{(n,1)},a))\\
     @Vh^{-1}VV @Vh^{-1}VV \\
     q_{(n,1)} @>a>> \delta_1(q_{(n,1)},a)\\
\end{CD}
}
$$ -->
$$
\text{If is proper homomorphism then }h^{-1}(F_2)=F_1\\
% (\forall q\in Q_1,\forall w\in \Sigma^{*})(h(\hat{\delta}_1(q,w)) =\hat{\delta}_2(h(q),w))(M_1\rightarrow M_2 \text{ is a morphism})\\
(\forall q\in Q_1,\forall a\in \Sigma)(h(\delta_1(q,a)) =\delta_2(h(q),a))\\
\text{Therefore } L(M_1)=L(M_2)\\
$$