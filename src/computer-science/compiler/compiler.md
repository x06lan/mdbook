# compiler
![](https://imgur.com/nYxPyXu.png)

## lexical analysis
![](https://imgur.com/BV1rlj5.png)

### follow
![](https://imgur.com/bXzjP9b.png)

$$
\begin{align*}
\text{follow}(c, \emptyset) &= \emptyset \\
\text{follow}(c, \epsilon) &= \emptyset \\
\text{follow}(c, a) &= \emptyset \\
\text{follow}(c, r_1 r_2) &= 
\begin{cases} 
\text{follow}(c, r_1) \cup \text{follow}(c, r_2) \cup \text{first}(r_2) & \text{if } c \in \text{last}(r_1) \\
\text{follow}(c, r_1) \cup \text{follow}(c, r_2) & \text{otherwise} 
\end{cases} \\
\text{follow}(c, r_1 \mid r_2) &= \text{follow}(c, r_1) \cup \text{follow}(c, r_2) \\
\text{follow}(c, r*) &= 
\begin{cases} 
\text{follow}(c, r) \cup \text{first}(r) & \text{if } c \in \text{last}(r) \\
\text{follow}(c, r) & \text{otherwise} 
\end{cases}
\end{align*}

$$

### first
![](https://imgur.com/jVHdZxq.png)
$$
\begin{align*}
\text{first}(\emptyset) &= \emptyset \\
\text{first}(\epsilon) &= \emptyset \\
\text{first}(a) &= \{a\} \\
\text{first}(r_1 r_2) &= 
\begin{cases} 
\text{first}(r_1) \cup \text{first}(r_2) & \text{if } \text{null}(r_1) \\
\text{first}(r_1) & \text{otherwise} 
\end{cases} \\
\text{first}(r_1 \mid r_2) &= \text{first}(r_1) \cup \text{first}(r_2) \\
\text{first}(r^*) &= \text{first}(r)
\end{align*}

$$

### nullity

$$
\begin{align*}
\text{null}(\emptyset) &= \text{false} \\
\text{null}(\epsilon) &= \text{true} \\
\text{null}(a) &= \text{false} \\
\text{null}(r_1 r_2) &= \text{null}(r_1) \land \text{null}(r_2) \\
\text{null}(r_1 \mid r_2) &= \text{null}(r_1) \lor \text{null}(r_2) \\
\text{null}(r^*) &= \text{true}
\end{align*}

$$

### regex to DFA

![](https://imgur.com/wPOFQzN.png)

## parser

![](https://imgur.com/ty8k2vY.png)

### arithmetic expressions
$$
\begin{align*}
    N &= \text{ is finite set of non-terminal symbols}\\
    T &= \text{ is finite set of terminal symbols}\\
    S \in N & =\text{ is the start symbol (the axiom)}\\
    R \subseteq N \times (N \cup T) &= \text{ is a finite set of production rules}\\
\end{align*}\\
$$

example
$$
\begin{align*}
N&=\{E\}\\
T&=\{+,*,(,),int\}\\
S&=E\\
R&=\{(E,E+E), (E,E*E), (E,(E)), (E,int) \}\\
\end{align*}\\
$$

look like this

$$
\begin{align*}
E \rightarrow & E+E \\
   \ | \ & E*E \\
   \ | \ &(E) \\
   \ | \ & int \\
\end{align*}\\
$$

### Derivation

$$
\begin{align*}
u&\in \{(N\cup T)^* \}\\
v&\in \{(N\cup T)^* \}\\
X&\in N\\
\beta &\in R \\
\end{align*}\\
$$

$$
\begin{align*}
u&=u_1 X u_2\\
v&=u_1 \beta u_2\\
\end{align*}\\
$$

$$
\begin{align*}
&\underbrace{E* ( \ }_{u_1} &&\underbrace{E}_{X} &\underbrace{ \ )}_{u_2} &\rightarrow E*(  && \underbrace{ E+E }_{\beta} &&)
\end{align*}\\
$$

![](https://imgur.com/AMWumTK.png)

### context free grammar
The language defined by a context-free grammar $G = (N, T , S, R)$

$$
\text{int} * ( \text{int} + \text{int} ) ∈ L(G)
$$


#### ambiguous grammar
give `int + int * int`

##### left derivation
$$
\begin{align*}
E & \rightarrow E+E\\
& \rightarrow \text{int}+E\\
& \rightarrow \text{int}+E*E\\
& \rightarrow \text{int}+\text{int}*E\\
& \rightarrow \text{int}+\text{int}*\text{int}\\
\end{align*}\\
$$

##### right derivation

$$
\begin{align*}
E & \rightarrow E+E\\
& \rightarrow E + E * E\\
& \rightarrow E + E * \text{int}\\
& \rightarrow E + \text{int} * \text{int}\\
& \rightarrow \text{int} + \text{int} * \text{int}\\
\end{align*}\\
$$

![](https://imgur.com/PrdASeh.png)

#### Non-ambiguous grammar



$$
\begin{align*}
E & \rightarrow E + T \\
& \rightarrow t\\
T & \rightarrow T * F \\
& \rightarrow F\\
F & \rightarrow (E) \\
& \rightarrow \text{int}\\

\end{align*}\\
$$

give `int + int * int * int`



$$
\begin{align*}
E & \rightarrow E + T\\
& \rightarrow T + T \\
& \rightarrow F + T \\
& \rightarrow \text{int} + T \\
& \rightarrow \text{int} + T * F \\
& \rightarrow \text{int} + T * F * F \\
& \rightarrow \text{int} + T * F * F * F \\
& \rightarrow \text{int} + \text{int} * F * F * F \\
& \rightarrow \text{int} + \text{int} * \text{int} * F * F \\
& \rightarrow \text{int} + \text{int} * \text{int} * \text{int} * F \\
& \rightarrow \text{int} + \text{int} * \text{int} * \text{int} * \text{int} \\
\end{align*}\\
$$

![](https://imgur.com/QPFuLeP.png)


## bottom-up parsing

* scan the input from left to right
* look for right-hand sides of production rules to build the derivation tree from bottom to top


![](https://imgur.com/WmHm00z.png)


###  LR parsing (Knuth, 1965)
Using an automaton and considering the first k tokens of the input;
this is called `LR(k)` analysis (LR means “Left to right scanning, Rightmost derivation”)

![](https://imgur.com/mgbEWBs.png)

### LR table

![](https://imgur.com/sCbAoLW.png)

example 

![](https://imgur.com/Wfcr77V.png)

## Construction of the automation and the table

### NULL
Let $\alpha \in (N \cup T)^*$. 

$\text{NULL}(\alpha)$ holds if and only if we can derive $\epsilon$ from $\alpha$, i.e., $\alpha \Rightarrow^* \epsilon$
### FIRST
Let $\alpha \in (N \cup T)^*$. 

$\text{FIRST}(\alpha)$ is the set of all terminals starting words derived from $\alpha$, i.e., $\{a \in T \mid \exists w . \alpha \Rightarrow^* aw \}$
### FOLLOW
Let $X \in N$. 

$\text{FOLLOW}(X)$ is the set of all terminals that may appear after $X$ in a derivation, i.e., $\{a \in T \mid \exists u, w . S \Rightarrow^* uXaw \}$


![](https://imgur.com/rZ8uPmj.png)
![](https://imgur.com/SMQZHTs.png)
![](https://imgur.com/qHDuT5j.png)
![](https://imgur.com/5hYssAk.png)
