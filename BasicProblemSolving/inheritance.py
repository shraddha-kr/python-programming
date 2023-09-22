class employee:
    num_emp=0
    raise_amount=1.04

    def __init__(self, first_name, last_name, sal):
        self.first_name=first_name
        self.last_name=last_name
        self.sal=sal
        self.email=first_name + '.' + last_name + '@company.com'
        employee.num_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
                              
                              
class developer(employee):
    pass
    

if __name__ == '__main__':
    emp_1 = developer('sam', 'johnson', 10000)
    print(emp_1.email)
