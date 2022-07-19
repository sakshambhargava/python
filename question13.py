sideOne = float(input("Enter the side A of a triangle: "))
sideTwo = float(input("Enter the side B of a triangle: "))
sideThree = float(input("Enter the side C of a triangle: "))
semiPerimeter = (sideOne+sideTwo+sideThree)/2
triangleArea = (semiPerimeter*(semiPerimeter-sideOne)*(semiPerimeter-sideTwo)*(semiPerimeter-sideThree))**0.5
print("The area of a triangle is",triangleArea)