import yaml 
from yaml.loader import SafeLoader

import argparse
import pandas as pd

from core 		 import core
from variaveis	 import var
from dicionarios import disc

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument("-m", "--meta", help="Specifies the meta-file from where the information will be retrieved", required=True)
parser.add_argument("-k", "--key", help="Specifies the name of the key series involved in the information transposition", required=True)
parser.add_argument("-a", "--attr", help="Specifies the set of attributes, according to its respective key, which are going to be transposed", required=True)
parser.add_argument("-dfile", "--diciofile", help="Specifies the dictionary File where the retrieved information is going to be added", required=False)
parser.add_argument("-dkey", "--diciokey", help="Column name of Key series from CIDACS Dictionary", required=True)
parser.add_argument("-dattr", "--dicioattr", help="Set of attributes to be retrieved from the meta file in order to be added on the target dictionary", required=True)

args = parser.parse_args()

print("Meta-data File: ",args.meta)
print("Key: ",args.key)
print("Attr: ",args.attr)
print(": ",args.attr)
print("Dicio file: ",args.diciofile)
print("Dicio key: ",args.diciokey)
print("Dicio attr: ",args.dicioattr)

tmp = disc.add_from_file_to_ext_by_key(args.diciofile, args.diciokey, args.dicioattr, args.meta, args.key, args.attr,True)
core.write_file([],args.diciofile,tmp,True)

# -- generate codes
#sim
#python from-meta-to-dict.py -m "..\..\data\sim\inspection\sim-arquivo_historicidade_2017-2019.csv" -k 'VAR' -a 'ANOS_PRESENTE' -dfile "..\..\data\sim\inspection\dicionario_sim_2000_a_2015 - testes.ods" -dkey "Nome da Variável" -dattr "Anos Presente"

#sinasc 
#python from-meta-to-dict.py -m "..\..\data\sinasc\inspection\sinasc-arquivo_historicidade_2001-2020.csv" -k 'VAR' -a 'ANOS_PRESENTE' -dfile "..\..\data\sinasc\inspection\dic_sinasc_v3 - final.ods" -dkey "Nome da variável original" -dattr "Anos presentesssx - the back"

#sifilis
#python from-meta-to-dict.py -m "..\..\data\sinasc\inspection\sinasc-arquivo_historicidade_2001-2020.csv" -k 'VAR' -a 'ANOS_PRESENTE' -dfile "..\..\data\sinan-sifilis\SIFGEN\base_sifilis_gen_2007_a_2018_net.xlsx" -dkey "Nome da variável original" -dattr "Anos presentesssx - the back"


#pbf-fam
#python from-meta-to-dict.py -m "..\..\data\pbf\fam\inspection\pbf-familia-historicidade-file_2021.csv" -k 'VAR' -a 'ANOS_PRESENTE' -dfile "..\..\data\pbf\fam\inspection\metadata-pbf-familia_2021 - Copia.ods" -dkey "Variável (Dicionário)" -dattr "Anos presentes"
#pessoa - python from-meta-to-dict.py -m "..\..\data\pbf\pes\inspection\pbf-pessoa-historicidade_file_2019-2021.csv" -k 'VAR' -a 'ANOS_PRESENTE' -dfile "..\..\data\pbf\pes\inspection\metadata_pbf-pessoa_2021.ods" -dkey "Variável (Dicionário)" -dattr "Anos presentes"