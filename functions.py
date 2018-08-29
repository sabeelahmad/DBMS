# module that stores all functions

import student
import faculty
import book
import pickle
import datetime


def check_avail_faculty(isbn, cp):
    # Load book data --> pls someone convert all the loadings to a function
    # don't curse me for shitty not dry code
    # ok cool bye
    get_books = []
    with open('books_data.pkl', 'rb') as fi_bk:
        while True:
            try:
                get_books.append(pickle.load(fi_bk))
            except EOFError:
                break
    for bk in get_books:
        if bk.isbn == isbn and bk.num_copies >= cp:
            return True
    return False


def modify_faculty(emp_id, issued):
    # load faculty data
    curr_emps = []

    with open('faculty_data.pkl', 'rb') as fi_fac:
        while True:
            try:
                curr_emps.append(pickle.load(fi_fac))
            except EOFError:
                break

    # modify faculty with emp_id
    for fac in curr_emps:
        if fac.eid == emp_id:
            fac.books_issued.append(issued)
            break

    # dump updated data to faculty pkl file
    for j in range(0, len(curr_emps)):
        if j == 0:
            with open('faculty_data.pkl', 'wb') as fi_fac:
                pickle.dump(curr_emps[j], fi_fac)
        else:
            with open('facutly_data.pkl', 'ab') as fi_fac:
                pickle.dump(curr_emps[j], fi_fac)


def modify_book(isbn, num_copies=1):
    # load data
    # num_copies has a default value of 1 for students
    get_books = []
    with open('books_data.pkl', 'rb') as fi_bk:
        while True:
            try:
                get_books.append(pickle.load(fi_bk))
            except EOFError:
                break
    # modify data
    for i in range(0, len(get_books)):
        if get_books[i].isbn == isbn:
            get_books[i].num_copies -= num_copies
            break
    # rewrite data
    for j in range(0, len(get_books)):
        if j == 0:
            with open('books_data.pkl', 'wb') as fi_bk:
                pickle.dump(get_books[j], fi_bk)
        else:
            with open('books_data.pkl', 'ab') as fi_bk:
                pickle.dump(get_books[j], fi_bk)


def check_if_already_issued_to_student(isbn, std_roll):
    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break
    for std in curr_students:
        if std.roll_no == std_roll:
            for bk in std.books_issued:
                if bk['isbn'] == isbn:
                    return False
    return True


def modify_student(std_roll, bk_issued):
    # load students
    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break
    # modify student with given roll no
    for std in curr_students:
        if std.roll_no == std_roll:
            std.books_issued.append(bk_issued)
            std.num_books_issued += 1
    # overwrite file with new data
    for i in range(0, len(curr_students)):
        if i == 0:
            with open('student_data.pkl', 'wb') as fs:
                pickle.dump(curr_students[i], fs)
        else:
            with open('student_data.pkl', 'ab') as fs:
                pickle.dump(curr_students[i], fs)


def check_available(isbn, std_roll):
    # load book data from file
    curr_data_books = []
    with open('books_data.pkl', 'rb') as fi_bk:
        while True:
            try:
                curr_data_books.append(pickle.load(fi_bk))
            except EOFError:
                break
    for bk in curr_data_books:
        if bk.isbn == isbn and bk.num_copies > 0:
            return check_if_already_issued_to_student(bk.isbn, std_roll)
    return False


def check_std_limit(std_roll):
    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break
    for std in curr_students:
        if std.roll_no == std_roll and std.num_books_issued <= 4:
            return True
    return False


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


def std_present(std_roll):

    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break

    for std in curr_students:
        if std.roll_no == std_roll:
            return True
    return False


def add_faculty():
    # ask input from user
    ename = input('Enter faculty name: ')
    eid = input('Enter faculty id (5 digits): ')
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

    branch_roll_mapping = {
        'COE': 'CO',
        'IT': 'IT',
        'ECE': 'EC',
        'ICE': 'IC',
        'MPAE': 'MP',
        'ME': 'ME',
        'BT': 'BT'
    }

    name = input('Enter name of Student: ')
    year_of_admn = input('Enter Year of Admission of Student: ')
    branch = input('Enter branch of student: ')
    admn_id_no = input('Enter Admission ID: ')
    std_roll = year_of_admn + 'U' + branch_roll_mapping[branch] + year_of_admn
    if std_present(std_roll):
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
                if j == 0:
                    with open('books_data.pkl', 'wb') as fi_bk:
                        pickle.dump(book.book_list[j], fi_bk)
                else:
                    with open('books_data.pkl', 'ab') as fi_bk:
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
        print('Books Issued : ' + str(st.num_books_issued))
        for bk in st.books_issued:
            print(f"Book ISBN : {bk['isbn']}")
            print(f"Date Of Issue : {bk['doi']}")


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


def issue_book_student():
    std_roll = input('Enter Student Roll No To Whom Book Has To Be Issued : ')
    # check if student present in library records
    if std_present(std_roll):
        # find student with given data and check if he has reached book limit
        if check_std_limit(std_roll):
            # getting here means book limit has not been reached and hence we can issue book
            # ask for book isbn
            book_isbn = int(input('Enter ISBN of Book That Has To Be Issued : '))
            # check if given isbn is present and num copies of it are > 0
            # also check is student has this book issued already or not
            if check_available(book_isbn, std_roll):
                # means isbn present and copies > 0
                # create a dict that will store isbn of book, and date of issue
                issue_obj = {
                    'isbn': book_isbn,
                    'doi': datetime.datetime.now()
                }
                # push created object into students issued books array
                modify_student(std_roll, issue_obj)
                # reached here means book has been issued successfully
                print('Book Issued To Student With ' + std_roll + ' Successfully.')
                # modify book details in library reduce copies
                modify_book(book_isbn)
            else:
                # either isbn not present or all copies exhausted
                print('Book Not Available, All Copies Have Exhausted OR Book Issued Already. Cannot Issue Book.')
        else:
            print('Student Has Reached Book Limit. Cannot Issue Book.')
    else:
        print('Student not found. Cannot Issue Book.')


def issue_book_facutly():
    emp_id = input('Enter Faculty ID To Whom Book Has To Be Issued: ')
    # check if emp_id present
    if check_if_eid_present(emp_id):
        # A faculty personal has no limit hence no need to check for anything
        # We can simply issue book to him/her
        book_isbn = int(input('Enter Book ISBN That Has To Be Issued: '))
        # Since faculty can issue more than one copy of book, we need to ask for num_copies as well
        num_copies = int(input('Enter Number Of Copies To Be Issued: '))
        # Check if this book is present and its copies are >= num_copies
        if check_avail_faculty(book_isbn, num_copies):
            # Means book available with num copies
            # Now just issue book to faculty
            issue_obj = {
                'isbn': book_isbn,
                'doi' : datetime.datetime.now()   # stores current date in doi => date_of_issue
            }
            # add book to faculty data
            modify_faculty(emp_id, issue_obj)
            # modify book details in library
            modify_book(book_isbn, num_copies)
            # Book issued
            print(f'Book with {book_isbn} has been issued to employee with eid {emp_id}')
        else:
            print(f'Book with {book_isbn} not available/Copies Exhausted. Cannot issue book')
    else:
        print(f'Employee with {emp_id} not present. Cannot issue book.')

# search book functions - minor
# return book by student
# return book by faculty

# fine calculation

# archive 4+ year students - will do this in main script before running init function
# eg : if __name__ == __main__ ==> archive_students()


# Add exception handling if time allows


# pls refactor code :'(((( not DRY at all, shitty as fuck code
