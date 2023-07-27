class StackExample:
    def createstack(self,size):
        self.Maxsize=size
        self.tos=-1
        self.stack=[]#list
        for i in range(self.Maxsize):
            self.stack.append(0)
        print("Stack of size",self.Maxsize,"created")

    def push(self,e):
        self.tos+=1 #self.tos=self.tos+1
        self.stack[self.tos]=e
        print(e,"pushed in stack")

