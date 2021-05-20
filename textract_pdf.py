import textract
import sys
text = textract.process('in1.pdf')
print("extracted text =>",text)