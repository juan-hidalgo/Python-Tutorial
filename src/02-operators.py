# operadores ariméticos 
print("10 + 3 = ", 10 + 3)
print("10 - 3 = ", 10 - 3)
print("10 * 3 = ", 10 * 3)
print("10 / 3 = ", 10 / 3)
print("10 % 3 = ", 10 % 3)
print("10 // 3 = ", 10 // 3)
print("10 ** 3 = ", 10 ** 3)
print("Hola " * 5)

# operadores comparativos - bool =>
print("3 > 4 ",  3 > 4)
print("3 < 4 ",  3 < 4)
print("3 <= 4 ", 3 <= 4)
print("3 >= 4 ", 3 >= 4)
print("3 == 4 ", 3 == 4)
print("3 != 4 ", 3 != 4)

print("Hola > Python", "Hola" > "Python")
print("Z > Python", "Z" > "Python")
print("Hola < Python", "Hola" < "Python")
print("Hola >= Python", "Hola" >= "Python")
print("Hola <= Python", "Hola" <= "Python")
print("Hola == Python", "Hola" == "Python")
print("Hola != Python", "Hola" != "Python")
print("Hola == Hola", "Hola" == "Hola")
print("Hola == hola", "Hola" == "hola")

# operadores lógicos
print(3 > 4 and "Z" > "A")        # FALSE and TRUE -> FALSE
print(3 > 4 or "Z" > "A")         # FALSE or TRUE ->  TRUE
print(3 > 4 and not "Z" > "A")    # FALSE and not TRUE -> FALSE
print(3 > 4 or not "Z" > "A")     # FALSE or not TRUE -> FALSE

print(3 < 4 and "Z" > "A")        # TRUE and TRUE -> TRUE
print(3 < 4 or "Z" > "A")         # TRUE or TRUE ->  TRUE
print(3 < 4 and not "Z" > "A")    # TRUE and not TRUE -> FALSE
print(3 < 4 or not "Z" > "A")     # TRUE or not TRUE -> TRUE
