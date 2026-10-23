def verifier_nombre(nombre):
    if not isinstance(nombre, int) or isinstance(nombre, bool):
        print("Erreur : veuillez saisir un nombre entier.")
    elif nombre < 0:
        print("Erreur : le nombre doit être positif.")
    elif nombre % 2 == 0:
        print(nombre, "est un nombre pair.")
    else:
        print(nombre, "est un nombre impair.")


# Appeler la fonction plusieurs fois avec des valeurs différentes
verifier_nombre(8)
verifier_nombre(5)
verifier_nombre(0)
verifier_nombre(-3)
verifier_nombre(12)
verifier_nombre(4.5)