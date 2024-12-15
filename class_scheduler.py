from flask import Flask, request, jsonify, json
from flask_cors import CORS
from write_questions import write_questions

app = Flask(__name__)

CORS(app)

last_topic = None

@app.route('/schedule_class', methods=['POST'])
def schedule_class():
    global last_topic
    data = request.get_json()  
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"message": "Topic is required."}), 400  

    last_topic = topic  

    success, message = write_questions(topic)

    if not success:
        return jsonify({"message": message}), 500

    try:
        with open('questions.json', 'r') as file:
            questions_data = json.load(file)
    except Exception as e:
        return jsonify({"message": f"Error reading questions file: {str(e)}"}), 500  

    success, message = get_content(topic)

    if not success:
        return jsonify({"message": message}), 500

    try:
        with open('content.txt', 'r') as file:
            content = ' '.join([line.strip() for line in file.readlines()])
    except Exception as e:
        return jsonify({"message": f"Error reading questions file: {str(e)}"}), 500

    link = open_zoom()
    
    response_data = {
        "questions": questions_data,
        "content": content,
        "link": link
    }
    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
