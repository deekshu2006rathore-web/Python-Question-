# Custom exception class
class NegativeNumberError(Exception):
    """Exception raised for negative number inputs."""
    pass

def check_positive_number():
    try:
        num = int(input("Enter a positive integer: "))
        
        if num < 0:
            raise NegativeNumberError(f"Number {num} is negative. Only positive numbers allowed.")
        
        print(f"You entered: {num}")
        print(f"Square root: {num ** 0.2:.2f}")  # Just a sample operation
    
    except ValueError:
        print("Error: Invalid input! Please enter an integer.")
    
    except NegativeNumberError as e:
        print(f"Custom exception caught: {e}")
    
    finally:
        print("This 'finally' block always executes, regardless of exceptions.")

# Run the function
check_positive_number()