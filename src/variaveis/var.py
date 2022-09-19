import csv
import pandas as pd
from core 		 import core
# module dedicated for treating with variables, such as transformations, concatenations, and so on.


#@file: dataframe, dictionary, list,.., opened file;
#@col_var: the name of the column, or its index, from which is expected to have the variables list;
#@col_year: the name of the column, or its index, from which is expected to have the years list;
#@printable: if it is needed to print the progressing steps throughout the method
def get_year_by_variable(file, col_var, col_year, printable): #adaptar para quando for número, ver se é a posição no nome do arquivo
	d_var_x_year = {}
	year = ''
	print("col_var", col_var," col_year: ",col_year, "file: ",file)
	if(type(file) is dict): #varios arquivos
		for key in file: 							#for each file
			for var in file[key][col_var]:
				if(type(col_year) is range): 			#year as a range
					col_year_1 = list(col_year)[0]
					col_year_2 = list(col_year)[-1]
					year = key[col_year_1:col_year_2] 	#ano no nome do arquivo

					if(printable):
						print("key: ",key, "year: ",year)

					if(var not in d_var_x_year):
						d_var_x_year[var] = list()
					if(year not in d_var_x_year[var]):
						d_var_x_year[var].append(year) #qnd adiciona a segunda já vira string a p td?

	elif(file is not None):
		for var in file[col_var]: #for each variable in the same file
			if(var not in d_var_x_year):
				d_var_x_year[var] = list()
				d_var_x_year[var].extend(file[file[col_var]==var][col_year].values)

	if(printable):
		print("Result:\n\n", d_var_x_year)

	return d_var_x_year #Dicio ou pandas frame



# function to know if a number is surrounded by another one.
# caso 99 and 
def is_surrounded(num1, num2):
	print("Num1: ",num1,"\nnum2:",num2)
	if(num1 == num2+1):
		return True
	if(num2 == num1+1):
		return True
	return False

def from_sequence_to_range_by_key(alist, printable):
	for key, years in alist.items(): #chaves por anos respectivos de presença, e.g. NUMERODV 2020,2019,...,2008
		
		idx = 0
		end = 0
		init = 0
		rangeY = ""
		ranges = []

		if(printable):
			print("--\nKEY:", key, "\nYEARS:", years, "\nidx:",idx, "\nlen:",len(years))
		while (idx < len(years)):
			init = years[idx] 
			rangeY = str(init)
			end = 0
			while(idx < (len(years)-1) and is_surrounded(int(years[idx]),int(years[idx+1]))): 
				idx = idx+1			#passa pelo loop, transforma o end em 2016
				end = years[idx] 	#saiu do loop, então tá com end, talvez n tenha terminado

			if(printable):
				print("INIT:",init,"\nEND:",end)

			if(end is not 0):
				rangeY = rangeY + ":" + str(end)
			
			ranges.append(rangeY)
			alist.update({str(key) : ranges})
			idx = idx+1 # já sai do loop com o range completo para 1 determinado intervalo de anos, referente a uma mesma variável (ou key)

	if(printable):
		print("\n\n\n\n\nALIST: \n",alist)
	return alist



