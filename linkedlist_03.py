class DoublyLinkedList:
    def createList(self):
        self.root=None

    def insert_left(self,data):
        n=Node(data)  #Node Creation
        if self.root==None:
            self.root=n
        else:
            n.right=self.root  #1
            self.root.left=n  #2
            self.root=n  #3
        print(data,"inserted")
