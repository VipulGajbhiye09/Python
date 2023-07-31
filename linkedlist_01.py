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

## MENU DRIVEN LINKED LIST
obj=LinkedList()
obj.createList()
while True:
    ch=int(input("1.Insert Left\n2.Delete Left\n3.Insert Right\n4.Delete Right\n5.PrintList\n6.Search List\n7.delete on key\n8.Insert at\n0.Exit\n:"))
    if ch==1:
        obj.insert_left(int(input("Enter the element to add at left : ")))
    elif ch==2:
        obj.delete_left()

    elif ch==3:
      obj.insert_right(int(input("Enter the element to add at right : ")))

    elif ch==4:
        obj.delete_right()

    elif ch ==5:
      obj.print_list()

    elif ch ==6:
      obj.search_list(int(input("Enter the element to search:")))

    elif ch==7:
        obj.delete_key(int(input("Enter the element to search:")))

    elif ch==8:
        obj.insert_at(int(input("Enter position:")),int(input("Enter the element:")))

    elif ch == 0:
      print("Thanks")
      break

    else:
        print("Wrong option selected")
