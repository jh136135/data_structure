#定义二叉树类结点
class BinTNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

t = BinTNode(1, BinTNode(2), BinTNode(3))

def count_BinTNodes(tree): #统计树中结点个数
    if tree is None:
        return 0
    else:
        return 1 + count_BinTNodes(tree.left) + count_BinTNodes(tree.right)

def sum_BinTNodes(tree): #求二叉树里所有数值之和
    if tree is None:
        return 0
    else:
        return tree.data + sum_BinTNodes(tree.left) + sum_BinTNodes(tree.right)

#以下所有参数tree都是BinTNode类型的对象

def preorder(tree): #前序遍历二叉树
    if tree is None:
        return
    print(tree.data) #打印结点元素，可改为对结点的其他操作
    preorder(tree.left)
    preorder(tree.right)

def midorder(tree): #中序遍历二叉树
    if tree is None:
        return
    midorder(tree.left)
    print(tree.data)  # 打印结点元素，可改为对结点的其他操作
    midorder(tree.right)

def postorder(tree): #后序遍历二叉树
    if tree is None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.data)  # 打印结点元素，可改为对结点的其他操作




