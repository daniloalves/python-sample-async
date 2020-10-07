import threading
from time import sleep
from flask import Flask, jsonify
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['DEBUG'] = True

## Example to call:
# curl http://localhost:5000/main

@app.route('/main')
def main():
    t1 = threading.Thread(target=mock_answer, args=(5,))

    t1.start()
    # t1.join()
    
    return jsonify({'status_code': 200, 'message': 'Your request received and in proccess..'})

def mock_answer(time=5):
    sleep(time)
    app.logger.debug(f"Finished your process in {time} seconds!")

app.run()