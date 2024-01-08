
# hw3 110590049

tags `data`

[2023 Educational Data Mining and Applications HW3.pdf](../../assets/pdf/Educational_Data_Mining_and_Applications_HW3.pdf)

## 8.11

$$ 
\begin{aligned}\\
\text{ F-measure}=&\frac{2}{\frac{1}{precision}+\frac{1}{recall}}\\
&=\frac{2}{\frac{TP+FP}{TP}+\frac{TP+FN}{TP}}\\
&=\frac{2}{\frac{2TP+FP+FN}{TP}}\\
&=\frac{2TP}{2TP+FP+TN}\\
\end{aligned}\\
$$
## 8.12

$$
TPR=\frac{TP}{TP+FN}\\
FPR=\frac{FP}{TN+FP}\\
$$


| sample                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | threshold sample                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <table><thead><tr><th>tuple</th><th>class</th><th>probability</th></tr></thead><tbody><tr><td>1</td><td>P</td><td>0.95</td></tr><tr><td>2</td><td>N</td><td>0.85</td></tr><tr><td>3</td><td>P</td><td>0.78</td></tr><tr><td>4</td><td>P</td><td>0.66</td></tr><tr><td>5</td><td>N</td><td>0.60</td></tr><tr><td>6</td><td>P</td><td>0.55</td></tr><tr><td>7</td><td>N</td><td>0.53</td></tr><tr><td>8</td><td>N</td><td>0.52</td></tr><tr><td>9</td><td>N</td><td>0.51</td></tr><tr><td>10</td><td>P</td><td>0.40</td></tr></tbody></table> | <table><thead><tr><th>thresholds</th><th>TP</th><th>FP</th><th>TN</th><th>FN</th><th>FPR</th><th>TPR</th></tr></thead><tbody><tr><td>0.40</td><td>5</td><td>5</td><td>0</td><td>0</td><td>1.0</td><td>1.0</td></tr><tr><td>0.51</td><td>4</td><td>5</td><td>0</td><td>1</td><td>1.0</td><td>0.8</td></tr><tr><td>0.52</td><td>4</td><td>4</td><td>1</td><td>1</td><td>0.8</td><td>0.8</td></tr><tr><td>0.53</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0.6</td><td>0.8</td></tr><tr><td>0.55</td><td>4</td><td>2</td><td>3</td><td>1</td><td>0.4</td><td>0.8</td></tr><tr><td>0.60</td><td>3</td><td>2</td><td>3</td><td>2</td><td>0.4</td><td>0.6</td></tr><tr><td>0.66</td><td>3</td><td>1</td><td>4</td><td>2</td><td>0.2</td><td>0.6</td></tr><tr><td>0.78</td><td>2</td><td>1</td><td>4</td><td>3</td><td>0.2</td><td>0.4</td></tr><tr><td>0.85</td><td>1</td><td>1</td><td>4</td><td>4</td><td>0.2</td><td>0.2</td></tr><tr><td>0.95</td><td>1</td><td>0</td><td>5</td><td>4</td><td>0.0</td><td>0.2</td></tr><tr><td>1.00</td><td>0</td><td>0</td><td>5</td><td>5</td><td>0.0</td><td>0.0</td></tr></tbody></table> |

<!-- 
| tuple | class | probability |
| ----- | ----- | ----------- |
| 1     | P     | 0.95        |
| 2     | N     | 0.85        |
| 3     | P     | 0.78        |
| 4     | P     | 0.66        |
| 5     | N     | 0.60        |
| 6     | P     | 0.55        |
| 7     | N     | 0.53        |
| 8     | N     | 0.52        |
| 9     | N     | 0.51        |
| 10    | P     | 0.40        |


| thresholds | TP  | FP  | TN  | FN  | FPR | TPR |
| ---------- | --- | --- | --- | --- | --- | --- |
| 0.40       | 5   | 5   | 0   | 0   | 1.0 | 1.0 |
| 0.51       | 4   | 5   | 0   | 1   | 1.0 | 0.8 |
| 0.52       | 4   | 4   | 1   | 1   | 0.8 | 0.8 |
| 0.53       | 4   | 3   | 2   | 1   | 0.6 | 0.8 |
| 0.55       | 4   | 2   | 3   | 1   | 0.4 | 0.8 |
| 0.60       | 3   | 2   | 3   | 2   | 0.4 | 0.6 |
| 0.66       | 3   | 1   | 4   | 2   | 0.2 | 0.6 |
| 0.78       | 2   | 1   | 4   | 3   | 0.2 | 0.4 |
| 0.85       | 1   | 1   | 4   | 4   | 0.2 | 0.2 |
| 0.95       | 1   | 0   | 5   | 4   | 0.0 | 0.2 |
| 1.00       | 0   | 0   | 5   | 5   | 0.0 | 0.0 |
 -->

### ROC
<image src="https://imgur.com/zo9hP6V.png" width="80%">



## 8.16
change the traing dataset to balance by oversampleing the fraudulent cases or undersampling nonfraudulent cases.
<image src="https://imgur.com/M2gR4vt.png" width="80%">


by threshold-moving to reduce the error chance on majority case
<image src="https://imgur.com/CqhipX8.png" width="80%">

## 9.4

|              | **Eager Classification**                                     | **Lazy Classification**                                           |
| ------------ | ------------------------------------------------------------ | ----------------------------------------------------------------- |
| Advantage    | Better interpretability<br> Better efficiency                | Robust to Noise                                                   |
| Disadvantage | Robust to Noise <br> Need for re-training when have new data | Vulnerability to irrelevant features <br>Limited interpretability |


## 9.5
```py=0
def distance(a,b):
    return sum([abs(a[i]-b[i]) for i in range(len(a))])
    
def KNN(input_data,k,dataset,answer):
    distances=[]
    i=0
    for data in dataset :
        distances.append({
            "distance":distance(input_data,data),
            "answer":answer[i]
        })
        i+=1
    nesrest=sorted(distances,key=lambda x:x["distance"])[:k]
    counter={key:0 for key in answer}
    for x in nesrest:
        counter[x["answer"]]+=1
    predict={key:counter[key]/k for key in counter}
    return predict
data=[[1,2,3],[0,-1,0],[1,4,4],[1,3,4]]
answer=["a","a","b","b"]
input_data=[0,0,0]
k=3
print(KNN(input_data,k,data,answer))
```
