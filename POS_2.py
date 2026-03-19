import nltk

# Download required resources (only first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tag_file(input_filename, output_filename):
    # Read input file
    with open(input_filename, 'r') as file:
        text = file.read()

    # Sentence tokenization
    sentences = nltk.sent_tokenize(text)

    # Open output file
    with open(output_filename, 'w') as out_file:
        for sent in sentences:
            # Word tokenization
            words = nltk.word_tokenize(sent)

            # POS tagging
            pos_tags = nltk.pos_tag(words)

            # Write sentence
            out_file.write(f"Sentence: {sent}\n")
            out_file.write("POS Tags:\n")

            # Write word-tag pairs
            for word, tag in pos_tags:
                out_file.write(f"[{word}] -> {tag}\n")

            out_file.write("\n")  # Blank line after each sentence

# Function call
pos_tag_file(r"C:\NLP program\.vscode\sample1.txt", "output.txt")

print("POS tagging complete! Results saved to output.txt")