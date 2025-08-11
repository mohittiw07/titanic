Titanic Survival Prediction using Random Forest
This project uses the Titanic dataset to predict whether a passenger survived or not, based on their demographic and travel details.
It trains a Random Forest Classifier and evaluates it using accuracy, precision, recall, and F1 score.

📌 Features
Data preprocessing (handling missing values, encoding categorical data)

Model training using RandomForestClassifier from scikit-learn

Performance evaluation (Accuracy, Precision, Recall, F1 Score)

Model saving with joblib for future predictions

📂 Dataset
You will need the file:

mathematica
Copy
Edit
Titanic-Dataset.csv
It should have columns like:

PassengerId

Name

Age

Sex

Ticket

Cabin

Embarked

Survived (Target variable)

🛠 Installation
Clone this repository or copy the script.

Install dependencies:

bash
Copy
Edit
pip install pandas scikit-learn joblib
🚀 Usage
Place the Titanic-Dataset.csv in the same folder as the script.

Run the Python file:

bash
Copy
Edit
python titanic_model.py
The output will show:

Accuracy

Precision

Recall

F1 Score

The trained model will be saved as:

Copy
Edit
titanic_model.pkl
📊 Model Workflow
Data Cleaning

Drops unused columns (Name, PassengerId, Cabin, Ticket)

Fills missing Age with the mean age

Converts categorical variables into numeric using one-hot encoding

Model Training

Splits data into 80% training and 20% testing

Trains a RandomForestClassifier

Evaluation Metrics

Accuracy

Precision

Recall

F1 Score

Model Saving

Saves the trained model to disk with joblib

📈 Example Output
vbnet
Copy
Edit
✅ Model Evaluation:
Accuracy: 85.42 %
Precision: 0.8021
Recall: 0.7568
F1 Score: 0.7788

💾 Model saved as 'titanic_model.pkl'
📌 Notes
You can tweak the RandomForestClassifier parameters for better performance.

For more accuracy, try feature engineering (e.g., family size, title extraction from name).

