#单链表反转，从一个单链表的表头不断取下结点，放入另一个表的表首，完成反转过程

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

    def reverselist(self):  #完成单链表反转
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

