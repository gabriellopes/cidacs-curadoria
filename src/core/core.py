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
		if(printable): print("FILE CSV!")
		doc = pd.read_csv(file_path).replace('"','')

	elif(os.path.isdir(file_path)): #ponteiro a todos arquivos 
		for file in os.listdir(file_path):
			print("FILE: ", file)
			if os.path.isfile(os.path.join(file_path, file)):
				print("\n. filename:\n[",os.path.join(file_path, file),"]") #os.path.join(file_path,file))
				#doc[file] = get_header_from_csv(os.path.join(file_path, file),False) #pega somente os headers quando arquivo for diretório, provavelmente BASE: verificar
				doc[file] = pd.read_csv(os.path.join(file_path, file)).replace('"','').replace('\n','')
				#dict, key: dataframe

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
			config['data'] = value['path']['data']
			config['name'] = value['name']


	if(printable):
		print("\nCONFIG: \n\n- ",config, "\n\n")
	return config


def get_header_from_csv(csv_file, printable):
	print("abrindo arquivo: \n"+csv_file,". . .")
	with open(csv_file,"r") as a_file:
		print("arquivo ["+csv_file+"] aberto com sucesso. . .")
		delim = ''
		data = a_file.readline()

		if(';' in data):
			print("; delimitator")
			delim = ';'
		elif(',' in data):
			print(", delimitator")
			delim = ','

		list_cols_file = data.replace('"','').replace('\n','').split(delim)
		#list_cols_file = list_cols_file.split(',')

		print("LIST:",list_cols_file)
		
		if(printable):
			print(list_cols_file,"\n----\n total: ",len(list_cols_file))
		return list_cols_file
	print("--")



def fromCSVToList(csv_file):
	with open(csv_file,"r") as l_file:
		reader = csv.reader(l_file)
		rows = []
		for row in reader:
			rows.append(row)
		return list(rows)



# quebrar função: write_to_file, detectar se é CSV, qual tipo de dado se quer plotar no arquivo, se é dict, etc.

def write_file(header,output_file, content, printable):
	ext = get_file_extension(output_file,True)

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
		#print("SIZE: "+str(len(dictio.values())))
	return

def write_to_excel(output_file, data, printable):
	df = pd.DataFrame(data)
	df.to_excel(output_file, index=False)
	if(printable):
		print("--\nData:\n",data,"\n-> wrote in [",output_file,"]\n--")

def write_dict_to_csv(header,output_file,dictio, printable):
	df = pd.DataFrame.from_dict(dictio, orient='index').reset_index()
	# mudança dos cabeçalhos para os passados por parâmetros
	new_cols = {}
	i=0
	for c in df.columns:
		new_cols[c] = header[i]
		print("column: ",df[c],"type:",type(df.columns))
		i = i + 1
	
	df = df.rename(columns=new_cols)
	print("NEW_COLS: ",new_cols)
	print("\n\n\n\nHEADER: ",header,"\n\n\nDF:\n",df)
	df.to_csv(output_file,index=False) 
	return




