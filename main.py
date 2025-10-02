from stats import count_words, count_characters
import sys

def get_book_text(filepath):
	# add encoding for windows..
	with open(filepath, encoding="utf-8") as f:
		file_contents = f.read()
	return str(file_contents)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	result = get_book_text(path)
	#print(result)
	print(
		f"============ BOOKBOT ============\n"
		f"Analyzing book found at {path}...\n"
		f"----------- Word Count ----------"
	   )
	print(f"Found {count_words(result)} total words")
	count_characters(result)

