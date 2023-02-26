import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
from xgboost import XGBClassifier


# pathing is relative
df = pd.read_csv('data/train.csv')
df.columns


# clean
df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex']]
df.info()


numeric_transformer = Pipeline(steps=[
       ('imputer', SimpleImputer(strategy='mean')),
       ('scaler', StandardScaler()),
       ('ohe', OneHotEncoder(handle_unknown ='ignore')),
])

categorical_transformer = Pipeline(steps=[
       ('imputer', SimpleImputer(strategy='constant')),
       ('ohe', OneHotEncoder(handle_unknown ='ignore')),
])


numeric_features = [
    'Pclass', 
    'Age', 
    'SibSp', 
    'Parch', 
    'Fare'
]

categorical_features = [
    'Sex'
]

preprocessor = ColumnTransformer(
   transformers=[
    ('numeric', numeric_transformer, numeric_features),
    ('categorical', categorical_transformer, categorical_features),
]) 


# define X, y
dependent_variable = 'Survived'

X = df.drop('Survived', axis=1)
y = df[dependent_variable]

X.head()


clf_xgb = XGBClassifier()


pipeline = Pipeline(
    steps = [
                ('preprocessor', preprocessor),
                ('classifier', clf_xgb)
           ]
)

clf = pipeline.fit(X, y)
print (clf)


# create model file and assign it to a classifier object

joblib.dump(clf, 'model.pkl')
clf = joblib.load('model.pkl')


# test prediction locally

json_payload = pd.DataFrame.from_dict([{"Pclass": "3", "Age": "22.0", "SibSp": "1", "Parch": "0", "Fare": "70", "Sex": "m"}])
prediction = clf.predict(json_payload)[0]
print(prediction)
