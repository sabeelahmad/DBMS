# module that stores all functions

import student
import faculty
import book
import pickle


def check_if_isbn_present(isbn):

    curr_data_books = []
    with open('books_data.pkl', 'rb') as fi_bk:
        while True:
            try:
                curr_data_books.append(pickle.load(fi_bk))
            except EOFError:
                break

    for bk in curr_data_books:
        if bk.isbn == isbn:
            return True
    return False


def check_if_eid_present(eid):

    curr_emps = []

    with open('faculty_data.pkl', 'rb') as fi_fac:
        while True:
            try:
                curr_emps.append(pickle.load(fi_fac))
            except EOFError:
                break

    for emp in curr_emps:
        if emp.eid == eid:
            return True
    return False


def verify_authentication(eid):
    return check_if_eid_present(eid)


def check_if_admnid_present(admn_id_no, year_of_admn, branch):

    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break

    for std in curr_students:
        if std.admn_id_no == admn_id_no and std.year_of_admn == year_of_admn and std.branch == branch:
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

    with open('faculty_data.pkl', 'ab') as fi_fac:
        # dumping data into file
        pickle.dump(f, fi_fac)


def add_student():
    # input returns a string by default

    name = input('Enter name of Student: ')
    year_of_admn = input('Enter Year of Admission of Student: ')
    branch = input('Enter branch of student: ')
    admn_id_no = input('Enter Admission ID: ')
    if check_if_admnid_present(admn_id_no, year_of_admn, branch):
        print('A student with the same details already entered. Cannot Add Student.')
        return

    # Now creating student using all the details that the user will enter
    s = student.StudentClass(name, year_of_admn, branch, admn_id_no)

    # add created student to list
    student.student_list.append(s)
    with open('student_data.pkl', 'ab') as fi_std:

        # dumping data
        pickle.dump(s, fi_std)


def add_book():
    # ask for parameters of a book from user

    title = input('Enter Book Title: ')
    author = input('Enter Name of Author: ')
    isbn = int(input('Enter Book ISBN: '))
    num_copies_to_add = int(input('Enter number of copies of this book to be added: '))
    if check_if_isbn_present(isbn):
        print('Book with same ISBN and title already exists, Book details have been updated')
        get_books = []
        with open('books_data.pkl', 'rb') as fi_bk:
            while True:
                try:
                    get_books.append(pickle.load(fi_bk))
                except EOFError:
                    break
        for i in range(0, len(get_books)):
            if get_books[i].isbn == isbn:
                cp = get_books[i].num_copies
                get_books.pop(i)
                bk_new = book.BookClass(title, author, isbn, num_copies_to_add + cp)
                book.book_list.append(bk_new)

            for j in range(0, len(book.book_list)):
                with open('books_data.pkl', 'wb') as fi_bk:
                    pickle.dump(book.book_list[j], fi_bk)

    else:
        # calling book constructor
        bk_new = book.BookClass(title, author, isbn, num_copies_to_add)

        #  add new book to list of books
        book.book_list.append(bk_new)

        # pickle book
        with open('books_data.pkl', 'ab') as fi_bk:

            # dump
            pickle.dump(bk_new, fi_bk)

    print('Book details updated in system..')


def print_student_details():

    student_details = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                student_details.append(pickle.load(f))
            except EOFError:
                break

    for st in student_details:
        print('Name : ' + st.name)
        print('Roll No :' + st.roll_no)


def print_faculty_details():

    faculty_details = []
    with open('faculty_data.pkl', 'rb') as fi_fac:
        while True:
            try:
                faculty_details.append(pickle.load(fi_fac))
            except EOFError:
                break
    for fc in faculty_details:
        print('Faculty Name : ' + fc.ename)
        print('Faculty ID : ' + fc.eid)


def print_book_details():

    book_details = []
    with open('books_data.pkl', 'rb') as fi_bk:
        while True:
            try:
                book_details.append(pickle.load(fi_bk))
            except EOFError:
                break

    for bk in book_details:
        print('Title : ' + bk.title)
        print('Author : ' + bk.author)
        print(f'ISBN {bk.isbn}')
        print(f'Copies available are : {bk.num_copies}')

# def issue_book():
#
#     verify_auth = input('Enter Unique Employee ID: ')
#     if verify_authentication(verify_auth):
#
#         # ask for student roll no
#         std_roll = input('Enter Roll No of Student: ')
#         if std_present(std_roll):
#             # if std_present search for book
#         else:
#             print('Student Not Found. Cannot Issue Book.')
#     else:
#         print('You are not authorized to issue a book. Try again.')


