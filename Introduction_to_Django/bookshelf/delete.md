retrieved_book.delete()
# Confirm deletion by trying to retrieve all books
books = Book.objects.all()
print(books)  # Expected output: <QuerySet []>
