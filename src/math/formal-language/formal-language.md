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
## DFA
$$
\begin{aligned}
DFA&=(Q,\Sigma,\delta,q_0,F)\\
&Q=\text{state set}\\
&\Sigma=\text{input char domain(set)}\\
&\delta=\delta(Q,\Sigma)\rightarrow Q' \\
&q_0=\text{start state}\\
&F=\text{accept state set}\\
\end{aligned}



$$
## regular language
### regular expression

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

### closure properties
$$
L_1 ,L_2 \text{ is regular language}\\
\text{operation}
\begin{cases}
    L_1 \cup L_2 \\
    L_1 \cap L_2 \\
    \overline{L_1}\\
    L_1 \circ L_2  \\
    L^{*} \\
    L_1-L_2=L_1 \cap \overline{L_2} \\
    \text{homomorphism} \\
\end{cases}  \text{ is regular language}\\
$$

### pumping lemma for regular languages

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

## DFA == regular language

For every NFA $N$ there is a regular expression $R$ such that $L(R) = L(N)$

L(q,p,k){w ∈ $\Sigma^∗$ | there is a run of M on w from state q to state p and let passing through states set length < k}.

![](https://imgur.com/cxbyQki.png)

## DFA to regular language

### state removal method

![](https://imgur.com/fqto3k2.png)

### brzozowski algebraic method

![](https://imgur.com/3ov9og2.png)




# PDA

![](https://imgur.com/EWhpFR9.png)

$$
\begin{aligned}
    
P &= (Q,\Sigma, \Gamma, \delta, q_0, Z_0, F )\\
&\begin{aligned}
Q     &=\text{state set}\\ 
\Sigma&=\text{input char domain(set)}\\
\Gamma&=\text{stack symbol set}\\
\delta&=\delta(Q,\Gamma,\Sigma)\rightarrow (Q',\Gamma ') \\
q_0   &=\text{init state}\\
Z_0   &=\text{init stack}\\
F     &=\text{accept state set}\\
\end{aligned}

\end{aligned}
$$

## context free language
$$
\begin{aligned}
    
G &= (V,\Sigma, P, S)\\

&\begin{aligned}
V     &=\text{state set}\\ 
\Sigma&=\text{input char domain(set)}\\
S     &=\text{start variable}\\ 
P     &=S \rightarrow S'\\ 

\end{aligned}

\end{aligned}

$$

$$
L_1=\{a^n b^m c^{m+n} | n,m \in \N_0\}
$$


$$

\begin{aligned}
    
G &= (V,\Sigma, P, S)\\

&\begin{aligned}
V     &=\{S,A,B\}\\ 
\Sigma&=\{0,1\}\\
S     &=\text{start variable}\\ 
P     &=
\begin{cases}
S &\rightarrow A\\ 
A &\rightarrow aAc \verb | B \\
B &\rightarrow  bBc \verb | \epsilon \\

\end{cases}

\end{aligned}

\end{aligned}\\

L_1 = L(G)
$$

<!-- ```dot
     s
     |
     A
    / \
  aAc  B
      / \
     bBc ε
``` -->

### pumping lemma for CFL
### closure properties
$$
L_1 ,L_2 \text{ is regular language}\\
\text{operation}
\begin{cases}
    L_1 \cup L_2 \\
    \overline{L_1}\\
    L_1 \circ L_2  \\
    L^{*} \\
    L_1-L_2=L_1 \cap \overline{L_2} \\
    \text{homomorphism} \\
\end{cases}  \text{ is regular language}\\
$$
