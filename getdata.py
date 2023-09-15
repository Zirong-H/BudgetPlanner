import tabula
import PyPDF2
import pdftotext
import pandas as pd
path = "statements/5293485_2023_08_11_2023_09_12.pdf"
# df_list = tabula.read_pdf("statements/5293485_2023_08_11_2023_09_12.pdf", pages=all)
#df = df_list[0]
#print(df)

# file = open("statements/5293485_2023_08_11_2023_09_12.pdf",'rb')
# fileReader = PyPDF2.PdfReader(file)
# test = fileReader.pages[0].extract_text()#.split("\n")
# print(test)
# for page in fileReader.pages:
#     text = page.extract_text()
#     i = 1
#     print("Page:", i)
#     print('_______________________________________________________________________________________')
#     print(text)

#     i+=1

with open(path, 'rb') as f:
    pdf = pdftotext.PDF(f)

# Read all the text into one string
pdftotext_text = "\n\n".join(pdf)

print(pdftotext_text)