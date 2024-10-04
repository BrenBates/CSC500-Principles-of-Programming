# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
# The program should first ask for the number of years.   The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.   
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall, 
# and the average rainfall per month for the entire period.
import array as arr

num_years = int(input('How many years?'))
rainfall = arr.array('f',[])
inches = 0
sum_inches = 0

# Outer loop - iterate once for each year

for i in range(num_years):

    # Inner loop, iterate 12 times, once for each month.  Each iteration ask the user for inches of rainfall for that month.
    for j in range(12):
        inches = float(input(f'How many inches of rainfall for month {j+1}?'))
        rainfall.append(inches)
        sum_inches += inches


print(f'You entered {num_years*12} months.')
print(f'The total inches of rainfall was {sum_inches:.2f} inches.')
print(f'The average rainfall per month for the entire period is {sum_inches/len(rainfall):.2f} inches.')