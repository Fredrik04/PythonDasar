try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
    print("The result is: ",result)

    #jika terjadi IndexError
    mylist = [1,2,3]
    print(mylist[4])

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error Invalid input, please enter a number")
except IndexError:
    print("Error: Index out of range")


    
