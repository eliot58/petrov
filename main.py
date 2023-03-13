from docx import Document
from docxcompose.composer import Composer

def combine_all_docx(filename_master,files_list):
    number_of_sections=len(files_list)
    master = Document(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document(files_list[i])
        composer.append(doc_temp)
    composer.save("combined_file.docx")

items = ["render/replace0.docx", "render/replace7.docx", "render/replace9.docx"]

combine_all_docx('template.docx', items)
