from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("test.html")


@app.route('/getValues', methods=['POST','GET'])
def getValues():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Username : ",username)
        print(f"Email : ",email)
        print(f"Password : ",password)
        
    return redirect(url_for('hello'))
    
    #return render_template("index.html")

if __name__ == '__main__':
    app.run()
    