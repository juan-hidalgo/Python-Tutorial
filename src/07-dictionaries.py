# Un diccionario es una esctructura donde se almacenan datos clave: valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict))

print(my_dict)
print(my_other_dict)

my_dict = {"Name": "Rupert", "Lastname": "McMillan", "Age": 34, 2: "abd"}

my_other_dict = {
    "Name": "Rupert",
    "Lastname": "McMillan",
    "Age": 34,
    2:    "abd"
    }

print(my_dict)
print(my_dict["Lastname"])
print(my_dict[2])

print(my_dict.items())
print(my_dict.values())
print(my_dict.keys())
print(my_dict.fromkeys("Name", 1))
print(my_dict.fromkeys(my_other_dict))
