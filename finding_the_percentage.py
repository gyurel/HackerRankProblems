n = int(input())

students_dict = {}

for i in range(n):
    student_info = input().split()
    name = student_info[0]
    mark1 = float(student_info[1])
    mark2 = float(student_info[2])
    mark3 = float(student_info[3])
    students_dict[name] = []
    students_dict[name].append(mark1)
    students_dict[name].append(mark2)
    students_dict[name].append(mark3)

searched_name = input()

for key, val in students_dict.items():
    if key == searched_name:
        average_mark = sum(val) / 3
        print(f"{average_mark:.2f}")
        break