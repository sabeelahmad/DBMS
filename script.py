from functions import add_book, add_faculty, add_student, issue_book_facutly, issue_book_student, return_book_facutly, \
    return_book_student, print_student_details, print_faculty_details, print_book_details, search_book


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


def show_search_menu():
    print('1. Search book by ISBN(13).')
    print('2. Search book by title.')
    print('3. Search book by author.')


def get_choice():
    return int(input('Enter the choice(1-11) of operation you want to perform OR Press -1 to exit: '))


def get_search_choice():
    return int(input('Enter the choice(1-3) OR Press -1 to exit: '))


def main():
    show_menu()
    choice = get_choice()

    while choice != -1:
        if choice == 1:
            add_student()
            show_menu()
        elif choice == 2:
            add_faculty()
            show_menu()
        elif choice == 3:
            add_book()
            show_menu()
        elif choice == 4:
            issue_book_student()
            show_menu()
        elif choice == 5:
            issue_book_facutly()
            show_menu()
        elif choice == 6:
            return_book_student()
            show_menu()
        elif choice == 7:
            return_book_facutly()
            show_menu()
        elif choice == 8:
            show_menu()
            src_choice = get_search_choice()
            while src_choice != -1:
                if src_choice == 1:
                    try:
                        data = int(input('Enter ISBN-13: '))
                    except ValueError:
                        print('Invalid Input, Enter A number.')
                    else:
                        search_book('i', data)
                elif src_choice == 2:
                    try:
                        data = input('Enter Title of book: ')
                    except ValueError:
                        print('Invalid Input.')
                    else:
                        search_book('t', data)
                elif src_choice == 3:
                    try:
                        data = input('Enter Author Name: ')
                    except ValueError:
                        print('Invalid Input.')
                    else:
                        search_book('a', data)
                else:
                    print('Invalid Input. Try again.')
                show_search_menu()
                src_choice = get_search_choice()
        elif choice == 9:
            print_student_details()
            show_menu()
        elif choice == 10:
            print_faculty_details()
            show_menu()
        elif choice == 11:
            print_book_details()
            show_menu()
        else:
            print('Invalid Choice, Enter Choice Again.')
            show_menu()
        choice = get_choice()


if __name__ == "__main__":
    main()


