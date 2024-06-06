def count_words(phrase):
    # Split the phrase into words using spaces as delimiters.
    words = phrase.split()
    # Counts the number of words.
    num_words =len(words)
    return num_words

if __name__ == "__main__":
    user_phrase =input("Enter a phrase: ")
    word_count = count_words(user_phrase)

print(f"The number of words in your phrase is: {word_count}")
