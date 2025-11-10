from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for demonstration
recipes = [
    {
        'id': 1,
        'name': 'Happy Pancakes',
        'mood_tags': ['happy', 'cheerful'],
        'ingredients': ['2 cups flour', '1 cup milk', '1 egg', '1 tbsp sugar'],
        'steps': ['Mix ingredients', 'Cook on griddle until golden'],
        'images': ['https://example.com/happy_pancakes.jpg']
    },
    {
        'id': 2,
        'name': 'Comfort Soup',
        'mood_tags': ['sad', 'comforting'],
        'ingredients': ['1 cup chicken broth', 'Vegetables', 'Salt and pepper'],
        'steps': ['Boil broth', 'Add vegetables', 'Simmer until cooked'],
        'images': ['https://example.com/comfort_soup.jpg']
    }
]

moods = ['happy', 'sad', 'cheerful', 'comforting']

@app.route('/moods', methods=['GET'])
def get_moods():
    return jsonify(moods)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    mood_filter = request.args.get('mood')
    if mood_filter:
        filtered = [r for r in recipes if mood_filter in r['mood_tags']]
        return jsonify(filtered)
    return jsonify(recipes)

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            return jsonify(recipe)
    return jsonify({'error': 'Recipe not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
