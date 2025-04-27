# GAN

# WGAN

## WGAN-GP
### Lipschitz continuous function
$$
K > 0 \\
|f(x)−f(y)| \leq K || x−y || \\
$$
### 1-Lipschitz continuity
$$
|f(x)−f(y)| \leq || x−y || \\
$$
### mean value theorem
if $f$ is differentiable function then $\exist c \in (b,a)$ 

$\exist \alpha \in (0,1) \rightarrow c=\alpha (a-b)+b$ 
$$
\begin{aligned}
f'(c)&=\frac{f(a)-f(b)}{a-b}\\
f(a)-f(b)&=f'(\alpha (a-b)+b)\times (a-b)\\
\end{aligned}
$$

### gradient penalty
by let $f'(\alpha (x-y)+y)$ close to 1 the $f$ function can satisfy 1-Lipschitz requires
$$
\begin{aligned}
|f(x)−f(y)| &\leq K|| x−y || \\
|f'(c)\times (x-y)| &\leq K || x−y || \\
||f'(c)|| \times| x-y| &\leq K\times || x−y || \\
||f'(\alpha (x-y)+y)|| \times| x-y| &\leq K\times || x−y || \\
||f'(\alpha (x-y)+y)|| \times| x-y| &\leq || x−y || \\
\end{aligned}
$$



```py
# https://github.com/Lornatang/WassersteinGAN_GP-PyTorch/blob/f2e2659089a4fe4cb7e1c4edeb5c5b9912e9c348/wgangp_pytorch/utils.py#L39
def calculate_gradient_penalty(model, real_images, fake_images, device,use_refiner):
    """Calculates the gradient penalty loss for WGAN GP"""
    # Random weight term for interpolation between real and fake data
    alpha = torch.randn((real_images.size(0), 1, 1 , 1), device=device)
    # Get random interpolation between real and fake data
    interpolates = (alpha * real_images + ((1 - alpha) * fake_images)).requires_grad_(True)

    _, interpolates_real = model(interpolates,return_feature=False,use_refiner=use_refiner)
    grad_outputs = torch.ones_like(interpolates_real, device=device)

    # Get gradient w.r.t. interpolates
    gradients = torch.autograd.grad(
        outputs=interpolates_real,
        inputs=interpolates,
        grad_outputs=grad_outputs,
        create_graph=True,
        retain_graph=True,
        only_inputs=True,
    )[0]
    gradients = gradients.reshape(gradients.size(0), -1)
    gradient_penalty = torch.mean((gradients.norm(2, dim=1) - 1) ** 2)
    return gradient_penalty
```


# CAN(GAN base)

