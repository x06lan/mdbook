# signals and systems mid
[SS_mid_hw.pdf](../../assets/pdf/SS_Mid_HW.pdf)
# 2
odd signal of $x[n]$ is $ \begin{cases} x[n] &, n>=0\\ -x[-n] &, n<0\end{cases}$
# 3
## a
odd signal $x[n]=-x[-n]$
## b
odd signal $x[n]=-x[-n]$<br>
even signal $x[n]=x[-n]$<br>
$x_o[n] = \begin{cases} x[n] &, n>=0\\ -x[-n] &, n<0\end{cases}$

$x_e[n] \begin{cases} x[n] &, n>=0\\ x[-n] &, n<0\end{cases}$

product of $x_o[n]$ and $x_e[n]$ is $ \begin{cases} x[n]^2 &, n>=0\\ -x[-n]^2 &, n<0\end{cases}$ still are odd signal since $x[n]=-x[-n]$
## c
$$
x=x_o+x_e\\
x(t)^2=x_o(t)^2+2x_o(t) x_e(t) +x_e(t)^2\\
\begin{aligned}\\
\int_{-\infty}^{\infty}x^2(t) \ dt&=\int_{-\infty}^{\infty}x_o^2(t) \ dt+\int_{-\infty}^{\infty}2x_o(t) x_e(t) \ dt+\int_{-\infty}^{\infty}x_e^2(t) \ dt\\
\int_{-\infty}^{\infty}x^2(t) \ dt&=\int_{-\infty}^{\infty}x_o^2(t) \ dt+0+\int_{-\infty}^{\infty}x_e^2(t) \ dt\\
\int_{-\infty}^{\infty}x^2(t) \ dt&=\int_{-\infty}^{\infty}x_e^2(t) \ dt\\
\end{aligned}\\
$$
# 4

|                        | linear | time invariant |
| ---------------------- | ------ | -------------- |
| $$y(t)=t^2x(t-1)$$     | no     | no             |
| $$y[n]=x[n+2]-x[n-3]$$ | yes    | yes            |
| $$y[n]=O_d\{x[n]\}$$   | yes    | no             |

# 5
|                                    | period            |
| ---------------------------------- | ----------------- |
| $$x(t)=3 \cos (4t+\frac{\pi}{3})$$ | $$\frac{\pi}{2}$$ |
| $$x(t)=O_d\{\sin(4\pi t)u(t)\}$$   | $$0.5$$           |
| $$x[n]=\cos( \frac{n}{8}-\pi)$$    | $$\text{None} $$  |
# 6

|                                                                                        | memoryless | time invariant | linear | causal | stable |
| -------------------------------------------------------------------------------------- | ---------- | -------------- | ------ | ------ | ------ |
| $$y[n]=E_v\{x[n-1]\}$$                                                                 | ❌          | ✅              | ✅      | ✅      | ✅      |
| $$y[n]=x[n-2]-2x[n-3]$$                                                                | ❌          | ✅              | ✅      | ✅      | ✅      |
| $$y(t)=cos(3t+2)x(t)$$                                                                 | ✅          | ✅              | ❌      | ✅      | ✅      |
| $$y[n]=\begin{cases} 0,& \text{if } t<0 \\ x(t)+x(t-2), &\text{otherwise}\end{cases}$$ | ❌          | ✅              | ❌      | ✅      | ✅      |