"""
loads and parses the json file
"""
import json

def load_config():

	with open("settings/db_file.json") as file:
		data = json.load(file)

	return data