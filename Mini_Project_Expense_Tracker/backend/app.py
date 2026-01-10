from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize App
app = Flask(__name__, 
            template_folder='../frontend/templates', 
            static_folder='../frontend/static')

# Configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database
db = SQLAlchemy(app)

# --- Models (The Schema) ---
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "date": self.date.strftime('%Y-%m-%d')
        }

# Create DB Tables
with app.app_context():
    db.create_all()

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')

# API: Get All Expenses
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return jsonify([e.to_dict() for e in expenses])

# API: Add Expense
@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.json
    
    # Basic Validation
    if not data or 'title' not in data or 'amount' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    new_expense = Expense(
        title=data['title'],
        amount=float(data['amount']),
        category=data.get('category', 'Other')
    )
    
    try:
        db.session.add(new_expense)
        db.session.commit()
        return jsonify(new_expense.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API: Delete Expense
@app.route('/api/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    try:
        db.session.delete(expense)
        db.session.commit()
        return jsonify({"message": "Deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API: Get Summary (For Charts)
@app.route('/api/summary', methods=['GET'])
def get_summary():
    # Group by category using SQL Alchemy
    summary = db.session.query(
        Expense.category, db.func.sum(Expense.amount)
    ).group_by(Expense.category).all()
    
    data = {category: amount for category, amount in summary}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)