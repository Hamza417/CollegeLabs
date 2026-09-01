text = "This is a sample text that will be used to demonstrate the functionality of the count_words function."


def count_words(text):
    """Counts the number of words in the given text.

    Args:
        text (str): The input text to count words from.

    Returns:
        int: The number of words in the text.
    """
    # Split the text into words based on whitespace and filter out empty strings
    words = [word for word in text.split() if word]
    return len(words)

if __name__ == "__main__":
    word_count = count_words(text)
    print(f"The number of words in the text is: {word_count}")