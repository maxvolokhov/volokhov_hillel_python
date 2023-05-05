# 1
from typing import List

john_salary = float(2.6)
marta_salary = float(4.3)
print(john_salary)
print(marta_salary)

# 2
john_age = int(28)
marta_age = int(23)
print(john_age)
print(marta_age)

# 3
john_name = 'Jack'
marta_name = 'Jenny'
print(john_name)
print(marta_name)

# 4
john_gender = False
marta_gender = True
print(john_gender)
print(marta_gender)

# 5
john_friends = ['Peter', 'James', 'Cole']
marta_friends = ['Rebecca', 'Jessica', 'Jenny']

# 6
names = ['Peter', 'James', 'Cole', 'Cole']
set(names)

# 7
latitude_tuple = (44.19,)
longitude_tuple = (28.6,)
#or latitude_longitude = (44.19, 28.6)
# 8
john = {'full_name': 'Johnatan', 'age': 28, 'salary': 2500, 'gender': False,
        'friends': ['Peter', 'James', 'Cole', 'Cole'], 'coordinates': [44.19, 28.6]}
marta = {'full_name': 'Martha', 'age': 23, 'salary': 1900, 'gender': True,
         'friends': ['Peter', 'James', 'Cole', 'Cole'], 'coordinates': [44.19, 28.6]}
for key, value in john.items():
    print(f'{key} => {value}')
for key, value in marta.items():
    print(f'{key} => {value}')

#Challenge
john_coords = (44.19, 28.6)
marta_coords = (44.19, 28.6)


john_friend1 = {
    'full_name': 'Peter',
    'age': 24,
    'salary': 2700,
    'gender': False,
    'friends': [],
    'coordinates': (48.23, 24.67)
}
john_friend2 = {
    'full_name': 'James',
    'age': 23,
    'salary': 1300,
    'gender': True,
    'friends': [],
    'coordinates': (27.91, 53.64)
}
marta_friend1 = {
    'full_name': 'Jeny',
    'age': 27,
    'salary': 2400,
    'gender': True,
    'friends': [],
    'coordinates': (36.19, 61.92)
}
marta_friend2 = {
    'full_name': 'Rebecca',
    'age': 25,
    'salary': 3000,
    'gender': True,
    'friends': [],
    'coordinates': (43.85, 36.94)
}


john = {
    'full_name': 'Johnatan',
    'age': 28,
    'salary': 2600,
    'gender': False,
    'friends': [john_friend1, john_friend2],
    'coordinates': john_coords
}

marta = {
    'full_name': 'Martha',
    'age': 23,
    'salary': 4300,
    'gender"': True,
    'friends': [marta_friend1, marta_friend2],
    'coordinates': marta_coords
}


for key, value in john.items():
    print(f'{key} => {value}')


for key, value in marta.items():
    print(f'{key} => {value}')
