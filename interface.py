# Let's import all the necessary libraries and modules
from flask import Flask,render_template,jsonify,request
from Project_app.utils import Boston_House
import os





app = Flask(__name__)
#  __name__ represents name of the application package and used by Flask to identify 
# resources like templates,static assets and their instance folder

# PicFolder = os.path.join('static','images')
# app.config['UPLOAD_FOLDER'] = PicFolder

# BASE API  
@app.route('/')
def Home():
    # pic_boston = os.path.join(app.config['UPLOAD_FOLDER'],'Boston_House1.png')
    print('This is Home API***************')
    # return render_template('index.html',user_image = pic_boston)
    return render_template('index.html')

# SUBMIT API
@app.route('/submit',methods = ['POST','GET'])
def Submit():
    print('THIS IS SUBMIT API*************')

    if request.method == 'POST':

        CRIM  = float(request.form['CRIM'])
        ZN    = float(request.form['ZN'])
        INDUS = float(request.form['INDUS'])
        CHAS  = float(request.form['CHAS'])
        NOX   = float(request.form['NOX'])
        RM    = float(request.form['RM'])
        AGE   = float(request.form['AGE'])
        DIS   = float(request.form['DIS'])
        RAD   = float(request.form['DIS'])
        TAX   =float(request.form['TAX'])
        PTRATIO=float(request.form['PTRATIO'])
        B     = float(request.form['B'])
        LSTAT = float(request.form['LSTAT'])
    
    bs = Boston_House(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    price = bs.Get_Price()
    
    return render_template('result.html',result = price)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1122)


