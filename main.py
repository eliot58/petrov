from python_docx_replace import docx_replace
from docx import Document

doc = Document("passport.docx")

my_dict = {
    "o_name": "Ivan",
    "qu": "3434"
}

docx_replace(doc, **my_dict)


doc.save("replaced.docx")