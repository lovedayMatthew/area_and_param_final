#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
length= float(input("Please enter the length:\t\t"))
width = float(input("Please enter the widt:\t"))

# calculate miles per gallon
area = round(length * width,1)
parmieter = round(2*length+2*width, 1)

            
# format and display the result
print()
print("Area =\t\t" + str(area))
print ("Perimeter\t\t"+ str(parmieter))
print()
print("Thank you for using this program!")
