def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "opérateur invalide"


num1 = float(input("entrez le premier nombre : "))
operator = input("entrez un opérateur (+, -, *, /, %) : ")
num2 = float(input("entrez le deuxième nombre : "))

print("Résultat :", calcule(num1, operator, num2))