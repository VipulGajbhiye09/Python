## Queue implementation with Linked List

class QueueExample:
    def createqueue(self):
        self.front=self.rear=None

    def enqueue(self,data):
            n=Node(data)
            if self.front==None:
                self.front=self.rear=n
            else:
                self.rear.next=n  #3
                self.rear=n
            print(data,"enqueued")
        
    def dequeue(self):
        if self.front==None:
            print("Queue Empty")
        else:
            t=self.front  #1
            self.front=self.front.next  #2
            print(t.data,"dequeued")

    def print_queue(self):
        if self.front==None:
            print("Empty Queue")
        else:
            print("Queue Has")
            t=self.front
            while t!=None:
                print(t.data,end="--")
                t=t.next
                
##Menu Driven Code
obj=QueueExample()
obj.createqueue()
while True:
    ch=int(input("\n1.Enqueue\n2.Dequeue\n3.Print\n0.Exit\n:"))
    if ch==1:
        obj.enqueue(int(input("Enter the element:")))
    elif ch==2:
        obj.dequeue()
    elif ch==3:
        obj.print_queue()
    elif ch == 0:
      print("Thanks")
      break
    else:
        print("Wrong option selected")
