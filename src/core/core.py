import csv

import pandas as pd

import itertools
import os 

import yaml 
from yaml.loader import SafeLoader


def get_file_extension(file_path, printable):
	file_e = os.path.splitext(file_path)

	if(printable):
		print("extension of [",file_path,"]: ",file_e)

	return file_e

def read_file(file_path, printable):
	file_e = get_file_extension(file_path,printable)[1]

	doc = []

	if(file_e == ".ods"):
		doc = pd.read_excel(file_path, engine='odf')

	elif(file_e == ".csv"):
		if(printable): print("FILE CSV!")
		doc = pd.read_csv(file_path).replace('"','')

	if(doc is not None and printable):
		print("file [",file_path,"] read successfully!")

	return doc

def read_config(file, printable):
	file_e = get_file_extension(file,True)[1]
	config = {}
	if(file_e == ".yaml"):
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


def getHeaderFromCSV(csv_file, printable):
	print("abrindo arquivo: \n"+csv_file,". . .")
	with open(csv_file,"r") as a_file:
		print("arquivo ["+csv_file+"] aberto com sucesso. . .")

		data = a_file.readline()
		list_cols_file = data.replace('"','').replace('\n','').split(';')
		
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

def writeDictionaryToCSV(header,output_file, dict):
	with open(output_file,"w", newline='', encoding='utf-8') as f:
		writer = csv.writer(f)

		writer.writerow(header)

		for key, value in dict.items():
			writer.writerow((key, value))

		print("Dictionary printed as file in ["+output_file+"] with success. . .")
		print("-- \n meta:")
		print("SIZE: "+str(len(dict.values())))
	return

