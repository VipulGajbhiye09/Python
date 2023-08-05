## Stack implementation using linked list 

class StackExample:
    def createstack(self):
        self.tos=None

    def push(self,data):
        n=Node(data)#Node Creation
        if self.tos==None:
            self.tos=n
        else:
            n.next=self.tos#1
            self.tos=n#2
        print(data,"Pushed")
