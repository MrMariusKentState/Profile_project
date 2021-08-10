


#1. Update values in Dictionaries and lists

# a. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# b. Change the last_name of the first student from 'Jordan' to 'Bryant'
# c. In the sports_directory, change 'Messi' to 'Andres'
# d. Change the value 20 in z to 30


x = [ [5,2,3], [10,8,9] ]

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
student0 = students[0]
print(student0)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])


(z[0]['y']) = 30
print(z[0]['y'])





#2. Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(x):
    i = 0
    while i < len(x):
        for key, val in x[i].items():
            print(key, "-", val)
        i = i + 1

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




# 3.  Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iteratedictionary2(x, y):
    i = 0
    while i < len(y):
        print(y[i][x])
        i = i + 1


iteratedictionary2('first_name',students)
iteratedictionary2('last_name',students)


# 4. Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def PrintInfo(x,y):
    i = 0
    count = 0
    info = []
    while i < len(x[y]):
        info.append(x[y][i])
        i = i + 1
        count = count + 1
    print(count, y.upper())
    j = 0
    while j < len(info):
        print(info[j])
        j = j + 1
    if j == len(info):
        print("\n")


PrintInfo(dojo, 'locations')
PrintInfo(dojo, 'instructors')

