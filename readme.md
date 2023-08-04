Problem Statement: NumberAdder Application

1. The NumberAdder application allows the user to add a specified number of numbers together.
2. The user first inputs the number of times they want to add numbers.
3. Then, the user provides the numbers one by one, limited to the specified count.
4. The application calculates and returns the sum of these numbers.

How to Use:

1. Run the main.py script in your Python environment.
2. The application will prompt you to enter the number of times you want to add numbers.
3. Please enter a positive integer greater than zero as the count.
4. After entering the count, the application will prompt you to input numbers one by one, equal to the specified count.
5. Please enter valid integers for each input.
6. The application will display the sum of the entered numbers in integer format.

Different Approaches:

<>Single Class Approach (main.py):

1. The single class approach uses the NumberAdder class defined in the main.py file.
2. The NumberAdder class encapsulates the functionality of the application.
3. It includes methods for getting the count of numbers, getting the numbers from the user, and calculating the sum.
4. The main logic of the program is inside the if __name__ == "__main__": block in main.py.

<>Modular Approach (number_adder.py and main.py):

1. The modular approach splits the functionality into separate files.
2. The NumberAdder class is defined in the number_adder.py file.
3. The number_adder.py file acts as a module containing the class definition.
4. The main script main.py imports the NumberAdder class from number_adder.py and utilizes its methods to achieve the application's functionality.
5. This approach promotes code modularity and reusability.

Dependencies:

1. The NumberAdder application requires Python 3.x to run.
