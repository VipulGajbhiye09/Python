class QueueExample:
    def createQueue(self,size):
        self.MaxSize=size
        self.front=0
        self.rear=-1
        self.queue=[]
        for i in range(self.MaxSize):
            self.queue.append(0)
        print("Queue of size",self.MaxSize,"created")

    def enqueue(self,e):
        self.rear+=1 #rear=rear+1
        self.queue[self.rear]=e
        print("Enqueued",e)
    def isFull(self):
        if self.rear==self.MaxSize-1:
            return True
        else:
            return False
