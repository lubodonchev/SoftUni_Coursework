n = int(input())
master_dic = {}

for i in range(n):
    student = input()
    if student not in master_dic.keys():
        master_dic[student] = []
    master_dic[student].append(float(input()))

for key, value in master_dic.items():
    average = sum(value) / len(value)
    if average >= 4.5:
        print(f'{key} -> {average:.2f}')
