import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

df = pd.read_csv("Titanic-Dataset.csv")

df = df.drop(["Name", "PassengerId", "Cabin", "Ticket"], axis=1)

df["Age"] = df["Age"].fillna(int(df["Age"].mean()))
df["Age"] = df["Age"].astype(int)

df = pd.get_dummies(df, drop_first=True)

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_p
              
print("✅ Model Evaluation:")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision, 4))
print("Recall:", round(recall, 4))
print("F1 Score:", round(f1, 4))

joblib.dump(model, "titanic_model.pkl")
print("\n💾 Model saved as 'titanic_model.pkl'")
