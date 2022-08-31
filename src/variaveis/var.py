import csv
import pandas as pd

# module dedicated for treating with variables, such as transformations, concatenations, and so on.


#@file: dataframe, dictionary, list,.., opened file;
#@col_var: the name of the column, or its index, from which is expected to have the variables list;
#@col_year: the name of the column, or its index, from which is expected to have the years list;
#@printable: if it is needed to print the progressing steps throughout the method
def get_year_by_variable(file, col_var, col_year, printable):
	d_var_x_year = {}
	if(file is not None):
		file = file[[col_var,col_year]] # reducing the dict
		for var in file[col_var]: #for each variable
			if(var not in d_var_x_year):
				d_var_x_year[var] = list()
				d_var_x_year[var].extend(file[file[col_var]==var][col_year].values)

	if(printable):
		print("DICIO:\n\n", d_var_x_year)

	return d_var_x_year #Dicio ou pandas frame


def from_sequence_to_range_by_key(alist, printable):
	for key, years in alist.items(): #chaves por anos respectivos de presença, e.g. NUMERODV 2020,2019,...,2008
		
		#years = ['2020','2019','2018','2017','2016','2012','2011','2010','2009','2008'] #teste
		#years = ['2007','2005','2004','2003'] to ['2007:2003',...]
		#years = ['2020', ' 2019', ' 2018', ' 2017', ' 2012']

		idx = 0
		end = 0
		init = 0
		rangeY = ""
		ranges = []

		if(printable):
			print("--\nKEY:", key, "\nYEARS:", years, "\nidx:",idx, "\nlen:",len(years))
		while (idx < len(years)):
			init = years[idx] #esperado 2020 na primeira passada
			rangeY = str(init)
			end = 0
			while(idx < (len(years)-1) and int(years[idx])==int(years[idx+1])+1): 
				idx = idx+1			#passa pelo loop, transforma o end em 2016
				end = years[idx] 	#saiu do loop, então tá com end, talvez n tenha terminado

			if(printable):
				print("INIT:",init,"\nEND:",end)

			if(end is not 0):
				rangeY = rangeY + ":" + str(end)
			
			#rangeY = rangeY + str(end) #vazio, manteve-se 0, então é porque n entrou no loop, ou seja, o item 0 já estava distante dos outros anos 

			ranges.append(rangeY)
			print("RANGE:",ranges)
			alist.update({str(key) : ranges})
#			print("ANO VIGENTE:",years[idx], "INIT: ",init, " END:", end, "IDX:",idx)
			idx = idx+1 # já sai do loop com o range completo para 1 determinado intervalo de anos, referente a uma mesma variável (ou key)

	if(printable):
		print("\n\n\n\n\nALIST: \n",alist)
	return alist



