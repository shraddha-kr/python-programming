"""
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
if __name__ == '__main__':
    T = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        T.append([name, score])

    # print the main list
    # for stu in T:
    print("Original List -")
    print(T)

    # sort as per the score, col 1 of the nested list
    T.sort(key=lambda x:x[1])
    # for stu in T:
    print("Score sorted List -")
    print(T)

    # sort as per the name, col 0 of the nested list
    out_list = []

    print("T[1][1]", T[1][1])
    for stu in T:                
        if(T[1][1]==stu[1]):
            out_list.append(stu)

    out_list.sort()
    print(out_list[0])

    # OR
    records = []
    scores= []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)
    scores.sort()
    i=0
    while scores[i] == scores[0]:
        i=i+1
    lowest_score = scores[i]
    selected_students = []
    for record in records:
        if record[1] == lowest_score:
            selected_students.append(record[0])
    selected_students = sorted(selected_students)
    for name in selected_students :
        print(name)
        