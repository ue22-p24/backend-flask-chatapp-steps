## also display newly created message

### the messages page displays the message it just sent

upon successful creation of a message, the API returns the message details so,
we can use that to display the message in the frontend

in the mix, we can also take care of any error that may occur, and inform the
user (actually in this rustic app we just log in the console)

we just need to extend the JS script to handle the response from the API; for
that
- we improve on the sequence of `.then()` calls
- if the response is a success, we create a new row in the messages table
- and if not we use a `.catch()` to log the error in the console
