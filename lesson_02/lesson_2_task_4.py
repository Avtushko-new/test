def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:  # Проверка делимости на 3 и 5 (т.е. на 15)
            print("FizzBuzz")
        elif i % 3 == 0:  # Проверка делимости только на 3
            print("Fizz")
        elif i % 5 == 0:  # Проверка делимости только на 5
            print("Buzz")
        else:
            print(i)

fizz_buzz(15)