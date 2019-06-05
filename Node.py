#定义一个简单的线性表的结点类

class Node():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


"""
创建空链表:
把表头变量设置为空链接，python设置为None

删除链表：
丢弃链表里所有结点，python中将表指针赋值为None

判断链表是否为空：
python中，检查相应变量是否为None

首端插入插入元素：
p = Node(5)
p.next = head.next
head = p

定位插入元素：(pre为插入的前一结点)
p = Node(3)
p.next = pre.next
pre.next = p    

删除表首元素：(修改表头指针，指向第二个结点，丢弃结点被自动回收)
head = head.next

一般情况的删除元素：(pre为要删除结点的前一结点)
pre.next = pre.next.next

链表扫描：
p = head
while p is not None:
    print(p.elem)
    p = p.next
"""




