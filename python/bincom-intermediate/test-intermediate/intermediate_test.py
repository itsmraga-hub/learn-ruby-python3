import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import preprocess
from sklearn.preprocessing import StandardScaler
import warnings


scaler = StandardScaler()
# preprocessor = PreprocessingClass()


# Step 1: Data Collection
data = pd.read_csv('train_loan.csv')

# Step 2: Data Preprocessing
data['Dependents'] = data['Dependents'].replace('3+', 3)

numeric_columns = ['CoapplicantIncome', 'LoanAmount']
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
data.dropna(inplace=True)

# Step 3: Feature Selection/Engineering
# Select relevant features or engineer new features if necessary

# Step 4: Model Selection
model = LogisticRegression(max_iter=2000)  # Choose the desired model algorithm

# Step 5: Model Training
X = data.drop(['Loan_Status', 'Loan_ID', 'Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area'], axis=1)  # Features
y = data['Loan_Status']  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)
scaler.fit(X_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 7: Model Tuning
new_applicant = pd.DataFrame({
    'Gender': ['Female'],
    'Married': ['No'],
    'Dependents': ['0'],
    'Education': ['Graduate'],
    'Self_Employed': ['No'],
    'ApplicantIncome': [4576],
    'CoapplicantIncome': [0],
    'LoanAmount': [128],
    'Loan_Amount_Term': [360],
    'Credit_History': [1],
    'Property_Area': ['Rural']
})
new_applicant['Dependents'] = new_applicant['Dependents'].replace('3+', 3)
new_applicant[numeric_columns] = new_applicant[numeric_columns].fillna(data[numeric_columns].mean())
new_applicant.dropna(inplace=True)

# new_applicant_features = new_applicant.drop(['Loan_ID', 'Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area'], axis=1)
new_applicant_features = new_applicant.drop(['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area'], axis=1)


# Apply the scaler transformation to the preprocessed new_applicant data
preprocessed_new_applicant = scaler.transform(new_applicant_features)

warnings.filterwarnings("ignore", category=UserWarning)
prediction = model.predict(preprocessed_new_applicant)
print("Loan Eligibility Prediction:", prediction)
