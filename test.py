# Jim Eddy
# CS - 21
# Exercise 4-3 (Mass and Weight)

# Global Constant
GRAVITY = 9.8

#Added this comment

def main():

    mass = float(input('Enter a mass in kilograms: '))

    if mass > 0:
        show_weight(mass)
    else:
        print('Please enter a positive value for mass.')

def show_weight(mass):
  
    # calculate weight
    weight = mass * GRAVITY
    
    # test for > 1000 newtons
    if weight > 1000:
        print('The object weighs',format(weight, '.2f'),
              'newtons, and is too heavy!') 

    elif weight < 10:
        print('The object weighs',format(weight, '.2f'),
              'newtons, and is too light!')

    else:
        print('The object weighs',format(weight, '.2f'),
              'newtons, and is within the acceptable range.')

main()

    mass = float(input('Enter a mass in kilograms: '))

    if mass > 0:
        show_weight(mass)
    else:
        print('Please enter a positive, non-zero value for mass.')
