import os


def pangrams(s):
    # Write your code here    
    thisset = list(s.strip().lower())
    # print(type(thisset))
    # print(len(thisset))
    for val in thisset:
        if(" "==val):
            thisset.remove(val)
    ss = set(thisset)        
    
    if(len(ss)==26):        
        print("pangram")
    else:
        print("not pangram")
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input() 

    result = pangrams(s)

    # fptr.write(result + '\n')

    # fptr.close()