import sys
class node(object) :
    left = None
    right = None
    data = 0
    color = False
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
        self.color = True
class LLRBTREE(object) :
    root = None
    def  rotateLeft(self, myNode) :
        print("povorot vlevo!!\n")
        child = myNode.right
        childLeft = child.left
        child.left = myNode
        myNode.right = childLeft
        return child
    def  rotateRight(self, myNode) :
        print("vrashhenie vpravo\n")
        child = myNode.left
        childRight = child.right
        child.right = myNode
        myNode.left = childRight
        return child
    def  isRed(self, myNode) :
        if (myNode == None) :
            return False
        return (myNode.color == True)
    def swapColors(self, node1,  node2) :
        temp = node1.color
        node1.color = node2.color
        node2.color = temp
    def  insert(self, myNode,  data) :
        if (myNode == None) :
            return node(data)
        if (data < myNode.data) :
            myNode.left = self.insert(myNode.left, data)
        elif(data > myNode.data) :
            myNode.right = self.insert(myNode.right, data)
        else :
            return myNode
        if (self.isRed(myNode.right) and not self.isRed(myNode.left)) :
            myNode = self.rotateLeft(myNode)
            self.swapColors(myNode, myNode.left)
        if (self.isRed(myNode.left) and self.isRed(myNode.left.left)) :
            myNode = self.rotateRight(myNode)
            self.swapColors(myNode, myNode.right)
        if (self.isRed(myNode.left) and self.isRed(myNode.right)) :
            myNode.color = not myNode.color
            myNode.left.color = False
            myNode.right.color = False
        return myNode
    def inorder(self, node) :
        if (node != None) :
            self.inorder(node.left)
            c = '?'
            if (node.color == False) :
                c = '?'
            print(str(node.data) + "" + str(c) + " ", end ="")
            self.inorder(node.right)
    @staticmethod
    def main( args) :
        node = LLRBTREE()
        scan =  "Python-inputs"
        ch = ' '
        while True :
            print("Vvedite czeloe chislo")
            num = input()
            LLRBTREE.root = node.insert(LLRBTREE.root, num)
            node.inorder(LLRBTREE.root)
            print("\nVy` xotite prodolzhit`? (vvedite y ili n)")
            ch = input()[0]
            if((ch == 'Y' or ch == 'y') == False) :
                    break


if __name__=="__main__":
    LLRBTREE.main(sys.argv)