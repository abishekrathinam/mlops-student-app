import os
import joblib
from sklearn.ensemble import RandomForestClassifier

MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0")

def generate_data():
# Features: study hours per day, attendance %, internal marks / 100
X = []
y = []

```
for hours in range(0, 11):
    for attendance in range(0, 101, 10):
        for marks in range(0, 101, 10):
            X.append([hours, attendance, marks])

            # Illustrative rule for generating training labels
            score = (
                hours * 5
                + attendance * 0.20
                + marks * 0.50
            )
            y.append("Pass" if score >= 50 else "Fail")

return X, y
```

def main():
X, y = generate_data()

```
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)

joblib.dump(
    {
        "model": model,
        "version": MODEL_VERSION
    },
    "model.joblib"
)

print(f"Model Version: {MODEL_VERSION}")
print("Model saved to model.joblib")
```

if **name** == "**main**":
main()
