def verifier_nombre(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("négatif")
    else:
        print("nul")


verifier_nombre(5)
verifier_nombre(-3)
verifier_nombre(0)
verifier_nombre(12)
verifier_nombre(-8)