class NumberAdder:
    def __init__(self):
        self.num_of_times = 0
        self.numbers = []

    def get_num_of_times(self):
        while True:
            try:
                self.num_of_times = int(input("Enter the number of times you want to add numbers: "))
                if self.num_of_times <= 0:
                    print("Please enter a positive integer greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid positive integer.")

    def get_numbers(self):
        for i in range(self.num_of_times):
            while True:
                try:
                    num = int(input(f"Enter number {i+1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer.")

    def get_sum(self):
        return sum(self.numbers)