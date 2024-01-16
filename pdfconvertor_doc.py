from pdf2docx import parse, Converter

pdf_file=input("Enter the name of the pdf file with extension .pdf : ")
word_file=input("Enter the name of the word file with extension .docx : ")
cv=Converter(pdf_file)
cv.convert(word_file,start=0,end=None)
cv.close()

#parse(pdf_file,word_file,start=0,end=None)