class Space:
    def __init__(self, kind='abc'):
        self.kind = kind

    def public(self):
        print("public")

    def __private(self):
         print("private")

obj = Space()

#Based on the Space class and the obj creation above, can you guess what the following code would return?


obj.public()

try:
    obj.__private()
except:
      print("inaccesible")

obj._Space__private()
"""
    public
    inaccesible
    private
"""