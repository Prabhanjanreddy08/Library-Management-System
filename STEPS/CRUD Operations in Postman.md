A. Create a Book (POST)
        Method: POST
        URL: http://127.0.0.1:5000/books
        Headers:
        
        Key: Authorization, Value: Bearer library123
        Key: Content-Type, Value: application/json
Body:
        Go to the Body tab in Postman.
        Select raw and then JSON from the dropdown.
        Enter the following JSON data in the body to create a new book:

        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald"
        }
        
Click Send to make the request.
Response (Expected):

        {
            "message": "Book added successfully",
            "book": {
                "id": 1,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald"
            }
        }

B. Get All Books (GET)
        Method: GET
        URL: http://127.0.0.1:5000/books
        Headers:
        
        Key: Authorization, Value: Bearer library123
        
Click Send to make the request.
Response (Expected):
        
        [
            {
                "id": 1,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald"
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell"
            }
        ]

C. Get a Single Book by ID (GET)
        Method: GET
        URL: http://127.0.0.1:5000/books/1 (Replace 1 with the ID of the book you want to retrieve)
        Headers:
        
        Key: Authorization, Value: Bearer library123
        
 Click Send to make the request.
Response (Expected):
        

        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald"
        }

D. Update a Book (PUT)
        Method: PUT
        URL: http://127.0.0.1:5000/books/1 (Replace 1 with the ID of the book you want to update)
        Headers:
        
        Key: Authorization, Value: Bearer library123
        Key: Content-Type, Value: application/json
Body:
        Go to the Body tab in Postman.
        Select raw and then JSON from the dropdown.
        Enter the following JSON data to update the book: 

        {
            "title": "The Great Gatsby - Updated",
            "author": "F. Scott Fitzgerald"
        }

 Click Send to make the request.
        Response (Expected):
        
        {
            "message": "Book updated successfully",
            "book": {
                "id": 1,
                "title": "The Great Gatsby - Updated",
                "author": "F. Scott Fitzgerald"
            }
        }

E. Delete a Book (DELETE)
        Method: DELETE
        URL: http://127.0.0.1:5000/books/1 (Replace 1 with the ID of the book you want to delete)
        Headers:
        
        Key: Authorization, Value: Bearer library123
 Click Send to make the request.
        Response (Expected):
        
        {
            "message": "Book deleted successfully"
        }
