# Formal Language

tags: `math`

<!-- <br> -->

[link](https://carquois42.github.io/formal.html)

# automata

- DFA(Deterministic Finite Automation)
- NFA(Nondeterministic Finite Automation)
- PDA(Push Down Automation)

![](https://imgur.com/JISgKkr.jpg)

# DFA / NFA

## regular expression

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

## DFA == regular expression

For every NFA $N$ there is a regular expression $R$ such that $L(R) = L(N)$

L(q,p,k){w ∈ $\Sigma^∗$ | there is a run of M on w from state q to state p and let passing through states set length < k}.

![](https://imgur.com/cxbyQki.png)

## DFA to regular expression

### state removal method

![](https://imgur.com/fqto3k2.png)

### brzozowski algebraic method

![](https://imgur.com/3ov9og2.png)

### pumping lemma for regular languages

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

# PDA

![](https://imgur.com/EWhpFR9.png)

## context free grammar
