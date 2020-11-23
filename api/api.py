import time
import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    # No need to jsonify the return because Flask does it for us
    return {'time.time()': time.time(),
            'datetime.date.today()': datetime.date.today(),
            'datetime.datetime.utcnow()': datetime.datetime.utcnow(),
            'datetime.date.fromtimestamp(time.time())': datetime.date.fromtimestamp(time.time())}