from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load your CSV dataset
file_path = 'detect_dataset.csv'
df = pd.read_csv(file_path)

# Assume the target variable is in the 'target_column' column
target_column = 'Output (S)'

# Separate features and target variable
X = df.drop(target_column, axis=1)
y = df[target_column]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initalize the model
neigh = DecisionTreeClassifier()

# Fit the model
neigh.fit(X_train, y_train)

# Check Accuracy
print(neigh.score(X_test, y_test))