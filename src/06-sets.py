# un set es una estructura no ordenada de elementos únicos, que no se repiten
# un set es una "bolsa" de elementos no repetidos

# constructor
my_set = set()
my_other_set = {}

print(type(my_set))

my_set = {"queen", "king", "princess"}
print(my_set)

my_set.add("prince")
print(my_set)

my_set.add("prince")
print(my_set)
