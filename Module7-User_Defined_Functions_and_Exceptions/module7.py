# Dictionary containing course numbers and room numbers of the roofms where the courses meet:

RoomNumber = {
    'CSC101' : 3004,
    'CSC102' : 4501,
    'CSC103' : 6755,
    'NET110' : 1244, 
    'COM241' : 1411
}

# Dicitonary containing course numbers and the names of the instructors that teach each course:

Instructors = {
    'CSC101' : 'Haynes',
    'CSC102' : 'Alvarado',
    'CSC103' : 'Rich',
    'NET110' : 'Burke',
    'COM241' : 'Lee'
}

# Dictionary containing course numbers and the meeting times of each course.

MeetingTime = {
    'CSC101' : '8:00 a.m.',
    'CSC102' : '9:00 a.m.',
    'CSC103' : '10:00 a.m.',
    'NET110' : '11:00 a.m.',
    'COM241' : '1:00 p.m.'
}

# Program should let the user enter a course number and then it should display the course's room number, instructor, and meeting time.


CourseNumber = input('Enter your course number:')

try:
    print('Course {} meets in room number {} at {}.'.format(CourseNumber,RoomNumber[CourseNumber],MeetingTime[CourseNumber]))
    print(f'The course instructor is {Instructors[CourseNumber]}.')

except KeyError:
    print(f'Error: Course {CourseNumber} not found.')