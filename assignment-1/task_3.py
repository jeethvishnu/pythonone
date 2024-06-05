import math


def calculate_square_root():
    while True:
        try:

            number = float(input("Enter a non-negative number: "))


            if number < 0:
                raise ValueError("Error: Please enter a non-negative number.")


            square_root = math.sqrt(number)


            print(f"The square root of {number} is: {square_root}")
            break

        except ValueError as e:
            print(f"Invalid input: {e}")
        except NameError as e:
            print(f"Unexpected error: {e}")
        finally:
            print("Program execution completed.")


# Call the function to start the program
calculate_square_root()
