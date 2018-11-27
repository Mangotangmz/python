面向对象 -OOP(Object Oriendted Programming)
面向对象的四大支柱：

- 抽象：类是抽象的，对象是具体的，定义类的过程就是一个抽象过程，  需要最

  数据抽象(发现静态特征（属性）)和行为抽象（发现动态特征（方法））

- 封装: 把数据和操作数据的方法绑定到一起形成对象，这是一个隐藏实现细节暴露
   简单的调用接口的过程。

- 继承：从已有的类创建新类的过程，提供继承信息的称为父类（基类/超类）得到继
   承信息的称为子类（派生类）

- 多态：子类在继承父类的过程中可以重写（override）父类已有的方法
   不同的子类可以给出不同放任实现版本，那么在调用该方法时会表现出多态行为

面向对象七原则：
1.单一职责原则 -SRP- 一个类只该做的事情
2.开闭原则 - 软件实体应该对扩展开放，对修改关闭
3.依赖倒转原则
4.里氏替换原则 - 在任何可以用子类对象替换父类对象
5.接口隔离原则
6.合成聚合复用原则 - 优先使用强关联关系而不是继承关系复用代码
7.最少知识原则（迪米特法则） - 不要给没有必然联系的对象发消息

GoF设计模式 -23种场景：



```


'''
from abc import ABCMeta,abstractmethod

# 元类 - 描述类
# 通过 metaclass=ABCmeta可以将一个类声明为抽象类
# 通过abstractment装饰器可以将方法装饰成抽象方法
# 抽象类不能实例化
class  Employee(object, metaclass=ABCMeta):
    """员工  """
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __salary__(self):
        pass

class Manager(Employee):
    """部门经理"""
    
    # 重写父类的抽象方法（如果没有重写抽象方法，也不能实例化）
    # 不同的子类都会重写这个抽象方法所以这个，所以这个方法是现了多态
    def get_salary(self):
        return 15000

class Programmer(Employee):
    """程序员"""
    def __init__(self, name):
        super ().__init__(name)
        self.working_hour = 0

    def get_salary(self):
        return 200 * self.working_hour

class Saleman(Employee):
    """docstring for Saleman"""
    def __init__(self, name):
        super().__init__(name)
        self.sale = 0

    def get_salary(self):
        return 0.05 * self.sale + 1800
        

def main():
    """主函数"""
    emps = [Manager('曹操'), Programmer('司马懿'),
    Saleman('郭嘉')
    ]
    for emp in emps:
        # 通过isinstance函数可以进行类型识别
        if isinstance(emp,Programmer):
            hour = int(input(f'{emp.name}本月工作时间：')) 
            emp.working_hour =hour
        elif isinstance(emp,Saleman):
            sale = float(input(f'{emp.name}本月销售额：'))
            emp.sale = sale
        print(f'{emp.name}本月工资：{emp.get_salary()}元')

if __name__ == '__main__':
    main()

```

