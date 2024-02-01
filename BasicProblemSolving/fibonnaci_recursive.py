# 1, 1, 2, 3, 5, 8, 13 ...

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
   
if __name__ == '__main__':
    terms = int(input("Enter user input: "))
    
    for i in range(terms):
        print(recur_fibo(i))