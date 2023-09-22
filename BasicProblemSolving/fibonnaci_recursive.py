# 0,1,1,2,3,5,8...
def fibo(n):
    if(n<=1):
        return n
    else:
        return (fibo(n-1)+fibo(n-2))


if __name__ == '__main__':

    terms = 10
    if(terms<=0):
        print("Enter a positive number")
    else:
        for(i in range(terms)):
            fibo(i)
