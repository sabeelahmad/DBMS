# module that stores all functions

import student
import faculty
import book


def check_if_isbn_present(isbn):
    for bk in book.book_list:
        if bk.isbn == isbn:
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
    while True:
        eid = input('Enter faculty id: ')
        if check_if_eid_present(eid):
            continue
        else:
            break

    # create faculty using constructor
    f = faculty.FacultyClass(ename, eid)

    # add created faculty to list
    faculty.faculty_list.append(f)


def add_student():
    # input returns a string by default

    name = input('Enter name of Student: ')
    year_of_admn = input('Enter Year of Admission of Student: ')
    branch = input('Enter branch of student: ')
    while True:
        admn_id_no = input('Enter Admission ID: ')
        if check_if_admnid_present(admn_id_no):
            continue
        else:
            break

    # Now creating student using all the details that the user will enter
    s = student.StudentClass(name, year_of_admn, branch, admn_id_no)

    # add created student to list
    student.student_list.append(s)


def add_book():

    # ask for parameters of a book from user
    title = input('Enter Book Title: ')
    author = input('Enter Name of Author: ')
    while True:
        isbn = input('Enter Book ISBN: ')
        if check_if_isbn_present(isbn):
            continue
        else:
            break
    num_copies = input('Enter Number of Copies of Book To Be Added To Library: ')

    # calling book constructor
    bk_new = book.BookClass(title, author, isbn, num_copies)

    # add new book to list of books
    book.book_list.append(bk_new)


# def issue_book(book_title):
#
#     verify_auth = input('Enter Unique Employee ID: ')
#     if verify_authentication(verify_auth):
#           # if authenticated search for book
#           # if book found , search for student
#           # if student found and student num_books < 4 and student not issued this book already issue book




