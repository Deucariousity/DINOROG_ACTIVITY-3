print("Minutes and Seconds Converter")
integer_seconds = int(input("Enter an integer for seconds:"))
minutes = integer_seconds // 60
seconds = minutes % 6 + 18
print(integer_seconds, "seconds is", int(minutes), "minutes and", int(seconds), "seconds.")
