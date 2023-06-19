class Stack:
    def __init__(self) -> None:
        self.__stack_list = []    

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self) -> None:
        super().__init__(self)
        # Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val =  Stack.pop(self)
        self.__sum -= val
        return val