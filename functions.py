# module that stores all functions

import student
import faculty
import book
import pickle


def check_if_isbn_present(isbn, num_copies_to_add):
    for bk in book.book_list:
        if bk.isbn == isbn:
            bk.num_copies += num_copies_to_add
            return True
    return False


def check_if_eid_present(eid):
    for emp in faculty.faculty_list:
        if emp.eid == eid:
            return True
    return False


def verify_authentication(eid):
    return check_if_eid_present(eid)


def check_if_admnid_present(admn_id_no):
    for std in student.student_list:
        if std.admn_id_no == admn_id_no:
            return True
    return False


def add_faculty():
    # ask input from user
    ename = input('Enter faculty name: ')
    eid = input('Enter faculty id: ')
    if check_if_eid_present(eid):
        print('Faculty with this eid already exists. Cannot add Faculty.')
        return

    # create faculty using constructor
    f = faculty.FacultyClass(ename, eid)

    # add created faculty to list
    faculty.faculty_list.append(f)

    with open('faculty_data.pkl', 'wb') as fi_fac:
        # dumping data into file
        pickle.dump(faculty.faculty_list, fi_fac)


def add_student():
    # input returns a string by default

    name = input('Enter name of Student: ')
    year_of_admn = input('Enter Year of Admission of Student: ')
    branch = input('Enter branch of student: ')
    admn_id_no = input('Enter Admission ID: ')
    if check_if_admnid_present(admn_id_no):
        print('A student with this admission ID already exists. Cannot add student.')
        return

    # Now creating student using all the details that the user will enter
    s = student.StudentClass(name, year_of_admn, branch, admn_id_no)

    # add created student to list
    student.student_list.append(s)
    with open('student_data.pkl', 'wb') as fi_std:

        # dumping data
        pickle.dump(student.student_list, fi_std)


def add_book():
    # ask for parameters of a book from user

    while True:
        title = input('Enter Book Title: ')
        author = input('Enter Name of Author: ')
        isbn = input('Enter Book ISBN: ')
        num_copies_to_add = int(input('Enter number of copies of this book to be added: '))
        if not check_if_isbn_present(isbn, num_copies_to_add):
            # calling book constructor
            bk_new = book.BookClass(title, author, isbn, num_copies)

            #  add new book to list of books
            book.book_list.append(bk_new)


def print_student_details():

    with open('student_data.pkl', 'rb') as fi_std:
        student.student_list = pickle.load(fi_std)

    for st in student.student_list:
        print(st.name)
        print(st.year_of_admn)
        print(st.branch)
        print(st.roll_no)


def print_faculty_details():

    with open('faculty_data.pkl', 'rb') as fi_fac:
        faculty.faculty_list = pickle.load(fi_fac)

# def issue_book(book_title):
#
#     verify_auth = input('Enter Unique Employee ID: ')
#     if verify_authentication(verify_auth):
#           # if authenticated search for book
#           # if book found , search for student
#           # if student found and student num_books < 4 and student not issued this book already issue book



