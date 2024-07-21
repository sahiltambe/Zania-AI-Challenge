import PyPDF2

def extract_text_from_pdf(pdf_file):
    print(f"Extracting text from {pdf_file}")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        print(f"Extracting text from page {page_num}...")
        page_text = page.extract_text()
        print(f"Page {page_num} text: {page_text}")
        text += page_text
    print(f"Text extracted from {pdf_file}: {text}")
    return text


# import PyPDF2

# def extract_text_from_pdf(pdf_file):
#     with open(pdf_file, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in reader.pages:
#             text += page.extract_text()
#     return text

