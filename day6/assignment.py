print("====== 🐣🐣SQUARE NUMBERS CALCULATOR🐣🐣\n")

N = int(input("Enter a number: "))
squares = []

for i in range(1, N + 1):
    squares.append(i * i)

print(squares)