import re
import PyPDF2
import os

#Give your pdf as input
f = open("ExampleCollegeCutoffs.pdf","rb")

pdf_reader = PyPDF2.PdfFileReader(f)
pdfWriter = PyPDF2.PdfFileWriter()

counter = 0;
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pageText = page.extractText()

    #Use your regEx pattern in re.search for matching desired data
    #Finds pages having electronics engineering as a course
    match = re.search("Electronic|electronic",pageText)

    #Example
    #Two lines of code below finds pages having percentages below 75%
    #match = re.search("\d*\.\d+%?",pageText)
    #if(match!= 0 and float(match.group().strip("%")) < 75.0):

    if(match):
        pdfWriter.addPage(page)
        counter = counter + 1
    
    os.system("cls")
    print(str(p+1) +"/"+ str(pdf_reader.numPages))

#Outputs a new file, OVER-WRITES if file exists
pdfOutput = open("PagesHavingElectronicsCourses.pdf","wb")

if(counter):
    pdfWriter.write(pdfOutput)
    print(str(counter) + " pages processed")
else:
    page = pdf_reader.getPage(0)
    pdfWriter.addPage(page)
    pdfWriter.write(pdfOutput)
    print("No Match Found")
