# Flask app (book_service/app.py)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([{"id": 1, "title": "DevOps 101", "author": "Jane Doe"}])

