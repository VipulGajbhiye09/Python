class QueueExample:
    def createqueue(self):
        self.front=self.rear=None

    def dequeue(self):
        if self.front==None:
            print("Queue Empty")
        else:
            t=self.front  #1
            self.front=self.front.next  #2
            print(t.data,"dequeued")
