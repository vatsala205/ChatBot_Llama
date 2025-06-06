from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    prompt = f"You are a helpful assistant for the trust Airtel app. Provide clear and concise answers to users about network coverage, availability, in-app functionality, and any related queries.\nUser: {user_message}\nAI:"

    try:
        process = subprocess.Popen(
            ['ollama', 'run', 'llama3'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output, error = process.communicate(prompt, timeout=30)

        if error:
            print("Ollama error:", error)
            reply = "Sorry, something went wrong with the model."
        else:
            reply = output.strip().split('\n')[-1]  # Take the last line as response

    except Exception as e:
        print("Exception:", e)
        reply = "Sorry, I ran into a problem. Please try again."

    return jsonify({'reply': reply})


if __name__ == '__main__':
    app.run(debug=True)
