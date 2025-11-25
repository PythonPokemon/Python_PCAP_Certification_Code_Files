
# customer_number = input('Enter the employee number (dd-ddd-dddd): ')
customer_number = '12-345-6789'     # True
# customer_number = '12345-6789'    # False
# customer_number = 'A2-345-6789'   # False
# customer_number = '112-345-6789'  # False
parts = customer_number.split('-')
valid = False
if len(parts) == 3:
  if len(parts[0]) == 2 and len(parts[1]) == 3 and len(parts[2]) == 4:
    if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
      valid = True
print(valid)

# You might have to scroll a little to the right to see everything
