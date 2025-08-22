import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# -------------------------
# Function to extract features from URL
# -------------------------
def extract_features(url):
    return {
        "url_length": len(url),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        "has_https": 1 if "https" in url else 0,
        "has_at_symbol": 1 if "@" in url else 0,
        "num_digits": sum(c.isdigit() for c in url)
    }

# -------------------------
# Load dataset (you need phishing_site_urls.csv)
# -------------------------
data = pd.read_csv("phishing_site_urls.csv")  # must have 'url' and 'label' columns
X = pd.DataFrame([extract_features(u) for u in data["url"]])
y = data["label"]

# -------------------------
# Train model
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("✅ Model trained. Ready to detect phishing URLs!")

# -------------------------
# User input loop
# -------------------------
while True:
    url = input("\nEnter a URL to check (or type 'exit' to quit): ")
    if url.lower() == "exit":
        break

    features = pd.DataFrame([extract_features(url)])
    result = model.predict(features)[0]

    if result == 1:
        print("⚠ ALERT: This looks like a PHISHING site!")
    else:
        print("✅ This looks like a LEGITIMATE site.")