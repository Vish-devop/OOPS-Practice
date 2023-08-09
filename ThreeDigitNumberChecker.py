class ThreeDigitNumberChecker:
    def __init__(self):
        self.number=0
    
    def get_number_from_user(self):
        while True:
            try:
                self.number=int(input("Enter a 3-digit number: "))
                # self.num1=int(input("Enter a 3-digit number1: "))
                # self.num2=int(input("Enter a 3-digit number2: "))
                if 100<=(self.number)<=999:
                    break
                else: 
                    print("Please enter a 3-digit number")
            except ValueError:
                print("Invalid input! Please enter only a 3-digit integer number")

    def check_three_digit(self):
        return 100<=self.number<=999
    