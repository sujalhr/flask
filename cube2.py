from flask import Flask, request, jsonify

# Create a Flask app
app = Flask(__name__)

# Define a route for calculating the cube of a number
@app.route('/cube', methods=['GET'])
def calculate_cube():
    # Extract the 'number' from the query parameters (?number=3)
    number = request.args.get('number', type=int)
    
    # If no number is provided, return an error response
    if number is None:
        return jsonify({"error": "No number provided"}), 400
    
    # Calculate the cube of the number
    #cube_value = number ** 3
    
    # Return the result as a JSON response
    return jsonify({
        "number": number,
        "cube": number ** 3
    })

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
