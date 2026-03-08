import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("data/pcb_test_data.csv")

X = data[["voltage","current","temperature","time"]]
y = data["result"]

X_train,X_test,y_train,y_test = train_test_split(X,y)

model = RandomForestClassifier()
model.fit(X_train,y_train)

sample = [[4.85,0.50,60,25]]

prediction = model.predict(sample)

print("Prediction:",prediction[0])