from collections import Counter
from typing import Dict
def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text:str) -> Dict[str, int]:
    counting_dict = Counter(text.lower())
    print("--------- Character Count -------")
    for key, value in counting_dict.most_common():
        print(f"{key}: {value}")

    return print(f"============= END ===============")

