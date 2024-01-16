# strings

my_string_01 = "Hello World"
my_string_02 = 'Hi people'

print("Cadena 1:")
print(my_string_01)
print("Largo: ", len(my_string_01))

print("Cadena 2:")
print(my_string_02)
print("Largo: ", len(my_string_02))

my_new_line = "String \ncon salto de línea"
print(my_new_line)

my_tab_string = "String \tcon tabulación"
print(my_tab_string)

my_string_scape = "String escapado \\t \\n"
print(my_string_scape)

# Formateo:
name, surname, age = "Winchester", "McMillan", 40
print("Soy {} {} y tengo {} años".format(name, surname, age))
print("Soy %s %s y tengo %d años" % (name, surname, age))
print(f"Soy {name} {surname} y tengo {age} años")

# No son buenas prácticas:
print("Soy " + name + " " + surname + " y tengo " + str(age)+" años")
print("Soy", name, surname, "y tengo", age, "años")

# Unpackaging chars
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)

# P Y T H O N
# 0 1 2 3 4 5

language_slice = language[1:3]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-3]
print(language_slice)
language_slice = language[-3]
print(language_slice)

reversed_language = language[::-1]
print(reversed_language)

print(language.capitalize())
print(language.casefold())
print(language.upper())
print(language.lower())
print(language.count("o"))
print(language.isnumeric())
print("42".isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))
print(language.startswith("py"))
