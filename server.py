from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "hello_key"
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    session['strawberry'] = request.form['strawberry']
    session['blackberry'] = request.form['blackberry']
    session['blackberry'] = request.form['blackberry']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    rasp_val = int(session['raspberry'])
    straw_val = int(session['strawberry'])
    blackberry_val = int(session['blackberry'])
    apple_val = int(session['apple'])
    passed_value= straw_val + rasp_val + apple_val + blackberry_val
    real_name= session['first_name'] +session['last_name'] 
    print('charging ' + real_name + str(passed_value) )
    return render_template("checkout.html")


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    