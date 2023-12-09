import mlflow
import pickle
import os

test = {"a":1,"b":2}

with open("test.pickle","wb") as f:
    pickle.dump(test,f)

os.environ["AWS_ACCESS_KEY_ID"] = "AWS_ACCESS_KEY_ID"
os.environ["AWS_SECRET_ACCESS_KEY"] = "AWS_SECRET_ACCESS_KEY"

tracking_uri =  "s3://creditcard-fraud-detection/artifacts/"
experiment_name = "testing-mlflow-s3"
artifact_uri= "s3://creditcard-fraud-detection/artifacts/"

# mlflow.set_tracking_uri(tracking_uri)
mlflow.create_experiment(experiment_name, artifact_location=artifact_uri)
mlflow.set_experiment(experiment_name)

with mlflow.start_run() as run:
    # mlflow.log_param("test1", 0)
    # mlflow.log_metric("test2", 1)

    mlflow.log_artifact("test.pickle")
    mlflow.end_run()