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
            
    def insert_right(self,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            t=self.root  #1
            while t.next!=None:  #2
                t=t.next
            t.next=n  #3
        print(data,"inserted")

    def delete_right(self):
        if self.root==None:
            print("List Empty")
        else:
            t=t2=self.root  #1
            while t.next!=None:  #2
                t2=t
                t=t.next
            t2.next=None
            print(t.data,"deleted")
            
    def print_list(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while t!=None:
                print(t.data,end="-->")
                t=t.next
