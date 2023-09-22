class Person:

    # overloaded method
    def name_details(self, name='shadobaa') -> str:
        if(name is not None):
            print('Hello ', name)
        else:
            print('Hello! stranger')

    def name_details(self, *name) -> str:
        if(name is not None):
            print('Hello All ', name)

if __name__ == '__main__':
    # create an object
    one = Person()
    one.name_details() # default gets picked
    one.name_details('shad') # actual 1 arg is sent
    one.name_details('shad', 'rishi') # error, 2nd def above with * will be needed

