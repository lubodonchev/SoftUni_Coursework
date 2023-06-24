# class Zoo:
#     animals = 0
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_animal(self, species, name):
#         if species == 'mammal':
#             mammals.append(name)
#         elif species == 'fish':
#             fishes.append(name)
#         elif species == 'bird':
#             birds.append(name)
#
#     def get_info(self, species):
#         if species == 'mammal':
#             c_species = 'Mammals'
#             lst = ', '.join(mammals)
#         elif species == 'fish':
#             c_species = 'Fishes'
#             lst = ', '.join(fishes)
#         elif species == 'bird':
#             c_species = 'Birds'
#             lst = ', '.join(birds)
#
#         return f'{c_species} in {zoo_name}: {lst}\nTotal animals: {Zoo.animals}'
#
#
# mammals, fishes, birds = [], [], []
#
# zoo_name = str(input())
# n = int(input())
#
# zoo = Zoo(zoo_name)
#
# for _ in range(n):
#     data_lst = input().split()
#     current_species, current_name = data_lst
#     zoo.add_animal(current_species, current_name)
#     Zoo.animals += 1
#
# chosen_species = str(input())
#
# print(zoo.get_info(chosen_species))

class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == 'mammal':
            c_species = 'Mammals'
            lst = ', '.join(self.mammals)
        elif species == 'fish':
            c_species = 'Fishes'
            lst = ', '.join(self.fishes)
        elif species == 'bird':
            c_species = 'Birds'
            lst = ', '.join(self.birds)

        return f'{c_species} in {self.name}: {lst}\nTotal animals: {Zoo.__animals}'


zoo_name = str(input())
n = int(input())

zoo = Zoo(zoo_name)

for _ in range(n):
    data_lst = input().split()
    current_species, current_name = data_lst
    zoo.add_animal(current_species, current_name)

chosen_species = str(input())

print(zoo.get_info(chosen_species))
