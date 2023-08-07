# NERF model

## model genera
### HyperDiffusion: Generating Implicit Neural Fields with Weight-Space Diffusion
[paper](https://arxiv.org/pdf/2303.17015.pdf)
![](https://hackmd.io/_uploads/B1swT78s3.png)
overfit the `MLP` to describe the 3d mesh then use the `diffustion model` to lean the associate of  `weight`、`bais`and the string
#### training time
 3-layer 128-dim MLPs contain ≈ 36k parameters, which are flattened and tokenized for diffusion. We use an `Adam optimizer` with batch size 32 and initial learning rate of $2e^{−4}$, which is reduced by 20% every 200 epochs. We train for ≈ 4000 epochs until convergence, which takes ≈ 4 days on a single A6000 GPU


### GRAF: Generative Radiance Fields for 3D-Aware Image Synthesis
[link](https://autonomousvision.github.io/graf/)
![](https://hackmd.io/_uploads/r17wI48o2.png)
use GAN and NERF to ganerative the 3D model 

generator : input direaction and position and `style latent space vector` return color and density;<br>
defector: input the image that render by volume rendering by genertor and real image predict loss;

### nvdiffrec
[link](https://nvlabs.github.io/nvdiffrec/)
![](https://hackmd.io/_uploads/Syos71ai3.png)
use instant-nerf as nerf base and use [DMTet](https://nv-tlabs.github.io/DMTet/) to reconstruct the 3D mesh. The render image by 3D mesh with neural genera `PBR` texture compare to the origin sample .



## mics
### LERF: Language Embedded Radiance Fields
[link](https://www.lerf.io/)
![](https://hackmd.io/_uploads/HJMm4IIjn.png)
#### CLIP
decode text or image to the same `latent space`
#### Multiscale CLIP Preprocessin
slice traing image to diffrent size of image and use as `ground truth`
#### LERF
input :image <br>
output :rgb、density 、`DINO feature`、`CLIP feature` <br>
By find `cosine similarity` the input text `CLIP feature`and the LERF predict `CLIP feature` can show the connection between the text and NERF scene; 


