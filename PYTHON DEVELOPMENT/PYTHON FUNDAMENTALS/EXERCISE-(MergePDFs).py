
# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf.

"""

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.
It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

"""

from PyPDF2 import PdfMerger

pdf_merger_object = PdfMerger()

pdf_merger_object.append(r"C:\Users\ratne\Desktop\UsedForPDFmergeEXERCISE\12th gradesheet.pdf")
pdf_merger_object.append(r"C:\Users\ratne\Desktop\UsedForPDFmergeEXERCISE\10th gradesheet.pdf")

pdf_merger_object.write(r"C:\Users\ratne\Desktop\UsedForPDFmergeEXERCISE\MergedOutputPDF.pdf")

pdf_merger_object.close()