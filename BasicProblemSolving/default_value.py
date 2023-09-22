# Base Class
class Account:
    def add(self, a):
        return a*a
        
    # def add(self, a, b=None):
    #     return a + b
    def add(self, a, b, c=None):
        return a + b + c
      
if __name__ == '__main__':
    c = Account()
    sum = c.add(3,4)
    print(sum)