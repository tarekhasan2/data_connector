from pathlib import Path
from llama_index import download_loader, GPTVectorStoreIndex
from langchain.document_loaders import UnstructuredPowerPointLoader as powerpointLoader
from langchain.document_loaders import NotionDBLoader as notionLoader

from Google import Create_Service
import dropbox
import requests



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
		try:
			page_element = slide['pageElements']
		except:
			continue
		for element in page_element:
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








