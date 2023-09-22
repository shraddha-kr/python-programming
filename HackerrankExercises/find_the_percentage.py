if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    score_list = student_marks.get(query_name)
    total, avg = 0
    
    for m in score_list:
        total = total + m
        
    avg = total / len(score_list)
    print(avg)