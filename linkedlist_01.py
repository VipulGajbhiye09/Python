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
                
    def search_list(self,key):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while t!=None and t.data!=key:
                t=t.next
            if t==None:
                print(key,"not found")
            else:
                print(key,"Found")
                
    def delete_key(self,key):
        if self.root==None:
            print("Empty List")
        else:
            t=t2=self.root
            while t!=None and t.data!=key:
                t2=t
                t=t.next
            if t==None:
                print(key,"not found")
            else:
                if t==self.root:    #case 1
                    self.root=self.root.next
                elif t.next==None:  #case 2
                    t2.next=None
                else:               #case 3
                    t2.next=t.next
                print(t.data,"deleted")

    def insert_at(self,pos,data):
        n=Node(data)
        if self.root==None:
            self.root=n
        else:
            t=t2=self.root   #1
            if pos==0:
                n.next=self.root
                self.root=n

            while pos>0 and t.next!=None:   #2
                t2=t
                t=t.next
                pos-=1
            t2.next=n
            n.next=t
            print(data,"inserted")
