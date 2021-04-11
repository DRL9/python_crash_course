while True:
    input_txt = input("please input: ")
    if input_txt == 'q':
        print("Bye!")
        break
    else:
        try:
            num = int(input_txt)
            result = 10 / num
        except ValueError:
            print(f"{input_txt} is not number")
        except ZeroDivisionError:
            print(f"{input_txt} cannot be divider")
        else:
            print(f"result is {result}")

