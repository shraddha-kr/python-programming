class CustomRange:
    def __init__(self, range):
        self.__range = range
        self.__i = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.__i
        self.__i += 1

        if self.__i > self.__range:
            raise StopIteration

        return res

range = CustomRange(10)

for i in range:
    print(i)
