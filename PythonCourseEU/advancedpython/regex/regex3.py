# static file
import re
fh = open("/home/ubuntu/Desktop/Github/python-programming-practice/PythonCourseEU/advancedpython/simpsons_phone_book.txt")
for line in fh:
    if re.search(r"J.*Neu",line):
        print(line.rstrip())
fh.close()