# Con una lista hay operaciones (ordenar, reajustar, etc).
# Con un array (vector) no hay operaciones (son fijos respecto a su orden).
# Una lista no es un array.

my_list = list()
print(len(my_list))

my_list = [51, 21, 30, 30, 21, "Naranja", 1.5]
print(my_list)
print(my_list.count(30))

my_other_list = [44, 1.68, "Winchester"]
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])

print("test")
print(my_list)
my_list.append("Hola")
my_list.insert(1, "rojo")
my_list.remove(51)

print(my_list)
my_list.pop()
print(my_list)
print(my_list.pop(2))
print(my_list)
my_list.clear()
print(my_list)
