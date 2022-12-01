import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
%matplotlib inline 
sns.set(color_codes=True)

#On récupère le fichier à visualiser
openFile = pd.read_csv(r'C:\Users\Naoufal\vehicules_final.csv')

df = pd.DataFrame(openFile)

#implémentation d'une fonction qui retourne la moyenne et l'écart type d'une colonne selon une autre
def return_statistics(data_frame, categorical_column, numerical_column):
    mean = []
    std = []
    field = []
    for i in set(list(data_frame[categorical_column].values)):
        new_data = data_frame[data_frame[categorical_column] == i]
        field.append(i)
        mean.append(new_data[numerical_column].mean())
        std.append(new_data[numerical_column].std())
    df = pd.DataFrame({'{}'.format(categorical_column): field, 'mean {}'.format(numerical_column): mean, 'std in {}'.format(numerical_column): std})
    df.sort_values('mean {}'.format(numerical_column), inplace = True, ascending = False)
    df.dropna(inplace = True)
    return df

#moyenne des prix selon les marques de voiture
stats = return_statistics(df, 'manufacturer', 'price')


################################################################################

#Exploration des données
print(stats)

#Vérifier l'zxistence de valeurs nulles
df.info()
df.isnull().sum()

################################################################################

#Visualiser la distribution du prix
df['price'].hist()

plt.boxplot(df['price'])

################################################################################

#Visualiser l'évolution du prix par rapport aux années
plt.scatter(df['year'], df['price'])

#Visualiser l'évolution du prix par rapport au kilométrage
plt.scatter(df['odometer'], df['price'])

################################################################################

#Visualiser la corrélation entre les éléments
plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c

################################################################################

#Visualiser la distribution des types de carburant
fig, ax = plt.subplots(1, 2, figsize=(15,8))
x=df['fuel'].value_counts().index
y=df['fuel'].value_counts().values.tolist()
data = df.groupby("fuel").size()
sns.set(style="dark", color_codes=True)
pal = sns.color_palette("magma", len(data))
rank = data.argsort().argsort() 
sns.barplot(x=x,y=y,palette=np.array(pal[::-1])[rank],ax = ax[0])
for p in ax[0].patches:
        ax[0].annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
ax[0].set_xlabel('Types of Fuel', weight='semibold', fontname = 'monospace')
_, _, autotexts= ax[1].pie(y, labels = x, colors = pal, autopct='%1.1f%%',
        explode=[0.03 for i in df['fuel'].value_counts().index])
for autotext in autotexts:
    autotext.set_color('white')
plt.legend(bbox_to_anchor=(1, 1))
plt.suptitle ('Types of Fuel',weight = 'bold')
plt.show()

################################################################################

#Visualiser la distribution des différentes marques
fig, ax = plt.subplots(1, 2, figsize=(15,8))
x=df['manufacturer'].value_counts().index
y=df['manufacturer'].value_counts().values.tolist()
data = df.groupby("manufacturer").size()
sns.set(style="dark", color_codes=True)
pal = sns.color_palette("magma", len(data))
rank = data.argsort().argsort() 
sns.barplot(x=x,y=y,palette=np.array(pal[::-1])[rank],ax = ax[0])
for p in ax[0].patches:
        ax[0].annotate('{:.0f}'.format(p.get_height()), (p.get_x()+0.3, p.get_height()),
                    ha='center', va='bottom',
                    color= 'black')
ax[0].set_xlabel('Manufacturers', weight='semibold', fontname = 'monospace')
_, _, autotexts= ax[1].pie(y, labels = x, colors = pal, autopct='%1.1f%%',
        explode=[0.03 for i in df['manufacturer'].value_counts().index])
for autotext in autotexts:
    autotext.set_color('white')
plt.legend(bbox_to_anchor=(1, 1))
plt.suptitle ('Manufacturers',weight = 'bold')
plt.show()

################################################################################

#Visualiser l'état de la voiture par rapport à son type de transmission (manuel,automatique) et son type de roues
g = sns.PairGrid(df , hue='condition' ,x_vars=["transmission" , "cylinders"],y_vars=["transmission" , "cylinders"],
                 height=6, aspect=1)
g = g.map_offdiag(plt.scatter , edgecolor="w", s=130)
g = g.map_diag(plt.hist , edgecolor ='w', linewidth=2)
g = g.add_legend()
plt.show()

################################################################################