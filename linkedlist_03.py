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

    def delete_left(self):
        if self.root==None:
            print("List Empty")
        else:
            t=self.root  #1
            self.root=self.root.right  #2
            self.root.left=None#3
            print(t.data,"deleted")

    def insert_right(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            t=self.root  #1
            while t.right!=None:  #2
                t=t.right
            t.right=n
            n.left=t
        print(data,"inserted")
        
 def delete_right(self):
        if self.root==None:
            print("List Empty")
        else:
            t=self.root  #1
            while t.right!=None:  #2
                t=t.right
            t2=t.left#3
            t2.right=None#4
            print(t.data,"deleted")

def print_list(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while t!=None:
                print(t.data,end="-->")
                t=t.right
