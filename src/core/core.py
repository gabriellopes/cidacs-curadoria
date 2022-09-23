import csv

import pandas as pd

import itertools
import os 

import yaml 
from yaml.loader import SafeLoader


def get_file_extension(file_path, printable):
	file_e = os.path.splitext(file_path)

	if(printable):
		print("extension OF [",file_path,"]: ",file_e[1])

	return file_e[1]

def read_file(file_path, printable):
	file_ext = get_file_extension(file_path,printable)
	doc = {}

	if(file_ext == ".ods"):
		doc = pd.read_excel(file_path, engine='odf')

	elif(file_ext == ".csv"):
		doc = pd.read_csv(file_path).replace('"','')

	elif(os.path.isdir(file_path)): #ponteiro a todos arquivos 
		for file in os.listdir(file_path):
			print("FILE: ", file)
			if os.path.isfile(os.path.join(file_path, file)):
				if(printable): 
					print("\n. filename:\n[",os.path.join(file_path, file),"]") #os.path.join(file_path,file))
				doc[file] = pd.read_csv(os.path.join(file_path, file)).replace('"','').replace('\n','')

	if(doc is not None and printable):
		print("file [",file_path,"] read successfully!\n:")
		print("file read:\n" ,doc,"\n--")

	return doc

def read_config(file, printable):
	file_ext = get_file_extension(file,True)
	config = {}
	if(file_ext == ".yaml"):
		stream = open(file,'r')
		dictionary = yaml.load(stream, Loader=SafeLoader)

		for key, value in dictionary.items():
			config['meta'] = value['path']['meta'] #how to bring such tag config for generality.
			config['outp'] = value['path']['outp']
			config['dict'] = value['path']['dict']
			config['name'] = value['name']


	if(printable):
		print("\nCONFIG: \n\n- ",config, "\n\n")
	return config


def get_header_from_csv(csv_file, printable):
	print("opening file: \n"+csv_file,". . .")
	with open(csv_file,"r") as a_file:
		print("file ["+csv_file+"] opened successfully. . .")
		delim = ''
		data = a_file.readline()

		if(';' in data):
			print("; delimitator")
			delim = ';'
		elif(',' in data):
			print(", delimitator")
			delim = ','

		list_cols_file = data.replace('"','').replace('\n','').split(delim)
		
		if(printable):
			print(list_cols_file,"\n----\n total: ",len(list_cols_file))
		return list_cols_file
	print("--")


def write_file(header,output_file, content, printable):
	ext = get_file_extension(output_file,True)

	if(not os.path.exists(os.path.dirname(output_file))):
		print("Path [",output_file,"] don't exist: trying to create it.")
		os.makedirs(os.path.dirname(output_file))
		print("Path [",output_file,"] created successfully.")
		
	if(printable):
		print("\nTrying to write according to the following: ")
		print("file: [",output_file,"]\nheaders: [",header,"] | size: ",len(header),"\ncontent: ",content,"\n> type:",type(content),"\n---")

	if(ext == '.csv'):
		write_dict_to_csv(header,output_file,content, printable)

	if(ext == '.ods'):
		write_to_excel(output_file,content,printable)

	if(printable):
		print("Dictionary printed as file in ["+output_file+"] with success. . .")
		print("-- \n meta:")
	return

def write_to_excel(output_file, data, printable):
	df = pd.DataFrame(data)
	df.to_excel(output_file, index=False)
	if(printable):
		print("--\nData:\n",data,"\n-> wrote in [",output_file,"]\n--")

def write_dict_to_csv(header,output_file,dictio, printable):
	df = pd.DataFrame.from_dict(dictio, orient='index').reset_index()
	new_cols = {}
	i=0
	for c in df.columns:
		new_cols[c] = header[i]
		print("column: ",df[c],"type:",type(df.columns))
		i = i + 1
	
	df = df.rename(columns=new_cols)
	if(printable):
		print("Cols to be added: ",new_cols)
		print("\n\n\n\nHEADERS: ",header,"\n\n\nDF:\n",df)
	df.to_csv(output_file,index=False) 
	return




