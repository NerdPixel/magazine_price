from typing import List

import PyPDF2 as pydf
import os


def getFileName(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.pdf' in file:
                files.append(os.path.join(r, file))
    return files


if __name__ == '__main__':
    inputPath = '../inputData'
    outputPath = '../outputData'

    filePdf = getFileName(inputPath)
    for f in filePdf:
        pdfFileObject = open(f, 'rb')
        pdfRead = pydf.PdfFileReader(pdfFileObject)
        nPages = pdfRead.getNumPages()
        fileTxt = f.replace(".pdf", ".txt").replace(inputPath, outputPath)
        txt = open(fileTxt, 'w')
        for i in range(nPages):
            page = pdfRead.getPage(i)
            pageContent = page.extractText()
            txt.write(pageContent)
        txt.close()
        pdfFileObject.close()
