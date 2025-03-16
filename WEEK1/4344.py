C = int(input())

for i in range(C):
    student_info = list(input().split(" "))
    student_num = int(student_info[0])
    student_score = list()
    for j in range(len(student_info) - 1):
        student_score.append(float(student_info[j + 1]))

    student_avg = float(sum(student_score) / student_num)
    overAvgstudent_num = 0
    underAvgstudent_num = 0
    
    for j  in range(student_num):
        if student_score[j] > student_avg:
            overAvgstudent_num = overAvgstudent_num + 1
        else:
            underAvgstudent_num = underAvgstudent_num + 1
    print(f"{(overAvgstudent_num/student_num)*100:.3f}" + '%')

