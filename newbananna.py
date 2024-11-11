#utility function to append data to a file
def append_to_file(filename,data):
    with open(filename,'a') as f:# this will open the files to append
        f.write(data+ '\n')# this will write the data

#utility function to read data from a file
def read_file(filename):
    try:
        with open(filename,'r') as f:# this will open the files to read
            return f.readlines()# this will read the data
    except FileNotFoundError:#this will handle the error
        return[]
    
#1. Function to add a new book
def add_book():
    #taking all the inputs like book id,title,author,category,status
    book_id=input("Enter Book ID: ")
    title=input("Enter Book title: ")
    author=input("Enter Author Name: ")
    category=input("Enter category: ")
    status='available'#book is initially available
    #write book details to books.txt
    book_record=f"{book_id},{title},{author},{category},{status}"
    append_to_file('books.txt',book_record)
    print("Book added successfully!")

#2. Function to view all the books
def view_books():
    books=read_file('books.txt')#this will read the data from the file
    if not books:#this will chech there are books in the file or not
        print("No books available")
        return
    
    print("Books Records")
    for book in books:
        book_id,title,author,genre,status=book.strip().split(',')
        print(f"ID:{book_id}, Title:{title}, Author:{author}, Genre:{genre}, Status:{status}")

#3. Function to seach books by title or author
def search_book():
    query=input("Enter book title or author to search: ").lower()#this takes query as input and it converts it to lower case
    books=read_file('books.txt')#this will read the data from the file
    found=False
    
    for book in books:#this iterates through the loop and checks for the title and author
        _,title,author,_,status=book.strip().split(',')
        if query in title.lower() or query in author.lower():
            print(f"Title:{title}, Author:{author}, Status:{status}")
            found=True

    if not found:
        print("No matching books found.")

#4. Function to delete a book
def delete_book():
    book_id = input("Enter Book ID to Delete: ")#taking book id to delete the book

    books = read_file('books.txt')#this will read the data from the file
    updated_books = []#empty list to append those books which is not given by the user
    for book in books:
        if not book.startswith(book_id):
            updated_books.append(book)#this updated book has all those boooks except the one which the user entered

    with open('books.txt', 'w') as f:
        for book in updated_books:
            f.write(book)

    print("Book deleted successfully!")
    
#5. Menu system using a dictionary-based switch
def menu():
    while True:#this is an infinite loop which will keep on running until we break it
        #here we display our library management system
        print("\n Library Management System")
        print("1. Add Book")
        print("2. View Book")
        print("3. Search Book")
        print("4. Delete a Book")
        print("5. Exit")
    

        choice=input("Enter your choice: ")#we take choice from the user
        actions={
            '1': add_book,
            '2': view_books,
            '3': search_book,
            '4': delete_book,
            '5': exit,
        }#function call are mapped with the user choices respectively

        action=actions.get(choice)
        if action:
            action()#here we call that function of which the user choice has been mapped
        else:
            print("Invalid choice! Please try again. ")

#Entry point of the program
if __name__=="__main__": #built in variable
    #python file is being run directly
    menu()
