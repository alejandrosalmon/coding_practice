class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, node):
        self.root = Node(node) 

    def preorder_search(self, value):
        return self.pre_search(self.root, value)

    def pre_search(self, node, value):
        if node:
            if node.value is value:
                return True
            else:
                return self.pre_search(node.left, value) or self.pre_search(node.right,value)
        return False

    def inorder_search(self):
        return
        
    def postorder_search(self):
        return

    def preorder_print(self):
        return self.preord_prnt(self.root,"")[:-1]

    def preord_prnt(self,node,string): 
        if node:
            print(node.value)
            string += (str(node.value) + "-")
            string = self.preord_prnt(node.left, string)
            string = self.preord_prnt(node.right, string)
        return string
    
    def inorder_print(self):
        return self.inord_prnt(self.root,"")[:-1]

    def inord_prnt(self, node, string):
        if node:
            string = self.preord_prnt(node.left, string)
            string += (str(node.value) + "-")
            string = self.preord_prnt(node.right, string)
        return string

    def postorder_print(self):
        return self.postord_prnt(self.root,"")[:-1]

    def postord_prnt(self, node, string):
        if node:
            string = self.preord_prnt(node.left, string)
            string = self.preord_prnt(node.right, string)
            string += (str(node.value) + "-")
        return string

test = BinaryTree(1)
test.root.left = Node(2)
test.root.right = Node(3)
test.root.left.left = Node(4)
test.root.left.right = Node(5)

