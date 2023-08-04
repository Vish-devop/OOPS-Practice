from NumberAdder import NumberAdder

def main():
    number_adder = NumberAdder()
    number_adder.get_num_of_times()
    number_adder.get_numbers()
    sum_of_numbers = number_adder.get_sum()
    print(f"Sum of the numbers: {sum_of_numbers}")


if __name__ == "__main__":
    main()