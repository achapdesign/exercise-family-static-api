
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
jackson_family = FamilyStructure('Jackson')
id == member_id
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": Int > 0,
            "lucky_numbers": []
        }]
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        POST /member

        REQUEST BODY (content_type: application/json):

        {
            first_name: String,
            age: Int,
            lucky_numbers: [],
            id: Int *optional
        }

        RESPONSE (content_type: application/json):

        status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

        body: empty
        
        # fill this method and update the return
        pass

    def delete_member(self, id):
        DELETE /member/<int:member_id>

        RESPONSE (content_type: application/json):

        status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

        body: {
            done: True
        }    
        
        # fill this method and update the return
        pass

    def get_member(self, id):
        GET /member/<int:member_id>

        RESPONSE (content_type: application/json):

        status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

        body:

        {
            "id": Int,
            "first_name": String,
            "age": Int,
            "lucky_numbers": List
        }
        
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        GET /members

        status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

        RESPONSE BODY (content-type: application/json):

        [], // List of members.
        
        return self._members
