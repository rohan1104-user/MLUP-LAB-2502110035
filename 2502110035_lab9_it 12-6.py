it 12- 
import os

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create 15 shift log records, including 3 deliberately faulty records
records = [
    "WO01,Employee: Rahul,Shift: Morning,Hours: 8",
    "WO02,Employee: Amit,Shift: Evening,Hours: 7",
    "WO03,Employee: Priya,Shift: Night,Hours: 8",
    "WO04,Employee: Neha,Shift: Morning,Hours: 6",
    "WO05,Employee: Ravi,Shift: Evening,Hours: 8",
    "WO06,Employee: Sita,Shift: Night,Hours: 7",
    "WO07,Employee: Karan,Shift: Morning,Hours: 8",

    # Three deliberately filthy (invalid) records
    "WO08,Employee: ,Shift: Morning,Hours: 8",       # Missing employee
    "WO09,Employee: Aman,Shift: Unknown,Hours: -5",  # Invalid shift and hours
    "WO10,Employee: Riya,Shift: Night,Hours: abc",   # Non-numeric hours

    "WO11,Employee: Arjun,Shift: Morning,Hours: 8",
    "WO12,Employee: Meena,Shift: Evening,Hours: 6",
    "WO13,Employee: Dev,Shift: Night,Hours: 7",
    "WO14,Employee: Pooja,Shift: Morning,Hours: 8",
    "WO15,Employee: Sanjay,Shift: Evening,Hours: 5"
]

# Write records to the file
with open("data/shift_log.txt", "w", encoding="utf-8") as file:
    for record in records:
        file.write(record + "\n")

# Read the file back and count the lines
with open("data/shift_log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Contents of shift_log.txt:")
print("".join(lines))

print("Total line count:", len(lines))

it 8- 
import os
import csv
from collections import defaultdict

os.makedirs("data", exist_ok=True)

valid = []
rejects = []
summary = defaultdict(lambda: [0, 0.0])

# Read and validate
with open("data/shift_log.txt", encoding="utf-8") as f:
    lines = f.readlines()

for n, line in enumerate(lines, 1):
    try:
        p = [x.strip() for x in line.strip().split(",")]
        if len(p) != 4:
            raise ValueError("Invalid fields")

        wo = p[0]
        emp = p[1].split(":", 1)[1].strip()
        shift = p[2].split(":", 1)[1].strip()
        hours = float(p[3].split(":", 1)[1].strip())

        if not wo or not emp:
            raise ValueError("Missing work order or employee")
        if shift not in ("Morning", "Evening", "Night"):
            raise ValueError("Invalid shift")
        if not 0 < hours <= 24:
            raise ValueError("Invalid hours")

        valid.append((wo, emp, shift, hours))
        summary[shift][0] += 1
        summary[shift][1] += hours

    except (ValueError, IndexError) as e:
        rejects.append([n, line.strip(), str(e)])

# Write report
with open("data/report.txt", "w", encoding="utf-8") as f:
    f.write(f"{'Work Order':<12}{'Employee':<20}{'Shift':<12}{'Hours':>6}\n")
    f.write("-" * 50 + "\n")
    for wo, emp, shift, hours in valid:
        f.write(f"{wo:<12}{emp:<20}{shift:<12}{hours:>6.2f}\n")

    f.write("\nSHIFT SUMMARY\n")
    for shift, (count, hours) in sorted(summary.items()):
        f.write(f"{shift}: {count} records, {hours:.2f} hours\n")

# Write rejected rows
with open("data/rejects.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Line", "Rejected Record", "Reason"])
    w.writerows(rejects)

print("Input lines:", len(lines))
print("Accepted:", len(valid))
print("Rejected:", len(rejects))
print("Created data/report.txt and data/rejects.csv")
