try:
    a = 1 / 0
except ZeroDivisionError as e:
    raise ValueError("Cannot divide by zero") from e
except ValueError as e:
    print("ValueError occured: ",e)

    