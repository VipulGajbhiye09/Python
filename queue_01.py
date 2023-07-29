class QueueExample:
    def createQueue(self,size):
        self.MaxSize=size
        self.front=0
        self.rear=-1
        self.queue=[]
        for i in range(self.MaxSize):
            self.queue.append(0)
        print("Queue of size",self.MaxSize,"created")
