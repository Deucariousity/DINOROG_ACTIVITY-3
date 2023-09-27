while True:
    print()
    print("Minutes and Seconds Converter")
    print("Enter an integer for seconds")
    integer_seconds = eval(input("INPUT:"))
    minutes = integer_seconds // 60
    seconds = integer_seconds % 60
    print("OUTPUT:", integer_seconds, "seconds is", minutes, "minutes and", seconds, "seconds.")

    another = input("Do you want to convert again?(yes/no):")
    if another != 'yes':
        break

