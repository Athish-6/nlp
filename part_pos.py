import nltk
# Ensure necessary NLTK data is downloaded (only needed once)
try:
 nltk.data.find('taggers/averaged_perceptron_tagger')
except nltk.downloader.DownloadError:
 nltk.download('averaged_perceptron_tagger')
# Sample text
text = "The quick brown fox jumps over the lazy dog."
# Tokenize the text into words
words = nltk.word_tokenize(text)
# Perform POS tagging
pos_tags = nltk.pos_tag(words)
# Print the results
print(pos_tags)