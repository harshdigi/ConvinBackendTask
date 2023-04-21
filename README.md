<<<<<<< HEAD
# ConvinBackendTask
=======
Task -> 
Please read carefully.
● You need to submit the assignment within 48 hours of receiving it.
● The assignment needs to be submitted on techhr@convin.ai
● In the mail kindly mention “Backend Fresher Task”
● Also send your resume & portfolio along with the assignment.
● We will revert back with the result within 15-20 days.
● Any sort of further communication can be done over the above mentioned
mail.
● Kindly revert back with the doubts and queries(if any) on techhr@convin.ai
Problem: In this assignment you have to implement google calendar
integration using django rest api. You need to use the OAuth2 mechanism to
get users calendar access. Below are detail of API endpoint and
corresponding views which you need to implement
/rest/v1/calendar/init/ -> GoogleCalendarInitView()
This view should start step 1 of the OAuth. Which will prompt user for
his/her credentials
/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()
This view will do two things
1. Handle redirect request sent by google with code for token. You
need to implement mechanism to get access_token from given
code
2. Once got the access_token get list of events in users calendar
You need to write the code in Django. You are not supposed to use any
existing third-party library other then google’s provided standard libraries
The submission should be shared as a public repl.it environment & also as a Github repo
(we need both - you can use repl.it’s ‘Version Control’ feature to sync to github)
Looking forward to your submission. Have a great day
Thank You


Steps to run this project ->

Add Credentails.json file after creat OAuth Client Credentials using Google Developer Console 
reference -> https://developers.google.com/identity/protocols/oauth2/web-server

Install Requirments using ->
pip install - r requriments.txt
>>>>>>> b490e811a4230809ff1ae61997ae66a32f1c0d88
