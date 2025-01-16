import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Okay, we will create a instance for you.")
elif type == "t3.medium":
    print("Your Instance Cost 4$/Month")
elif type == "t3.medium":
    print("Your Instance Cost 8$/Month")
 elif type == "t3.medium":
    print("Your Instance Cost 16$/Month")
else:
    print("Please Provide a valid Instance Type.")