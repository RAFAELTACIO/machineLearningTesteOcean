#IMPORTAÇÕES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
pd.options.display.max_columns = 150


data = pd.read_csv('data-final.csv', sep='\t')

#APAGANDO OS ATRIBUTOS QUE EU NÃO QUERO USAR, DA COLUNA 1 A 50, SÃO AS REPOSTAS DAS QUESTÕES, O RESTANTE, NÃO ME INTERESSA
data.drop(data.columns[50:110], axis = 1, inplace=True)