#建立空栈对应于创建一个空表[]，判断空栈对应于检查是否为空表
#list采用动态顺序表技术(分离式实现)，作为栈的表不会满
#压入元素应在表尾进行，对应于list.append(x)
#访问栈顶元素用list[-1]
#弹出操作也在表尾进行，list.pop()默认弹出表尾元素

class StackUnderflow(ValueError):
    pass

#(1)顺序栈，尾端插入和删除是O(1)操作，作为栈顶，首端作为栈底
class SStack():
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.elems == []:#空栈
            raise StackUnderflow("stack is none")
        return self.elems[-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.elems == []:
            raise StackUnderflow("stack is none")
        return self.elems.pop()

# stack1 = SStack()
# for i in range(4,9):
#     stack1.push(i)
# while not stack1.is_empty():
#     print(stack1.pop())


#(2)链栈，首端插入和删除是O(1)操作，作为栈顶
class Node():
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LStack():
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, elem):
        self.top = Node(elem, self.top)

    def top(self):
        if self.top is None:
            raise StackUnderflow("stack is none")
        return self.top.elem

    def pop(self):
        if self.top is None:
            raise StackUnderflow("stack is none")
        p = self.top
        self.top = p.next
        return p.elem

stack2 = LStack()
for i in range(3,8):
    stack2.push(i)
while not stack2.is_empty():
    print(stack2.pop())

