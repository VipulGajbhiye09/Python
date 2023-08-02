## Circular Linked List

class CircularLinkedList:
    def createList(self):
        self.root=self.last=None

    def insert_left(self,data):
        n=Node(data)   #Node Creation
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            n.next=self.root  #1
            self.root=n  #2
            self.last.next=self.root#3
        print(data,"inserted")
        
    def delete_left(self):
        if self.root==None:
            print("List Empty")
        else:
            t=self.root  #1
            if self.root==self.last:  #one element
                self.root=self.last=None
            else:
                self.root=self.root.next  #2
                self.last.next=self.root  #3
            print(t.data,"deleted")
            
    def insert_right(self,data):
        n=Node(data)  #Node Creation
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            self.last.next=n  #1
            self.last=n  #2
            self.last.next=self.root  #3
        print(data,"inserted")
        
    def delete_right(self):
        if self.root==None:
            print("List Empty")
        else:
            t=t2=self.root  #1
            if self.root==self.last:  #one element
                self.root=self.last=None
            else:
                while t!=self.last:  #2
                    t2=t
                    t=t.next
                self.last=t2  #3
                self.last.next=self.root  #4
            print(t.data,"deleted")

    def print_list(self):
        if self.root==None:
            print("Empty List")
        else:
            t=self.root
            while True:
                print(t.data,end="-->")
                t=t.next
                if t==self.root:
                    break
                    
## Menu Driven Code
obj=CircularLinkedList()
obj.createList()
while True:
    ch=int(input("1.Insert Left\n2.Delete Left\n3.Insert Right\n4.Delete Right\n5.PrintList\n0.Exit\n:"))
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

    elif ch == 0:
      print("Thanks")
      break
        
    else:
        print("Wrong option selected")
