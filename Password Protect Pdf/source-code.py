from PyPDF2 import PdfWriter, PdfReader
pdfwriter = PdfWriter()
pdf = PdfReader("1.pdf")

for page_num in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[page_num])

passw = input('Enter Password: ')  # changed to input()

pdfwriter.encrypt(passw)

with open('ho.pdf', 'wb') as f:
    pdfwriter.write(f)
