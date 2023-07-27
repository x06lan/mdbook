# leetcode
## N-Queens II
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