## /api/users/*id*/messages : v0 **for** a user

more useful now, we need an API endpoint to retrieve messages for a given user  
like always we will refer to the user **by its primary key**, so that is the
expected parameter in the URL

in other words, `/api/users/1/messages` will return all messages for the user with `id` 1

### a first implementation

in this first naive approach:

- we return messages **with only user ids** (i.e. without their nickname)  
- also we will only return messages where the user is the **recipient**  

this is not very useful, but again it will help us understand how to properly deal with relationships

### nothing out of the ordinary

we can use the exact same approach as for the users:

- we run a query on the `messages` table
- and we simply filter it by the `recipient_id` column

### something missing

in a practical app, we would probably need to return **BOTH** messsages that have the user as recipient **and as author**

but let's not get ahead of ourselves, we will improve all this later on
