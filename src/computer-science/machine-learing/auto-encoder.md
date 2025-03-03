
# AE
![AE from https://lilianweng.github.io/posts/2018-08-12-vae/](https://imgur.com/CDEzbh3.png)
# VAE
![VAE from https://lilianweng.github.io/posts/2018-08-12-vae/](https://imgur.com/ZSRdtWg.png)
## reparameterization trick

Assuming the distribution of the output is a Gaussian distribution, the model only predicts the mean ($\mu$) and std ($\sigma$). We then sample the latent variable from this Gaussian distribution. The sample latent distribution parameters should match the true distribution, which is enforced using the KL divergence.

## VAE loss

### Evidence Lower Bound (ELBO)

We want replace $p_{\theta}(z|x)$ with $q_{\phi}(z)$ since we dont have `GT` of $p_{\theta} (z|x)$

$$
\begin{aligned}
\log p_\theta(x) &= E_{(q_\phi)} [\log p_\theta (x)]\\
&= E_{q_\phi(z)} [\log (\frac{p_\theta (x,z)}{p_\theta (z|x)})]\\
&= E_{q_\phi(z)} [\log (\frac{p_\theta (x,z)}{p_\phi(z)}\frac{p_\phi(z)}{p_\theta (z|x)})]\\
&= E_{q_\phi(z)} [\log (\frac{p_\theta (x,z)}{p_\phi(z)})]+E_{q_\phi(z)}[\log (\frac{p_\phi(z)}{p_\theta (z|x)})]\\
&= E_{q_\phi(z)} [\log (\frac{p_\theta (x,z)}{p_\phi(z)})]+KL(q_{\phi}(z)||p_{\theta}(z|x))\\
\log p_\theta(x)&= {\color{orange}E_{q_\phi(z)} [\log (\frac{p_\theta (x,z)}{p_\phi(z)})]}+KL(q_{\phi}(z)||p_{\theta}(z|x))\\
\log p_\theta(x)&= {\color{orange}\mathcal{L}_{ELBO}}+KL(q_{\phi}(z)||p_{\theta}(z|x))\\
{\color{orange}\mathcal{L}_{ELBO}} &=\log p_\theta(x) - KL(q_{\phi}(z)||p_{\theta}(z|x))\\
\end{aligned}
$$

<!-- $$
\begin{aligned}
KL(q_\phi(z|x),p(z|x))&=E_q[\log q_\phi(z∣x)-\log p(z|x)]\\
&=E_q​[\log q_\phi​(z∣x)−\log (\frac{p(z,x)}{p(x)})]\\
&=E_q[\log q_\phi(z∣x)−(\log p(z,x)-\log p(x))]\\
&=E_q[\log q_\phi(z∣x)−\log p(z,x)+\log p(x)]\\
&=E_q[\log q_\phi(z∣x)−\log p(z,x)]+\log p(x)\\
&=E_q​[\log q_\phi​(z∣x)−\log p_\phi​(x∣z)p(z)]+\log p(x) \\
\log p(x) &=E_q​[\log q_\phi​(z∣x)−\log p_\theta(x∣z)p(z)] + KL(q_\phi(z|x),p(z|x)) \\

\end{aligned}
$$

$$
\begin{aligned}
\mathcal{L}_\text{ELBO}&=E_q​[\log p_\theta(x∣z)p(z)−\log q_\phi​(z∣x)]\\
&=E_q​[\log p_\theta​​(x∣z)+\log p(z)−\log q_\phi​(z∣x)]\\
&=E_q​[\log p_\theta​​(x∣z)]+E_q​[\log p(z)−\log q_\phi​(z∣x)]\\
&=E_q​[\log p_\theta​(x∣z)]+KL(p(z),q_\phi​(z∣x))\\
\end{aligned}
$$ -->

<!-- $$
\begin{align}
  
\log p(x) & = KL(q(z)\|p(z|x))+
{\color{orange}{
\mathbb{E}_{z\sim q}\left[\log \frac{p(x,z)}{q(z)}\right]}
}\\
\log p(x) & =KL(q(z)\|p(z|x))+{\color{orange}{
\mathbb{E}_{z\sim q}\left[\log p(x,z) - \log q(z)\right]}
}\\
 \log p(x) & =KL(q(z)\|p(z|x))+\color{orange}{{\mathcal{L}_\text{ELBO}}}\\
\color{orange}{\mathcal{L}_\text{ELBO}} & =\log p(x) - KL(q(z)\|p(z|x))\\

\end{align}
$$ -->

### base on difference condition KL divergence can simplify to difference term 

- Variational Inference
- Importance Sampling to ELBO
- Variational EM

refs
- [kvfrans](https://kvfrans.com/deriving-the-kl/)
- [odie2630463](https://odie2630463.github.io/2018/08/21/vi-1/)
- [bobondemon](https://bobondemon.github.io/2024/07/18/%E7%B4%80%E9%8C%84-Evidence-Lower-BOund-ELBO-%E7%9A%84%E4%B8%89%E7%A8%AE%E7%94%A8%E6%B3%95/)

# VQVAE(d-vae)
[Variational Autoencoder (Kingma & Welling, 2014)](https://arxiv.org/abs/1312.6114)

## quantise bottleneck

![](https://imgur.com/6MiZYhw.png)
- random init centroids
- find the nearest centroids of each unquantise vector
  - if quantise have low usage then random init a new centroids
- calculate average center of unquantise vector
- Exponential Moving Average Update between new centroid and old centroid

## loss

- VQ loss: The L2 error between the embedding space and the encoder outputs.
- Commitment loss: A measure to encourage the encoder output to stay close to the embedding space and to prevent it from fluctuating too frequently from one code vector to another.
- where $\text{sg}[.]$ is the `stop_gradient` operator.

$$
L = \underbrace{\|\mathbf{x} - D(\mathbf{e}_k)\|_2^2}_{\textrm{reconstruction loss}} + 
\underbrace{\|\text{sg}[E(\mathbf{x})] - \mathbf{e}_k\|_2^2}_{\textrm{VQ loss}} + 
\underbrace{\beta \|E(\mathbf{x}) - \text{sg}[\mathbf{e}_k]\|_2^2}_{\textrm{commitment loss}}
$$

# CVAE
