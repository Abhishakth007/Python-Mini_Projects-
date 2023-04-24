def add(x,y):
  return x+y
  

def sub(x,y):
  return x-y

def mul(x,y):
  return x*y
  

def div(x,y):
  return x/y
  

def mod(x,y):
  return x%y
  
x = int(input("What is your first_operand : "))
y = int(input("What is your second_operand : "))
def all_operators():
  print('''+
-
*
/
%''')

all_operators()
operation = input("Select an Operator from the above given operators : ")
if operation == "+":
   result = add(x,y)  
elif operation == "-":
   result = sub(x,y)
elif operation == "*":
  result = mul(x,y)
elif operation == "/":
   result = div(x,y)
elif operation == "%":
   result = mod(x,y)
else:
  print("Please enter a valid operator from the given opeartors.")


print(f'\nThe result of the operation {operation} is : {result}')

end_of_result = False
while not end_of_result:
      next_operation = input(f"\nType 'yes' if you want to perform another operation with the previous output '{result}'.").lower()
      if next_operation == "yes":
        x = result
        print(f'The first_operand is : {result}')
        y = int(input("Enter the second operand : "))
        all_operators()
        operation = input("Select an Operator from the above given operators : ")
        if operation == "+":
           result = add(x,y)  
        elif operation == "-":
           result = sub(x,y)
        elif operation == "*":
          result = mul(x,y)
        elif operation == "/":
           result = div(x,y)
        elif operation == "%":
           result = mod(x,y)
        else:
          print("Please enter a valid operator from the given opeartors.")
        print(f'\nThe result of the operation {operation} is : {result}')
      else:
        end_of_result = True
        print(f'Final result of your calculations is : {result}')
        print("Bye")
        
        


  




