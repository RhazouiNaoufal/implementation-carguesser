import pandas as pd
import numpy as np

#On récupère le fichier à nettoyer
openFile = pd.read_csv(r'C:\Users\Naoufal\vehicules.csv')

df = pd.DataFrame(openFile)

#On définit les valeurs nulles
nan_val= float("NaN")

#On remplace les valeurs null par une case vide
df.replace("",nan_val,inplace=True)

#On supprime les lignes contenant des cases vides
df.dropna(axis=0, how='any', inplace=True)

#On supprime toutes les lignes ayant un prix inférieur à 1000$
df.drop(df[df.price < 1000].index)

#On supprime toutes les lignes ayant un prix supérieur à 100000$
df.drop(df[df.price > 100000].index)

#On supprime toutes les lignes ayant une année de sortie inférieure à 2005
df.drop(df[df.year < 2005].index)

#On remplace des valeurs qualitatives en quantitatives
df.replace({'condition':{'salavage':1,'fair':2,'good':3,'like new':4,'new':5,'excellent':6}},inplace=True)
df.replace({'cylinders':{'8 cylinders':8,'6 cylinders':6,'4 cylinders':4,'10 cylinders':10,'3 cylinders':3,'12 cylinders':12,'5 cylinders':5,'other':0}},inplace=True)
df.replace({'fuel':{'diesel':1,'electric':2,'gas':3,'hybrid':4,'other':5}},inplace=True)
df.replace({'transmission':{'automatic':1,'manual':2,'other':3}},inplace=True)
df.replace({'paint_color':{'black':1,'blue':2,'brown':3,'custom':4,'green':5,'grey':6,'orange':7,'purple':8,'red':9,'silver':10,'white':11,'yellow':12}},inplace=True)
df.replace({'state':{'al':1,'ak':2,'az':3,'ar':4,'ca':5,'co':6,'ct':7,'dc':8,'de':9,'fl':10,'ga':11,'hi':12,'id':13,'il':14,'in':15,'ia':16,'ks':17,'ky':17,'la':18,'me':19,'md':20,'ma':21,'mi':22,'mn':23,'ms':24,'mo':25,'mt':26,'nc':27,'ne':28,'nv':29,'nj':30,'nm':31,'ny':32,'nh':33,'oh':34,'ok':35,'or':36,'pa':37,'ri':38,'sc':39,'sd':40,'tn':41,'tx':42,'vt':43,'va':44,'wa':45,'wv':46,'wi':47,'wy':48}},inplace=True)

#On change le type des colonnes
df['cylinders'].astype('int')
df['fuel'].astype('int')
df['condition'].astype('int')
df['transmission'].astype('int')
df['paint_color'].astype('int')
df['state'].astype('int')

#On récupère le tableau nettoyé dans un fichier csv
df.to_csv("vehicules_final.csv")