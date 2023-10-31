# data science
## 5v
* volume
* variety
* value
* velocity
* veracity
## data processing chain
* data
* database
* data store
* data ming
* data vu
## data warehouse
* subject oriented
* integrate
* non-volatile
* time variant

星形
雪花
實例星座
## data type


| name                                                                    | exmple           |
| ----------------------------------------------------------------------- | ---------------- |
| nominal data , unordered collection,明目                                | dog cat name     |
| ordinal data , ordered data ,次序                                       | level            |
| interval data , equal intervals,(not Ture zero)(相除 不可代表比值),區間 | 溫度             |
| ratio data , fraction data,比值                                         | float            |
| BLOB(binary large objects)                                              | image sound file |

## entropy(熵)
$$P(x)=\text{probability of x} \\
\text{space have n condition}\\
entropy(space)=-\sum_i^n(P(i)\times log_2(P(i)))$$

## Information Gain(IG)
if then entropy is geting less then it is good divide point
$$IG(S,A)=entropy(S)-\sum_i ^{A\in S} P(i|S)\times entropy(i) $$
### gini index(Impurity)
$$GI(S,A)=1-\sum_i ^{A\in S} P(i|S)^2 $$


## Quantile
Q1:small 0%~25%<br>
Q2:small 25%~50%<br>
Q3:small 50%~75%<br>
Q4:small 75%~100%(the biggest)<br>
interQuartile range:Q3-Q1<br>

## confusion matrix
$$TP:\text{predict True and is Positive}$$
$$TN:\text{predict negative and is negative}$$
$$FP:\text{predict Positive and is negative}$$
$$FN:\text{predict negative and is Positive}$$
$$TPR\text{(sensitivity)}:\frac{TP}{TP+FN}$$
$$TNR(\text{specificity}):\frac{TN}{TN+FP}$$
$$PPV:\text{(precision|positive predictive)}:\frac{TP}{TP+FP}$$
$$NPV\text{(negative predictive)}:\frac{TN}{TN+FN}$$
$$F_1=\frac{2TP}{2TP+FP+TN}$$

## correlations

$$r=\frac{\underset{i}{\sum}(x_{i}-\hat x)(y_{i}-\hat y)}{ \sqrt{\underset{i}{\sum}(x_{i}-\hat x)^2}\sqrt{\underset{i}{\sum}(y_{i}-\hat y)^2}}$$

$$r^2=\frac{(\underset{i}{\sum}(x_{i}-\hat x)(y_{i}-\hat y))^2}{{\underset{i}{\sum}(x_{i}-\hat x)^2}{\underset{i}{\sum}(y_{i}-\hat y)^2}}$$

## linear regression 
$\hat{y}=a+bx$
$$b=\frac{\underset{i}{\sum }( x_i- \bar{x})( y_i- \bar{y})}{\underset{i}{\sum }( x_i- \bar{x})}=\frac{\underset{i}{\sum }( x_i- \bar{x})( y_i- \bar{y})}{\underset{i}{\sum }( x_i- \bar{x})^2}=\frac{\frac{1}{n}\underset{i}{\sum }( x_i- \bar{x})( y_i- \bar{y})}{\frac{1}{n}\underset{i}{\sum }( x_i- \bar{x})^2}=\frac{cov(x,y)}{var(x)}$$
$a=\bar{y}-b\bar{x}$

## naive bayes 
$$P(h|\{a,b,a,c\})=P(h)*P(a|h)^2P(b|h)P(c|h)$$
$$P(\lnot h|\{a,b,a,c\})=P(\lnot h)*P(a|\lnot h)^2P(b|\lnot h)P(c|\lnot h)$$
### zero conditional 

t :possible condition number<br>
n :case number<br>
c :possble c<br>
m :virtual sample<br>

$P(a|c)=\frac{a_c+m_c\frac{1}{t}}{n_c+m_c}$


## ann

### training set
60% data
### validation set
20% data
### Testing set
20% data
### k fold cross validtion
在 K-Fold 的方法中我們會將資料切分為 K 等份，K 是由我們自由調控的，以下圖為例：假設我們設定 K=10，也就是將訓練集切割為十等份。這意味著相同的模型要訓練十次，每一次的訓練都會從這十等份挑選其中九等份作為訓練資料，剩下一等份未參與訓練並作為驗證集。

### Tanh
range (-1 ~ 1)
$f(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$
### sigmoid(logistic)
range (0 ~ 1)
$f(x)=\frac{1}{1-e^{-x}}$
### relu
range (0 ~ ∞) 
$f(x)=max(0,x)$

### softPlus
range (0 ~ ∞) 
$f(x)=\frac{e^x}{1+e^x}=\frac{1}{1+e^{-x}}$




## scale features (nomralize)

### z score normalization
standariztion
$\sigma=\text{standard deviation}$
$x'=\frac{x-\hat x}{\sigma}$

### Min Max scaling
x range 0 ~ 1
$x'=\frac{x-min(x)}{max(x)-min(x)}$

### maximum absolute scaling
range 0~1
$x'=\frac{x}{max(
|x|)}$

### Robust scaling
Q=四分位
$x'=\frac{x-median(x)}{Q3-Q1}$

## Clustering Algorithms
* Partition algorithms
    * K means clustering
    * Gaussian Mixture Model
* Hierarchical algorithms
    * Bottom-up, agglomerative
    * Top-down, divisive
### K means 
give K point move point to find position fit all data
### K-Medoids
group some point and find the mass center if the point is close merge in to the group if is far then remove from the group

### Hierarchical Clustering(Bottom-up)
merge all point by dstance of clusters
#### distance of clusters
* single-link(closest point of group)
* complete-link(farthest point of group)
* centroid(centers point of group)
* average-link (average distance between of all elements of group)
#### weight vs unweight
use point number of group as weight or averge two group distance
### DBSCAN (Bottom-up)
1. start with every point as group it self
2. if a,b group are in range of "high densty area" then merge as same group


## rule
* support(A->B)=$P(A\cap B)$
* confidence(A->B)=$P(A| B)$
* lift(A->B)=$\frac{P(A\cap B)}{P(A)P(B)}$
* AllConf(A,b)=$\frac{P(A \cap  B)}{\max(P(A),P(B))}$
* MaxConf(A,b)=$\max(P(A|B),P(B|A))$
* Kulc(A,b)=$\frac{1}{2}(P(B|A)+P(A|B))$
* Cosine(A,B)=$\frac{A \cdot B}{|A|\times |B|}$

if lift(A,B) >1 then A,B is effective

## FP tree
1. count the word number
2. sort the set by start word count
3. build tree by set
4.

## similar function


|     |  h1   |  h2   | h3  | h4  |
| --- | :---: | :---: | --- | --- |
| a   |   1   |   _   | _   | 0.5 |
| b   |  0.5  |   _   | 0.3 | _   |
| c   |   _   |  0.7  | _   | 0.4 |


### jaccard similarity
$$ 
A=\{h1,h4 \},
B=\{h1,h3 \},
C=\{h2,h4 \}\\
sim(a,b)=\frac{a\cap b}{a\cup b}=\frac{\{h1,h4\}}{\{h1,h3,h4 \}}=\frac{1}{3}
$$
### cosine similarity
$$ 
A=\begin{bmatrix}
    1\\ 0\\ 0\\0.5 \\
\end{bmatrix}
B=\begin{bmatrix}
    0.5\\ 0\\ 0.3\\ 0 \\
\end{bmatrix}
C=\begin{bmatrix}
    0 \\ 0.7\\ 0 \\ 0.4 \\
\end{bmatrix}\\
sim(A,B)=\frac{A\cdot B}{|A|\times|B|}=0.29
$$
### peason correlation coeffiecient
$$
\text{cosine similarity}(x−\hat x,y−\hat y)
$$