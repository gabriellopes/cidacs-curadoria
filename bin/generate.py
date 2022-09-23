import yaml 
from yaml.loader import SafeLoader

import argparse
import pandas as pd
import os 

from core 		 import core
from variaveis	 import var
from dicionarios import disc

parser = argparse.ArgumentParser(description='A test program.')

#parser.add_argument("--print_string", help="Prints the supplied argument.", default="A random string.", required=True)
parser.add_argument("-c", "--config", help="Config file with database metadata required", required=True)
parser.add_argument("-k", "--key", help="Specifies the name of the Feature of Interested, key, involved in the process: generating historicity of what?", required=True)
parser.add_argument("-a", "--attr", help="Specifies the attributes according to which the key historicity is going to be generated.", required=True)
parser.add_argument("-H", "--header", help="Set of headers for outputing the file", required=True)
parser.add_argument("-dkey", "--diciokey", help="Column name of Key series from CIDACS Dictionary", required=True)
parser.add_argument("-dattr", "--dicioattr", help="Column name of Attribute series from CIDACS Dictionary", required=True)
parser.add_argument("-o", "--output", help="Generated output file", required=False, default="generated-file.csv")

args = parser.parse_args()

print("Config File: ",args.config)
print("Key: ",args.key)
print("Attr: ",args.attr)
print("Headers: ",args.header)
print("Output file: ",args.output)

# -- args treatement

if(',' in args.attr):
	print("tem virgula, range!")
	args.attr = args.attr.replace("[","").replace("]","")
	print(":",args.attr)
	args.attr = args.attr.split(',')
	args.attr = range(int(args.attr[0]),int(args.attr[1]))

# -- config

config = core.read_config(args.config,True)

output_path = config['outp']
dict_path = config['dict']
meta_path = config['meta']

dicio = core.read_file(dict_path,True)
tmp = core.read_file(meta_path, True)

tmp = var.get_year_by_variable(tmp,args.key,args.attr,True) #cast to int
tmp = var.from_sequence_to_range_by_key(tmp,True)

tmp = disc.add_attr_from_ext_by_key(tmp, args.diciokey, args.dicioattr, dicio, True) #SINASC

core.write_file(str(args.header).split(','),output_path+config['name']+'-'+args.output,tmp, True)




# -- generate codes
# sim 
#python generate.py -c ..\cidacs-curadoria\tests\resources\config-sim.yaml -k variavel -a [13,18] -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "Nome da Variável" -dattr "Descrição Original" -o "histor_teste-file_123-sim.csv"

# sinasc
#python generate.py -c ..\cidacs-curadoria\tests\resources\config-sinasc.yaml -k variavel -a ano -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "Nome da variável original" -dattr "Descrição original" -o "histor_teste-file_123-s5.csv"

# sifilis
# python generate.py -c ..\cidacs-curadoria\tests\resources\config-sifilis.yaml -k variavel -a [35,38] -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "" -dattr "" -o "histor_teste-file-sifilis.csv"
# CN: python generate.py -c ..\cidacs-curadoria\tests\resources\config-sifilis.yaml -k variavel -a [36,39] -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "" -dattr "" -o "histor_teste-file-sifilis.csv"
# SIFGEN: python generate.py -c ..\cidacs-curadoria\tests\resources\config-sifilis.yaml -k variavel -a [36,39] -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "" -dattr "" -o "histor_teste-file-sifilis.csv"

# pbf
# python generate.py -c ..\cidacs-curadoria\tests\resources\config-pbf_familia.yaml -k "Variável (Dicionário)" -a [13,18] -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "Variável (Dicionário)" -dattr "Descrição/Categorias (Dicionário)" -o "historicidade_file.csv"
# pessoa - python generate.py -c ..\cidacs-curadoria\tests\resources\config-pbf_pessoa.yaml -k "Variável (Dicionário)" -a [13,18] -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "Variável (Dicionário)" -dattr "Descrição/Categorias (Dicionário)" -o "historicidade_file.csv"
#