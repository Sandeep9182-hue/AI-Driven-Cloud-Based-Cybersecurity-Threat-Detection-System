import json
import joblib

model = joblib.load("/var/task/model.pkl")

def lambda_handler(event, context):
    data = json.loads(event["body"])
    prediction = model.predict([[data["login_attempts"], data["failed_attempts"]]])
    result = "Threat Detected!" if prediction[0] == 1 else "No Threat"
    
    return {"statusCode": 200, "body": json.dumps({"message": result})}
