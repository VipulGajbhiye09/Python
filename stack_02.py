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

    def pop(self):
        if self.tos==None:
            print("Empty Stack")
        else:
            t=self.tos#1
            self.tos=self.tos.next#2
            print(t.data,"poped")

    def peek(self):
        if self.tos==None:
            print("Empty Stack")
        else:
             print(self.tos.data,"element at peek")

    def print_stack(self):
        if self.tos==None:
            print("Empty Stack")
        else:
            print("Stack has")
            t=self.tos
            while t!=None:
                print(t.data)
                t=t.next
