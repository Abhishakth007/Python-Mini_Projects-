print("Hello there welcome to the RollerCoaster Ride....!")
height = int (input("Enter you height in centimeters : "))
if height >=120:
    print("You are eligible to ride ..:)")
    age = int(input("Enter your age : "))
    if age <= 12:
        photo = input ("Types y if you want a photo along with your ticket ,if no then type anything ..")
        if photo == "y":
         print("You have to pay $8.")
        else :
          print("You have to pay $5.")
    elif((age>12) and (age <18)):
       photo = input ("Types y  if you want a photo along with your ticket ,if no then type anything ..")
       if photo == "y":
          print("You have to pay $10.")
       else :
          print("You have to pay $7")
    else:
       photo = input ("Types y  if you want a photo along with your ticket,if no then type anything ..")
       if photo =="y":
         print("You have to pay $15.")
       else :
           print("You have to pay $12")
else :
   print("You have to be more than 120 cm ..Sorry")


#The above code is just a sample for  understanding nested if statements .... Hint(You can reduce the size of code by taking a variable for bill counter)
