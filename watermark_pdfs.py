from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

import os
import sys

base_path=os.getcwd()

if len(sys.argv)==4:
    input_file_name=base_path+'/'+sys.argv[1]
    watermark_file_name=base_path+'/'+sys.argv[2]
    output_file_name=base_path+'/'+sys.argv[3]
else:
    print('Please give input in following order: input_PDF_path1 watermark_pdf output_PDF_path.')
    sys.exit()
pdf_writer=PdfFileWriter()
pdf_merger=PdfFileMerger()

watermark_pdf=PdfFileReader(watermark_file_name)
input_pdf=PdfFileReader(input_file_name)

watermark_page=watermark_pdf.getPage(0) # this only has template page with watermark

for page in range(input_pdf.getNumPages()):
    tmp_input_page=input_pdf.getPage(page)
    tmp_input_page.mergePage(watermark_page)
    pdf_writer.addPage(tmp_input_page)

with open(output_file_name,'wb') as output_file:
    pdf_writer.write(output_file)