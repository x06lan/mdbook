# SIGNALS and SYSTEMS
## CT vs DT
### CT(continuous-time)
For a continuous-time (CT) signal, the independent variable is
always enclosed by a parenthesis $(N)$<br>
Example: $ x(t), y(t), z(t), A(x, y)$


### DT(discrete-time)
For a discrete-time (DT) signal, the independent variable is always
enclosed by a brackets $[N]$<br>
Example: $x[n], y[n], z[n], A[m, n]$

## Signal Energy and Power

$$
p(t)=v(t)i(t)=\frac{1}{R}v^2(t)
$$
$$\triangleq \text{is "by definition"symbol}$$
### Energy
$$
E  =\int^{t_2}_{t_1}p(t)dt=\int^{t_2}_{t_1}\frac{1}{R}v^2(t)dt
$$
### average power
$$
P  =\frac{E}{t_2-t_1}=\int^{t_2}_{t_1}p(t)dt=\int^{t_2}_{t_1}\frac{1}{R}v^2(t)dt
$$
### ex1
$$
x(t)=\begin{cases}
        x& 0<x<3\\
        6-x& 3<x<6\\
    \end{cases}\\
E=\int^{6}_{0}x(t)^2dt=\int^{3}_{0}(t)^2dt+\int^{6}_{3}(6-t)^2dt\\
P=\frac{E}{6-0}=\frac{1}{6}(\int^{3}_{0}(t)^2dt+\int^{6}_{3}(6-t)^2dt)
$$
### ex2
$$
x[t]=\begin{cases}
        x& 0<x<3\\
        6-x& 3<x<6\\
    \end{cases}\\
E=\sum^{3}_{t=0}x(t)^2=\sum^{3}_{t=0}(t)^2+\sum^{6}_{t=3}(6-t)^2\\
P=\frac{E}{6-0}=\frac{1}{6}(\sum^{3}_{t=0}(t)^2+\sum^{6}_{t=3}(6-t)^2)
$$


## function transform
<iframe src="https://www.desmos.com/calculator/rxadxdsm8y?embed" width="800" height="800" style="border: 1px solid #ccc" frameborder=0></iframe>


## unit step function and unit impulse function 
|            |                                                                       unit step                                                                        |                                                                       unit impules                                                                       |
| :--------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------: |
|  discrcte  | $$u[n]\stackrel{def}{=}\begin{cases}1 & n\geq 0\\0 & n< 0\\\end{cases}\\u[n-n_0]\stackrel{def}{=}\begin{cases}1 & n_0\geq 0\\0 & n_0< 0\\\end{cases}$$ | $$\delta[n]\stackrel{def}{=}\begin{cases}1& n=0\\0& n\neq 0\end{cases}\\  \delta[n-n_0]\stackrel{def}{=}\begin{cases}1& n=n_0\\0& n\neq n_0\end{cases}$$ |
| continouse |                                       $$u(n)\stackrel{def}{=}\begin{cases}1 & n\geq 0\\0 & n< 0\\\end{cases}\\$$                                       |              $$ \delta(n)\stackrel{def}{=}\begin{cases}\infty & n= 0\\0 & n\neq 0\\\end{cases}\\\int_{-\infty}^{\infty}\delta(x) \ dx=1\\$$              |
|            |

## basic system properties
### memory and memoryless
#### memoryless systems
only the current signal<br>
$$
y[n]=(2x[n]-x[n]^2)^2
$$

#### memory systems
only the current signal<br>
$$
\begin{aligned}\\
&y[n]=\sum_{k=-\infty}^{n}x[k]     & \text{(accumulator)}\\
&y(t)=\int_{-\infty}^{t} x(t) \ dt & \text{(integral)}\\
&y[n]=x[n] & \text{(delay)}\\
\end{aligned}
$$


### invertibility
function is invertable
$$
\begin{aligned}\\
&y(t)=2x(t)&,&y(t)^{-1}=\frac{1}{2}x(t)\\
&y[n]=\sum_{-\infty}^{n}x[n]&,&y[t]^{-1}=x[n]-x[n-1]\\
\end{aligned}
$$
### causality
only the current and past signal are relate then it is causal system<br>
#### causal systems
$$
y(t)=x(t-1)\\
y[n]=x[n]-x[n-1]
$$
#### non-causal systems
$$
y(t)=x(t+1)\\
y[n]=x[n]-x[n+1]
$$
### stability (BIBO stable )
can find BIBO(bounded-input and bounded-output) in another word the function is diverage or not.
$$
|x(t)|\leq \infty \text{ and }|y(t)|\leq \infty \text{ for all t}
$$
#### BIBO stable
$$
y[n]=x[n]+x[n+1]
$$
#### BIBO  unstable
$$
y(t)=1.01x[n-1]\\
$$
### time invariance
the function shift input will only shift and dont have any effect 
### linearity
if $x(at)+x(bt)== x(at+bt)$ then is linearty

### test
|                                                    | memoryless | stable | causal | linaer | time invariant |
| :------------------------------------------------: | :--------: | :----: | :----: | :----: | :------------: |
|                 $$y(t)=cos(x(t))$$                 |     ✅      |   ✅    |   ✅    |   ❌    |       ✅        |
|                 $$y[n]=2x[n]u[n]$$                 |     ✅      |   ✅    |   ✅    |   ✅    |       ❌        |
|       $$y(t)=\int_{-\infty}^{t/2} x(u) du$$        |     ❌      |   ✅    |   ❌    |   ✅    |       ❌        |
|        $$y[n]=\sum_{k=-\infty}^{n} x[k+2]$$        |     ❌      |   ✅    |   ❌    |   ✅    |       ✅        |
|                  $$y(t)=x(2-t)$$                   |     ❌      |   ✅    |   ❌    |   ✅    |       ❌        |
| $$y[n]=x[n]\sum_{k=-\infty}^{\infty}\delta[n-2k]$$ |     ✅      |   ✅    |   ✅    |   ✅    |       ✅        |