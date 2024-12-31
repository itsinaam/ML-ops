import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Set MLflow tracking URI to your remote server or the MLflow server
mlflow.set_tracking_uri("http://ec2-13-48-136-237.eu-north-1.compute.amazonaws.com:5000")  # Replace with your MLflow server URL
mlflow.set_experiment("Iris_Classification_Experiment")

# Load dataset and split into train and test
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Start MLflow run to log the experiment
with mlflow.start_run():
    # Train a RandomForest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Log model parameters, metrics, and model itself
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("random_state", 42)
    mlflow.log_metric("accuracy", accuracy)
    
    # Log the trained model
    mlflow.sklearn.log_model(model, "model")
    
    # Optionally, log any other artifacts (e.g., plots, files) if needed
    # mlflow.log_artifact("path/to/file")
    
    print(f"Model logged with accuracy: {accuracy}")

# The experiment and model will be saved on the remote MLflow server.
