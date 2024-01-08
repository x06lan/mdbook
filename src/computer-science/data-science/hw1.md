
# hw1 110590049

tags `data`

[2023 Educational Data Mining and Applications HW1.pdf](../../assets/pdf/Educational_Data_Mining_and_Applications_HW1.pdf)

# 2.2(e)
Five number summary: min, Q1, median, Q3, max<br>

| min |  Q1   | median | Q3  | max |
| --- | :---: | :----: | --- | --- |
| 13  |  20   |   25   | 35  | 70  |
# 2.2(f)
<image src="https://imgur.com/rWMvu22.png" width="80%">


# 2.8(a)

following 2D data set<br>
x={1.4,1.6}

|     |  A1   |  A2   |
| --- | :---: | :---: |
| x1  |  1.5  |  1.7  |
| x2  |  2.0  |  1.9  |
| x3  |  1.6  |  1.8  |
| x4  |  1.2  |  1.5  |
| x5  |  1.5  |  1.0  |

## Manhattan distance
$$
d(x,y)=\sum_{i=0}^n{|x_{i}-y_{i}|}
$$

|     |  A1   |  A2   | distance |
| --- | :---: | :---: | :------: |
| x   |  1.4  |  1.6  |    0     |
| x1  |  1.5  |  1.7  |   0.2    |
| x4  |  1.2  |  1.5  |   0.3    |
| x3  |  1.6  |  1.8  |   0.4    |
| x5  |  1.5  |  1.0  |   0.5    |
| x2  |  2.0  |  1.9  |   0.9    |
## Euclidean distance
$$
d(x,y)=\sqrt[2]{\sum_{i=0}^n{(x_{i}-y_{i})^2}}
$$

|     |  A1   |  A2   | distance | rank  |
| --- | :---: | :---: | :------: | :---: |
| x   |  1.4  |  1.6  |    0     |       |
| x1  |  1.5  |  1.7  |  0.141   |   1   |
| x2  |  2.0  |  1.9  |  0.670   |   5   |
| x3  |  1.6  |  1.8  |  0.282   |   3   |
| x4  |  1.2  |  1.5  |  0.223   |   2   |
| x5  |  1.5  |  1.0  |  0.508   |   4   |
## supremum distance
$$
d(x,y)=\max_{i=0}^{n}{|x_i-y_i|}
$$

|     |  A1   |  A2   | distance | rank  |
| --- | :---: | :---: | :------: | :---: |
| x   |  1.4  |  1.6  |    0     |       |
| x1  |  1.5  |  1.7  |   0.1    |   1   |
| x2  |  2.0  |  1.9  |   0.6    |   5   |
| x3  |  1.6  |  1.8  |   0.2    |   3   |
| x4  |  1.2  |  1.5  |   0.2    |   2   |
| x5  |  1.5  |  1.0  |   0.4    |   4   |
## cosine similarity
$$
d(x,y)=\frac{x \cdot y}{||x||\times ||y||}
$$

|     |  A1   |  A2   | similarity | rank  |
| --- | :---: | :---: | :--------: | :---: |
| x   |  1.4  |  1.6  |     0      |       |
| x1  |  1.5  |  1.7  |   0.9999   |   1   |
| x2  |  2.0  |  1.9  |   0.9957   |   3   |
| x3  |  1.6  |  1.8  |   0.9999   |   2   |
| x4  |  1.2  |  1.5  |   0.9990   |   5   |
| x5  |  1.5  |  1.0  |   0.9653   |   4   |

# 2.8(b)
$$
normalize(x)=\frac{x}{\sqrt[2]{\sum_{i=0}^n{(x_{i})^2}}}
$$

|     |  A1   |  A2   | distance | rank  |
| --- | :---: | :---: | :------: | :---: |
| x   | 0.658 | 0.752 |    0     |       |
| x1  | 0.661 | 0.749 |  0.0042  |   1   |
| x2  | 0.642 | 0.789 |  0.0403  |   3   |
| x3  | 0.724 | 0.688 |  0.0919  |   4   |
| x4  | 0.664 | 0.747 |  0.0078  |   2   |
| x5  | 0.832 | 0.554 |  0.2635  |   5   |


# 3.3(a)
| Bin   | Data            |
|-------|-----------------|
| Bin 1 | 13, 15, 16      |
| Bin 2 | 16, 19, 20      |
| Bin 3 | 20, 21, 22      |
| Bin 4 | 22, 25, 25      |
| Bin 5 | 25, 25, 30      |
| Bin 6 | 33, 33 ,35      |
| Bin 7 | 35, 35, 35      |
| Bin 8 | 35, 35, 36      |
| Bin 9 | 36, 40, 45      |
| Bin 10| 46, 52, 70      |


| Bin    | Smoothed Data   |
|--------|-----------------|
| Bin 1  | 14.67, 14.67, 14.67 |
| Bin 2  | 18.33, 18.33, 18.33 |
| Bin 3  | 21.00, 21.00, 21.00 |
| Bin 4  | 24.00, 24.00, 24.00 |
| Bin 5  | 26.67, 26.67, 26.67 |
| Bin 6  | 33.67, 33.67, 33.67 |
| Bin 7  | 35.00, 35.00, 35.00 |
| Bin 8  | 35.33, 35.33, 35.33 |
| Bin 9  | 40.33, 40.33, 40.33 |
| Bin 10 | 56.00, 56.00, 56.00 |


# 3.3(b)
find the outlier value using the IQR method:
$$
IQR=Q3-Q1=35-20=15\\
\begin{aligned}{}
\text{Lower Bound} & = Q1 - 1.5 * IQR\\
& = 20 - 1.5 * 15 = 20 - 22.5 = -2.5\\
\end{aligned}\\

\begin{aligned}{}
\text{Upper Bound} & = Q3 + 1.5 * IQR\\
& = 35 + 1.5 * 15 = 35 + 22.5 = 57.5\\
\end{aligned}\\
70>\text{Upper Bound}\\
\text{70 is the outlier value}
$$
# 3.7(a)
$$
\begin{aligned}{}
\text{min-max-normalizaion}&=\frac{x-min}{max-min}\\
&=\frac{35-13}{70-13}\\
&=0.3859\\
\end{aligned}
$$
# 3.7(b)
$$
\mu=29.96,\sigma=12.7\\
\begin{aligned}{}
\text{z-index}&=\frac{x-\mu}{\sigma}\\
&=\frac{35-29.96}{12.7}\\
&=0.3968
\end{aligned}
$$

# 3.8(b)


| age | fat  |
| --- | ---- |
| 23  | 9.5  |
| 23  | 26.5 |
| 27  | 7.8  |
| 27  | 17.8 |
| 39  | 31.4 |
| 41  | 25.9 |
| 47  | 27.4 |
| 49  | 27.2 |
| 50  | 31.2 |
| 52  | 34.6 |
| 54  | 28.8 |
| 56  | 33.4 |
| 57  | 30.2 |
| 58  | 34.1 |
| 58  | 32.9 |
| 60  | 41.2 |
| 61  | 35.7 |

$$
\begin{aligned}
r&=\frac{\underset{i}{\sum}(x_{i}-\hat x)(y_{i}-\hat y)}{ \sqrt{\underset{i}{\sum}(x_{i}-\hat x)^2}\sqrt{\underset{i}{\sum}(y_{i}-\hat y)^2}}\\
&=\frac{1590.6}{\sqrt{2910}\sqrt{1256.731}}\\
&=0.8329
\end{aligned}
$$
$$
\begin{aligned}
cov(x,y)&=\frac{1}{n}\sum_{i}((x_i-E(x))(y_i-E(y))\\
&=99.41
\end{aligned}
$$

# 3.11(a)
<image src="https://imgur.com/PHobsZJ.png" width="80%">





