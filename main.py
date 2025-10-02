def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return str(file_contents)

if __name__ == "__main__":
	path = "/root/bookbot/books/frankenstein.txt"
	result = get_book_text(path)
	print(f"{result}")
