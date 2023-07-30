class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
      
class LinkedList:
    def createList(self):
        self.root=None
        
    def insert_left(self,data):
        n=Node(data)   #Node Creation
        if self.root==None:
            self.root=n
        else:
            n.next=self.root  #1
            self.root=n  #2
        print(data,"inserted")

    def delete_left(self):
        if self.root==None:
            print("List Empty")
        else:
            t=self.root  #1
            self.root=self.root.next  #2
            print(t.data,"deleted")
