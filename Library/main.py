#Library Project
import random

print("Welcome to the library!")

books = ["Lord of the Rings", "Harry Potter", "The Secret Garden", "Pax"] #this is the default library, you can change it
request = ""

while True: 
  #This stuff prints out the current library everytime you do an action
  print("")
  print("Current library: ")
  print(books)
  print("")

  #you should either input take, return, volunteer, destroy or goodbye, there are if and elif messages for each of these cases.
  print("Options: take, return, recommend, volunteer")
  request = input("What do you want to do (say goodbye to leave): ")

  if request.lower() == 'take': 
    request = input("What book do you want to take: ")
    #this loop ilterates through the library and checks if the request matches any book
    book_not_there = True #boolean, stays True if the book wasn't in the library, will be useful for the elif statement
    for book in books: 
      #case insenstive because of .lower() method
      if book.lower() == request.lower(): 
        #you can't use request because the request might not match the case, so you use book
        print("Great! I found the book at index " + str(books.index(book)))
        #removes the book from the library
        books.remove(book)
        book_not_there = False #set it to False because it was in the library
      #this elif statement will run if the for loop  is at the last book and it didn't find the book. that way we don't run into errors and print the statement at the right instance
      elif book == books[-1] and book_not_there: #if it's the last book, and it was never to be found
        print("Sorry, I can't find your book")
  
  elif request.lower() == 'return': 
    #when you return a book, it appends a book to the list
    request = input("What book do you want to return: ")
    print("Okay!")
    books.append(request)

  elif request.lower() == 'recommend':
    #avoids an error if the library is empty
    if len(books) == 0:
      print("Oh sorry, the library is currently empty")
    else: 
      #chooses a random book to recommend
      recommendation = random.choice(books)
      #finds the index of the book
      index = books.index(recommendation)
      #prints out the index of the book and the book
      print("Thank you for asking!")
      print("I recommend this book: " + recommendation)
      print("It's on index " + str(index))

  elif request.lower() == 'volunteer': 
    # when you volunteer, it sorts the list
    print("Oh, thank you so much!")
    books.sort()

  elif request.lower() == 'destroy': 
    #destroying the library removes it from the list
    print(";-;")
    books.clear()

  elif request.lower() == 'goodbye':
    print("Goodbye! Thank you for coming to the library")
    break

  else: 
    #anything else will get a sorry message
    print("Sorry I didn't get that")
