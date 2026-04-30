#EMPLOYEE DATA VAULT SYSTEM



import pickle
import os

def addEmployee():
    with open('employee.bin', 'ab') as file:
        eid      = input("\n\tEnter Employee ID: ")
        name     = input("\tEnter Employee Name: ")
        dept     = input("\tEnter Employee Department: ")
        position = input("\tEnter Employee Position: ")
        email    = input("\tEnter Employee Email: ")
        phone    = input("\tEnter Employee Phone: ")
        pickle.dump(eid, file)
        pickle.dump(name, file)
        pickle.dump(dept, file)
        pickle.dump(position, file)
        pickle.dump(email, file)
        pickle.dump(phone, file)
    print("\tEmployee Added Successfully!")
    input("\tPress Enter To Continue...")

def viewEmployee():
    try:
        with open('employee.bin', 'rb') as file:
            found = False
            while True:
                eid      = pickle.load(file)
                name     = pickle.load(file)
                dept     = pickle.load(file)
                position = pickle.load(file)
                email    = pickle.load(file)
                phone    = pickle.load(file)
                found = True
                print("\n\t==========================")
                print(f"\tEmployee ID       : {eid}")
                print(f"\tEmployee Name     : {name}")
                print(f"\tEmployee Dept     : {dept}")
                print(f"\tEmployee Position : {position}")
                print(f"\tEmployee Email    : {email}")
                print(f"\tEmployee Phone    : {phone}")
                print("\t==========================")
    except FileNotFoundError:
        print("\tNo Employee Data Found!")
    except EOFError:
        if not found:
            print("\tNo Records Found!")
    input("\tPress Enter To Continue...")

def deleteEmployee():
    try:
        file1 = open('employee.bin', 'rb')
    except FileNotFoundError:
        print("\tNo Data Found!")
        return
    file2 = open('temp.bin', 'wb')
    eid   = input("\n\tEnter Employee ID To Delete: ")
    found = 0
    try:
        while True:
            e        = pickle.load(file1)
            name     = pickle.load(file1)
            dept     = pickle.load(file1)
            position = pickle.load(file1)
            email    = pickle.load(file1)
            phone    = pickle.load(file1)
            if e == eid:
                print(f"\tEmployee Found: {name}")
                found = 1
            else:
                pickle.dump(e, file2);        pickle.dump(name, file2)
                pickle.dump(dept, file2);     pickle.dump(position, file2)
                pickle.dump(email, file2);    pickle.dump(phone, file2)
    except EOFError:
        pass
    file1.close()
    file2.close()
    os.remove('employee.bin')
    os.rename('temp.bin', 'employee.bin')
    print("\tEmployee Deleted!" if found else "\tEmployee Not Found!")
    input("\tPress Enter To Continue...")

def addSalary():
    eid        = input("\n\tEnter Employee ID: ")
    basic      = int(input("\tEnter Basic Salary: "))
    allowance  = int(input("\tEnter Allowance: "))
    deductions = int(input("\tEnter Deductions: "))
    net        = basic + allowance - deductions
    with open('salary.bin', 'ab') as file:
        pickle.dump(eid, file)
        pickle.dump(basic, file)
        pickle.dump(allowance, file)
        pickle.dump(deductions, file)
        pickle.dump(net, file)
    print(f"\tSalary Added! Net Salary: {net}")
    input("\tPress Enter To Continue...")

def viewSalary():
    try:
        with open('salary.bin', 'rb') as file:
            found = False
            while True:
                eid   = pickle.load(file)
                basic = pickle.load(file)
                allow = pickle.load(file)
                ded   = pickle.load(file)
                net   = pickle.load(file)
                found = True
                print("\n\t==========================")
                print(f"\tEmployee ID  : {eid}")
                print(f"\tBasic Salary : {basic}")
                print(f"\tAllowance    : {allow}")
                print(f"\tDeductions   : {ded}")
                print(f"\tNet Salary   : {net}")
                print("\t==========================")
    except FileNotFoundError:
        print("\tNo Salary Data Found!")
    except EOFError:
        if not found:
            print("\tNo Records Found!")
    input("\tPress Enter To Continue...")

def saveTransaction(eid, ttype, amt):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('trans.bin', 'ab') as file:
        pickle.dump(eid, file)
        pickle.dump(ttype, file)
        pickle.dump(amt, file)
        pickle.dump(ts, file)

def updateSalary():
    try:
        file1 = open('salary.bin', 'rb')
    except FileNotFoundError:
        print("\tNo Salary Data Found!")
        return
    file2 = open('temp.bin', 'wb')
    eid   = input("\n\tEnter Employee ID To Update Salary: ")
    found = 0
    try:
        while True:
            e     = pickle.load(file1)
            basic = pickle.load(file1)
            allow = pickle.load(file1)
            ded   = pickle.load(file1)
            net   = pickle.load(file1)
            if e == eid:
                print(f"\tCurrent Net Salary : {net}")
                basic = int(input("\tEnter New Basic Salary: "))
                allow = int(input("\tEnter New Allowance: "))
                ded   = int(input("\tEnter New Deductions: "))
                net   = basic + allow - ded
                saveTransaction(eid, "Salary Update", net)
                print(f"\tUpdated Net Salary : {net}")
                found = 1
            pickle.dump(e, file2);    pickle.dump(basic, file2)
            pickle.dump(allow, file2);pickle.dump(ded, file2)
            pickle.dump(net, file2)
    except EOFError:
        pass
    file1.close()
    file2.close()
    os.remove('salary.bin')
    os.rename('temp.bin', 'salary.bin')
    print("\tSalary Updated!" if found else "\tEmployee Not Found!")
    input("\tPress Enter To Continue...")

def addBonus():
    try:
        file1 = open('salary.bin', 'rb')
    except FileNotFoundError:
        print("\tNo Salary Data Found!")
        return
    file2 = open('temp.bin', 'wb')
    eid   = input("\n\tEnter Employee ID: ")
    amt   = int(input("\tEnter Bonus Amount: "))
    found = 0
    try:
        while True:
            e     = pickle.load(file1)
            basic = pickle.load(file1)
            allow = pickle.load(file1)
            ded   = pickle.load(file1)
            net   = pickle.load(file1)
            if e == eid:
                net += amt
                saveTransaction(eid, "Bonus", amt)
                found = 1
            pickle.dump(e, file2);    pickle.dump(basic, file2)
            pickle.dump(allow, file2);pickle.dump(ded, file2)
            pickle.dump(net, file2)
    except EOFError:
        pass
    file1.close()
    file2.close()
    os.remove('salary.bin')
    os.rename('temp.bin', 'salary.bin')
    print("\tBonus Added!" if found else "\tEmployee Not Found!")
    input("\tPress Enter To Continue...")

# MAIN MENU
while True:
    print("\n\t===== EMPLOYEE DATA VAULT SYSTEM =====")
    print('''
        1 - Add Employee
        2 - View Employees
        3 - Delete Employee
        4 - Add Salary
        5 - View Salary
        6 - Update Salary
        7 - Add Bonus
        0 - Exit
    ''')
    try:
        choice = int(input("\n\tEnter Choice: "))
    except Exception:
        print("\tInvalid Input!")
        continue

    if   choice == 1: addEmployee()
    elif choice == 2: viewEmployee()
    elif choice == 3: deleteEmployee()
    elif choice == 4: addSalary()
    elif choice == 5: viewSalary()
    elif choice == 6: updateSalary()
    elif choice == 7: addBonus()
    elif choice == 0: print("\tThank You!"); break
    else: print("\tInvalid Choice! TRY AGAIN!")
