#定义单链表及相关操作

#自定义异常
class LinkedListUnderflow(ValueError):
    pass

class Node():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class List():
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem): #表头插入结点
        self._head = Node(elem, self._head)

    def pop(self): #删除表头结点
        if self._head is None:
            raise LinkedListUnderflow("pop failed")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):  #表尾插入结点
        if self._head is None:
            self._head = Node(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Node(elem)

    def pop_last(self): #删除最后结点，必须找到倒数第二个结点
        if self._head is None:
            raise LinkedListUnderflow("pop failed")
        p = self._head
        if p.next is None:  #只有一个结点的情况
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e
