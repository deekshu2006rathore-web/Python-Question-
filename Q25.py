def multiple_exceptions_demo():
    try:
        # Get two numbers from user
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        # Perform division
        result = a / b
        print(f"Result: {a} / {b} = {result}")
    
    except ValueError:
        print("Error: Invalid input! Please enter numeric values only.")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero! Second number cannot be zero.")
    
    except TypeError:
        print("Error: Type mismatch occurred (this usually doesn't happen with float inputs).")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the demo
multiple_exceptions_demo()