
from file_extractor import extract_csv, extract_rdf, extract_text, extract_markdown, extract_powerpoint, extract_doc_docx, extract_epub, extract_pdfs, extract_mobi
from extarnal_file_extractor import extract_google_slide, extract_google_doc


def main():
	source_url = input('Enter the url of the file: ')
	file_type  = input('''There are 11 file type:
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
			your file type (1-11) : 
								''')
	file_type = file_type.strip()

	if file_type == '1':
		file_extention = '.pdf'
		json_data = extract_pdfs(source_url, file_extention)
	
	elif file_type == '2':
		file_extention = '.epub'
		json_data = extract_epub(source_url, file_extention)

	elif file_type == '3':
		file_extention = '.doc'
		json_data = extract_doc_docx(source_url, file_extention)

	elif file_type == '4':
		file_extention = '.docx'
		json_data = extract_doc_docx(source_url, file_extention)

	elif file_type == '5':
		file_extention = '.pptx'
		json_data = extract_powerpoint(source_url, file_extention)

	elif file_type == '6':
		file_extention = '.md'
		json_data = extract_markdown(source_url, file_extention)

	elif file_type == '7':
		file_extention = '.rdf'
		json_data = extract_rdf(source_url, file_extention)

	elif file_type == '8':
		file_extention = '.txt'
		json_data = extract_text(source_url, file_extention)

	elif file_type == '9':
		file_extention = '.csv'
		json_data = extract_csv(source_url, file_extention)

	elif file_type == '10':
		json_data = extract_google_doc(source_url)

	elif file_type == '11':
		json_data = extract_google_slide(source_url)

	else:
		print("Please type the correct number from 1-11")
		json_data = {}

	print(json_data)
	

if __name__ == "__main__":
    main()


# PDF: https://www.junkybooks.com/administrator/thebooks/64459b396311b-agroforestry-and-biodiversity-conservation-in-tropical-landscapes.pdf
# EPUB: https://filesamples.com/samples/ebook/epub/Around%20the%20World%20in%2028%20Languages.epub
# DOC or DOCx: https://api.abcdoffice.com/cache/files/data/a7WKWYKt3VYueuo_6832/output.docx/new_document-created_by_abcdpdf.docx?md5=j5YUnkPyzlcXd6p4pfnsCg&expires=1686460170&filename=new_document-created_by_abcdpdf.docx
# PPTX: https://k4f4w9c2.stackpathcdn.com/wp-content/uploads/01_big_files_kim7/2023_best_ppt/Happy%20Independence%20Day%20PowerPoint%20Templates.pptx
# md: 
# rdf:
# text: https://filesamples.com/samples/document/txt/sample3.txt
# csv: https://www.data.va.gov/api/views/feae-sz69/rows.csv?accessType=DOWNLOAD
