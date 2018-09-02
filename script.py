from functions import add_book, add_faculty, add_student, issue_book_facutly, issue_book_student, return_book_facutly, \
    return_book_student, print_student_details, print_faculty_details, print_book_details


def show_menu():
    print('-'*37)
    print('Welcome To Library Management System')
    print('-'*37)
    print('\n')
    print('-'*35)
    print('Library Main Menu')
    print('1. Add a student member to library.')
    print('2. Add a faculty member to library.')
    print('3. Add a book to library.')
    print('4. Issue book to student.')
    print('5. Issue book to faculty')
    print('6. Return book by student')
    print('7. Return book by faculty')
    print('8. Search for a book in library.')
    print('9. Print student records.')
    print('10. Print faculty records.')
    print('11. Print book records')
    print('-'*35)


def get_choice():
    return int(input('Enter the choice(1-11) of operation you want to perform OR Press -1 to exit: '))


def main():
    show_menu()
    choice = get_choice()

    while choice != -1:
        if choice == 1:
            add_student()
        elif choice == 2:
            add_faculty()
        elif choice == 3:
            add_book()
        elif choice == 4:
            issue_book_student()
        elif choice == 5:
            issue_book_facutly()
        elif choice == 6:
            return_book_student()
        elif choice == 7:
            return_book_facutly()
        elif choice == 8:
            pass
        elif choice == 9:
            print_student_details()
        elif choice == 10:
            print_faculty_details()
        elif choice == 11:
            print_book_details()
        else:
            print('Invalid Choice, Enter Choice Again.')
        choice = get_choice()


if __name__ == "__main__":
    main()


