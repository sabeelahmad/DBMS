# module that stores all functions

import student
import faculty
import book
import pickle
import datetime


def load_student():
    # load student data
    curr_students = []
    with open('student_data.pkl', 'rb') as f:
        while True:
            try:
                curr_students.append(pickle.load(f))
            except EOFError:
                break
    return curr_students


def load_faculty():
    # load faculty data
    curr_emps = []
    with open('faculty_data.pkl', 'rb') as fi_fac:
        while True:
            try:
                curr_emps.append(pickle.load(fi_fac))
            except EOFError:
                break
    return curr_emps


def load_books():
    # load books data
    get_books = []
    with open('books_data.pkl', 'rb') as fi_bk:
        while True:
            try:
                get_books.append(pickle.load(fi_bk))
            except EOFError:
                break
    return get_books


def dump_students(curr_students):
    for i in range(0, len(curr_students)):
        if i == 0:
            with open('student_data.pkl', 'wb') as f:
                pickle.dump(curr_students[i], f)
        else:
            with open('student_data.pkl', 'ab') as f:
                pickle.dump(curr_students[i], f)


def dump_faculty(curr_emps):
    for i in range(0, len(curr_emps)):
        if i == 0:
            with open('faculty_data.pkl', 'wb') as f:
                pickle.dump(curr_emps[i], f)
        else:
            with open('faculty_data.pkl', 'rb') as f:
                pickle.dump(curr_emps[i], f)


def search_book(mode, data):
    books = load_books()
    if mode == 'i':
        # isbn search
        for bk in books:
            if bk.isbn == data:
                print(f'Book details are: \nAuthor:{bk.author}\nTitle:{bk.title}\nCopies Available:{bk.num_copies}')
        print('Book not available.')
    elif mode == 't':
        # title search
        for bk in books:
            if bk.title.lower() == data.lower():
                print(f'Book details are: \nAuthor:{bk.author}\nTitle:{bk.title}\nCopies Available:{bk.num_copies}')
                return
        print('Book not available.')
    elif mode == 'a':
        # search using author
        flag = 0
        for bk in books:
            if bk.author.lower() == data.lower():
                print(f'Book details are: \nAuthor:{bk.author}\nTitle:{bk.title}\nCopies Available:{bk.num_copies}')
                flag = 1
        if flag == 0:
            print('Book not available.')


def modify_std_on_return(book_isbn, roll):
    # load student data
    curr_students = load_student()
    # modify student
    for st in curr_students:
        if st.roll_no == roll:
            for bk in st.books_issued:
                if bk['isbn'] == book_isbn:
                    st.num_books_issued -= 1
                    st.books_issued.remove(bk)

    # replace old file data with new
    dump_students(curr_students)


def calc_fine(roll, book_isbn):
    curr_students = load_student()
    # search for student with given roll and issued isbn
    dor = 0
    doi = 0
    for s in curr_students:
        if s.roll_no == roll:
            for bk in s.books_issued:
                if bk['isbn'] == book_isbn:
                    # get doi and calc dor using datetime module
                    doi = bk['doi']
                    dor = datetime.datetime.now()
                    break
    # check for fine
    diff_days = dor - doi
    if diff_days.days > 14:
        fine = 2 * (diff_days.days - 14)
        print(f'Fine amount payable is : Rs.{fine}')
    else:
        print('Thank you for returning the book within the stipulated time.')


def modify_faculty_on_return(book_isbn, emp_id):
    # load faculty data
    curr_emps = load_faculty()
    # modification
    nc = 0
    for e in curr_emps:
        if e.eid == emp_id:
            for bk in e.books_issued:
                if bk['isbn'] == book_isbn:
                    nc = bk['nc']
                    e.books_issued.remove(bk)
    # dump modified data
    dump_faculty(curr_emps)
    return nc


def issued_faculty(book_isbn, emp_id):
    curr_emps = load_faculty()
    # search for isbn in loaded data
    for emp in curr_emps:
        if emp.eid == emp_id:
            for bk in emp.books_issued:
                if bk['isbn'] == book_isbn:
                    return True
    return False


def check_avail_faculty(isbn, cp):
    get_books = load_books()
    for bk in get_books:
        if bk.isbn == isbn and bk.num_copies >= cp:
            return True
    return False


def modify_faculty(emp_id, issued):
    curr_emps = load_faculty()
    # modify faculty with emp_id
    for fac in curr_emps:
        if fac.eid == emp_id:
            fac.books_issued.append(issued)
            break
    # dump updated data to faculty pkl file
    dump_faculty(curr_emps)


def modify_book(isbn, num_copies=1, mode=0):
    # load data
    # num_copies has a default value of 1 for students
    get_books = load_books()
    # modify data
    for i in range(0, len(get_books)):
        if get_books[i].isbn == isbn and mode == 0:
            get_books[i].num_copies -= num_copies
            break
        if get_books[i].isbn == isbn and mode == 1:
            get_books[i].num_copies += num_copies
    # rewrite data
    for j in range(0, len(get_books)):
        if j == 0:
            with open('books_data.pkl', 'wb') as fi_bk:
                pickle.dump(get_books[j], fi_bk)
        else:
            with open('books_data.pkl', 'ab') as fi_bk:
                pickle.dump(get_books[j], fi_bk)


def check_if_already_issued_to_student(isbn, std_roll):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll:
            for bk in std.books_issued:
                if bk['isbn'] == isbn:
                    return False
    return True


def modify_student(std_roll, bk_issued):
    curr_students = load_student()
    # modify student with given roll no
    for std in curr_students:
        if std.roll_no == std_roll:
            std.books_issued.append(bk_issued)
            std.num_books_issued += 1
    # overwrite file with new data
    dump_students(curr_students)


def check_available(isbn, std_roll):
    # load book data from file
    curr_data_books = load_books()
    for bk in curr_data_books:
        if bk.isbn == isbn and bk.num_copies > 0:
            return check_if_already_issued_to_student(bk.isbn, std_roll)
    return False


def check_std_limit(std_roll):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll and std.num_books_issued <= 4:
            return True
    return False


def check_if_isbn_present(isbn):
    curr_data_books = load_books()
    for bk in curr_data_books:
        if bk.isbn == isbn:
            return True
    return False


def check_if_eid_present(eid):
    curr_emps = load_faculty()
    for emp in curr_emps:
        if emp.eid == eid:
            return True
    return False


def verify_authentication(eid):
    return check_if_eid_present(eid)


def std_present(std_roll):
    curr_students = load_student()
    for std in curr_students:
        if std.roll_no == std_roll:
            return True
    return False


def add_faculty():
    # ask input from user
    try:
        ename = input('Enter faculty name: ')
        while True:
            eid = input('Enter faculty id (5 digits): ')
            if len(eid) != 5:
                print('eid has to be 5 digits long, try again.')
            else:
                break
    except ValueError:
        print('Invalid Input')
    else:
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
    try:
        name = input('Enter name of Student: ')
        while True:
            year_of_admn = input('Enter Year of Admission of Student: ')
            if int(year_of_admn) > datetime.datetime.now().year:
                print(f'Year of admission cannot be greater than {datetime.datetime.now().year}')
            else:
                break
        branch = input('Enter branch of student: ')
        while True:
            admn_id_no = input('Enter Admission ID (4 digits): ')
            if len(admn_id_no) != 4:
                print('Admission ID has to be 4 digits long.')
            else:
                break
        std_roll = year_of_admn + 'U' + branch_roll_mapping[branch] + admn_id_no
    except ValueError and KeyError:
        print('Invalid Input. Try again')
        return
    else:
        if std_present(std_roll):
            print('A student with the same details already exists. Cannot Add Student.')
        else:
            # Now creating student using all the details that the user will enter
            s = student.StudentClass(name, year_of_admn, branch, admn_id_no)
            # add created student to list
            student.student_list.append(s)
            with open('student_data.pkl', 'ab') as fi_std:
                # dumping data
                pickle.dump(s, fi_std)
            print(f'Student with name {name} and roll no {std_roll} has been created.')


def add_book():
    # ask for parameters of a book from user
    try:
        title = input('Enter Book Title: ')
        author = input('Enter Name of Author: ')
        while True:
            isbn = int(input('Enter Book ISBN (13 digit ISBN is followed by this library): '))
            check_isbn = str(isbn)
            if len(check_isbn) == 13:
                break
            else:
                print('Length of ISBN has to be 13. Try again.')
        num_copies_to_add = int(input('Enter number of copies of this book to be added: '))
    except ValueError:
        print('Invalid Input, ISBN/Number of copies has to be a number. Try again.')
        return
    else:
        if check_if_isbn_present(isbn):
            print('Book with same ISBN and title already exists, Book details have been updated')
            get_books = load_books()
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

    student_details = load_student()
    for st in student_details:
        print('Name : ' + st.name)
        print('Roll No :' + st.roll_no)
        print('Books Issued : ' + str(st.num_books_issued))
        for bk in st.books_issued:
            print(f"Book ISBN : {bk['isbn']}")
            print(f"Date Of Issue : {bk['doi']}")


def print_faculty_details():
    faculty_details = load_faculty()
    for fc in faculty_details:
        print('Faculty Name : ' + fc.ename)
        print('Faculty ID : ' + fc.eid)
        for bk in fc.books_issued:
            print(f"Book ISBN : {bk['isbn']}")
            print(f"Date Of Issue : {bk['doi']}")
            print(f"{bk['nc']} copies of book having ISBN {bk['isbn']}")


def print_book_details():
    book_details = load_books()
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
                'doi': datetime.datetime.now(),   # stores current date in doi => date_of_issue
                'nc': num_copies
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


def return_book_facutly():
    # ask for eid
    emp_id = input('Enter Faculty ID: ')
    # if eid present
    if check_if_eid_present(emp_id):
        # ask for book isbn to be returned
        book_isbn = int(input('Enter Book ISBN to be Returned: '))
        # check if isbn issued to faculty
        if issued_faculty(book_isbn, emp_id):
            # since isbn present, return book
            # modify faculty details on return (new func)
            num_copies = modify_faculty_on_return(book_isbn, emp_id)
            # modify book details on return (would require new func)
            modify_book(book_isbn, num_copies, 1)
        # else exit func
        print(f'This Book Was Not Issued To Employee With ID {emp_id}.')
    # eid not present exit func
    print('Employee ID Not Found.')


def return_book_student():
    # ask for roll no
    std_roll = input('Enter Student Roll No Who Is Returning The Book: ')
    # if present
    if std_present(std_roll):
        # ask for book isbn
        book_isbn = int(input('Enter Book ISBN To Be Returned: '))
        # check if it was issued to this roll no at all or not
        if not check_if_already_issued_to_student(book_isbn, std_roll):
            # since book was issued
            # calc fine, if applied
            calc_fine(std_roll, book_isbn)
            # book returned => modify student details and modify book details
            modify_book(book_isbn, 1, 1)
            modify_std_on_return(book_isbn, std_roll)
        # else exit
        else:
            print(f'Book with ISBN: {book_isbn} has not been issued to this student.')
    # else exit
    else:
        print('Student not present in database. Error.')


def archive():
    # function archives all students who have passed out
    # load student data
    print('Archiving students...')
    curr_std = load_student()
    # search for students whose year of admission is 4+ years before than current year
    for std in curr_std:
        diff = datetime.datetime.now().year - int(std.year_of_admn)
        if diff > 4:
            print(f'Archiving {std.name} with roll no {std.roll_no}..')
            # return their books (loop possibly?)
            for bk in std.books_issued:
                modify_book(bk['isbn'], 1, 1)
            # since his books have been returned remove his book data
            std.books_issued.clear()
            std.num_books_issued = 0
            # move this students detail to a new file named archived
            with open('archived_students.pkl', 'ab') as file:
                pickle.dump(std, file)
            # after moving remove from current student data, and update curr student data file
            curr_std.remove(std)
            print(f'{std.name} with roll no {std.roll_no} has been archived and moved to archived database.')
    dump_students(curr_std)
    print('Archiving completed.')

# PROJECT CREATED BY : SABEEL AHMAD
