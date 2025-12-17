# ===================================
# PAYROLL PROCESSING SYSTEM
# ===================================

# Employee database
employees = {
    "1111": {"first": "Harry", "last": "Potter", "rate": 25.50},
    "1112": {"first": "Hermione", "last": "Granger", "rate": 28.75},
    "1113": {"first": "Ron", "last": "Weasley", "rate": 22.00},
    "1114": {"first": "Albus", "last": "Dumbledore", "rate": 45.00},
    "1115": {"first": "Severus", "last": "Snape", "rate": 38.50},
    "1116": {"first": "Luna", "last": "Lovegood", "rate": 24.00},
    "1117": {"first": "Draco", "last": "Malfoy", "rate": 30.00},
    "1118": {"first": "Neville", "last": "Longbottom", "rate": 21.50},
    "1119": {"first": "Ginny", "last": "Weasley", "rate": 26.75},
    "1120": {"first": "Rubeus", "last": "Hagrid", "rate": 20.00}
}

def menu():
    """Display menu and get choice"""
    print("\n" + "=" * 40)
    print("  PAYROLL PROCESSING SYSTEM")
    print("=" * 40)
    print("1. Process Payroll")
    print("2. Add Employee (Admin)")
    print("3. View Employees")
    print("4. Exit")
    print("=" * 40)
    
    choice = input("Choice: ").strip()
    return choice

def authenticate_admin():
    """Check if user is Brandon Moe"""
    print("\n--- Admin Authentication ---")
    first = input("First Name: ").strip()
    last = input("Last Name: ").strip()
    emp_id = input("Admin ID: ").strip()
    
    if first.lower() == "brandon" and last.lower() == "moe" and emp_id == "1983":
        print("✓ Authenticated")
        return True
    else:
        print("✗ Access Denied")
        return False

def add_employee():
    """Add or update employee (admin only)"""
    if not authenticate_admin():
        return
    
    print("\n--- Add Employee ---")
    first = input("First Name: ").strip()
    last = input("Last Name: ").strip()
    emp_id = input("Employee ID (4 digits): ").strip()
    
    # Validate ID
    while not emp_id.isdigit() or len(emp_id) != 4:
        emp_id = input("Error: Must be 4 digits. Try again: ").strip()
    
    # Check if exists
    if emp_id in employees:
        print(f"Employee exists: {employees[emp_id]['first']} {employees[emp_id]['last']}")
        print(f"Current rate: ${employees[emp_id]['rate']:.2f}")
        update = input("Update rate? (Y/N): ").strip().upper()
        if update == "Y":
            rate = float(input("New rate: $"))
            employees[emp_id]["rate"] = rate
            print("✓ Rate updated")
    else:
        rate = float(input("Hourly rate: $"))
        employees[emp_id] = {"first": first, "last": last, "rate": rate}
        print("✓ Employee added")

def view_employees():
    """Display all employees"""
    print("\n--- Employee List ---")
    for emp_id in sorted(employees.keys()):
        emp = employees[emp_id]
        print(f"{emp_id}: {emp['first']} {emp['last']} - ${emp['rate']:.2f}/hr")

def get_input():
    """Get employee info for payroll"""
    print("\n--- Process Payroll ---")
    
    first = input("First Name: ").strip()
    while not first:
        first = input("Required. First Name: ").strip()
    
    last = input("Last Name: ").strip()
    while not last:
        last = input("Required. Last Name: ").strip()
    
    emp_id = input("Employee ID: ").strip()
    while not emp_id.isdigit() or len(emp_id) != 4:
        emp_id = input("Error: Must be 4 digits. Try again: ").strip()
    
    deps = int(input("Dependents (0-15): "))
    while deps < 0 or deps > 15:
        deps = int(input("Error: 0-15 only. Try again: "))
    
    hours = float(input("Hours worked (0-60): "))
    while hours < 0 or hours > 60:
        hours = float(input("Error: 0-60 only. Try again: "))
    
    return first, last, emp_id, deps, hours

def lookup_employee(emp_id, first, last):
    """Verify employee and return rate"""
    if emp_id not in employees:
        print("✗ Employee ID not found")
        return None
    
    emp = employees[emp_id]
    if first.lower() != emp["first"].lower() or last.lower() != emp["last"].lower():
        print(f"✗ Name mismatch. Expected: {emp['first']} {emp['last']}")
        return None
    
    print(f"✓ Verified: {emp['first']} {emp['last']}")
    return emp["rate"]

def calculate_pay(hours, rate):
    """Calculate gross pay with overtime"""
    if hours > 40:
        reg_pay = 40 * rate
        ot_pay = (hours - 40) * rate * 1.5
    else:
        reg_pay = hours * rate
        ot_pay = 0
    
    gross = reg_pay + ot_pay
    return reg_pay, ot_pay, gross

def calculate_taxes(gross):
    """Calculate taxes and net pay"""
    state = gross * 0.056
    federal = gross * 0.079
    total = state + federal
    net = gross - total
    return state, federal, total, net

def display_summary(first, last, emp_id, deps, hours, rate, reg, ot, gross, state, fed, total, net):
    """Show payroll summary"""
    print("\n" + "=" * 40)
    print("  PAYROLL SUMMARY")
    print("=" * 40)
    print(f"Employee: {first} {last} (ID: {emp_id})")
    print(f"Dependents: {deps}")
    print("-" * 40)
    print(f"Hours: {hours:.2f} @ ${rate:.2f}/hr")
    print(f"Regular Pay: ${reg:.2f}")
    print(f"Overtime Pay: ${ot:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print("-" * 40)
    print(f"State Tax: ${state:.2f}")
    print(f"Federal Tax: ${fed:.2f}")
    print(f"Total Tax: ${total:.2f}")
    print("-" * 40)
    print(f"NET PAY: ${net:.2f}")
    print("=" * 40)

def save_record(first, last, emp_id, deps, hours, rate, reg, ot, gross, state, fed, total, net):
    """Save to CSV file"""
    try:
        with open("payroll_records.csv", "a") as f:
            f.write(f"{first},{last},{emp_id},{deps},{hours:.2f},{rate:.2f},"
                   f"{reg:.2f},{ot:.2f},{gross:.2f},{state:.2f},{fed:.2f},"
                   f"{total:.2f},{net:.2f}\n")
        print("✓ Record saved")
    except Exception as e:
        print(f"✗ Save error: {e}")

def process_payroll():
    """Main payroll processing"""
    first, last, emp_id, deps, hours = get_input()
    
    rate = lookup_employee(emp_id, first, last)
    if not rate:
        print("Payroll cancelled")
        return
    
    reg, ot, gross = calculate_pay(hours, rate)
    state, fed, total, net = calculate_taxes(gross)
    
    display_summary(first, last, emp_id, deps, hours, rate, reg, ot, gross, state, fed, total, net)
    save_record(first, last, emp_id, deps, hours, rate, reg, ot, gross, state, fed, total, net)

def main():
    """Main program loop"""
    print("Welcome to Hogwarts Payroll System!")
    
    while True:
        choice = menu()
        
        if choice == "1":
            process_payroll()
        elif choice == "2":
            add_employee()
        elif choice == "3":
            view_employees()
        elif choice == "4":
            print("\nGoodbye! 🧙‍♂️")
            break
        else:
            print("Invalid choice")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
