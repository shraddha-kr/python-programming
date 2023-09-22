
from collections import OrderedDict

subjects = ['physics', 'chemistry','biology']
# print(subjects)

subjects[2] = 'whatever'
# print(subjects)

mylist = [10,1,2,3,3,1,4,10,5,6,4]
b = list(OrderedDict.fromkeys(mylist))
b.sort()
print(b)

programming_languages = ["Python", "Swift","Java", "C++", "Go", "Rust"]

programming_languages.sort(key=len, reverse=True)

print(programming_languages)

#output

#['Go', 'C++', 'Java', 'Rust', 'Swift', 'Python']

programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

def get_year(element):
    return element['year']

programming_languages.sort(key=get_year)

print(programming_languages)

programming_languages = [{'language':'Python','year':1991},
{'language':'Swift','year':2014},
{'language':'Java', 'year':1995},
{'language':'C++','year':1985},
{'language':'Go','year':2007},
{'language':'Rust','year':2010},
]

programming_languages.sort(key=lambda element: element['year'])

print(programming_languages)