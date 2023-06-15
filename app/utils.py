
import requests
from langchain.indexes import VectorstoreIndexCreator

from llama_index import GPTVectorStoreIndex

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain


def get_the_title(langchain_documents, qa_chain):
	question="What's the title of this documents?"
	title = qa_chain.run(input_documents=langchain_documents, question=question)
	
	if 'not provided' in title:
		return ''
	else:
		return title.split('document is')[1]

def get_publish_date(langchain_documents, qa_chain):
	question="What's the publish data of the document?"
	published_data = qa_chain.run(input_documents=langchain_documents, question=question)
	
	if 'not provided' in published_data:
		return ''
	else:
		return published_data.split('published in')[1]	

def get_authur_name(langchain_documents, qa_chain):
	question="What's the author name of the document?"
	author_name = qa_chain.run(input_documents=langchain_documents, question=question)
	
	if 'not provided' in author_name:
		return ''
	else:
		return author_name.split('document is')[1]	


def get_extra_data(documents):
	try:
		langchain_documents = [d.to_langchain_format() for d in documents]
	except:
		langchain_documents = documents
	llm = OpenAI(temperature=0)
	qa_chain = load_qa_chain(llm)

	try:
		title 			= get_the_title(langchain_documents, qa_chain)
		published_data 	= get_publish_date(langchain_documents, qa_chain)
		author_name 	= get_authur_name(langchain_documents, qa_chain)
	except:
		return '', '', ''

	return title, published_data, author_name




def download_file(file_url, file_extention):
	response = requests.get(file_url)

	if response.status_code == 200:
		file_name = file_url.split("/")[-1]
		file_name = file_name.split('.')[0]
		print(file_name)

		file_downloaded_path = f'../files/{file_name}{file_extention}'
		with open(file_downloaded_path, "wb") as file:
			file.write(response.content)

		print("File downloaded successfully.")

	else:
		print("Failed to download the file.")

	return file_downloaded_path

