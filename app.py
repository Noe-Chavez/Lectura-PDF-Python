import PyPDF2

# leeremos el archivo especificando nombre y ruta y adicional el especificados el modo de lectura binaria (Reader binary).  
#pdf_file_obj = open('202436.pdf', 'rb')
#pdf_file_obj = open('C:/Users/zephon/Downloads/PARA ROBOT/BASE/2024131 actualizado.pdf', 'rb')
pdf_file_obj = open('C:/Users/zephon/Downloads/PARA ROBOT/BASE/2024131.pdf', 'rb')

# Pasamos el archivo al objeto reader, para poder interactura con el PDF.
pdf_reader = PyPDF2.PdfReader(pdf_file_obj)

# Obtener número de páginas
num_pages = len(pdf_reader.pages)

contenido = ""

# Iterar sobre todas las hojas del archivo PDF.
for i in range(num_pages):
    # Especificar indice de la hoja del PDF a Leer.
    page_obj = pdf_reader.pages[i]
    # Obtenemos todo el contenido del la hoja especificada en cuestión al índice.
    text = page_obj.extract_text()
    contenido += f"Hoja {i} \n {text} \n\n"

# especificamos la página para leer el contenido.
#page_obj = pdf_reader.pages[0]

# Obtenemos todo el contenido del la hoja especificada.
# contenido = page_obj.extract_text()

print("CONTENIDO PDF")
print(contenido)