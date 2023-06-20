---
description: video edit
---

# ffmpeg

**tags: `tool`**

## ffmpeg

### get all frame

```bash
//%03d 如果小於三位數以三位數呈現
ffmpeg -i "path.mp4" "path_%03d.jpg"

```

### get fps

```bash
ffmpeg -i "file"
```

### images to video

```bash
ffmpeg -i "%03d.png" -c:v libx264 -vf fps=25 -pix_fmt yuv420p "out.mp4"

```

### png to gif

```bash
ffmpeg -i %04d.png -vf palettegen=reserve_transparent=1 palette.png
ffmpeg -framerate 25 -i %04d.png -i palette.png -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting treegif.gif
```

### m4a to mp3

```bash
ffmpeg -i in.m4a -c:v copy -c:a libmp3lame -q:a 4 out.mp3
```

### cut video

4:00\~4:10

```bash
ffmpeg -ss 00:04:00 -i qg.mp4 -to 00:04:10 -c copy output.mp4
```

### replace aduio on video

```bash
ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest output.mp4
```

### Add audio

```bash
ffmpeg -i video.mkv -i audio.mp3 -map 0 -map 1:a -c:v copy -shortest output.mkv
```
