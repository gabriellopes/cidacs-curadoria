# curadoria package v.0.0.244

. obj: 
	> Establish a code repository related to Digital Curation processes, taking as a use case the one existing in CIDACS, in order to facilitate maintenance, scalability, and evolution, in addition to deploying, of the code and its respective functionalities.

## Modules organization

> Dicionarios, Arquivos de Historicidades, Bases de dados,
	.csv, .dbf, .ods, 


. /core 
	- common functionalities shared among the modules 
		e.g. extractHeader, readFiles, writeFiles,...,

./descritivas
	- functionalities related to [development of descriptives](https://gabriellopes.github.io/cidacs-curadoria/)
		e.g. non-zero variables, frequency per variable, ...

./dicionarios
	- funções relacionadas à buscas, escritas e populações de dicionarios
		e.g. addFromHistoFileToDicio

./validacao
	- funções relacionadas a validação de dados.
		e.g. 


> fazer de tal forma a usar pela linha de comando.
	ex: generate-hist --meta '../metadata-sinasc' --d '../../dicio-sinasc' --output '.../inspection/historicidade-sinasc.csv'

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

	> python -m pip install --index-url https://test.pypi.org/simple/ curadoria --upgrade    

[URL_TO_PACKAGE](https://test.pypi.org/project/cidacs-curadoria-example-package-22-08-2022/0.0.1/)

