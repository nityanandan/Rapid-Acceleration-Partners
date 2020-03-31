n = int(input("Enter a number:"))

for number in range(1,n):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
        continue
    print(number)
    

    