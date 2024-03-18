# hw1

[formal_language_HW1.pdf](../../assets/pdf/formal_language_HW1.pdf)

# 1.a

```graphviz
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q0
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

```graphviz
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

```graphviz
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

```graphviz
digraph finite_state_machine {
    rankdir=LR;
    splines=false;
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

```graphviz
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

todo

```graphviz
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

todo

```graphviz
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q4;
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
    q3 -> q1 [ label = "0" ];
    q3 -> q4 [ label = "1" ];
    q4 -> q4 [ label = "0,1" ];

}
```

# 3.c

# 3.d

```graphviz
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

```graphviz
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q2,q3;
    node [shape=plaintext] s;
    s [label=""];
    node [shape = circle];
    s  -> q0 [ label = "start" ];
    q0 -> q4 [ label = "0" ];
    q0 -> q1 [ label = "1" ];
    q1 -> q4 [ label = "0" ];
    q1 -> q2 [ label = "1" ];
    q2 -> q4 [ label = "0" ];
    q2 -> q3 [ label = "1" ];
    q3 -> q4 [ label = "0" ];
    q3 -> q2 [ label = "1" ];

}
```

# 4.a

$$
R=(0^* 1^+ )^3\Sigma^*
$$

[ref](https://chat.openai.com/share/9d8e1c78-f6ec-47b3-957c-38226e5fa2df)

# 4.b

todo

$$
R=\Sigma^*0\Sigma^*0\Sigma^*
$$

[ref](https://chat.openai.com/share/e9bbc771-30ac-49e0-a95b-5d3b1c4b352b)

# 4.c

$$
R=( 1 \circ  \Sigma )^*
$$

# 5

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

<!-- $$
\text{let }\delta(q,p,i) = \text{all the transaction set of from state }q\text{ to state }p \text{ and passing through state set length } \leq i
$$ -->
