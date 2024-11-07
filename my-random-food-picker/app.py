from flask import Flask, jsonify, request
app = Flask(__name__)

# Route to get the random food choice
@app.route('/choose_food', methods=['POST'])
def choose_food():
      # Get the list of foods from the POST request body
      data = request.get_json()
      if not data or 'foods' not in data:
            return jsonify({"error": "No food list provided"}), 400
      
      foods = data['foods']
      if len(foods) == 0:
         return jsonify({"error": "Food list cannot be empty"}), 400
      
      # Randomly choose a food item from the list
      chosen_food = random.choice(foods)

      return jsonify({"chosen_food": chosen_food})
if __name__ == "__main__":
   app.run(debug=True)