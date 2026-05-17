from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User
from billing import create_checkout_session
from crawler import crawl_url, crawl_domain
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "instance", "site.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

PLAN_OPTIONS = [
    {
        'name': 'free',
        'label': 'Free',
        'price_id': os.getenv('STRIPE_PRICE_FREE', 'price_1TYBz7Cj4JvUQsAzcWExOFDM'),
    },
    {
        'name': 'premium',
        'label': 'Premium',
        'price_id': os.getenv('STRIPE_PRICE_PREMIUM', 'price_1TYBz7Cj4JvUQsAz653JSI46'),
    },
]
PLAN_BY_PRICE_ID = {plan['price_id']: plan for plan in PLAN_OPTIONS}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/imprint')
def imprint():
    return render_template('imprint.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('profile'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('landing'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user, plans=PLAN_OPTIONS)

@app.route('/subscribe', methods=['POST'])
@login_required
def subscribe():
    plan = request.form.get('plan')
    print(f"Selected plan: {plan}")
    selected_plan = PLAN_BY_PRICE_ID.get(plan)
    if not selected_plan:
        return redirect(url_for('profile'))
    session['selected_plan'] = selected_plan['name']
    checkout_url = create_checkout_session(current_user, plan)
    return redirect(checkout_url)

@app.route('/success')
@login_required
def success():
    selected_plan = session.pop('selected_plan', 'free')
    if selected_plan == 'premium':
        current_user.subscription_plan = 'premium'
        current_user.crawls_remaining = 100
    else:
        current_user.subscription_plan = 'free'
        current_user.crawls_remaining = 10
    db.session.commit()
    return render_template('success.html')

@app.route('/cancel')
@login_required
def cancel():
    session.pop('selected_plan', None)
    return render_template('cancel.html')

@app.route('/crawl', methods=['POST'])
@login_required
def crawl():
    if current_user.crawls_remaining <= 0:
        return jsonify({"error": "No crawls remaining"}), 403
    url = request.form.get('url')
    version = request.form.get('version')
    
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    if version == 'v1':
        external_links = crawl_url(url)
    elif version == 'v2':
        external_links = crawl_domain(url)
    else:
        return jsonify({"error": "Invalid version"}), 400
    
    current_user.crawls_remaining -= 1
    db.session.commit()
    
    return jsonify({"links": external_links})

@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return redirect(url_for('landing'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
