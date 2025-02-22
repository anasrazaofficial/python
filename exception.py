try:
    num = int(input("Divide 10 by: "))
    print(10 / num)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Can not divide by zero")
