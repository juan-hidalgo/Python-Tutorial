# convención = variables en minúsculas y snake_case como mi_variable

first_name = "Rupert"
age = 20
agent = False

print("Name: ", first_name, "\n",
      "Age: ", age, "\n",
      "Conscript?: ", agent)

print(age + age)
print(str(age) + str(age))

alias, team = "Jackie Joy", "Bravo28"
print(alias, "-", team)

alias = input("What's your alias?: ")
team = input("What's your team?: ")
print(alias, "-", team)
