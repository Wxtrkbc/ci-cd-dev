from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/values/<key>')
def get_value(key):

    value = cache.get(key)
    if value is None:
        value = "default"
        cache.set(key, value)
    else:
        value = str(value) + "1"

    return jsonify({key: value})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
