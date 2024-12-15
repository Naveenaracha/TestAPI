from flask import Flask, request, jsonify, json
from flask_cors import CORS
import os
from write_questions import write_questions

app = Flask(__name__)

CORS(app)

last_topic = None

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/schedule_class', methods=['POST'])
def schedule_class():
    global last_topic
    data = request.get_json()  
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"message": "Topic is required."}), 400  
    success, message = write_questions(topic)
    if not success:
        return jsonify({"message": f"Something went wrong"}), 500  
    last_topic = topic  
    try:
        with open('questions.json', 'r') as file:
            questions_data = json.load(file)
    except Exception as e:
        return jsonify({"message": f"Error reading questions file: {str(e)}"}), 500  

    response_data = {
        "questions": questions_data,
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port, debug=True)
