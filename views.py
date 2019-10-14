from flask import *
from data import *

app = Flask(__name__)


@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/userinfo/')
def userinfo():
    dataget = Getcalender()
    datelst = dataget.getlst()
    print(datelst)

    return render_template('userinfo.html',**locals())





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=22222,debug=True)