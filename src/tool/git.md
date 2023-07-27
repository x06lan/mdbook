# git
tags `git`

## command line
```bash
git config --global user.email ""
git config --global user.name ""
git status
git init
git add --all
git commit -m "what do you done"
git branch -M main
git remote add origin https://github.com/lanx06/heroku.git
git push -u origin main
```
## add 儲存 暫存
### git add . and git add --all
#### git add .
只會新增或修改已存在檔案不會刪除
#### git add --all
所有檔案直接同步
如果有刪除檔案則會直接刪除 github上的版本

## push 上傳
> ### 強制上傳
> ```bash
> git push -f origin main
> ```
> ### 更改上傳位置
> ```bash
> git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
> ```
> ### 確認上傳位置
> ```bash
> git remote -v
> ```

> ## pull 同步檔案
> ```bash
> git pull origin master
> ```


## Clone or download
```bash
git clone https://github.com/lanx06/heroku.git
```

## checkout index
```bash
git checkout index.py
```
## checkout commit
```bash
git checkout commithash
```

## branch 分支
> ### checkout remote branch
> ```bash
> git checkout -b branch_name origin/branch_name
> ```
> ### 分支清單
> ```bash
> git branch 
> ```
> ### 開啟分支
> ```bash
> git branch branch_name
> ```
> ### 合併分支
> ```bash
> git merge {new-feature}
> ```
> ### 刪除分支
> ```bash
> git branch -d branch_name
> ```

## 其他

> ### 初始化專案
> ```bash
> git init
> ```
> ### 查看狀態
> ```bash
> git status
> ```
> ### 檢查差異
> ```bash
> git diff 
> ```
> ### 將變更檔案放入暫存區
> ```bash
> git add index.py
> ```
> ### 使用 commit -m 提交變更
> ```bash
> git -a -m 'init commit'
> ```
> ### 查看歷史
> ```bash
> git log --oneline
> ```
> ### 放棄已經 commit 的檔案重回暫存區
> ```bash
> git reset HEAD index.py
> ```

