import pandas as pd
import numpy as np
import PyPDF2
import textract
import re
import os

# filename = 'paper8.pdf'

directory = 'C:/Users/malsha/PycharmProjects/wordcount/new3/'
for filename in os.listdir(directory):
    print(filename)
    pdfFileObj = open(directory + '/' + filename, 'rb')
    #pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    num_pages = pdfReader.numPages

    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    if text != "":
        text = text

    else:
        text = textract.process('words.txt', method='tesseract', language='eng')

    text = text.encode('ascii', 'ignore').lower()
    text_decoded = text.decode()
    keywords_tmp = re.findall(r'[a-zA-Z]\w+', text_decoded)

    # digits of length N
    N = 5


    def filterString(n):
        if len(n) > N:
            return True
        else:
            return False


    keywords = list(filter(filterString, keywords_tmp))

    df = pd.DataFrame(list(set(keywords)), columns=['keywords'])


    def weightage(word, text, number_of_documents=1):
        word_list = re.findall(word, text_decoded)
        number_of_times_word_appeared = len(word_list)
        tf = number_of_times_word_appeared / float(len(text_decoded))
        idf = np.log((number_of_documents) / float(number_of_times_word_appeared))
        tf_idf = tf * idf
        return number_of_times_word_appeared, tf, idf, tf_idf


    df['number_of_times_word_appeared'] = df['keywords'].apply(lambda x: weightage(x, text)[0])
    df['tf'] = df['keywords'].apply(lambda x: weightage(x, text)[1])
    df['idf'] = df['keywords'].apply(lambda x: weightage(x, text)[2])
    df['tf_idf'] = df['keywords'].apply(lambda x: weightage(x, text)[3])

    df = df.sort_values('tf_idf', ascending=True)
    df.head(25)
    df.to_csv(filename + '_out_put.csv', index=False)
    print(df)
