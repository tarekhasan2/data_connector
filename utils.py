
import requests


### WORKING ON IT
def get_the_title():
	return None 

### WORKING ON IT
def get_publish_date():
	return None 

### WORKING ON IT
def get_authur_name():
	return None


def download_file(file_url, file_extention):
	response = requests.get(file_url)

	if response.status_code == 200:
		file_name = file_url.split("/")[-1]
		file_name = file_name.split('.')[0]
		print(file_name)

		file_downloaded_path = f'files/{file_name}{file_extention}'
		with open(file_downloaded_path, "wb") as file:
			file.write(response.content)

		print("File downloaded successfully.")

	else:
		print("Failed to download the file.")

	return file_downloaded_path

