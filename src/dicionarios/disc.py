
# module dedicated for dealing with dictionaries, specially in ods, csv and excel

def funcao():
	print("Sou uma função do módulo DICIONARIO  v0.0.25")


#@key_list: lista com chaves a serem consultadas em dicio_file
#@col_key: nome da coluna aonde a key se encontra; 
#@col_attr: nome da coluna aonde o atributo em questão se encontra;
#@dicio_file: arquivo em DataFrame do dicionário lido

def add_by_key_attr_from_ext(key_list, col_key, col_attr, dicio_file, printable): 
	tmp = {}
	if(dicio_file is not None):
		dicio_file = dicio_file[[col_key,col_attr]] # reducing the file to key x attr
		for key in key_list:
			if(key not in tmp and key is not None):
				desc = dicio_file[dicio_file[col_key]==key][col_attr].values
				years = key_list[key]
				print("VAR: ",key,"| DESC: ",desc, "| YEARS: ",years)

				tmp[key] = list()
				tmp[key].extend(desc)
				tmp[key].extend(years)
	if(printable):
		print("DICIO:\n\n", tmp)
	return tmp



#pd = new DataFrame("var","desc","anos")

#pd.var  = 
#pd.desc = 
