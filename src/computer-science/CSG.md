tags: `3D` `js`

# CSG (Constructive Solid Geometry) note
# vector
> ## values
> x,y,z for a point or normal
> ## clone
> return new same vector
> ## negated
> return new same negated
> ## plus(a)
> return new vector add a vector
> ## minus(a)
> this-a
> ## times(a)
> 乘a
> ## divideBy(a)
> 除a
> ## dot(a)
> 內積
> ```javascript
> return x*a.x+y*a.y+z*a.z
> ```
> ## lerp(a,t)
> t通常小於1
> 用來表示this 到a 之間的某個數
> ```javascript
> this-(this-a)*t
> ```
> ## len
> ## unit 
> 單位為1的向量
> ## cross
> 降階值
> ```javascript
> [[x  ,y   ,z  ],
> [a.x,a.y ,a.z]]
> ```


# vertex

> ## value
> 1. pos( vector)
> 2. noraml (vector)
> ## clone
> ## flip
> 修改normal 方向
> ## interpolate(a,t)
> 用lerp的方式產生一個介於this 與a 之間的pos and normal並用 t控制落點

# plane

> ## value
> 1. normal 面的髮線
> 2. w
> 3. epsilon 可接受誤差值
> ## clone
> ## flip
> change the side of the normal
> ## formpoints(a,b,c)
> create plane by 3 point vector 
> and w is plane dot with fisrt verctor(position)
> ## splitPolygon(polygon, coplanarFront, coplanarBack, front, back)
> 以這個面為基準將多個面區分為語法線面相同的front 或back
> 如果有交集則切割面

# polygon

> ## valuemagnitude
> 1. vertices(lot of vertex)
> 2. shared
> 3. plane
> 4. EPSILON(對於點是否在面上的容忍值)
> ## clone
> ## flip
> flip vertex
> flip plane

# node
> bsp:binary space partitioning tree

> 利用每個面的髮線區切割空間，如果空間在髮線的背面則視為true(或是包含)

> ![](https://i.imgur.com/EaayJ5Q.png)


> ## value
> 1. plane
> 2. front=node
> 3. back=node
> 4. polygons=[]
> ## clone
> ## invert
> flip polygons
> flip plane
> flip back and front
> and change back to front 、 change front to back
> ## clip Polygons
> ## clipTo(bsp)

> bsp:binary space partitioning tree
> ![](https://i.imgur.com/OfUwEIp.png)

> a和b的 bsp tree 合併=a-b的截面
> ```javascript
> +-------+            +-------+
> |       |            |       |
> |   A   |            |       |
> |    +--+----+   =   |       +
> +----+--+    |       +----+
>     |   B   | 
>     |       |
>     +-------+

> ```

> ## allPolygons
> return combon all polygon from back and front to one array


# Boolean operations

> ## union
> ```javascript
> a.clipTo(b);
> b.clipTo(a);
> b.invert();
> b.clipTo(a);
> b.invert();
> a.build(b.allPolygons());
> ```
> my way
> ```javascript
> a.clipTo(b);
> b.clipTo(a);
> a.build(b.allPolygons());
> ```
> ## subtract
> ```javascript
> a.invert();
> a.clipTo(b);
> b.clipTo(a);
> b.invert();
> b.clipTo(a);
> b.invert();
> a.build(b.allPolygons());
> a.invert();
> ```

> my way
> ```javascript
> a.invert();
> a.clipTo(b);
>
> b.invert();
> b.clipTo(a);
> a.invert();
> a.build(b.allPolygons());
> ```
> ## intersect

> ```javascript
> a.invert();
> b.clipTo(a);
> b.invert();
> a.clipTo(b);
> b.clipTo(a);
> a.build(b.allPolygons());
> a.invert();
> ```

> another way to intersect
> ```javascript
> a.invert();
> b.clipTo(a);
>
> b.invert();
> a.clipTo(b);
>
> a.build(b.allPolygons());
> a.invert();
> ```

 ## links
* [other way](http://groups.csail.mit.edu/graphics/classes/6.837/F98/talecture/)
* [paper link](https://static1.squarespace.com/static/51bb9790e4b0510af19ea9c4/t/51bf7c34e4b0a897bf550945/1371503668974/CSG_report.pdf)
* [github](https://github.com/x06lan/three_face_boolean)