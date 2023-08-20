from flask import Flask, request, jsonify


app = Flask(__name__)


# Create (POST) operation
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()  
    
    return jsonify(data), 201

# Run the Flask app
if __name__ == '__main__':    
    app.run(debug = True)
