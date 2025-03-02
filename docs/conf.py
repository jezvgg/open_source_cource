import os
import sys
sys.path.insert(0, os.path.abspath('../testing_mocks'))  


project = 'Teasting mocks'
author = 'Volovicov, Gorbachevskiy'
release = '1.0.0'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon', 
]



html_theme = 'sphinx_rtd_theme' 

html_title = 'Документация Teasting mocks'

