# The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month.   The points are awarded as follows:
# If a customer purchases 0 books, they earn 0 points.
# If a customer purchases 2 books, they earn 5 points.
# If a customer purchases 4 books, they earn 15 points.
# If a customer purchases 6 books, they earn 30 points.
# If a customer purchases 8 or more books, they earn 60 points.
# Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.

books = int(input('How many books have you purchased this month?'))
points = 0

if 0 <= books < 2:
    points = 0
elif 2 <= books < 4:
    points = 5
elif 4 <= books < 6:
    points = 15
elif 6 <= books < 8:
    points = 30
elif books >= 8:
    points = 60
print(f'Congratulations, you earned {points} points!')
