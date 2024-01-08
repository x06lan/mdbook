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
* data value
## data warehouse
* subject oriented
* integrate
* non-volatile
* time variant
## data warehouse type
* 星形
* 雪花
* 實例星座

## data type


| name                                                                    | exmple           |
| ----------------------------------------------------------------------- | ---------------- |
| nominal data , unordered collection,明目                                | dog cat name     |
| ordinal data , ordered data ,次序                                       | level            |
| interval data , equal intervals,(not Ture zero)(相除 不可代表比值),區間 | 溫度             |
| ratio data , fraction data,比值                                         | float            |
| BLOB(binary large objects)                                              | image sound file |




# Quantile
Q1:small 0%~25%<br>
Q2:small 25%~50%<br>
Q3:small 50%~75%<br>
Q4:small 75%~100%(the biggest)<br>
interQuartile range:Q3-Q1<br>

# confusion matrix
|                         | Predicted Positive | Predicted Negative |
| ----------------------- | ------------------ | ------------------ |
| Actual Positive (True)  | TP                 | FN                 |
| Actual Negative (False) | FP                 | TN                 |

$$TPR\text{(recall | sensitivity)}:\frac{TP}{TP+FN}$$
$$FPR=\frac{FP}{TN+FP}$$
$$TNR(\text{specificity}):\frac{TN}{TN+FP}$$
$$PPV:\text{(precision | positive predictive)}:\frac{TP}{TP+FP}$$
$$NPV\text{(negative predictive)}:\frac{TN}{TN+FN}$$
$$ F_1\text{ score(F-measure | F-score)}=\frac{2TP}{2TP+FP+TN}=\frac{2}{\frac{1}{precision}+\frac{1}{recall}}$$

## ROC curve
<image src="https://upload.wikimedia.org/wikipedia/commons/6/6b/Roccurves.png" width="80%">


# correlations


$$cov(x,y)=\frac{\underset{i}{\sum}(x_{i}-\hat x)(y_{i}-\hat y)}{n}$$
$$r=\frac{\underset{i}{\sum}(x_{i}-\hat x)(y_{i}-\hat y)}{ \sqrt{\underset{i}{\sum}(x_{i}-\hat x)^2}\sqrt{\underset{i}{\sum}(y_{i}-\hat y)^2}}$$

$$r^2=\frac{(\underset{i}{\sum}(x_{i}-\hat x)(y_{i}-\hat y))^2}{{\underset{i}{\sum}(x_{i}-\hat x)^2}{\underset{i}{\sum}(y_{i}-\hat y)^2}}$$

# linear regression 
$\hat{y}=a+bx$
$$b=\frac{\underset{i}{\sum }( x_i- \bar{x})( y_i- \bar{y})}{\underset{i}{\sum }( x_i- \bar{x})}=\frac{\underset{i}{\sum }( x_i- \bar{x})( y_i- \bar{y})}{\underset{i}{\sum }( x_i- \bar{x})^2}=\frac{\frac{1}{n}\underset{i}{\sum }( x_i- \bar{x})( y_i- \bar{y})}{\frac{1}{n}\underset{i}{\sum }( x_i- \bar{x})^2}=\frac{cov(x,y)}{var(x)}$$
$a=\bar{y}-b\bar{x}$

# similar function
|     |  h1   |  h2   | h3  | h4  |
| --- | :---: | :---: | --- | --- |
| a   |   1   |   _   | _   | 0.5 |
| b   |  0.5  |   _   | 0.3 | _   |
| c   |   _   |  0.7  | _   | 0.4 |


## jaccard similarity
$$ 
A=\{h1,h4 \},
B=\{h1,h3 \},
C=\{h2,h4 \}\\
sim(a,b)=\frac{a\cap b}{a\cup b}=\frac{\{h1,h4\}}{\{h1,h3,h4 \}}=\frac{1}{3}
$$
## cosine similarity
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
## peason correlation coeffiecient
$$
\text{cosine similarity}(x−\hat x,y−\hat y)
$$
# Feature Selection Methods
* Filter methods
* Wrapper methods
* Embedded methods

<image src="https://imgur.com/4Kv4iL6.png" width="80%">


# Classification

## Decision Tree 
<image src="https://imgur.com/vdxbW5E.png" width="80%">


### entropy(熵)
$$P(x)=\text{probability of x} \\
\text{space have n condition}\\
entropy(space)=-\sum_i^n(P(i)\times log_2(P(i)))$$

### Information Gain(IG)
if then entropy is geting less then it is good divide point
$$IG(S,A)=entropy(S)-\sum_i ^{A\in S} P(i|S)\times entropy(i) $$
#### gini index(Impurity)
$$GI(S,A)=1-\sum_i ^{A\in S} P(i|S)^2 $$
### random forest(Bootstrap Aggregation for decision tree)

use mutilple random Decision Tree to vote asnwer
<image src="https://imgur.com/ISGENWw.png" width="80%">

<image src="https://imgur.com/XLte186.png" width="80%">

## naive bayes 

<image src="../../assets/image/Bayes_Theorem.gif" width="80%">

$$P(h|\{a,b,a,c\})=P(h)*P(a|h)^2P(b|h)P(c|h)$$
$$P(\lnot h|\{a,b,a,c\})=P(\lnot h)*P(a|\lnot h)^2P(b|\lnot h)P(c|\lnot h)$$
### zero conditional(when probability is zero)

t :possible condition number<br>
n :case number<br>
c :possble c<br>
m :virtual sample<br>

$$
P(a|c)=\frac{a_c+m_c\frac{1}{t}}{n_c+m_c}
$$
### Bayesian Network
Bayesian networks are directed and acyclic, whereas Markov networks are undirected and could be cyclic. 

<image src="https://codesachin.files.wordpress.com/2017/03/bayesian-networks-a-brief-introduction-7-638.jpg" width="80%">



## SVM(Support Vector Machines)
<image src="https://imgur.com/BOIczf9.png" width="80%">

### linear separable SVM
<image src="https://imgur.com/DbyeGOz.png" width="80%">

### linear inseparable SVM
map data to higher dimension 

<image src="https://imgur.com/FTRlnAw.png" width="80%">


## KNN( K Nearest Neighbor)

* KNN 的演算法步驟如下：
    1. KNN 中的 K 代表找出距離你最近的 K 筆資料進行分類。
    2. 假設 K 是 3，代表找出前三筆相近的資料。
    3. 當這 K 筆資料被選出後，就以投票的方式統計哪一種類的資料量最多，然後就被分到哪一個類別。


## Linear Classifiers
### Logistic Regression
$$\frac{y}{1-y}= w^T x + b$$

### Gradient Descent
<image src="https://imgur.com/iaNLmgC.png" width="80%">

### Coordinate Descent
Coordinate descent updates one parameter at a time, while gradient descent attempts to update all parameters at once

<image src="https://imgur.com/hr0emoK.png" width="80%">

## Improve Classification Accuracy
### Bagging:Bootstrap aggregating
給定一個大小為 n 的訓練集 D，Bagging算法從中均勻、有放回地（即使用自助抽樣法）選出 m個大小為 $n'$的子集 $D_i$，作為新的訓練集。在這 m 個訓練集上使用分類、回歸等算法，則可得到 m 個模型，在透過取平均值、取多數票等方法，即可得到Bagging的結果。 

### Boosting
1. A series of k classifiers are iteratively learned
1. After a classifier Mi is learned, set the subsequent classifier, Mi+1, to pay more
1. attention to the training tuples that were misclassified by Mi
1. The final M* combines the votes of each individual classifier, where the weight of each classifier's vote is a function of its accuracy


## Imbalanced Data Sets
* **Oversampling**: Oversample the minority class.
* **Under-sampling**: Randomly eliminate tuples from majority class
* **Synthesizing**: Synthesize new minority classes

<image src="https://imgur.com/M2gR4vt.png" width="80%">


* Threshold-moving 
  * Move the decision threshold, t, so that the rare class tuples are easier to classify, and hence, less chance of costly false negative errors

<image src="https://imgur.com/CqhipX8.png" width="80%">

# MLP(ANN)

* 人工神经元Artificial Neural Unit
* 多层感知机Multi-Layer Perception(MLP)
* 激活函数Activation function
* 反向传播Back Propagation
* 学习率Learning Rate
* 损失函数Loss Function（MSE均方误差，Cross Entropy（CE）交叉熵：softmax函数）
* 权值初始化Initialization (Xavier初始化，MSRA初始化）
* 正则化Regularization（Dropout随机失活）
$$y= w^T x + b$$
* training set 
  * 60% data
* validation set
  * 20% data
* Testing set
  * 20% data
## k fold cross validtion
在 K-Fold 的方法中我們會將資料切分為 K 等份，K 是由我們自由調控的，以下圖為例：假設我們設定 K=10，也就是將訓練集切割為十等份。這意味著相同的模型要訓練十次，每一次的訓練都會從這十等份挑選其中九等份作為訓練資料，剩下一等份未參與訓練並作為驗證集。

## Activation Function
| Activation Function | Formula                                                        | Range            |
| ------------------- | -------------------------------------------------------------- | ---------------- |
| Tanh                | $$f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$                   | $$ (-1, 1)    $$ |
| Sigmoid (Logistic)  | $$f(x) = \frac{1}{1 + e^{-x}}             $$                   | $$ (0, 1)     $$ |
| ReLU                | $$f(x) = \max(0, x)                       $$                   | $$ (0, \infty)$$ |
| SoftPlus            | $$f(x) =\frac{e^x}{1+e^x}= \frac{1}{1 + e^{-x}}             $$ | $$ (0, \infty)$$ |



# scale features (nomralize)

Certainly! Here's a markdown table summarizing the formulas for different types of feature scaling:

| Scaling Method           | Formula                                                                 | Range                  |
| ------------------------ | ----------------------------------------------------------------------- | ---------------------- |
| Z-Score Normalization    | $$\sigma=\text{standard deviation} \\ x' = \frac{x - \bar{x}}{\sigma}$$ | $(- \infty, + \infty)$ |
| Min-Max Scaling          | $$x' = \frac{x - \min(x)}{\max(x) - \min(x)}$$                          | $(0, 1)              $ |
| Maximum Absolute Scaling | $$x' = \frac{x}{\max(x)}$$                                              | $(0, 1)              $ |
| Robust Scaling           | $$x' = \frac{x - \text{median}(x)}{Q3 - Q1} $$                          | $(- \infty, + \infty)$ |




# Clustering Algorithms
* Partition algorithms
    * K means clustering
    * Gaussian Mixture Model
* Hierarchical algorithms
    * Bottom-up, agglomerative
    * Top-down, divisive
## K means 
give K point move point to find position fit all data
## K-Medoids
group some point and find the mass center if the point is close merge in to the group if is far then remove from the group

## Hierarchical Clustering(Bottom-up)
merge all point by dstance of clusters
### distance of clusters
* single-link(closest point of group)
* complete-link(farthest point of group)
* centroid(centers point of group)
* average-link (average distance between of all elements of group)
### weight vs unweight
use point number of group as weight or averge two group distance
## DBSCAN (Bottom-up)
1. start with every point as group it self
2. if a,b group are in range of "high densty area" then merge as same group



# pattern mining

## FP tree
<image src="https://imgur.com/AwWn0IU.png" width="80%">

<image src="https://imgur.com/i0hjUGG.png" width="80%">

<image src="https://imgur.com/UTtd0PT.png" width="80%">

## rule (is the itemset are frequent itemset)
* $$\text{support}(A \rightarrow B)=P(A\cap B)$$
* $$\text{confidence}(A\rightarrow B)=P(A| B)$$
* $$\text{lift}(A \rightarrow B)=\frac{P(A\cap B)}{P(A)P(B)}$$
* $$\text{AllConf}(A,B)=\frac{P(A \cap  B)}{\max(P(A),P(B))}$$
* $$\text{MaxConf}(A,B)=\max(P(A|B),P(B|A))$$
* $$\text{Kulczynski}(A,B)=\frac{1}{2}(P(B|A)+P(A|B))$$
* $$\text{Cosine}(A,B)=\frac{A \cdot B}{|A|\times |B|}$$

if lift(A,B) >1 then A,B is effective

## pattern type
* Rare Patterns 
* Negative Patterns(Unlikely to happen together)
  *  Kulczynski(A,B) Less than threshold
* Multilevel Associations
* Multidimensional Associations

## constrant type
<!-- 
### user-specified constrant type
* Knowledge type constraint—Specifying what kinds of knowledge to mine
  * Classification, association, clustering, outlier finding, …
* Data constraint—using SQL-like queries
  * Find products sold together in NY stores this year
* Dimension/level constraint—similar to projection in relational database 
  * In relevance to region, price, brand, customer category
* Interestingness constraint—various kinds of thresholds
  * **Strong rules**: min_sup = 0.02, min_conf =  0.6, min_correlation=0.7
* Rule (or pattern) constraint
  * Small sales (price < \$10) triggers big sales (sum > $200) 
-->
### pruning Strategies
use diff condiation to pruning the iteamset early
* **Monotonic(相關性)**: 
  * If c is satisfied, no need to check c again
* **Anti-monotonic**:  
  *  If constraint c is violated, its further mining can be terminated
* **Convertible**: 
  * c can be converted to monotonic or anti-monotonic if items can be properly ordered in processing
* **Succinct**:  
  * If the constraint c can be enforced by directly manipulating the dat

## Sequential Patterns

items within an element are unordered and we list them alphabetically
<a(bc)dc> is a subsequence of <a(abc)(ac)d(cf)>

Representative algorithms

* **GSP (Generalized Sequential Patterns)**: 
  * Generate “length-(k+1)” candidate sequences from “length-k” frequent sequences using Apriori
* **Vertical format-based mining**: SPADE (Zaki@Machine Leanining’00)
* **Pattern-growth methods**: PrefixSpan

# dimensionality reduction(降维)

## PCA(Principal component analysis )
## PCoA(principal coordinate analysis )
## SVD(Singular Vector Decomposition )
