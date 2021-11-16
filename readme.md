Installation guide:
1. pip install -r requirements.txt
2. cd test_task
3. make start

API Guide:
Actions requiring authentification:
1) Creating, updating, deleting Polls;
2) Creating, updating, deleting Questions;
3) Getting the list of answers by the User.

1. Authentication:
   (for actions requiring authentication)
POST request to /login/ with json body:
   {"username":"admin", "password": "admin"}.
   The response will provide you with neccessary cookies
   and csrf token. You should additionally specify your request header
   X-CSRFToken with the data in Cookies "csrftoken" field.
   
2. Polls:
Schema for POST-requests looks like this:
   {"name": ..., "start_date": ..., "end_date": ..., "description": ...}
1) Getting the polls list:
GET request to /polls/
2) Getting the poll by its ID:
GET request to /polls/id
3) Creating new poll:
POST request to /polls/. All the model fields are optional, but you can specify
   them accordingly to the schema above.
   All date fields are JSON-formatted DateTime objects.
4) Updating a poll:
POST request to /polls/id. You should specify fields you need to update.
5) Deleting a poll:
DELETE request to /polls/id.
3. Questions:
Schema for POST-requests looks like this:
   {"text": ..., "choice_type": ..., "poll": ...}. Text is CharField with max_length of 255 characters.
   Choice_type is one of three: "open", "single", "multiple". Poll is the ID of the poll the question is connected to.
    All the API entrypoints are the same with the Poll's, url is /questions/ and /questions/id accordingly.
4. Answers:
GET request to /answers/id. Here you will need an Id of the RespondentUser entry, to get the list of its answers.
   <br>
<b>-- User functionality: (does not require any authorization)</b>
5. Get the list of the polls available:
   GET request to /active-polls/ will return you the list of all polls with end_date which did not come yet.
6. Answering the question:
POST request to /leave-an-answer/ with the body:
   {"question":..., "answer_text": ...}. Where question is the id of the question entry.
   <br>If user did not commit to any polls before, RespondentUser entry will be created automatically.
   It will be tied with cookies of unauthorized user or with username of authorized.