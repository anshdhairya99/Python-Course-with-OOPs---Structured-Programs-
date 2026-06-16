# Coroutines in Python:------

def searcher():
    import time
    #Some 4 seconds time consuming task
    book = "This book is Ansh Dhairya with code"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is in book")
        else:
            print("Text is not in book")

search = searcher() 
next(search)
search.send("Ansh")
input("press any key")
search.send("Ansh")


print("Next method")
search.send("Ansh")
search.close() # to close the search coroutines off 

