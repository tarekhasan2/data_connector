
from file_extractor import extract_csv, extract_rdf, extract_text, extract_markdown, extract_powerpoint, extract_doc_docx, extract_epub, extract_pdfs
from extarnal_file_extractor import extract_google_slide, extract_google_doc


def main():
	source_url = input('Enter the url of the file: ')
	file_type  = input('''Select the file type:
							1. PDF
							2. EPUB
							3. DOC
							4. DOCX
							5. POWERPOINT (PPT, PPTX)
							6. MARKDOWN 
							7. RDF
							8. TXT 
							9. CSV
							10. GOOGLE DOCS
							11. GOOGLE SLIDES
								''')
	file_type = file_type.strip()

	if file_type == '1':
		file_extention = '.pdf'
		extract_pdfs(source_url, file_extention)
	
	elif file_type == '2':
		file_extention = '.epub'
		extract_epub(source_url, file_extention)

	elif file_type == '3':
		file_extention = '.doc'
		extract_doc_docx(source_url, file_extention)

	elif file_type == '4':
		file_extention = '.docx'
		extract_doc_docx(source_url, file_extention)

	elif file_type == '5':
		file_extention = '.pptx'
		extract_powerpoint(source_url, file_extention)

	elif file_type == '6':
		file_extention = '.md'
		extract_markdown(source_url, file_extention)

	elif file_type == '7':
		file_extention = '.rdf'
		extract_rdf(source_url, file_extention)

	elif file_type == '8':
		file_extention = '.txt'
		extract_text(source_url, file_extention)

	elif file_type == '9':
		file_extention = '.csv'
		extract_csv(source_url, file_extention)

	elif file_type == '10':
		extract_google_doc(source_url)

	elif file_type == '11':
		extract_google_slide(source_url)

	else:
		print("Please type the correct number from 1-11")

main()


