import fitz  # PyMuPDF
from nltk import ngrams
from collections import Counter
from nltk.corpus import stopwords
import requests

# Define the path to your PDF file
pdf_file_path = "paper7.pdf"


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    doc = fitz.open(pdf_file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Tokenize the text into words
words = pdf_text.split()

# Load NLTK stopwords

# stopwords_list = requests.get("https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt").content
# stopwords = set(stopwords_list.decode().splitlines())
nltk_stopwords = set(stopwords.words('english'))
print(nltk_stopwords)
# print(stopwords)

# Filter out stopwords from the words
filtered_words = [word for word in words if word.lower() not in nltk_stopwords]



# Create trigrams (adjacent three words)
trigrams = list(ngrams(filtered_words, 3))

# Count the frequency of each trigram
trigram_counts = Counter(trigrams)

# Find the five most frequent trigrams
most_common_trigrams = trigram_counts.most_common(5)

# Print the results
for trigram, count in most_common_trigrams:
    print(f"{trigram[0]} {trigram[1]} {trigram[2]} - Frequency: {count}")
