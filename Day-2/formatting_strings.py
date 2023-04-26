#Formatfunction: enables you to concatenate parts of a
#string at desired intervals. Multiple pairs of curly braces can
#be used while formatting the string. Python will replace the
#placeholders with values in order.

car_color = "blue"
plate = "1234"
print("My car is {}, and it's license plate is {}" .format(car_color,plate))
#formatted string literals (f-strings): the newer way to
#format strings (Python 3.8+), with a simple and less
#verbose syntax: just include f at the beginning of the string
#and call the variables inside curly brackets.
print(f"My car is {car_color}, and it's license plate is {plate}")
