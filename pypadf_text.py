<<<<<<< HEAD
# importing required modules
import PyPDF2
import sys

filename = sys.argv[1]
# creating a pdf file object
pdfFileObj = open(filename, 'rb')
	
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
# printing number of pages in pdf file
print(pdfReader.numPages)
	
# creating a page object
pageObj = pdfReader.getPage(0)
	
# extracting text from page
print(pageObj.extractText())
	
# closing the pdf file object
pdfFileObj.close()
=======
# importing required modules
import PyPDF2
import sys

filename = sys.argv[1]
# creating a pdf file object
pdfFileObj = open(filename, 'rb')
	
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
# printing number of pages in pdf file
print(pdfReader.numPages)
	
# creating a page object
pageObj = pdfReader.getPage(0)
	
# extracting text from page
print(pageObj.extractText())
	
# closing the pdf file object
pdfFileObj.close()
>>>>>>> 5bd02288a5e9afb7d3c87de9a39db744458503fa
