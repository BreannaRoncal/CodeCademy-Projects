"""
You recently began employment at “A Sorted Tale”, an independent bookshop. Every morning, 
the owner decides to sort the books in a new way.

Some of his favorite methods include:

- By author name
- By title
- By number of characters in the title

Throughout the day, patrons of the bookshop remove books from the shelf. Given the strange ordering of the store, 
they do not always get the books placed back in exactly the correct location.

The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning. 
It is currently taking too long!

"""


import utils
import sorts

# Short bookshelf
bookshelf = utils.load_books('books_small.csv')
for book in bookshelf:
  print(book['title_lower'])

# Long bookshelf
long_bookshelf = utils.load_books('books_large.csv')

print(ord("a"))
print(ord(" "))
print(ord("A"))

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_total_length(book_a, book_b):
  book_a_total = len(book_a['title']) + len(book_a['author'])
  book_b_total = len(book_b['title']) + len(book_b['author'])

  return book_a_total > book_b_total

### Test the different sorts ###
# Sort by titles
#sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
#for book in sort_1:
#  print(book['title'])

# Sort by author
# Create new list because sorting mutates the original
# Test with bubble_sort
#bookshelf_v1 = [book for book in bookshelf]
#sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
#for book in bookshelf_v1:
#  print(book['title'])

# Create new copy of bookshelf to test with quicksort
bookshelf_v2 = [book for book in bookshelf]
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
for book in bookshelf_v2:
  print(book['title'])


# Test for long_bookshelf list
long_bookshelf_v1 = [book for book in long_bookshelf]
#long_sort = sorts.bubble_sort(long_bookshelf_v1, by_total_length)
sorts.quicksort(long_bookshelf_v1, 0, len(long_bookshelf) - 1, by_total_length)
print('finished')
