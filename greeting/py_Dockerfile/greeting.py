from flask import Flask, jsonify
import random
import datetime
import pytz

app = Flask(__name__)

@app.route('/v1/greeting', methods=['GET'])
def generate_greeting():
    greetings = ['Welcome', 'Hello', 'Hi', 'Good to see you', 'Nice to meet you', 'How are you', 'Have a nice day', 'Enjoy your day', 'Good luck', 'Thank you', 'Guten Tag', 'Hey what\'s up', 'See you later', 'Bon appétit', 'Cheers', 'Let\'s celebrate', 'Have a great time']
    greeting = random.choice(greetings)
    
    gmt8 = pytz.timezone('Asia/Hong_Kong')
    current_time = datetime.datetime.now(gmt8).strftime('%H:%M:%S')
    
    greeting_phrase = f"{greeting}, the current time in GMT +8 is {current_time}"
    return jsonify({'greeting': greeting_phrase})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def fallback(path):
    return jsonify(message="Sorry, please use the right endpoint")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
