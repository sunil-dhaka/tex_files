from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

import os
import sys

base_path=os.getcwd()

if len(sys.argv)>1:
    input_file_names=[base_path+'/'+file_name for file_name in sys.argv[1:]]
else:
    print('Please give input in following order: input_PDF_path1 input_PDF_path2 input_PDF_path3.')
    sys.exit()

pdf_merger=PdfFileMerger()

watermark_file_name='watermark_iitpal_90_A4.pdf'

watermark_pdf=PdfFileReader(watermark_file_name)
watermark_page=watermark_pdf.getPage(0) # this only has template page with watermark

for i,input_file in enumerate(input_file_names):
    pdf_writer=PdfFileWriter()
    input_pdf=PdfFileReader(input_file)

    for page in range(input_pdf.getNumPages()):
        tmp_input_page=input_pdf.getPage(page)
        tmp_input_page.mergePage(watermark_page)
        pdf_writer.addPage(tmp_input_page)

    with open(input_file,'wb') as output_file:
        pdf_writer.write(output_file)