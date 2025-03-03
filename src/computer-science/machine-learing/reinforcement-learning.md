# reinforce learning

## actor-critic

### origin
- $s_{t}$: state at time t
- $V(s_{t})$: value function predict reward with $s_{t}$
- $A(s_{t})$: action function return action probability base on $s_{t}$
- top1: select the action with max probability
- $R(a_{[0:t]})$: reward function input a sequence of action out float
- advantages value: if the can get more reward then positive value else negative value

$$
\begin{aligned}
\text{action probability}&=A(s_{[0:t-1]}) \\
a_{[0:t-1]}&=\text{top1}(\text{action probability})\\
\text{reward}&=R(a_{[0:t-1]})\\
L_\text{critic}&=MSE(reward,V(s_{t-1}))\\
\text{advantages value}&=\text{reward}-V(s_{t-1})\\

L_\text{actor}&=\text{CrossEntropy}(\text{action probability},a_{[0:t-1]})\times {\text{advantages value}}\\
\end{aligned}
$$

### with Temporal Difference error(TD-error)

- Hope $V(s_{t})$ can predict reward that may get in future with proportion $\gamma$
- note: you should add `stop gradient` to $TD_\text{target}$ (aka detach in pytorch)

$$
\begin{aligned}
TD_\text{target}&=\text{reward}+\gamma V(s_{t})\\
TD_\text{error} &=TD_\text{target} - V(s_{t-1})\\
L_\text{critic}&=MSE(TD_\text{error},0) =MSE(TD_\text{target},V(s_{t-1}))\\
\text{advantages value}&=TD_\text{error}\\
L_\text{actor}&=\text{CrossEntropy}(\text{action probability},a_{[0:t-1]})\times {\text{advantages value}}\\
\end{aligned}
$$
