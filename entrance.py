from flask import Flask,request,jsonify,make_response
import traceback
import getPointData,getPeriodData

app = Flask(__name__)

@app.route('/kjkj', methods=['GET'])
def data():
    try:
        #获取推理机来取数据时带着的token
        Authorization = request.headers.get('Authorization')
        #print(Authorization)
        return getPointData.getData(Authorization)
    except:
        app.logger.error(traceback.format_exc())

@app.route('/asdf', methods=['POST'])
def date():
    try:
        return getPeriodData.getDate()
    except:
        app.logger.error(traceback.format_exc())

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
