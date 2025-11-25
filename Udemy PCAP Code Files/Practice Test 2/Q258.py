
employees = []

# for i in range(1, 196):
for i in range(1, 6): # Just for convenience
    employees.append('Employee' + str(i))

for i in range(1, 6):
    employees.append('Manager' + str(i))

print(employees)
print(employees[:-5])
print(employees[0:-5])
print(employees[1:-4])
# One manager present and one employee is missing
print(employees[1:-5])  # One employee is missing
print(employees[0:-4])  # One manager present
