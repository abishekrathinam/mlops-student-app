import os
import joblib
from flask import Flask, request, render_template_string

app = Flask(**name**)

MODEL_PATH = os.path.join(os.path.dirname(**file**), "model.joblib")

PAGE = """

<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Student Result Predictor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f3f5fb;
            margin: 0;
            padding: 30px 15px;
        }
        .card {
            max-width: 480px;
            margin: 30px auto;
            padding: 28px;
            background: white;
            border-radius: 14px;
            box-shadow: 0 5px 24px #0001;
        }
        h1 { color: #263b72; }
        label { display: block; margin-top: 16px; }
        input {
            box-sizing: border-box;
            width: 100%;
            padding: 11px;
            margin-top: 6px;
        }
        button {
            width: 100%;
            margin-top: 22px;
            padding: 12px;
            background: #304f9c;
            color: white;
            border: 0;
            border-radius: 6px;
            cursor: pointer;
        }
        .version { color: #555; }
        .result { font-size: 22px; font-weight: bold; }
        .error { color: #b42318; }
    </style>
</head>
<body>
<div class="card">
    <h1>Student Result Predictor</h1>
    <p class="version">Model Version: {{ version }}</p>
    <p>Enter the student's details to predict Pass or Fail.</p>

```
<form method="post">
    <label>Study hours per day (0–10)</label>
    <input type="number" name="hours" min="0" max="10"
           step="0.1" required value="{{ hours }}">

    <label>Attendance percentage (0–100)</label>
    <input type="number" name="attendance" min="0" max="100"
           step="0.1" required value="{{ attendance }}">

    <label>Internal marks (0–100)</label>
    <input type="number" name="marks" min="0" max="100"
           step="0.1" required value="{{ marks }}">

    <button type="submit">Predict Result</button>
</form>

{% if result %}
  <p class="result">Prediction: {{ result }}</p>
{% endif %}
{% if error %}
  <p class="error">{{ error }}</p>
{% endif %}
<p><small>Demonstration model trained on generated sample data.</small></p>
```

</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
result = ""
error = ""
hours = "5"
attendance = "80"
marks = "60"

```
try:
    saved = joblib.load(MODEL_PATH)
    model = saved["model"]
    version = saved["version"]
except (OSError, ValueError, KeyError):
    return "Model is not ready. Please train the model first.", 503

if request.method == "POST":
    hours = request.form.get("hours", "")
    attendance = request.form.get("attendance", "")
    marks = request.form.get("marks", "")

    try:
        values = [
            float(hours),
            float(attendance),
            float(marks)
        ]

        if not all(map(lambda v: v == v and abs(v) != float("inf"), values)):
            raise ValueError

        if not (0 <= values[0] <= 10
                and 0 <= values[1] <= 100
                and 0 <= values[2] <= 100):
            error = "Please enter values within the specified ranges."
        else:
            result = str(model.predict([values])[0])

    except (ValueError, TypeError):
        error = "Enter valid numeric values in all fields."

return render_template_string(
    PAGE,
    version=version,
    result=result,
    error=error,
    hours=hours,
    attendance=attendance,
    marks=marks
)
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)
