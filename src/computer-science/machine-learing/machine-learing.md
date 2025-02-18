# machine-learing

# resnet

# residual block(skip-connection)

# transformer

## attention

### self attention

transformer encoder

### cross attention

transformer decoder

### causal attention

# CLIP


```py
class Clip(nn.Module):
    def __init__(self,motion_dim=75,music_dim=438,feature_dim=256):
        super(Clip, self).__init__()

        self.motion_encoder = MotionEncoder(input_channels=motion_dim,feature_dim=feature_dim)
        self.music_encoder = MusicEncoder(input_channels=music_dim,feature_dim=feature_dim)

        self.motion_project = nn.Linear(feature_dim, feature_dim)
        self.music_project = nn.Linear(feature_dim, feature_dim)

        self.temperature = nn.Parameter(torch.tensor(1.0))

        self.criterion = nn.CrossEntropyLoss()

    def forward(self, motion:Tensor, music:Tensor):
        assert motion.shape[1] == music.shape[1]

        b,s,c= motion.shape

        motion_features = self.motion_encoder(motion)
        music_features = self.music_encoder(music)

        motion_features =F.normalize( self.motion_project(motion_features),p=2,dim=-1)
        music_features = F.normalize( self.music_project(music_features),p=2,dim=-1)


        # relation=(motion_features@music_features.T)*(1.0 / math.sqrt(c))

        # batch matrix multiplication and .mT is batch transpose matrix
        logits=torch.bmm(motion_features,music_features.mT)*self.temperature

        labels=torch.arange(s).repeat(b,1).to(motion.device)

        loss_motion = self.criterion(logits, labels)
        loss_music = self.criterion(logits.mT, labels)

        loss=(loss_motion+loss_music)/2

        return (motion_features,music_features),(loss,loss_motion,loss_music)
```

# CAN(GAN base)

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
