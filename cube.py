from flask import Flask, request, jsonify

# Create the Flask application
app = Flask(__name__)

# Define the route for the cube calculation
@app.route('/cube', methods=['GET'])
def calculate_cube():
    # Get the 'number' from the query parameter (e.g., ?number=3)
    number = request.args.get('number', type=int)
    
    if number is None:
        # If 'number' is not provided, return an error response
        return jsonify({"error": "No number provided"}), 400

    # Calculate the cube
    cube_value = number ** 3
    
    # Return the result as a JSON response
    return jsonify({
        "number": number,
        "cube": cube_value
    })

# Run the Flask application locally
if __name__ == "__main__":
    app.run(debug=True)
