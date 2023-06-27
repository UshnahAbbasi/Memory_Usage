from flask import Flask, jsonify,request
from db_connect import get_data, get_query

app = Flask(__name__)


@app.route('/usage', methods=['POST'])
def get_usage():
    
    data = request.get_json()
    print(data)
    
    
    timestamp = data.get('timestamp')
    hour = data.get('hour')
    minute = data.get('minute')
    second = data.get('second')
  
    query=get_query(timestamp, hour, minute, second)
        

    #print(query)
    data= get_data(query)
    if data == []:
        return "no data available at this time"
    else:
        
        keys = ['id', 'timestamp', 'memory_footprint', 'cpu_usage', 'hour', 'minute', 'second']
        
        result = []
        for sublist in data:
            dictionary = dict(zip(keys, sublist))
            result.append(dictionary)
            
        print(result)
            
        return jsonify(result)


if __name__ == '__main__':
    app.run(port=2910)
