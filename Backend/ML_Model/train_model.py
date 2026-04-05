import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib


data = pd.read_excel('dataset/Weather data.xlsx')

data["rain"] = np.where(data["precip_mm"] > 0, 1, 0)

X = data[["temperature_celsius","humidity","pressure_mb","wind_kph"]]

# 4. Features & target
y = data["rain"]

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# 7. Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# # 8. Save model
joblib.dump(model, "model/weather_model.pkl")
print("Model saved successfully")