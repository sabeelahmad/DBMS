# This file will include the class for students of the library

student_list = []


class StudentClass:

    branch_roll_mapping = {
        'COE': 'CO',
        'IT': 'IT',
        'ECE': 'EC',
        'ICE': 'IC',
        'MPAE': 'MP',
        'ME': 'ME',
        'BT': 'BT'
    }

    # instance initializer/constructor
    def __init__(self, name, year_of_admn, branch, admn_id_no):
        self.name = name
        self.year_of_admn = year_of_admn
        self.branch = branch
        self.admn_id_no = admn_id_no
        # Creating roll no string using variables that will be taken as input from users
        self.roll_no = self.year_of_admn + 'U' + StudentClass.branch_roll_mapping[self.branch] + self.admn_id_no
        # initialising details of books issued to student when student is created
        self.num_books_issued = 0
        self.books_issued = []



