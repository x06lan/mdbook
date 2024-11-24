# Deferred Rendering
## old way
![](https://imgur.com/UWUJ7dz.png)

The old render pipeline used to directly transport the rendered pixel results to the screen, without providing a way to save the rendered image.

Before using Deferred Rendering, we used to calculate the mesh information required for lighting in one shader. This method is efficient when there is a constant number of lights in the scene, as we only need to run one shader for each model to properly apply lighting.

But we have 2 defect
1. The number of lights in the shader needs to be constant because the shader has to be compiled at runtime for each frame. 
2.  The same information used to calculate lighting for a mesh (such as mesh normal and mesh color) cannot be shared with another shader, such as a post-processing shader. Therefore, the same information needs to be recalculated in each shader that uses it.


## framebuffer
![](https://ars.els-cdn.com/content/image/3-s2.0-B978012415992100002X-f02-01-9780124159921.jpg)

The frame buffer is a hardware implementation in the GPU that can be used as a temporary buffer to store the rendered results. It can also save the results back to the texture memory in the GPU.

With the frame buffer, we can render the information that we will use multiple times and reuse it from the texture memory, rather than recalculating it each time.
## deferred lighting
### shadow
A shadow is created when one mesh occludes another in the path of a light source. The way to achieve this is to render a depth texture and then render the closest mesh in the path of the light source. This is done repeatedly for each light source, and the resulting images are saved as textures in a framebuffer.
<!-- ![](https://learnopengl.com/img/advanced-lighting/shadow_mapping_theory.png) -->
![](https://learnopengl.com/img/advanced-lighting/shadow_mapping_theory_spaces.png)

By comparing the depth of a mesh to the closest depth to the light source, we can determine whether the mesh is the closest or not.
### shadow projection
![](https://learnopengl.com/img/advanced-lighting/shadow_mapping_projection.png)

1. orthographic: use on direction light like sun.
1. prespective: use on point light like flash.
### lighting compose
The deferred lighting is based on the G-buffer (which stores information like position and normal on a texture), and calculates the lighting in screen space. Each light is rendered as a separate layer. However, there is a problem with adding lighting layer by layer in the same texture, as it can cause race conditions due to simultaneous reading and writing.


![](https://i.imgur.com/gy3TraG.jpg)

Interestingly, when the VRAM in GPU is fast enough, which means that reading is faster than writing, the race condition may not occur. This is why we were initially confused about this problem, as it did not show up on my computer but did on another computer.

| Lighting Type                 | Image                           |
|-------------------------------|---------------------------------|
| Point Light                   | ![](https://i.imgur.com/oYVRTKw.jpg) |
| Point and Direction Light      | ![](https://i.imgur.com/HkrBqJ4.jpg) |
| Point, Direction, and Ambient Light | ![](https://i.imgur.com/hyXhGZ8.jpg) |



<!-- point depthMap
![point depthmap](https://i.imgur.com/76BaHsi.jpg) -->




## postprocess
the postprocess effect on render often relia on the mesh information  for example like outliner need a mesh id mask for edge delection.

distance fog from minecraft
![](https://hackmd.io/_uploads/r1wPc_oVn.jpg)
our scene
![](https://doc.qt.io/qt-6/images/fog_depthnear_lower.jpg)


use distance to blend with fog color because use the deferred render it is easy to acess depth and position from scene 
## deferred rendering
:::spoiler images
each G-Buffer

| Render Type | Image                               |
|-------------|-------------------------------------|
| Albedo      | ![](https://i.imgur.com/TvQfUxt.png) |
| Normal      | ![](https://i.imgur.com/NO9KLDz.png) |
| Arm         | ![](https://i.imgur.com/Sp9m7D3.png) |
| Depth       | ![](https://i.imgur.com/pJXs8d5.png) |
| ID          | ![](https://i.imgur.com/Lg1j3ls.png) |
| Lighting    | ![](https://i.imgur.com/t9Pnh6o.png) |

:::

