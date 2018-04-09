import abc

class Command:    
    def __init__(self, params):
        self.myparam = params
        
    @abc.abstractmethod
    def execute(self, data, myparam): pass

# make class all inherit from base class that takes parameters
class func1(Command):
    def __init__(self, params):
        super().__init__(params)
    def execute(self, data, myparam):
        return data*myparam

class func2(Command):
    def __init__(self, params):
        super().__init__(params)
    def execute(self, data, myparam):
        return data+myparam

# An object that holds commands:
class Transformer:
    
    def __init__(self, Input, commands):
        self.pipeInput = Input
        self.commands = commands

    def run(self):
        for c in self.commands:
            self.pipeInput = c.execute(self.pipeInput, c.myparam)
        return self.pipeInput
























pipeline = Transformer(3, [func1(8), func2(1)])
print(pipeline.run())





















