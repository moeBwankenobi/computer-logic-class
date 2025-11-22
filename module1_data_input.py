# MODULE 1: Data Input & Validation
# Purpose: Get employee information from user and validate inputs

def collect_employee_data():
    """Collect and validate employee information"""
    
    print("=== EMPLOYEE DATA ENTRY ===\n")
    
    # Collect and validate first name
    while True:
        first_name = input("Enter employee first name: ").strip()
        
        if len(first_name) == 0:
            print("Error: First name cannot be empty")
        elif len(first_name) > 50:
            print("Error: First name too long (max 50 characters)")
        elif not first_name.replace(" ", "").replace("-", "").isalpha():
            print("Error: First name must contain only letters")
        else:
            break  # Valid input, exit loop
    
    # Collect and validate last name
    while True:
        last_name = input("Enter employee last name: ").strip()
        
        if len(last_name) == 0:
            print("Error: Last name cannot be empty")
        elif len(last_name) > 50:
            print("Error: Last name too long (max 50 characters)")
        elif not last_name.replace(" ", "").replace("-", "").isalpha():
            print("Error: Last name must contain only letters")
        else:
            break
    
    # Collect and validate employee ID
    while True:
        employee_id = input("Enter employee ID (4-10 characters): ").strip()
        
        if len(employee_id) == 0:
            print("Error: Employee ID cannot be empty")
        elif not employee_id.isalnum():
            print("Error: Employee ID must be alphanumeric (letters and numbers only)")
        elif len(employee_id) < 4 or len(employee_id) > 10:
            print("Error: Employee ID must be 4-10 characters")
        else:
            break
    
    # Collect and validate number of dependents
    while True:
        try:
            num_dependents = int(input("Enter number of dependents: "))
            
            if num_dependents < 0:
                print("Error: Number of dependents cannot be negative")
            elif num_dependents > 20:
                confirm = input("Warning: Unusual number of dependents (>20). Is this correct? (Y/N): ")
                if confirm.upper() == 'Y':
                    break
            else:
                break
        except ValueError:
            print("Error: Please enter a whole number")
    
    # Collect and validate hours worked
    while True:
        try:
            hours_worked = float(input("Enter hours worked this period: "))
            
            if hours_worked < 0:
                print("Error: Hours worked cannot be negative")
            elif hours_worked > 168:
                print("Error: Hours worked exceeds hours in a week (168)")
            elif hours_worked > 80:
                confirm = input("Warning: Unusual hours worked (>80). Is this correct? (Y/N): ")
                if confirm.upper() == 'Y':
                    break
            else:
                break
        except ValueError:
            print("Error: Please enter a valid number")
    
    # Display summary for confirmation
    print("\n=== EMPLOYEE INFORMATION SUMMARY ===")
    print(f"Name: {first_name} {last_name}")
    print(f"Employee ID: {employee_id}")
    print(f"Dependents: {num_dependents}")
    print(f"Hours Worked: {hours_worked}")
    
    final_confirm = input("\nIs this information correct? (Y/N): ")
    
    if final_confirm.upper() == 'Y':
        return first_name, last_name, employee_id, num_dependents, hours_worked
    else:
        print("\nRestarting data entry...\n")
        return collect_employee_data()


# Main program execution
if __name__ == "__main__":
    # Call the function and store the returned values
    first, last, emp_id, dependents, hours = collect_employee_data()
    
    print("\n=== DATA COLLECTION COMPLETE ===")
    print(f"Successfully collected data for {first} {last}")