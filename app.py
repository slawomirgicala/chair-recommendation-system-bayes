from flask import Flask, flash, redirect, render_template, request, url_for

from bayes import model_probabilites
from database import customers

CATEGORIES = ['ergonomic', 'baby_chair', 'leasing', 'residence']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
customer_id = len(customers)


def seed_database():
    for k,v in customers.items():
        v_c = v.copy()
        del v_c['id']
        del v_c['name']
        
        for c in CATEGORIES:
            customers[k][c] = model_probabilites(v_c, [c])[c]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/add_customer', methods=('GET', 'POST'))
def add_customer():
    global customer_id
    if request.method == 'POST':
        name = request.form['name']
        ergonomic_evidence = {}
        earnings = None
        sedentary = None
        weightlifting = None
        yoga = None
        cardio = None
        sex = None
        married = None
        if 'earnings' in request.form:
            earnings = request.form['earnings']
            ergonomic_evidence['earnings'] = earnings
        if 'sedentary' in request.form:
            sedentary = request.form['sedentary']
            ergonomic_evidence['sedentary'] = sedentary
        if 'weightlifting' in request.form:
            weightlifting = request.form['weightlifting']
            ergonomic_evidence['weightlifting'] = weightlifting
        if 'yoga' in request.form:
            yoga = request.form['yoga']
            ergonomic_evidence['yoga'] = yoga
        if 'cardio' in request.form:
            cardio = request.form['cardio']
            ergonomic_evidence['cardio'] = cardio
        if 'sex' in request.form:
            sex = request.form['sex']
            # na razie nie uzywamy tego do szacowania ergonomic, ani nie dodajemy do drzewka
            # ergonomic_evidence['sex'] = sex
        if 'married' in request.form:
            married = request.form['married']
            # na razie nie uzywamy tego do szacowania ergonomic, ani nie dodajemy do drzewka
            # ergonomic_evidence['married'] = married

        results = {}

        for c in CATEGORIES:
            results[c] = model_probabilites(ergonomic_evidence, [c])

        if not name:
            flash('Name is required!')
        else:
            customers[customer_id] = {
                'id': customer_id,
                'name': name,
                'earnings': earnings,
                'sedentary': sedentary,
                'weightlifting': weightlifting,
                'yoga': yoga,
                'sex': sex,
                'cardio': cardio,
                'married': married,
            }
            
            for c in CATEGORIES:
                customers[customer_id][c] = results[c][c]
            
            customer_id = customer_id + 1
            return redirect(url_for('home'))
    return render_template('add_form.html')


@app.route('/all_customers')
def all_customers():
    return render_template('customers.html', customers=list(customers.values()))


@app.route('/customer/<int:c_id>')
def customer(c_id):
    if c_id in customers:
        c = customers[c_id]
        return render_template('customer.html', customer=c, probs=CATEGORIES)
    else:
        flash('No such customer!')
        return redirect(url_for('home'))


@app.route('/ergonomic')
def ergonomic():
    customers_prob = []
  
    for c in customers.values():
        prob = {
            'id': c['id'],
            'name': c['name'],
            'probability':  c['ergonomic']
        }

        customers_prob.append(prob)
        
    return render_template('customers_by_prob.html', customers=customers_prob)


@app.route('/leasing')
def leasing():
    customers_prob = []
  
    for c in customers.values():
        prob = {
            'id': c['id'],
            'name': c['name'],
            'probability':  c['leasing']
        }
        customers_prob.append(prob)
    
    return render_template('customers_by_prob.html', customers=customers_prob)


@app.route('/babychair')
def babychair():
    customers_prob = []
  
    for c in customers.values():
        prob = {
            'id': c['id'],
            'name': c['name'],
            'probability':  c['baby_chair']
        }

        customers_prob.append(prob)

    return render_template('customers_by_prob.html', customers=customers_prob)


@app.route('/residence')
def residence():
    customers_prob = []
  
    for c in customers.values():
        prob = {
            'id': c['id'],
            'name': c['name'],
            'probability':  c['residence']
        }

        customers_prob.append(prob)
    return render_template('customers_by_prob.html', customers=customers_prob)


if __name__ == '__main__':
    seed_database()
    app.run()
