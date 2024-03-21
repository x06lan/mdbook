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
    size="8,5"


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

    q21 -> q22 [ label = "1" ];//2 2
    q12 -> q22 [ label = "0" ];
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

    node [shape = doublecircle]; q3,q4;
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

if $L_1$ and $L_2$ is regular then $L_1 \cup L_2 $ is regular

<!-- By definition any regular language can convert finite machine. -->

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


$$

# 6.f

yes

# 6.g

# 6.h

yes

# 6.i

not

# 6.j

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
(\forall i  \geq  0)(xy^iz \in L )\\
\text{But }xy^0z=(a\cup b)^{p-i}c(a\cup b)^p \notin L \\
\text{Therefor this is not regular languages}


$$

# 7.b

$$
L=\{xy| x,y\in \{a,b\}^* \text{ and } |x|=|y|\}
$$

$$
xy=\{a,b\}^p\{a,b\}^p\\
\{a,b\}^p\{a,b\}^p=\underbrace{\{a,b\}^{p-2}}_{x} \ \ \underbrace{\{a,b\}^{2}}_{y} \ \ \underbrace{\{a,b\}^{p}}_{z}\\
|y|\geq 1\\
|xy| \leq p\\
(\forall i  \geq  0)(xy^iz \in L )\\
\text{By pumping lemma this is regular languages}
$$

# 7.c

$$
L = \{a^n | n \text{ is a prime number}\}
$$

$$


$$

# 7.d

$$
L = \{a^mb^n | gcd(m, n) = 17\}
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
