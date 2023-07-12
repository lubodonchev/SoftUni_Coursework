dic = {}

while True:
    data = input()
    if data[0].isupper():
        name, aidi, course = data.split(':')
        dic[aidi] = {
            'name': name,
            'course': course
        }
    else:
        break

modified_data = " ".join(data.split('_'))

for key, value in dic.items():
    if value['course'] == modified_data:
        print(f"{value['name']} - {key}")
