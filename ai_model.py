from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

def generate_fake_data():
    X = np.random.rand(200, 3)  # features: entropy, size, protocol
    y = np.random.randint(0, 2, 200)  # 0: benign, 1: malicious
    return X, y

def train_and_save_model():
    X, y = generate_fake_data()
    model = RandomForestClassifier(n_estimators=50)
    model.fit(X, y)
    joblib.dump(model, "packet_model.pkl")
    print("[+] Model trained and saved as packet_model.pkl")

if __name__ == "__main__":
    train_and_save_model()
