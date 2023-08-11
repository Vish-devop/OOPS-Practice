from ThreeDigitNumberChecker import ThreeDigitNumberChecker
from calculation import Calcultion
from ReverseAscii import ReverseAscii

class BaseProgram():

    def __init__(self):
        self.result=[]

    def main(self):
        NumberChecker=ThreeDigitNumberChecker()
        

        while True: 
             #for inputting a line b/w 2-iteration inputs.

            num2,num1=NumberChecker.get_number_from_user(),NumberChecker.get_number_from_user()
            print("*"*10)
            if not NumberChecker.check_three_digit():
                print("Please enter a Valid 3-digit number.")
                continue
                
            calculator=Calcultion(num1,num2)
            reverse_ascii_calculator=ReverseAscii(num1,num2)
                    
            self.result.append([
                f"Addition:{calculator.add()},Substraction:{calculator.subtract()},Multiply:{calculator.multiply()},Division:{calculator.divide()}"
            ])
            self.result.append([
                f"Reverse_num1_ascii:{reverse_ascii_calculator.reversed_ascii_values_num1()}, Reverse_num2_ascii: {reverse_ascii_calculator.reversed_ascii_values_num2()}"
            ])
            # self.result.append(result_row)
           
            self.print_result()

            if not self.ask_to_continue():
                break
                    
    # method: printing the result
    def print_result(self):    
            print("Result Matrix: ")
            for row in self.result:
                print("\n".join(row))
                
        
    # method: asking for continue
    def ask_to_continue(self):
        choice=input("Do you want to continue? Yes or No ")
        return choice.lower()=='yes'
        
            
        
    # def get_number_from_user(self):
    #     return int(input("Enter a number: "))
    
    # def check_three_digit(self,number):
    #     return 100<=number<=999
            


if __name__=='__main__':
    program=BaseProgram()
    program.main()

# choice=input("Do you want to continue? (Yes/no)")
# if choice.lower=='yes':
#     main()