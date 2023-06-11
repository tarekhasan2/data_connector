
## SETUP

1. Clone this repository

2. Install the requirements

   ```
   $ pipenv install
   ```
3. Create Google Credential
	I. Enable Google Slide api: https://developers.google.com/slides/api/quickstart/python#enable_the_api
	
	II. Enable Google Doc api: https://developers.google.com/docs/api/quickstart/python#enable_the_api
	
	III. Create and download credentials. Follow this 7 steps: https://developers.google.com/drive/api/quickstart/python#authorize_credentials_for_a_desktop_application
	
	IV. Rename the downloaded file to credential.json.

	V. Put the credentials.json file in the working folder.

4. Create the pipenv env.
	```
   $ pipenv shell
   ```
5. Run the script.
	```
   $ python data_connectors.py
   ```

### Example urls for texting...

# PDF: https://book.thenetworkstate.com/tns.pdf
# EPUB: https://filesamples.com/samples/ebook/epub/Around%20the%20World%20in%2028%20Languages.epub
# DOC or DOCx: https://api.abcdoffice.com/cache/files/data/a7WKWYKt3VYueuo_6832/output.docx/new_document-created_by_abcdpdf.docx?md5=j5YUnkPyzlcXd6p4pfnsCg&expires=1686460170&filename=new_document-created_by_abcdpdf.docx
# PPTX: https://k4f4w9c2.stackpathcdn.com/wp-content/uploads/01_big_files_kim7/2023_best_ppt/Happy%20Independence%20Day%20PowerPoint%20Templates.pptx
# md: 
# rdf:
# text: https://filesamples.com/samples/document/txt/sample3.txt
# csv: https://www.data.va.gov/api/views/feae-sz69/rows.csv?accessType=DOWNLOAD
# Google doc: https://docs.google.com/document/d/1oA928yNXEuIGdwtIWvBj94rtHzCUyh_VrAvutOu_hSo/edit#heading=h.fo9jasw3q4kp
# Googlw slide: https://docs.google.com/presentation/d/1kUu6Ouv18t_tsaCxQvTvbPPT30bRE-1PqtCAy4Nehfk/edit#slide=id.p