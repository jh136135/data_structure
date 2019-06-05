#定义循环单链表类
class LinkedListUnderflow(ValueError):
    pass

class Node():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class CycleList():
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem): #前端插入结点，不需要更新尾指针的引用
        p = Node(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem): #尾端插入结点，需要更新尾指针的指向
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):  #前端弹出结点
        if self._rear is None:
            raise LinkedListUnderflow("pop falied")
        p = self._rear.next
        if self._rear is p: #只有一个结点的情况
            e = self._rear.elem
            self._rear = None
        else:
            e = self._rear.next.elem
            self._rear.next = p.next
        return e



