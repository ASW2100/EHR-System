import os
import numpy as np
import random

def store_data(patient_data):
    pid = patient_data['pid']
    filename = f"{pid}.txt"
    
    with open(filename, 'a') as file:
        file.write(f"{patient_data}\n")
    
    if not os.path.exists("pid_dir.txt"):
        open("pid_dir.txt", 'w').close()
    
    with open("pid_dir.txt", 'r+') as pid_file:
        pids = pid_file.read().splitlines()
        if pid not in pids:
            pid_file.write(f"{pid}\n")

def show_data(pid):
    filename = f"{pid}.txt"
    if not os.path.exists(filename):
        print("Patient does not exist in our records.")
        return
    
    with open(filename, 'r') as file:
        print(file.read())

def cost_data():
    if not os.path.exists("pid_dir.txt"):
        print("No patient records available.")
        return
    
    costs = []
    with open("pid_dir.txt", 'r') as pid_file:
        pids = pid_file.read().splitlines()
        for pid in pids:
            filename = f"{pid}.txt"
            with open(filename, 'r') as file:
                for line in file:
                    record = eval(line.strip())
                    costs.append(record['cost'])
    
    if costs:
        print(f"Average cost: {np.mean(costs):.2f}")
        print(f"Median cost: {np.median(costs):.2f}")
        print(f"Standard deviation: {np.std(costs):.2f}")
    else:
        print("No cost data available.")

def rand_data():
    pids = ["Alice123", "Bob456", "Charlie789"]
    reasons = ["Flu symptoms", "Routine check-up", "Injury", "Allergy treatment"]
    return {
        "pid": random.choice(pids),
        "reason for visit": random.choice(reasons),
        "cost": round(random.uniform(0, 250), 2)
    }

def main():
    if not os.path.exists("pid_dir.txt"):
        open("pid_dir.txt", 'w').close()
    
    while True:
        print("\nElectronic Health Record System")
        print("1) Store patient data")
        print("2) Show patient data")
        print("3) Show cost data")
        print("4) Quit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            pid = input("Enter patient ID: ")
            reason = input("Enter reason for visit: ")
            cost = float(input("Enter cost: "))
            store_data({"pid": pid, "reason for visit": reason, "cost": cost})
        elif choice == "2":
            pid = input("Enter patient ID: ")
            show_data(pid)
        elif choice == "3":
            cost_data()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
