<<<<<<< HEAD
import pdfplumber
import sys

filename = sys.argv[1]
def pdftotext(filename):
   all_text = '' # new line
   with pdfplumber.open(filename) as pdf:
       for pdf_page in pdf.pages:
           single_page_text = pdf_page.extract_text()
           all_text = all_text + '\n' + single_page_text
   return all_text

=======
import pdfplumber
import sys

filename = sys.argv[1]
def pdftotext(filename):
   all_text = '' # new line
   with pdfplumber.open(filename) as pdf:
       for pdf_page in pdf.pages:
           single_page_text = pdf_page.extract_text()
           all_text = all_text + '\n' + single_page_text
   return all_text

>>>>>>> 5bd02288a5e9afb7d3c87de9a39db744458503fa
print(pdftotext(filename))