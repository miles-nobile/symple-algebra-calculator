import MilesMath
#test
print("what would you like to use?")
usrInput = input("press 1 to find slope from two points or 2 for point slope to slope intercept conversion 3 for transformation: ")
if usrInput == "1":
    MilesMath.findSlopeFromPoint()
elif usrInput == "2":
    MilesMath.pointSlopeToSlopeIntercept()
elif usrInput == "3":
    MilesMath.transformation()
