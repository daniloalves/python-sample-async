from multiprocessing import Process

from time import sleep
from flask import Flask, jsonify
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['DEBUG'] = True

## Example to call:
# curl http://localhost:5000/main

@app.route('/main')
def index():
    process = Process(target=mock_answer, args=(3,), daemon=True)
    process.start()
    return jsonify({'status_code': 200, 'message': 'Your request received and in proccess..'})


def mock_answer(time=5):
    sleep(time)
    app.logger.debug(f"Finished your process in {time} seconds!")
    return 'ok'


app.run()
