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
