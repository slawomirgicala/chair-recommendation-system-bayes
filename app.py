from flask import Flask, flash, redirect, render_template, request, url_for

from bayes import model_probabilites
from database import customers

CATEGORIES = ['ergonomic', 'baby_chair', 'leasing', 'residence']

FIELDS = [
        'earnings',
        'sedentary',
        'weightlifting',
        'yoga',
        'cardio',
        'sex',
        'married',
        'age',
        'traveller',
    ]

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

        for f in FIELDS:
            if f in request.form:
                ergonomic_evidence[f] = request.form[f]

        results = {}

        for c in CATEGORIES:
            results[c] = model_probabilites(ergonomic_evidence, [c])

        if not name:
            flash('Name is required!')
        else:
            ergonomic_evidence['id'] = customer_id
            ergonomic_evidence['name'] = name

            for c in CATEGORIES:
                ergonomic_evidence[c] = results[c][c]
            
            customers[customer_id] = ergonomic_evidence
            
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
