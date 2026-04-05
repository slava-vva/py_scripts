from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Dynamic data: can be any length or content
    headers = ["ID", "Product", "Price"]
    data = [
        {"ID": 1, "Product": "Laptop", "Price": "$999"},
        {"ID": 2, "Product": "Mouse", "Price": "$25"}
    ]
    return render_template('table.html', headers=headers, data=data)
