from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__, static_url_path='/static', static_folder='static')
client = OpenAI(api_key="sk-proj-57Lz8gVquVhrbQ23EIDnT3BlbkFJvQ8vpdll2NZmFB7PjP4x")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-script', methods=['POST'])
def generate_script():
    video_idea = request.form.get('video_idea')
    if not video_idea:
        return jsonify({'error': 'Video idea is required'}), 400

    user_prompt = f'As an expert content creator, please generate an idea for a short form video that is both intriguing and has the chance to go viral. This is the idea: {video_idea}. Please give your response in 5 portions: 1. The flow of the video 2. the script for all dialogue 3. Key elements to make the video stand out 4. a caption for the video 5. any hastags or keywords'
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    script = chat_completion.choices[0].message.content
    return jsonify({'script': script})

if __name__ == '__main__':
    app.run(debug=True)
