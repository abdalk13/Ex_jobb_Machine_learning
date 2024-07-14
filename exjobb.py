import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score, roc_auc_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


data= pd.read_excel('xxxx.xlsx') #läs data

X=data.drop(['m24'],axis=1).copy()
X.head()

y=data['m24'].copy()
y.head()

X_encoded=pd.get_dummies(X, columns=['Motortyp'])
X_encoded.head()
X_encoded.sample(100)

# nu ser vi att vår Y är bara unika värde så att vi inte kör om med samma värde
len(y.unique())
#nu behöver vi normalisera våra värden i y för att man ska kunna få rätt 

min_value = np.min(y)
max_value = np.max(y)
normalized_y = (y - min_value) / (max_value - min_value)
print(normalized_y)
sum(normalized_y)/len(normalized_y) #kan inte använda y som den är
#nu splitrar vi vår data

#datan splitras om vi ska kolla modellens anpassning till data
#X_train, X_test, y_train, y_test= train_test_split(X_encoded,normalized_y,test_size=0.2, random_state=20220328)

#datan splitras om vi ska prediktera
X_train, X_test, y_train, y_test= train_test_split(X_encoded,y,test_size=0.28, random_state=20220328)
#de ska var så när som möjli
sum(y_train)/len(y_train)
sum(y_test)/len(y_test)
#fixa ett problem som dyker i Gboost med y_train i classification
#from sklearn.preprocessing import LabelEncoder
#le = LabelEncoder()
#y_train = le.fit_transform(y_train)
#här skapar vi xgboost modellen


#clf_xgb = xgb.XGBClassifier(objective='multi:softmax', seed=42, eval_metric='merror')

# Träna  modell
#clf_xgb.fit(X_train, y_train, eval_set=[(X_test, y_test)],  early_stopping_rounds=10, verbose=True)
#print("Bästa mätvärdet:", clf_xgb.best_score)
#from xgboost import XGBRegressor
clf_xgb = xgb.XGBRegressor()

clf_xgb.fit(X_train, y_train)
clf_xgb.score(X_test, y_test)
#prova med lambda

#första

#param_grid = {
#    'max_depth': [3, 4, 5],
#    'learning_rate': [0.1, 0.01, 0.05],
#    'gamma': [0, 0.25, 1.0],
#    'reg_lambda': [0, 1.0, 10.0],
#    'scale_pos_weight': [1, 3, 5] 
#}

#två
#param_grid = {
 #   'max_depth': [4],
 #   'learning_rate': [0.1, 0.5, 1],
 #   'gamma': [0.25],
 #   'reg_lambda': [10.0, 20, 100],
 #   'scale_pos_weight':[3]
#}

import pandas as pd

y_test = y_test
#---------------------------------------
#den används inte om test fil används
X_test = X_test
#-----------------------------------
#--------------------------------
#ifall test fil används
#X_test = pd.read_excel('try1.xlsx')
#X_test.drop(['Product group','Fiscal year/period','Motorkod','Order','Reperation','m24' ],axis=1, inplace=True)
#X_test=pd.get_dummies(X_test, columns=['Motortyp'])
#-----------------------------------------------------
predictions_last_five = clf_xgb.predict(X_test)

# Skapa DataFrame för de verkliga värdena och förutsägelserna
comparison_df = pd.DataFrame({
    #--------------------------------------
    #behövs inte om datan i test fil
    'verkliga data': y_test.values,
    #------------------------------------
    'Förutsägelser': predictions_last_five
})


#--------------------------------------------
#ifall test fil används

#comp = pd.read_excel('verkliga_data.xlsx')
#comparison_df = pd.concat([comp, comparison_df], axis=1)
#---------------------------------------------
comparison_df.to_excel('verkliga_och_forutsagelser.xlsx', index=False)

comparison_df.sample(20)

import pandas as pd
import plotly.graph_objects as plt

# Läs in data
comparison_df = pd.read_excel('verkliga_och_forutsagelser.xlsx')

fig = plt.Figure()

# Lägg till linjer för verkliga värden och förutsägelser
fig.add_trace(plt.Scatter(x=comparison_df.index, y=comparison_df['verkliga data'], mode='markers', name='verkliga data', marker=dict(color='blue')))
fig.add_trace(plt.Scatter(x=comparison_df.index, y=comparison_df['Förutsägelser'], mode='markers', name='Förutsägelser', marker=dict(color='red')))



# Visa diagrammet
fig.show()

import plotly.express as plt
xdata=data.drop(['m24','Equi Number','Motortyp','Year of construction','LMH cost carrier'],axis=1).copy()
melted_data = xdata.melt(value_vars=['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 'm11', 'm12', 'm13', 'm14', 'm15', 'm16', 'm17', 'm18', 'm19', 'm20', 'm21', 'm22', 'm23'],
var_name='Month', value_name='Cost')
fig = plt.box(melted_data, x='Month', y='Cost', title='Cost over time')
fig.show()