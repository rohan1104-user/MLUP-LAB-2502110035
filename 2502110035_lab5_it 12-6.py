it 12-
#Raw bench line
line = "P123 25.4 3.5"

# Extract the fields
part_code, dia, shift = line.split()

# Convert diameter to a real float
dia = float(dia)

# Print each value with a label
print("Part code:", part_code)
print("Diameter:", dia)
print("Shift:", shift)

# Prove diameter is a number
print("Diameter + 0.01:", dia + 0.01)

it 10-
# 10 log lines with messy spacing
logs = [
    "P101   25.4   A",
    "P102  30.2 B",
    "P103    18.7    C",
    "P104 22.5 D",
    "P105     27.8 E",
    "P106  31.0    F",
    "P107   19.6 G",
    "P108  24.3     H",
    "P109 29.7 I",
    "P110    21.5    J"
]

# One list to store all diameters
diameters = []

# Parse each log line
for line in logs:
    parts = line.split()

    part_code = parts[0]
    diameter = float(parts[1])
    shift = parts[2]

    diameters.append(diameter)

# Report the results
count = len(diameters)
average = sum(diameters) / count
minimum = min(diameters)
maximum = max(diameters)

print("Diameters:", diameters)
print("Count:", count)
print("Average:", average)
print("Minimum:", minimum)
print("Maximum:", maximum)

# Justification:
# A list is used because we want to keep every diameter,
# including duplicate values, and preserve their order.
# A set would remove duplicate values and does not preserve
# the original order in the same way. 

it-8
# 10 messy log lines
logs = [
    "P101   25.4   A",
    "P102  30.2 B",
    "P103    18.7    C",
    "P104 22.5 D",
    "P105     27.8 E",
    "P106  31.0    F",
    "P107   19.6 G",
    "P108  24.3     H",
    "P109 29.7 I",
    "P110    21.5    J"
]

# Three separate bins
accepted = []
rework = []
scrap = []

# Store the part codes that are scrapped
scrap_parts = []

# Parse and classify each log
for line in logs:
    parts = line.split()

    part_code = parts[0]
    diameter = float(parts[1])

    # Example diameter rules:
    # 22 <= diameter <= 28: accepted
    # 20 <= diameter < 22 or 28 < diameter <= 30: rework
    # Otherwise: scrap
    if 22 <= diameter <= 28:
        accepted.append(diameter)

    elif 20 <= diameter < 22 or 28 < diameter <= 30:
        rework.append(diameter)

    else:
        scrap.append(diameter)
        scrap_parts.append(part_code)

# Counts
print("Accepted count:", len(accepted))
print("Rework count:", len(rework))
print("Scrap count:", len(scrap))

# Accepted average
if accepted:
    accepted_average = sum(accepted) / len(accepted)
    print("Accepted average:", accepted_average)
else:
    print("Accepted average: No accepted parts")

# Part codes that were scrapped
print("Scrapped part codes:", scrap_parts)
