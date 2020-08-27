from flask import Flask, render_template, request
import packages
app = Flask(__name__)
mode = packages.mode #whether just conda or (conda and pip)
env = None
@app.route('/')
def index():
    if mode:
        options={'pip','conda'}
    else:
        options={'pip'}
    return render_template('index.html',lent = len(options),options = options)

@app.route('/list',methods=['POST'])
def cards():
    #print('#########',request.form.get("name"))
    env = request.form.get("name")
    if env  == 'pip':
        data = packages.pip_pack()
        #print('##########',len(data[0]))
    elif env == 'conda':
        data = packages.conda_pack()
    return render_template('index.html',data = data[0])

@app.route('/info',methods=['POST'])
#This is very ugly!
def info():
    name = tuple(request.form.keys())[0]
    test = packages.get_info(env,name)
    return test
    #return render_template('info.html')

if __name__=='__main__':
    app.run(debug=True)