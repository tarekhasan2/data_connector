
from pathlib import Path
from llama_index import download_loader, GPTVectorStoreIndex
import requests
from langchain.document_loaders import UnstructuredPowerPointLoader as powerpointLoader
from Google import Create_Service
import dropbox
from utils import download_file, get_extra_data
import mobi
import html2text
import os


def extract_csv(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)
	SimpleCSVReader = download_loader("SimpleCSVReader")

	loader = SimpleCSVReader()
	documents = loader.load_data(file=Path(file_downloaded_path))

	content = "".join(doc.text for doc in documents)

	title, published_data, author_name = get_extra_data(documents[:5])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}




def extract_text(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)
	with open(file_downloaded_path) as f:
		lines = f.readlines()

	content = "".join(line for line in lines)

	title, published_data, author_name = get_extra_data(lines[:15])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}


def extract_rdf(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)
	
	RDFReader = download_loader("RDFReader")

	loader = RDFReader()
	documents = loader.load_data(file=Path(file_downloaded_path))

	content = "".join(doc.text for doc in documents)

	title, published_data, author_name = get_extra_data(documents[:5])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}




def extract_markdown(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)

	MarkdownReader = download_loader("MarkdownReader")

	loader = MarkdownReader()
	documents = loader.load_data(file=Path(file_downloaded_path))

	content = "".join(doc.text for doc in documents)

	title, published_data, author_name = get_extra_data(documents[:5])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}




def extract_powerpoint(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)

	documents = powerpointLoader(file_downloaded_path)

	content = "".join(doc.page_content for doc in documents.load())
	content = content.replace('<PAGE BREAK>', '')

	title, published_data, author_name = get_extra_data(documents)

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}





def extract_doc_docx(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)
	DocxReader = download_loader("DocxReader")
	loader = DocxReader()

	documents = loader.load_data(file=Path(file_downloaded_path))
	content = "".join(doc.text for doc in documents)

	title, published_data, author_name = get_extra_data(documents[:5])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}




def extract_mobi(url):
	file_downloaded_path = download_file(url)
	
	filename="files/tns.mobi"
	tempdir, filepath = mobi.extract(filename)
	file = open(filepath, "r")
	content = file.read()
	content = html2text.html2text(content)

	# title, published_data, author_name = get_extra_data(documents[:5])

	# return {
	# 	'source_url': url, 
	# 	'date_time'	: published_data,
	# 	'title'		: title, 
	# 	'author'	: author_name, 
	# 	'content'	: content
	# }


def extract_epub(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)
	EpubReader = download_loader("EpubReader")

	loader = EpubReader()
	documents = loader.load_data(file=Path(file_downloaded_path))

	content = "".join(doc.get_text() for doc in documents)
	content = content.split('# Document Outline')[0]

	title, published_data, author_name = get_extra_data(documents[:5])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}


def extract_pdfs(url, file_extention):
	file_downloaded_path = download_file(url, file_extention)

	PDFReader = download_loader("PDFReader")
	loader = PDFReader()

	documents = loader.load_data(file=Path(file_downloaded_path))
	
	content = "".join(doc.text for doc in documents)
	
	title, published_data, author_name = get_extra_data(documents[:5])

	return {
		'content'	: content,
		'source_url': url, 
		'date_time'	: published_data,
		'title'		: title, 
		'author'	: author_name
	}
