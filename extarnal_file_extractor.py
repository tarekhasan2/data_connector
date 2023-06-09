from pathlib import Path
from llama_index import download_loader, GPTVectorStoreIndex
from langchain.document_loaders import UnstructuredPowerPointLoader as powerpointLoader
from Google import Create_Service
import dropbox
import requests


### WORKING ON IT 
# def extract_dropbox_doc(url):  
# 	#token = 'sl.Bf8Dz7-leDivqSpvoc-jftFOhD517GcSGiEyqqBx4Ag7JjYvq6HDWs0ReBDDc2VgcEsayqPVhtm8MbVdfvV0HM9mXPxD1VvL6fmqrUTeKwfiuS_RFdMhRylRmsHUPJ9-QSjkt5EO'

# 	dbx = dropbox.Dropbox(token)
	
# 	split_url = url.split('fi/')[1]
# 	file_path_dropbox = split_url.split('/')[0]
# 	file_path_dropbox = f'id:{file_path_dropbox}'
# 	file_path_dropbox = 'id:94qvdehf27b37m0o89swvu03n'

# 	file_path_local = f'files/{file_path_dropbox}'
# 	print(file_path_local)
# 	dbx.files_download_to_file(file_path_local, file_path_dropbox)

# 	DocxReader = download_loader("DocxReader")
# 	loader = DocxReader()

# 	documents = loader.load_data(file=Path(file_path_local))
# 	content = "".join(doc.text for doc in documents)
	
# 	print(content)

# 	date_time 	= ''
# 	title 		= ''
# 	author 		= ''

# 	return {
# 		'source_url': url, 
# 		'date_time'	: date_time, 
# 		'title'		: title, 
# 		'author'	: author, 
# 		'content'	: content
# 	}





def extract_google_slide(url):
	slide_id = url.split('presentation/d/')[1]
	if '/edit' in slide_id:
		slide_id = slide_id.split('/edit')[0]

	CLIENT_SECRET_FILE 	= 'credentials.json'
	API_NAME 			= 'slides'
	API_VERSION 		= 'v1'
	SCOPES 				= ['https://www.googleapis.com/auth/presentations.readonly']
	
	slide_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

	presentation = slide_service.presentations().get(presentationId=slide_id).execute()

	content = ''
	slides = presentation.get('slides')
	for slide in slides:
		for element in slide['pageElements']:
			try:
				text_in_element = element['shape']['text']
			except:
				continue
			for text_element in text_in_element['textElements']:
				try:
					content = content + text_element['textRun']['content'] + '\n'
				except:
					pass

	date_time 	= ''
	title 		= ''
	author 		= ''

	return {
		'source_url': url, 
		'date_time'	: date_time,
		'title'		: title, 
		'author'	: author, 
		'content'	: content
	}





def extract_google_doc(url):
	doc_id = url.split('document/d/')[1]
	if '/edit' in doc_id:
		doc_id = doc_id.split('/edit')[0] 

	GoogleDocsReader = download_loader('GoogleDocsReader')
	gdoc_ids = [doc_id]
	loader = GoogleDocsReader()
	documents = loader.load_data(document_ids=gdoc_ids)

	content = "".join(doc.text for doc in documents)

	# index = GPTVectorStoreIndex.from_documents(documents)
	# index.query('Where did the author go to school?')
	print(content)
	date_time 	= ''
	title 		= ''
	author 		= ''

	return {
		'source_url': url, 
		'date_time'	: date_time,
		'title'		: title, 
		'author'	: author, 
		'content'	: content
	}


### WORKING ON IT
# def extract_notion_doc(url):
# 	NotionPageReader = download_loader('NotionPageReader')
	
# 	integration_token = os.getenv("NOTION_INTEGRATION_TOKEN")
# 	page_ids = ["<page_id>"]
# 	reader = NotionPageReader(integration_token=integration_token)
# 	documents = reader.load_data(page_ids=page_ids)






