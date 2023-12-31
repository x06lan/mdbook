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

## odd vs even

$$
x(t)=E_v\{x(t)\}+O_d\{x(t)\}\\
$$
## even
$$
E_v\{x(t)\}=\frac{x(t)+x(-n)}{2}
$$
## odd
$$
O_d\{x(t)\}=\frac{x(t)-x(-n)}{2}
$$
## some prove
$$
\begin{aligned}\\
\int_{-\infty}^{\infty} E_v\{x(t)\}\times O_d\{x(t)\} \ dt&=\int_{-\infty}^{\infty} \frac{x(t)+x(-t)}{2}\times\frac{x(t)-x(-t)}{2} \ dt\\
&=\int_{-\infty}^{\infty}\frac{x(t)^2-x(-t)^2}{4} \ dt \\
&=\int_{-\infty}^{\infty}\frac{x(t)^2}{4} \ dt - \int_{-\infty}^{\infty}\frac{x(-t)^2}{4} \ dt\\
&=0\\
\end{aligned}\\
$$

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
the function shift input will only shift and dont have any effect <br>
#### example
$$
\begin{aligned}\\
&,&&y(t)=tx(t)&\\
\text{define } y_1(x)\text{ let } x(t)=x(t+t_0)&,&&y_1(t)=tx(t+t_0)&\\
\text{if }y_1(t)==y(t+t_0) \text{then it is invariance}&,&&\because (t+t_0)x(t+t_0)\neq tx(t+t_0)& \therefore \text{not invariance}\\

\end{aligned}

$$
### linearity
if $ ay(x(t))+b y(x(t))== y(ax(t)+bx(t))$ then is linearty

### test
|                                                    | memoryless | stable | causal | linaer | time invariant |
| :------------------------------------------------: | :--------: | :----: | :----: | :----: | :------------: |
|                 $$y(t)=cos(x(t))$$                 |     ✅      |   ✅    |   ✅    |   ❌    |       ✅        |
|                 $$y[n]=2x[n]u[n]$$                 |     ✅      |   ✅    |   ✅    |   ✅    |       ❌        |
|       $$y(t)=\int_{-\infty}^{t/2} x(u) du$$        |     ❌      |   ✅    |   ❌    |   ✅    |       ❌        |
|        $$y[n]=\sum_{k=-\infty}^{n} x[k+2]$$        |     ❌      |   ✅    |   ❌    |   ✅    |       ✅        |
|                  $$y(t)=x(2-t)$$                   |     ❌      |   ✅    |   ❌    |   ✅    |       ❌        |
| $$y[n]=x[n]\sum_{k=-\infty}^{\infty}\delta[n-2k]$$ |     ✅      |   ✅    |   ✅    |   ✅    |       ✅        |
## complex plane

$$
j=\sqrt{-1}\\
 \\
\begin{aligned}
z&=r\times e^{j\theta}\\
&=r\times (\sin( \theta) +j \cos(\theta))\\
&=r\times \sin( \theta) +j r \cos(\theta)\\
&=\alpha+j\omega\\
\end{aligned}\\
$$
## exponential signal & sinusoidal signal
$$
x(t)=Ce^{\alpha t}\\
$$


|                 |       C is real        |                                                                                                            C is complex                                                                                                            |
| :-------------: | :--------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|    a is real    | $$x(t)=Ce^{\alpha t}$$ |                                                                                                                                                                                                                                    |
| a is  imaginary |                        |                                                                                $$C=r\times e^{j\phi}\\a=j w_0 \\ x(t)=r\times e^{j(w_0 t+ \phi)}$$                                                                                 |
|  a is  complex  |                        | $$C=r_1\times e^{j\phi} \\ a=\alpha +j w_0\\ \begin{aligned} x(t)&=(r\times e^{j\phi})(e^{\alpha t+j w_0t})\\ x(t)&=r(e^{\alpha t}e^{j (w_0t+\phi )})\\ x(t)&=r \ e^{\alpha t}(\cos(w_0t+\phi )+j \sin(w_0t+\phi ))\end{aligned}$$ |

### periods
#### CT
$$
x(t)=r \ e^{j w_0 t}\\
\text{fundamental period }T_0=\frac{2\pi}{w_0}
$$
##### example
$$
x(t)=e^{j2t}+e^{j3t}\\
\text{fundamental period of }e^{j2t}=\pi\\
\text{fundamental period of }e^{j3t}=\frac{2\pi}{3}\\
\text{LCD(Least Common Denominator) of }\pi \text{ and } \frac{2\pi}{3} \text{ is } 2\pi\\
\text{fundamental period of }e^{j2t}+e^{j3t}=2\pi\\
$$
#### DT

fundamental period $T_0$ is integer that $x[n]=x[n+i\% T_0]$ for all integer $i$<br>

> $T_0$ have to be integer.<br>
> not every "sinusoidal signal" have $T_0$

$$
x[n]=r \ e^{j w_0 t}=r \ e^{j\frac{m}{N}n}\\
\text{fundamental period }T_0=N\\
\text{fundamental frequency }=\frac{2\pi}{N}\\
$$
##### example
$$
x[n]=e^{j(\frac{2\pi}{3})n}+e^{j(\frac{3\pi}{4})n}\\
\text{fundamental period of } e^{j(\frac{2\pi}{3})n}=3\\
\text{fundamental period of } e^{j(\frac{3\pi}{4})n}=8  \ \because(2\pi=\frac{24 \pi}{4})\\
\text{LCD(Least Common Denominator) of } 3 \text{ and } 8 \text{ is } 24\\
\text{fundamental period of }e^{j(\frac{2\pi}{3})n}+e^{j(\frac{3\pi}{4})n}=24\\
$$
## convolution
### CT
$$
(f*g)(t)=\int_{-\infty}^{\infty}{f(\tau)g(t-\tau) \ d\tau }
$$
### DT
$$
(f*g)[n]=\sum_{k=-\infty}^{\infty}{f[k]g[n-k] }
$$

$$
\begin{aligned}
x[n]=&
\begin{cases}
0.5^{n} &, 0\leq n\\
0 &, else
\end{cases}\\

h[n]=&
\begin{cases}
0.5^{n} &, 0\leq n<3\\
0 &, else
\end{cases}
\end{aligned}

$$

| h\x  | x[n]                | 0   | 1     | 2      | 3       | 3        |
| ---- | ------------------- | --- | ----- | ------ | ------- | -------- |
| h[n] | $$x[n]\times h[n]$$ | 1   | 0.5   | 0.25   | 0.125   | 0.0625   |
| 0    | 1                   | 1   | 0.5   | 0.25   | 0.125   | 0.0625   |
| 1    | 0.5                 | 0.5 | 0.25  | 0.125  | 0.0625  | 0.03125  |
| 2    | 0.25                | 0.5 | 0.125 | 0.0625 | 0.03125 | 0.015625 |
| 3    | 0                   | 0   | 0     | 0      | 0       | 0        |
| 4    | 0                   | 0   | 0     | 0      | 0       | 0        |

$$
\begin{aligned}
(x*h)[0]&=x[0]\times h[0]\\
(x*h)[1]&=x[0]\times h[1]+x[1]\times h[0]\\
(x*h)[2]&=x[0]\times h[2]+x[1]\times h[1]+x[2]\times h[0]\\
\end{aligned}
$$

### commutative
$$
\begin{aligned}
x(t)*h(t)&=h(t)*x(t)\\
\int_{-\infty}^{\infty}{x(\tau)h(t-\tau) \ d\tau }&=\int_{-\infty}^{\infty}{h(\tau)x(t-\tau) \ d\tau }\\
\end{aligned}
$$

### distributive
$$
\begin{aligned}
x(t)*(h_1(t)+h_2(t))&=x(t)*h_1(t)+x(t)*h_2(t)\\
\end{aligned}
$$
### associative
$$
\begin{aligned}
x(t)*(h_1(t)*h_2(t))&=(x(t)*h_1(t))*h_2(t)\\
\end{aligned}
$$


<!-- <iframe src="https://phiresky.github.io/convolution-demo/" width="100%" height="800px"> -->

## LTI(Linear Time-Invariant)
### Linear
$$
\begin{aligned}
y(t)&=x(t)*h(t)\\
    &=\int_{-\infty}^{\infty} {x(t-\tau)h(\tau) } \ d \tau\\
    &=\int_{-\infty}^{\infty} {x(\tau)h(t-\tau) } \ d \tau\\

\end{aligned}
$$

### Time-invariant
$$
\begin{aligned}
y(t)&=x(t)*h(t)\\
y(t-k)&=x(t-k)*h(t)\\
\end{aligned}
$$

## LTI systems and convolution

### stability for LTI Systems
$$
\text{if }|x(t)|\text{ is bounded, then }|y(t)|\text{ is also bounded.}\\
\text{Sufficient condition for a continuous-time LTI system to be stable}
$$
### Unit Step Response of an LTI System
#### CT
$$
\begin{aligned}
y[n]&=h[n]*u[t]\\
&=\int_{-\infty}^{\infty}u[n-\tau]h[\tau] \ d \tau \\
&=\int_{-\infty}^{n} h[\tau] \ d \tau \\
\end{aligned}\\
h[n]=y[n]-y[n-1]
$$
#### DT
$$
\begin{aligned}
y(t)&=h(t)*u(t)\\
&=\sum_{-\infty}^{\infty}u(t-\tau)h(\tau) \ d \tau \\
&=\sum_{-\infty}^{t}h(\tau) \ d \tau \\
\end{aligned}\\
h(t)=y'(t)
$$

## eigen function and eigen value of LTI systems
The response of an LTI system to a eigen function is the same eigen function with only a change in amplitude(eigen value)

$$
x(t) \rightarrow H(t)x(t)\\
x(t)\text{ is eigenfunction }\\
H(t)\text{ is eigen value}\\
$$
### The Response of LTI Systems to Complex Exponential Signals
$$
x(t)=e^{st}\\
\begin{aligned}
y(t)&=h(t)*x(t)\\
&=\int_{-\infty}^{\infty}h(\tau)x(t-\tau) \ dt\\
&=\int_{-\infty}^{\infty}h(\tau)e^{s(t-\tau)} \ dt\\
&=e^{st}\int_{-\infty}^{\infty}h(\tau)e^{-s\tau} \ dt\\
\end{aligned}\\
H(t)=\int_{-\infty}^{\infty}h(\tau)e^{-s\tau} \ dt
$$
#### example
$$
x(t)=e^{j2t}\\
y(t)=e^{j2(t-3)}=e^{j6}e^{j2t}\\
H(t)=\int_{-\infty}^{\infty}\delta(\tau-3)e^{-s\tau} \ dt=e^{-3s}\\
$$

## system

### delay system
$$
x(t) *\delta(t-t_0) = x(t-t_0)\\
x[t] *\delta[t-t_0] = x[t-t_0]\\
$$

### difference system
$$
x[n] * \delta[t-t_0] = x[t-t_0]
$$

### accumulation system
$$
y[n]  = \sum_{m-\infty}^{n} x[m]
$$

## example
$$
\int_{T_0}e^{jw_0t} \ dt
$$
$$
\int_{T_0}e^{jw_0t} \ dt
$$
