history=[]


def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b==0:
        return None
    return a / b

def modulus(a,b):
    if b==0:
        return None
    return a % b

def  power(a,b):
    return a**b

def display_menu():
    print("\n =============CALCULATOR APP================")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Power")
    print("7.View History")
    print("8.Clear History")
    print("9.Exit")
    print("================================================")
    
    
def get_number(message):
        
    while True:
            
        try:
            number=float(input(message))
            return number
            
        except ValueError:
            print("Error: please enter a valid number")

while True:
    display_menu()
    
    choice= input("Enter value (1-9)---")
        
        #Exit
    if choice=="9":
        print("Thank you for using calculator")
        break
               
        #view history
    if choice =="7":
        print("==========Calculation History================")
        if len(history)==0:
            print("No history found")
        else:
            for calculation in history:
                print(calculation)  
        continue
        # clear history
    if choice =="8":
        history.clear()
        print("Calculation history cleared")
        continue
                  
        #check operation 
    elif choice in["1","2","3","4","5","6"]:
        num1= get_number("Enter first number: ")
        num2= get_number("Enter second number: ")
            
            #addition
        if choice== "1":
            result=addition(num1,num2)
            calculation=f"{num1}+{num2} = {result}"
                
        elif choice =="2":
            result=subtraction(num1,num2)
            calculation=f"{num1}-{num2} = {result}"
                
        elif choice =="3":
            result=multiplication(num1,num2)
            calculation=f"{num1}*{num2}= {result}"
                
        elif choice =="4":
            result=division(num1,num2)
            if result is None:
                print("Error: cannot divided by zero")
                continue
            calculation=f"{num1}/{num2}={result}"
                
        elif choice =="5":
            result=modulus(num1,num2)
            if result is None:
                print("The number cannot perform module by zero")
                continue
            calculation=f"{num1}%{num2}={result}"
                
        elif choice =="6":
            result=power(num1,num2)
            calculation=f"{num1}^{num2}={result}"
                                          
            #Display result
        print("\nResult= ",result) 
            
            #save calculation:
        history.append(calculation)
            
            
    else:
            print("\nInvalid Choice")
            print("please choice a number between 1 to 9")       
 
            
                