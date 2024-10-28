import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error

# Load your dataset from the CSV file
df = pd.read_csv('coffee_lat_lon_updated_cleaned(latest2).csv')

# Fill missing values in 'desc_1' and 'roast' columns with placeholders
df['desc_1'] = df['desc_1'].fillna('Unknown')
df['roast'] = df['roast'].fillna('Unknown')

# Drop rows with missing values in the target columns
target_columns = ['aroma', 'acid', 'body', 'flavor', 'aftertaste']
df = df.dropna(subset=target_columns)

# Verify that no NaN values remain in 'desc_1', 'origin', 'roast', and target columns
if df[['desc_1', 'origin', 'roast']].isna().sum().any() or df[target_columns].isna().sum().any():
    print("There are still NaN values in 'desc_1', 'origin', 'roast', or target columns after handling.")
else:
    print("No NaN values in 'desc_1', 'origin', 'roast', or target columns.")

# Features and target
X = df[['cost_12oz', 'desc_1', 'origin', 'roast']]
y = df[target_columns]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['cost_12oz']),
        ('text', TfidfVectorizer(max_features=50), 'desc_1'),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['origin', 'roast'])
    ]
)

# Model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42)))
])

# Train the model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred, multioutput='raw_values')
rmse = np.sqrt(mse)

# Output results
print("Root Mean Squared Error for each category:")
for col, error in zip(target_columns, rmse):
    print(f"{col.capitalize()}: {error:.2f}")

# User input for prediction
def get_user_input():
    try:
        cost_12oz = float(input("Enter the cost per 12 ounces (USD): "))
    except ValueError:
        print("Please enter a valid number for cost per 12 ounces.")
        return None

    origin = input("Enter the origin of the coffee: ").strip()
    roast = input("Enter the roast level of the coffee (e.g., Light, Medium, Dark): ").strip()
    desc_1 = input("Enter a brief description of the coffee: ").strip()

    return pd.DataFrame({
        'cost_12oz': [cost_12oz],
        'origin': [origin],
        'roast': [roast],
        'desc_1': [desc_1]
    })

# Get user input
user_input = get_user_input()

if user_input is not None:
    # Predict ratings based on user input
    predicted_ratings = model.predict(user_input)

    # Output predicted ratings
    print("\nPredicted Ratings for the input:")
    for col, rating in zip(target_columns, predicted_ratings[0]):
        print(f"{col.capitalize()}: {rating:.2f}")
    
    # Calculate the overall rating (sum of the five predicted ratings)
    overall_rating = np.sum(predicted_ratings[0])
    
    # Calculate the Website Rating
    website_rating = round(overall_rating / 2 + 50)
    
    # Output the results
    print(f"\nOverall Rating predicted is: {overall_rating:.2f}")
    print(f"Website Rating predicted is: {website_rating}")
else:
    print("No valid input received. Exiting...")
