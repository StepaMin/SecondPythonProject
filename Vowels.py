print("Программа подсчитывает кол-во гласных в строке")


Vowels = ["a", "A", "o", "O", "u", "U", "i", "I", "e", "E", "y", "Y"]
Counter = [0, 0, 0, 0, 0, 0]

def FindVowels():
    inputValues = input("Введите любой текст латиницей: ")
    for i in range(len(Vowels)):
        for j in range(len(inputValues)):
            if Vowels[i] == inputValues[j]:
                Counter[int((i)/2)] += 1
while(True):
    FindVowels()
    print("[a, o, u, i, e, y]")
    print(Counter)
    Counter = [0, 0, 0, 0, 0, 0]
