# Program to demonstrate exception handling with try-except

def safe_division():
    try:
        numerator = float(input("Enter numerator: "))
        denominator = float(input("Enter denominator: "))
        result = numerator / denominator
        print(f"Result: {numerator} / {denominator} = {result}")
    
    except ValueError:
        print("Error: Please enter numeric values only.")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
safe_division()