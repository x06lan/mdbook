# Formal Language

tags: `math` 
<!-- <br> -->

[link](https://carquois42.github.io/formal.html)

# automata
* DFA(Deterministic Finite Automation)
* NFA(Nondeterministic Finite Automation)
# DFA NFA 
# regular expression
$$
% \begin{cases}
\begin{aligned}
\empty&=\text{empty set}\\
\epsilon&=\text{empty expression}\\
\circ&=\text{concat}\\
R^{k}&=\underbrace{R\circ R \circ \cdots \circ R}_{k \text{ times}}\\
R^+ &=R\circ R^{*}\\
R^* &=R^{+} \cup \epsilon\\
\end{aligned}
% \end{cases}
$$


# NFA == regular expression 

For every NFA $N$ there is a regular expression $R$ such that $L(R) = L(N)$


L(q,p,k){w ∈ $\Sigma^∗$ | there is a run of M on w from state q to state p and let passing through states set length < k}.

![](https://imgur.com/cxbyQki.png)

# NFA to regular expression
## state removal method

![](https://imgur.com/fqto3k2.png)
## brzozowski algebraic method
![](https://imgur.com/3ov9og2.png)




















```graphviz
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; S;
    node [shape = point ]; qi

    node [shape = circle];
    qi -> S;
    S  -> q1 [ label = "a" ];
    S  -> S  [ label = "a" ];
    q1 -> S  [ label = "a" ];
    q1 -> q2 [ label = "b" ];
    q2 -> q1 [ label = "b" ];
    q2 -> q2 [ label = "b" ];
}
```