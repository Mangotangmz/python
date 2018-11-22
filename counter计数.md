

#  counter计数

一：定义一个list数组，求数组中每个元素出现的次数**

**如果用Java来实现，是一个比较复杂的，需要遍历数组list。**

**但是Python很简单：看代码**

**[python]** [view plain](http://blog.csdn.net/u013628152/article/details/43198605#) [copy](http://blog.csdn.net/u013628152/article/details/43198605#)

```
a = [1,4,2,3,2,3,4,2]  

 from collections import Counter  
 print Counter(a)  
a = [1,4,2,3,2,3,4,2]  

from collections import Counter  
print Counter(a)  

```

打印结果:

**Counter({2: 3, 3: 2, 4: 2, 1: 1})**

**结果表示：元素2出现了3次；元素3出现了2次；元素4出现了2次；元素1出现了1次。**