import sys

try:
    book_path = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print(book_path)