#定义双向链表(带有尾指针rear)

class LinkedListUnderflow(ValueError):
    pass

#双向链表结点类
class DoubleNode():
    def __init__(self, elem, prior_=None, next_=None):
        self.elem = elem
        self.prior = prior_
        self.next = next_

class DoubleList():
    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self,elem):#前端插入结点
        p = DoubleNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prior = p
        self._head = p

    def append(self, elem): #尾端插入结点
        p = DoubleNode(elem)
        if self._head is None:
            self._head = p
        else:
            p.prior.next = p
        self._rear = p

    def pop(self):#前端弹出结点
        if self._head is None:
            raise LinkedListUnderflow("pop failed")
        e = self._rear.next.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prior = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("pop failed")
        e = self._rear.elem
        self._rear = self._rear.prior
        return e




