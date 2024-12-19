
1. Check Flask Server is Running
Ensure the Flask server is running on your local machine. Run the following command in the terminal:
        python app.py
You should see output like:
        Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. Verify the Endpoint URL
        Use the exact endpoint paths defined in your Flask app. 
        For example:
        To retrieve all books: http://127.0.0.1:5000/books
        To add a new book: http://127.0.0.1:5000/books
        To retrieve all members: http://127.0.0.1:5000/members
        Ensure there are no typos in the URL or method mismatch (e.g., POST for a GET endpoint)
