# import csv

def add_book():
    Book_Title = input("Enter a tittle: ").strip().title()
    Author = input("Enter the authors name: ").strip().title()
    Year = int(input("Enter Year published: "))

    with open("info.csv", mode="a") as book_lib:
        book_lib.write(f"\n{Book_Title},{Author},{Year}")

def get_books():
    all_books = []

    with open("info.csv", mode="r", encoding='UTF8') as book_lib:
        book_contents = book_lib.readlines()
        # print(f"{book_contents}")

    if len(book_contents) < 2:
        print("No books found!")
        return

    title = book_contents[0].strip().split(",")

    for info in book_contents[1:]:
        book_info = info.strip().split(",")
        my_dict = dict(zip(title, book_info))
        all_books.append(my_dict)

    return all_books

def display_books():
    books_list = get_books()

    for book in books_list:
        print(book)


    # for i, line in enumerate(lib_contents, start=1):
    #     print(f"{i}: {line.strip()}")

def search_book():
    with open("info.csv", mode="r", encoding='UTF8') as books:
        lib_contents = books.read()
        print(f"{lib_contents}")

    search_title = input("Enter book tittle: ")
    for book in search_title:
        if search_title in book:
            print(book)

        else:
            print("INVALID BOOK NAME OR INCORRECT SPELLING")

def exit():
    pass

option = int(input(f"\nSelect an action\n \n(1) Add a Book \n(2) Display Books list \n(3) Search a book \n(4) Exit Program \n\nEnter Option: "))
print()

# while True:
if option == 1:
    add_book()

elif option == 2:
    display_books()

elif option == 3:
    search_book()

elif option == 4:
    exit()

else:
    print("INVALID OPTION")
