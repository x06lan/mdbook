# leetcode
tags: `leetcode`

## 22. Generate Parentheses
dfs
```c++
class Solution {
public:
    std::vector<std::string> ans;
    int n;
    void gen(string v,int i,int j){
        if(i>j)
            if(i<n)
                gen(v+"(",i+1,j);
            if(j<n)
                gen(v+")",i,j+1);
        if(i==j)
            if(j==n)
                ans.push_back(v);
            else
                gen(v+"(",i+1,j); 
    }
    std::vector<std::string> generateParenthesis(int nn) {
        n=nn;
        
        gen("(",1,0);
        return ans;
    }
};

```
## 52. N-Queens II
dfs
```c++
class Solution {
public:
std::vector<std::vector<std::pair<int, int>>> solve;

    bool safeSol(const std::vector<std::pair<int, int>>& queens) {
        for (int i = 0; i < queens.size(); i++) {
            for (int j = i + 1; j < queens.size(); j++) {
                auto a = queens[i];
                auto b = queens[j];
                int x = a.first - b.first;
                int y = a.second - b.second;
                if (x == 0 || y == 0 || y == x || y == -x) {
                    return false;
                }
            }
        }
        return true;
    }

    void branch(std::vector<std::pair<int, int>> queens, int y, int n) {
        if (y != n) {
            for (int x = 0; x < n; x++) {
                queens.push_back({ x, y });
                if (safeSol(queens)) {
                    if (y == n - 1) {
                        solve.push_back(queens);
                    } else {
                        branch(queens, y + 1, n);
                    }
                }
                queens.pop_back();
            }
        }
    }

    std::vector<std::string> convert(const std::vector<std::pair<int, int>>& queens, int n) {
        std::vector<std::string> s(n, std::string(n, '.'));
        for (const auto& queen : queens) {
            s[queen.second][queen.first] = 'Q';
        }
        return s;
    }

    int totalNQueens(int n) {
                std::vector<std::pair<int, int>> q;
        branch(q, 0, n);
        return solve.size();
    }
};
```
## 98. Validate Binary Search Tree
dfs inorder 
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int last=INT_MIN;
    bool take=false;
    //dfs in inorder check is vaild
    bool dfs(TreeNode* n){
        if(n!=nullptr){
            //leaf node
            if(n->right==n->left){
                //if value smailer then last value then is not vaild
                if( (n->val!=INT_MIN && last>=n->val) ||(take && n->val==INT_MIN ))
                    return false;
                last=n->val;
                take=true;
            }
            else{
                //if left node is not vaild or the current node is not vaild then return false 
                if(!dfs(n->left) || (n->val!=INT_MIN && last>=n->val) ||(take && n->val==INT_MIN ))
                    return false;
                last=n->val;
                take=true;
                if(!dfs(n->right))
                    return false;
            }
        }
        return true;
    }
    bool isValidBST(TreeNode* root) {
       
        return dfs(root) ;
    }
};
```
## 198. House Robber
use DP

M(k) = money at the kth house<br>
P(0) = 0<br>
P(1) = M(1)<br>
P(k) = max(P(k−2) + M(k), P(k−1))<br>

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
        vector<int> dp=vector<int>(n,0);

        for(int i =n-1;i>=0;i--){
            if(i==n-1)
                dp[i]=nums[i];
            else if(i==n-2)
                dp[i]=max(nums[i],dp[i+1]);
            else
                dp[i]=max(nums[i]+dp[i+2],dp[i+1]);
        }

        return dp[0];
    }
};

```
## 1143. Longest Common Subsequence



```c++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp;
        int n=text1.size(),m=text2.size();
        dp.assign(n+1,vector(m+1,0));
        for(int i =1;i<n+1;i++){
            for(int j =1;j<m+1;j++){
                if(text1[i-1]==text2[j-1]){
                    dp[i][j]=dp[i-1][j-1]+1;
                }else{
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
    }
};

```
## 1218. Longest Arithmetic Subsequence of Given Difference

dp 

```c++
class Solution {
public:

    unordered_map<int,int> dp;

    int longestSubsequence(vector<int>& arr, int difference) {
        int maxV=1;
        int n=arr.size();
        
        for(int &v:arr){
            if(dp.find(v-difference)!=dp.end())
                dp[v]=dp[v-difference]+1;
            else
                dp[v]=1;
            maxV=max(maxV,dp[v]);
        }
        return maxV;
    }
};
```

## 1705. Maximum Number of Eaten Apples
priorty_queue

alway take the apple that is closest to the Validity limte

```c++
class Solution {
public:
    int eatenApples(vector<int>& apples, vector<int>& days) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int i=0;
        int number = 0;
        
        while (!pq.empty() || i < days.size()) {
            while (!pq.empty()&&pq.top().first<=i)
                pq.pop();
            if (i < days.size() && apples[i] != 0) {
                pq.push({i+days[i],apples[i]});
            }
            if(!pq.empty()){
                auto take=pq.top();
                pq.pop();
                if(--take.second>0){
                    pq.push(take);
                }
                number++;
            }
            i++;
        }
        
        return number;
    }
};

```
## 2024. Maximize the Confusion of an Exam
sliding window
maintain the range that fit the requirement
```c++
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int left =0;
        int right=0;
        int n =answerKey.size();
        int t=0,f=0;
        int ans=INT_MIN;
        int minC=0;
        while(left <answerKey.size()){
            minC=min(t,f);
            while(minC<=k &&right<n){
                ans=max(ans,right-left);
                if(answerKey[right]=='T')
                    t++;
                else
                    f++;
                minC=min(t,f);
                right++;
                if(minC<=k)
                    ans=max(ans,right-left);
            }
            if(right==n)
                ans=max(ans,right-left-1);
            if(answerKey[left++]=='T')
                t--;
            else
                f--;
        }
        return ans;
        return ans==INT_MIN?n:ans;

    }
};
```


## 2305. Fair Distribution of Cookies
dfs find every possible

```c++
class Solution {
public:
    int minMax=INT_MAX;
    vector<int>c;
    int k=0;
    int t=0;
    void dfs(vector<int> &status,int n){
        if(n<t){
            auto v=c[n++];
            for(int i=0;i<k;i++){
                status[i]+=v;
                dfs(status,n);
                status[i]-=v;
            }
        }else{
            int maxV=INT_MIN;
            for(auto i:status)
                maxV=max(i,maxV);
            minMax=min(minMax,maxV);
        }
    }
    int distributeCookies(vector<int>& cookies, int kk) {
        c.insert(c.begin(),cookies.begin(),cookies.end());
        t=c.size();
        k=kk;
        vector<int> temp(k,0);
        dfs(temp,0);
        return minMax;
    }
};
```