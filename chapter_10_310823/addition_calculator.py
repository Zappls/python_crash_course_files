def addition():
    """Adds the 2 arguments,
    prints an error message if the input is not a number."""
    print("Type 'quit' to exit.")
    flag = True
    while flag:
        number1 = input("Type in the first number you wish to add: ")
        if number1.lower() == 'quit':
            break
        else:
            try:
                num1 = int(number1)
            except ValueError:
                print("Only numbers can be added!")
            else:
                while True:
                    number2 = input("Type in the second number you wish to add: ")
                    if number2.lower() == 'quit':
                        flag = False
                        break
                    else:
                        try:
                            num2 = int(number2)
                        except ValueError:
                            print("Only numbers can be added!")
                        else:
                            result = int(num1) + int(num2)
                            print(f"The result is {result}.")
                            break


addition()
