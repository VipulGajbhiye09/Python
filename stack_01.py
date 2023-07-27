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

    def pop(self):
        temp=self.stack[self.tos]
        self.tos-=1
        return(temp)
        
    def isfull(self):
        if self.tos==self.Maxsize-1:
            return True
        else:
            return False

    def isempty(self):
        if self.tos==-1:
            return True
        else:
            return False
            
    def peek(self):
        return self.stack[self.tos]            
