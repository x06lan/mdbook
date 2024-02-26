# signals and systems final
[SS_final_hw.pdf](../../assets/pdf/SS_Final_HW.pdf)
# 1
$$
\text{real and odd }\rightarrow \int_{-\infty}^{\infty}x(t)\ dt =0
$$
$$
\begin{aligned}
\frac{1}{2} \int_0^2 |a\sin(\pi t)|^2 dt&=1\\
a^2\int_0^2 |\sin(\pi t)|^2 dt&=2\\
a^2\int_0^2 \cos(\pi t)^2 dt&=2\\
a^2&=2
\end{aligned}\\
x(t)=\pm \sqrt{2} \sin(\pi t)
$$
# 2
$$
\begin{aligned}
a_k&=\frac{1}{5}\int_{0}^{5}x(t)e^{-jk\frac{2\pi}{5} t }\ dt\\
a_0&=\frac{1}{5}\int_{0}^{5}x(t) \ dt\\
&=\frac{5}{2}\\
a_k&=\frac{1}{5}\int_{0}^{5}x(t)e^{-jk\frac{2\pi}{5} t }\ dt\\
a_k&=\frac{1}{5}\{ x(t)\frac{e^{-jk\frac{2\pi}{5} t} }{-jk\frac{2\pi}{5} t} \} \Big|_0^5 \ dt\\
\end{aligned}
$$
# 3
## 3.a
$$
h(t)=\text{if }t\geq 1  \text{ then } e^{-2(t-1)} \text{ else } 0
$$
## 3.b
yes
$$
h(t)=0 \text{ when } t<0
$$
## 3.c
yes
$$
\int_{-\infty}^{\infty}|h(t)| \ dt=\int_{1}^{\infty}|e^{-2(t-1)}| \ dt < \infty
$$

# 4
## 4.a
