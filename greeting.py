

# Ask the user for their name
name = input("Please enter your name: ")

# Ask what day it is
day = input("What day of the week is it today? ")

# Print a greeting message
print("Hello,", name + "! Happy", day + "!")


# Define the feedback function
def get_feedback():
    feedback = input("What do you think of this greeting program? ")
    print("Thank you for your feedback!")

# Call the feedback function
get_feedback()
