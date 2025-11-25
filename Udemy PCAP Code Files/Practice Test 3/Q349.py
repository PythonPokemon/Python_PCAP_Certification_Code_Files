
# distance = float(input('Enter the distance travelled in feet'))
distance = float('437723.42')  # Just for convenience
distance_miles = distance/5280

# time = float(input('Enter the time elapsed in seconds'))
time = float('1723.9')  # Just for convenience
time_hours = time/3600  # convert to hours

velocity = distance_miles/time_hours
print('The average Velocity : ', velocity, 'miles/hour')
# The average Velocity : 173.1236071486956 miles/hour

print((float('437723.42')/5280) / (float('1723.9')/3600))
# 173.1236071486956
# print((int('437723.42')/5280) / (int('1723.9')/3600))
# ValueError
print((int(float('437723.42'))/5280) / (int(float('1723.9'))/3600))
# 173.21387115496228
