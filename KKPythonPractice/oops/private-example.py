class Stack:
    def __init__(self) -> None:
        print("I am in constructor")
        # self.stack_list = []        
        # AttributeError: 'Stack' object has no attribute 'stack_list'Error in sys.excepthook:
        self.__stack_list = []

    def get_stack_list_len():
        stack_object = Stack()
        print(len(stack_object.stack_list))         

# stack_object = Stack()
# stack_object.get_stack_list_len()

Stack.get_stack_list_len()