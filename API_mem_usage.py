from flask import Flask, jsonify,request
from db_connect import get_data, get_query

app = Flask(__name__)


@app.route('/usage', methods=['GET'])
def get_usage():
    timestamp = request.args.get('timestamp')

    print(timestamp)
    
    hour = request.args.get('hour')
    print(hour)

    minute = request.args.get('minute')
    print(minute)

    second = request.args.get('second')
    print(second)

    
    query=get_query(timestamp, hour, minute, second)
        

    print(query)
    data= get_data(query)
    if data == []:
        return "no data available at this time"
    else:
        return jsonify(data)


if __name__ == '__main__':
    app.run(port=2910)
