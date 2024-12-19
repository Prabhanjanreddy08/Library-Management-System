A. Create a Member (POST)
        Method: POST
        URL: http://127.0.0.1:5000/members
        Headers:
        Key: Authorization, Value: Bearer library123
        Key: Content-Type, Value: application/json
        Body:
        Go to the Body tab in Postman.
        Select raw and then JSON from the dropdown.
        Enter the following JSON data to create a new member:

        {
            "name": "John Doe"
        }
 Click Send to make the request.
        Response (Expected):

        {
            "message": "Member added successfully",
            "member": {
                "id": 1,
                "name": "John Doe"
            }
        }

B. Get All Members (GET)
        Method: GET
        URL: http://127.0.0.1:5000/members
        Headers:
        Key: Authorization, Value: Bearer library123
        Click Send to make the request.
        Response (Expected):
        
        [
            {
                "id": 1,
                "name": "John Doe"
            },
            {
                "id": 2,
                "name": "Jane Smith"
            }
        ]

C. Get a Single Member by ID (GET)
        Method: GET
        URL: http://127.0.0.1:5000/members/1 (Replace 1 with the ID of the member you want to retrieve)
        Headers:
        Key: Authorization, Value: Bearer library123
        Click Send to make the request.
        Response (Expected):

        {
            "id": 1,
            "name": "John Doe"
        }

D. Update a Member (PUT)
        Method: PUT
        URL: http://127.0.0.1:5000/members/1 (Replace 1 with the ID of the member you want to update)
        Headers:
        Key: Authorization, Value: Bearer library123
        Key: Content-Type, Value: application/json
        Body:
        Go to the Body tab in Postman.
        Select raw and then JSON from the dropdown.
        Enter the following JSON data to update the member:

        {
            "name": "John Smith"
        }

 Click Send to make the request.
        Response (Expected):

        {
            "message": "Member updated successfully",
            "member": {
                "id": 1,
                "name": "John Smith"
            }
        }

E. Delete a Member (DELETE)
        Method: DELETE
        URL: http://127.0.0.1:5000/members/1 (Replace 1 with the ID of the member you want to delete)
        Headers:
        Key: Authorization, Value: Bearer library123
        
 Click Send to make the request.
        Response (Expected):
        
        {
            "message": "Member deleted successfully"
        }
