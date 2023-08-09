from ThreeDigitNumberChecker import ThreeDigitNumberChecker
from calculation import Calcultion
from ReverseAscii import ReverseAscii

def main():
    NumberChecker=ThreeDigitNumberChecker()
    result=[]

    while True: 
        NumberChecker.get_number_from_user()

        if NumberChecker.check_three_digit():
            num1=NumberChecker.number
            NumberChecker.get_number_from_user()
            

            if NumberChecker.check_three_digit():
                num2=NumberChecker.number

                calculator=Calcultion(num1,num2)
                reverse_ascii_calculator=ReverseAscii(num1,num2)

                #appending the values into the result.
                result.append(["Addition: ",calculator.add(),
                            "Subtract: ",calculator.subtract(),
                            "Multiply: ",calculator.multiply(),
                            "Division: ",calculator.divide()])
                result.append([
                            "reverse_ascii_num1: ",reverse_ascii_calculator.reversed_ascii_values_num1(),"reverse_ascii_num2: ",reverse_ascii_calculator.reversed_ascii_values_num2()
                            ])
                
            
        
        print("Result Matrix: ")
        for row in result:
            print(row)
            

        choice=input("Do you want to continue? Yes or No ")
        if choice.lower()=='no':
            break
    
    
        


if __name__=='__main__':
    main()

# choice=input("Do you want to continue? (Yes/no)")
# if choice.lower=='yes':
#     main()