word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) ## checking if its equal to each other
total_words = pages * word_per_page

print(f"pages= {pages}")
print(f"words_per_page= {word_per_page}")

print(total_words)