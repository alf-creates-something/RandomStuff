for i in range(1,101):
    text = ""
    if i % 3 == 0:
        text += "Fizz"
    if i % 5 == 0:
        text += "Buzz"
    if i % 3 != 0 and i % 5 != 0:
        text += str(i)
    print(text)