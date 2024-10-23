
#psudocode
#add dictionarie, to file, 
# print out each of the items requeted 


course_rooms = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

course_instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

course_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

def display_info(course_number): 
    if course_number in course_rooms: 
        print(f"course: {course_number}")
        print(f"room: {course_rooms[course_number]}")
        print(f"instructor: {course_instructors[course_number]}")
        print(f"time: {course_times[course_number]}")
    else: 
        print("course not found")

def main(): 
    for key in course_rooms.keys():
        print(key)
    course = input("enter one of the courses above: ")
    display_info(course)

if __name__=="__main__":
    main()