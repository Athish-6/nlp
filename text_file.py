import nltk

# Download resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to tag sentences from a file
def pos_tag_file(filename):

    with open(filename, 'r') as file:
        text = file.read()

    # Split text into sentences
    sentences = nltk.sent_tokenize(text)

    # Process each sentence
    for sent in sentences:
        words = nltk.word_tokenize(sent)
        pos_tags = nltk.pos_tag(words)

        print("\nSentence:", sent)
        print("POS Tags:")
        for word, tag in pos_tags:
            print(f"{word} -> {tag}")


# Call the function OUTSIDE the function definition
pos_tag_file("sample.txt")
