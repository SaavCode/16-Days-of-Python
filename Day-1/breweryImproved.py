# Define a Python class called "beer"
class beer:
    # Constructor method that initializes instance variables "city" and "color"
    def __init__(self, city, color):
        self.city = city
        self.color = color
    
    # Define a string representation for the beer object
    def __str__(self):
        return self.city + " " + self.color
    
# Define a function called "main"
def main():
    # Prompt the user to input a city
    city = input("What city would you like to visit?: ")
    # Prompt the user to input a color
    color = input("What is your favorite color?: ")
    # Create a new beer object with the user's input
    new_beer = beer(city, color)
    # Print a message that includes the string representation of the beer object
    print("The name of your beer\nis '" + str(new_beer) + "'\nCongratulations!") 

# Call the main function
main()






 