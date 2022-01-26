from flask import Flask, render_template, request, flash, redirect, url_for

from bayes import ergonomic_probability
from database import customers

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
customer_id = 0


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
        if 'earnings' in request.form:
            earnings = request.form['earnings']
            ergonomic_evidence['earnings'] = earnings
        sedentary = None
        if 'sedentary' in request.form:
            sedentary = request.form['sedentary']
            ergonomic_evidence['sedentary'] = sedentary
        ergonomic = ergonomic_probability(ergonomic_evidence)

        if not name:
            flash('Name is required!')
        else:
            customers[customer_id] = {
                'id': customer_id,
                'name': name,
                'earnings': earnings,
                'sedentary': sedentary,
                'ergonomic': ergonomic
            }
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
        return render_template('customer.html', customer=c)
    else:
        flash('No such customer!')
        return redirect(url_for('home'))


@app.route('/customers_by_ergonomic')
def customers_by_ergonomic():
    sorted_customers = sorted(list(customers.values()), key=lambda d: d['ergonomic'], reverse=True)
    for c in sorted_customers:
        c['probability'] = c['ergonomic']
    return render_template('customers_by_prob.html', customers=sorted_customers)


if __name__ == '__main__':
    app.run()
