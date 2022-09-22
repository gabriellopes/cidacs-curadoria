from core 		 import core
# module dedicated for dealing with dictionaries, specially in ods, csv and excel

def funcao():
	print("Sou uma função do módulo DICIONARIO  v0.0.25")


#@key_list: lista com chaves a serem consultadas em dicio_file
#@col_key: nome da coluna aonde a key se encontra; 
#@col_attr: nome da coluna aonde o atributo em questão se encontra;
#@dicio_file: arquivo em DataFrame do dicionário lido

def add_attr_from_ext_by_key(key_list, col_key, col_attr, dicio_file, printable): 
	tmp2 = {}
	if(printable):
		print("Trying to read [",dicio_file,"] for adding values from col: [",col_attr,"] against col: [",col_key,"]")

	if(dicio_file is not None):
		#dicio_file = dicio_file[[col_key,col_attr]] # reducing the file to key x attr
		for key in key_list:
			if(key not in tmp2 and key is not None):
				adding = list(dicio_file[dicio_file[col_key]==key][col_attr].values) if len(dicio_file) > 0 else []
				years = key_list[key] # adding without having what had before
				if(printable):
					print("VAR: ",key,"| DESC: ",adding, " TYPE_DESC: ",type(adding),"| YEARS: ",years)
				tmp2[key] = list()
				tmp2[key] = [adding,years]
	else: 
		tmp2 = tmp
	if(printable):
		print("DICIO:\n\n", tmp2)
	return tmp2


def add_from_file_to_ext_by_key(ext_file, ext_key_col_name, ext_new_col_name, key_list, key_col_index, key_add_col_index, printable):
	df_key = core.read_file(key_list,True)
	df_ext = core.read_file(ext_file,True)	

	df_ext[ext_new_col_name] = ""

	if(printable):
		print("ext_key: ",key_add_col_index)
		print("\n\ndf:\n",df_key,"\n\n--")
	for i in range(len(df_ext)):
		tmp = df_ext[ext_key_col_name][i] # nome da variável
		adding = df_key[df_key[key_col_index]==tmp][key_add_col_index] # anos correspondente a key em questão
		df_ext[ext_new_col_name][i] = str(adding.values).replace("[\"",'').replace("\"]",'')
		if(printable):
			print("Column to be added [",str(adding.values),"] at the key [",tmp,"]")

	if(printable):
		print("New data:",df_ext)

	return df_ext

