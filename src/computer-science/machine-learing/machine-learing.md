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

# VAE

## VQVAE(d-vae)

# CVAE

# reforce learing

## actor-critic

## Temporal Difference error(TD-error)
