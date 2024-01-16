# una tupla es una lista inmutable y fija

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (44, 1.70, "Little", "Timmy")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])

# se puede convertir a lista para poder tener modificaciones

my_tuple = list(my_tuple)
