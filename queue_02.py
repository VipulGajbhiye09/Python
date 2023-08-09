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
