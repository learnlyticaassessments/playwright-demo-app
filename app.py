from urllib.parse import urlparse
from datetime import date

from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import secrets

from i18n import (
    DEFAULT_LOCALE,
    SUPPORTED_LOCALES,
    detect_locale_from_header,
    format_currency,
    format_date,
    format_number,
    normalize_locale,
    translate,
)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Mock database
users_db = {
    'testuser': {'password': 'password123', 'email': 'test@example.com', 'role': 'user'},
    'admin': {'password': 'admin123', 'email': 'admin@example.com', 'role': 'admin'}
}

products_db = [
    {'id': 1, 'name': 'Laptop Pro 15', 'price': 1299.99, 'category': 'Electronics', 'stock': 25},
    {'id': 2, 'name': 'Wireless Mouse', 'price': 29.99, 'category': 'Accessories', 'stock': 150},
    {'id': 3, 'name': 'USB-C Cable', 'price': 12.99, 'category': 'Accessories', 'stock': 200},
    {'id': 4, 'name': 'Mechanical Keyboard', 'price': 89.99, 'category': 'Accessories', 'stock': 75},
    {'id': 5, 'name': 'Monitor 27"', 'price': 349.99, 'category': 'Electronics', 'stock': 40},
    {'id': 6, 'name': 'Webcam HD', 'price': 79.99, 'category': 'Electronics', 'stock': 60},
]


def current_locale() -> str:
    return normalize_locale(session.get("locale", DEFAULT_LOCALE))


@app.before_request
def setup_locale():
    query_locale = request.args.get("lang")
    if query_locale:
        session["locale"] = normalize_locale(query_locale)
        return

    if "locale" not in session:
        session["locale"] = detect_locale_from_header(request.headers.get("Accept-Language"))


@app.context_processor
def inject_i18n():
    locale = current_locale()
    demo_date = date(2026, 2, 16)
    demo_number = 1234567.89
    demo_currency = 1299.99
    return {
        "t": lambda key, **kwargs: translate(key, locale, **kwargs),
        "current_locale": locale,
        "supported_locales": SUPPORTED_LOCALES,
        "format_number_locale": lambda value, decimals=2: format_number(value, locale, decimals),
        "format_currency_locale": lambda value: format_currency(value, locale),
        "format_date_locale": lambda value: format_date(value, locale),
        "demo_localized_date": format_date(demo_date, locale),
        "demo_localized_number": format_number(demo_number, locale),
        "demo_localized_currency": format_currency(demo_currency, locale),
    }


@app.route("/set-locale/<locale>")
def set_locale(locale):
    session["locale"] = normalize_locale(locale)
    next_path = request.args.get("next") or url_for("home")
    parsed = urlparse(next_path)
    safe_path = parsed.path if parsed.path.startswith("/") else url_for("home")
    return redirect(safe_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users_db and users_db[username]['password'] == password:
        session['user'] = username
        session['role'] = users_db[username]['role']
        return jsonify({
            'success': True,
            'message': translate("api.login.success", current_locale()),
            'role': users_db[username]['role']
        })
    
    return jsonify({
        'success': False,
        'message': translate("api.login.invalid", current_locale())
    }), 401

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if username in users_db:
        return jsonify({
            'success': False,
            'message': translate("api.register.user_exists", current_locale())
        }), 400
    
    users_db[username] = {'password': password, 'email': email, 'role': 'user'}
    return jsonify({'success': True, 'message': translate("api.register.success", current_locale())})

@app.route('/products')
def products_page():
    category = request.args.get('category', 'all')
    return render_template('products.html', category=category)

@app.route('/api/products')
def get_products():
    category = request.args.get('category', 'all')
    search = request.args.get('search', '').lower()
    
    filtered_products = products_db
    
    if category != 'all':
        filtered_products = [p for p in filtered_products if p['category'] == category]
    
    if search:
        filtered_products = [p for p in filtered_products if search in p['name'].lower()]
    
    return jsonify(filtered_products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return translate("api.product.not_found", current_locale()), 404

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

@app.route('/checkout')
def checkout_page():
    if 'user' not in session:
        return render_template('login.html')
    return render_template('checkout.html')

@app.route('/api/place-order', methods=['POST'])
def place_order():
    if 'user' not in session:
        return jsonify({
            'success': False,
            'message': translate("api.order.login_required", current_locale())
        }), 401
    
    data = request.json
    return jsonify({
        'success': True, 
        'message': translate("api.order.success", current_locale()),
        'order_id': 'ORD-12345'
    })

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return render_template('login.html')
    return render_template('dashboard.html', username=session['user'], role=session.get('role', 'user'))

@app.route('/profile')
def profile():
    if 'user' not in session:
        return render_template('login.html')
    user_data = users_db.get(session['user'], {})
    return render_template('profile.html', username=session['user'], email=user_data.get('email', ''))

@app.route('/api/update-profile', methods=['POST'])
def update_profile():
    if 'user' not in session:
        return jsonify({
            'success': False,
            'message': translate("api.profile.unauthorized", current_locale())
        }), 401
    
    data = request.json
    username = session['user']
    
    if 'email' in data:
        users_db[username]['email'] = data['email']
    
    return jsonify({'success': True, 'message': translate("api.profile.updated", current_locale())})

@app.route('/logout')
def logout():
    session.clear()
    return render_template('home.html')

@app.route('/forms')
def forms_demo():
    return render_template('forms_demo.html')

@app.route('/components')
def components_demo():
    return render_template('components_demo.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
