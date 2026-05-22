def grades():
    nota = int(input())

    if 9 <= nota <= 10:
        print("Excelente")
    elif 7 <= nota <= 8:
        print("Bueno")
    elif 5 <= nota <= 6:
        print("Regular")
    elif 0 <= nota <= 4:
        print("Insuficiente")
