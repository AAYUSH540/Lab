def set_feet_get():
    feet_value = float(input("Enter Number of Feet : "))
    return feet_value

def feet_to_inches(feet_value):
    inches_value= 12 * feet_value
    return inches_value

def display(inches_value):
    print(f"\nNumber Of Inches is ---> ",inches_value)

feet_value=set_feet_get()
inches_value=feet_to_inches(feet_value)
display(inches_value)