







# 1 连接远程仓库

1. 安装git

2. 在本地建立一个仓库 打开gitbash，到本地仓库的路径下，输入  :  git init  ,成功之后所在的目录下面会出现   .git文件。里面会存放我们的分支和版本。其实这就是我们的本地库。　　　

   ```
           git init
   ```

3.第三步，创建git 用户名 邮箱,在gitbash中输入：

```
    git config user.name "xiaochao"  
    git config user.email '188*******@163.com'  
```

4.生成sshkey 与 github关联 

```
$ ssh-keygen -t rsa -C "188*******@163.com"
```



5.第五步，与github关联，生成的key在电脑的用户下.ssh文件下，  rsa_pub是公钥，rsa是私钥。把公钥复制到github上（前提你得有github账号）

![img](file:///C:\Users\Administrator\AppData\Roaming\Tencent\Users\1990486426\TIM\WinTemp\RichOle\QY7~]DJ`LML2[{BTNL_G7V9.png)



查看当前连接的远程仓库

**git remote show origin**



解决github版本冲突 **git push -u origin master -f **

把本地仓库推到远程仓库
**git push origin master**
（第一次推）
**git push -u origin master**



 # 2 版本库repository



* 首先，选择一个合适的地方，创建一个空目录
* 通过**git init**命令把这个目录变成Git可以管理的仓库

```
$ git init
Initialized empty Git repository in /Users/michael/learngit/.git/
```


添加文件到Git仓库，分两步：

* **git add <file>**，注意，可反复多次使用，添加多个文件,添加文件到缓存区；
* **git commit -m <message> **  完成 提交文件到仓库。


**git status** 命令看看结果

**git diff** 查看修改内容



# 3 版本回退

## 3.1 查看版本日志



**git log**   命令显示从最近到最远的提交日志

git当前版本用head表示，上一个版本是head^,上上个版本就是head^^



## 3.2 回退



**git reset --hard HEAD^**   回到上一个版本

**cat filename**   查看内容版本
版本
**$ git reset --hard 1094a** 通过版本号回到以前的

注：

- `HEAD`指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令`git reset --hard commit_id`。
- 穿梭前，用`git log`可以查看提交历史，以便确定要回退到哪个版本



## 3.3 丢弃工作区内容



**checkout -- file**可以丢弃工作区的修改：

```
$ git checkout -- readme.txt
```

命令**git checkout -- readme.txt**意思就是，把`readme.txt`文件在工作区的修改全部撤销，这里有两种情况：

* 一种是`readme.txt`自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；
* 一种是`readme.txt`已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。

### 总结



* 场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令`git checkout -- file`。
* 场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令`git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考[版本回退](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013744142037508cf42e51debf49668810645e02887691000)一节，不过前提是没有推送到远程库。