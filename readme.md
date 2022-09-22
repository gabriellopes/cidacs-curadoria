<<<<<<< HEAD
# curadoria package v.0.0.244

. obj: 
	> Establish a code repository related to Digital Curation processes, taking as a use case the one existing in CIDACS, in order to facilitate maintenance, scalability, and evolution, in addition to deploying, of the code and its respective functionalities.
=======
# curadoria package v.0.0.1
>>>>>>> cd4dd7f7a7f2f2a9e003df9ab58f090bf5c726b3

## Modules organization

> Dicionarios, Arquivos de Historicidades, Bases de dados,
	.csv, .dbf, .ods, 


<<<<<<< HEAD
- /core 
	- common functionalities shared among the modules 
		e.g. extractHeader, readFiles, writeFiles,...,

- /descritivas
	- functionalities related to [development of descriptives](https://gabriellopes.github.io/cidacs-curadoria/)
		e.g. non-zero variables, frequency per variable, ...

- /dicionarios
	- funções relacionadas à buscas, escritas e populações de dicionarios
		e.g. addFromHistoFileToDicio

- /validacao
	- funções relacionadas a validação de dados.
		e.g. 


> fazer de tal forma a usar pela linha de comando.
	ex: generate-hist --meta '../metadata-sinasc' --d '../../dicio-sinasc' --output '.../inspection/historicidade-sinasc.csv'

=======
./core 
	- common functions shared among the modules
		e.g. extractHeader, readFiles, writeFiles,...,

./descritivas
	- funções relacionadas ao desenvolvimento de descritivas
		e.g. variaveis não nulas, frequência por variáveis, 

./dicionarios
	- funções relacionadas à buscas, escritas e populações de dicionarios

./validacao
	- funções relacionadas a validação de dados.




-- propo2:

./variables
	- tratamento do conteúdo das variáveis, como mudar a apresentação ou testar determinado valor;

./descritivas
	- funções que gerem elementos da especificação de descritivas;

./dicionarios
	- ler arquivo de dicionario, procurar determinada coluna, descrição, alterar segundo determinado conteúdo, e por aí vai;

./validacao
	- procedimentos relacionados à etapa de validação 

./core
	- funções comuns à todos módulos, ou necessário à eles;

	
> fazer de tal forma a usar pela linha de comando.
	ex: generate-hist --meta '../metadata-sinasc' --d '../../dicio-sinasc' --output '.../inspection/historicidade-sinasc.csv'



## project structure

. *example.py* is an example of a module within the package that could contain the logic (functions, classes, constants, etc.) of your package. 

. *pyproject.toml* tells “frontend” build tools like pip and build what “backend” tool to use to create distribution packages for your project.
	
	. *requires* is a list of packages that are needed to build your package. You don’t need to install them; build frontends like pip will install them automatically in a temporary, isolated virtual environment for use during the build process.

	. *build-backend* is the name of the Python object that frontends will use to perform the build.

	. *license* describes the respective license chose for the project/package according to [this documentation](https://choosealicense.com/)


. *tar.gz* file is a source distribution whereas the 
. *whl* file is a built distribution. 


. [*TWINE*](https://packaging.python.org/en/latest/key_projects/#twine) is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes. It is a command-line program that passes program files and metadata to a web API. Developers use it because it’s the official PyPI upload tool, it’s fast and secure, it’s maintained, and it reliably works.


>>>>>>> cd4dd7f7a7f2f2a9e003df9ab58f090bf5c726b3
### Uploading package workflow


1. CREATE folder hierarchy with:
	[FOLDER_NAME],
		- src/
			- [package_name]
				. __init__.py
				. example.py
		- tests/

2. CREATE package files:
	[PACKAGE_NAME],
		-LICENSE, pyproject.toml & readme.md

3. CONFIGURE metadata (pyproject.toml, similars to packages.json in NODEjs, readme, and LICENSE)

4. BUILD with python -m build (needs to install such package through -m pip install --upgrade build)
	-m indicates to execute the module as a script, thus, w/o option list.


5. UPLOAD with [twine package](https://packaging.python.org/en/latest/key_projects/#twine)
	> needs to create an account in <https://packaging.python.org/en/latest/key_projects/#twine>

6. INSTALL the new uploaded package and test it out ;-)

<<<<<<< HEAD
	> python -m pip install --index-url https://test.pypi.org/simple/ curadoria --upgrade    
=======
>>>>>>> cd4dd7f7a7f2f2a9e003df9ab58f090bf5c726b3

[URL_TO_PACKAGE](https://test.pypi.org/project/cidacs-curadoria-example-package-22-08-2022/0.0.1/)


<<<<<<< HEAD
### Usability 

. generate:

> python generate.py -c ..\cidacs-curadoria\config-sim.yaml -k 18 -a 22 -H 'VAR','DESCRICAO','ANOS_PRESENTE' -dkey "Nome da Variável" -dattr "Descrição Original" -o "histor_teste-file_123-sim.csv"

. from-meta-to-dict:

> python from-meta-to-dict.py -m "..\..\data\sim\inspection\sim-histor_teste-file_123-sim.csv" -k 'VAR' -a 'ANOS_PRESENTE' -dfile "..\..\data\sim\inspection\dicionario_sim_2000_a_2015 - testes.ods" -dkey "Nome da Variável" -dattr "Anos Presente - the back"
=======




>>>>>>> cd4dd7f7a7f2f2a9e003df9ab58f090bf5c726b3
