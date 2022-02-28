from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

import sys,glob


if len(sys.argv)>1:
    input_file_names=[]
    for file_name in sys.argv[1:]:
        if '*' in file_name:
            input_file_names.expand(glob.glob(file_name))   # to expand unix wildcards that uses '*'
        else:
            input_file_names.append(file_name)
    # print(input_file_names)
    # sys.exit()
else:
    print('Please give input in following order: input_PDF_path1 input_PDF_path2 input_PDF_path3.')
    sys.exit()

pdf_merger=PdfFileMerger()

watermark_file_name='watermark_iitpal_90_A4.pdf'

watermark_pdf=PdfFileReader(watermark_file_name)
watermark_page=watermark_pdf.getPage(0) # this only has template page with watermark

for i,input_file in enumerate(input_file_names):
    if '.pdf' in input_file: # is somehow non-pdfs are present in input files then it filters them out
        pdf_writer=PdfFileWriter()
        input_pdf=PdfFileReader(input_file)

        for page in range(input_pdf.getNumPages()):
            tmp_input_page=input_pdf.getPage(page)
            tmp_input_page.mergePage(watermark_page)
            pdf_writer.addPage(tmp_input_page)

        with open(input_file,'wb') as output_file:
            pdf_writer.write(output_file)