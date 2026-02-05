from flask import Flask, jsonify, render_template

# import osmnx as ox
# import matplotlib.pyplot as plt 

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
