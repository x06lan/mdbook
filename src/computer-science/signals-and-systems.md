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


## unit step function
$$
u[n]\stackrel{def}{=}
\begin{cases}
1 & n\geq 0\\
0 & n< 0\\
\end{cases}\\
$$

## unit impulse function 
$$
\int_{-\infty}^{\infty}\delta(x) \ dx=1\\
\delta[n]\stackrel{def}{=}
\begin{cases}
1& n=0\\
0& n\neq 0
\end{cases}\\
\delta[n-n_0]=
\begin{cases}
1& n=n_0\\
0& n\neq n_0
\end{cases}\\
$$