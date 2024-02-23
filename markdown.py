def markdown():
    x = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in numbers:
        if x < 5:
            print("I'm adding 1 to x")
            x +=1
            print(f"x equals {x}!")
        else:
            print("I'm done adding")

markdown()