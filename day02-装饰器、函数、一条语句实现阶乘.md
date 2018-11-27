# day02-装饰器、函数、一条语句实现阶乘

filter -->map -->  reduce

过滤       映射       归约

过滤      映射     

```
a =[12, 95, 88, 45]
sum([x**x for x in a if x % 2]) 


fn = lambda x,y :x**y
def foo():
	pass
fn =foo
```

在python中函数式一等对象（一定公民）

1. 函数可以赋值给变量
2. 函数可以作为函数的参数   --->fillter
3. 函数可以作为函数的返回值 --->装饰器

函数参数:

1. 位置参数

2. 可变参数 -tuple

3. 关键字参数 - dict

4. 命名关键字参数

   ​

自定义装饰器 - 装饰函数 / 装饰类  --设计模式（代理模式）

代理模式

用代理对象（装饰器函数）去执行被代理对象（被装饰的函数）的行为

面向切面编程 —AOP

在程序中跟正常业务逻辑没有必然联系而且会重复使用的功能通常被称为横切关注功能，这种横切关注功能不应该写在业务逻辑代码是上，而应该使用装饰器或中间件来完成



指令式编程（汇编语言） /过程式语言（c语言）

Python既支持面向对象编程，也支持函数式编程



一条语句求阶乘

``` 
fn = lambda n: functools.reduce(__int.mul__, range(1,n+1))
```

heapq内置模块  提供基于堆的优先排序算法

```
import heapq
list1[1,4,5,63,24]
heapq.nsmallest(list1,n)  #最小的n个
heapq.nlargest(list1,3)		#最大的n个

```

全排列

```
import itertools
for val in itertools.combinations('abcde', 3):
	print (val)
```

笛卡尔积

```
for val in itertools.product('ABCD',123):
	print(val)
```

装饰器

```
from functools import wraps
def record(func):
	@wraps(func)
	def wrapper(args, **kwargs):
	
		ret_value = func(*args, *kwargs)
		return ret_value
		
	return wrapper
```

带参数的装饰器

```
import time
from functools import wraps 
from random import randint

def record_time(output):

    def func(function):

        # 装饰器函数，计算函数执行时间
        @wraps(function)
        def timeCount(*args, **kwargs):
            timestart = time.time()
            result = function(*args, **kwargs)
            timesend= time.time()
            output(function.__name__, timesend - timestart) 
            return result
        return timeCount

    return func

def log_to_file(fn, duration):
    with open('result.txt', 'a')as fs:
        fs.write('%s: %.3f秒\n' %(fn,duration))


@record_time(log_to_file)
def fool():
    time.sleep(randint(1,3))


def main():
    for _ in range(5):
        # 此处调用foo并不是真正执行分两类而是执行了wrpper
        fool()
    # 取消装饰器 
    foo2 = fool.__wrapped__
    for _ in range(3):
        # 此处调用被装饰之前写的函数
        foo2()



if __name__ == '__main__':
    main()
```