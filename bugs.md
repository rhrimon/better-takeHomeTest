# BUGS
1. When user sends a message by clicking the send button the character counter does not automatically reset to 140, instead only resetting when user types something new into the message field.
This issue is not present when user sends message by pressing Enter.

2. "what's happening" text in message field not properly capitalized.

3. Hardcoded messages in data.json file can easily surpass 140 characters, manipulation of data possible

# USABILITY
1. Upon hovering over any message, the entire message is obstructed by the "Last Active" text. This prevents user from seeing the message and also clicking any potential links (ie. the cornwall.jpg link sent by @baratunde). "Last Active" text should not obstruct message and would perhaps be better positioned as a small text hover above/under message or showing on some sort of profile page when user avatar is clicked.

2. "data.json" file has a "verified" boolean yet user verified status is not reflected in app.

3. No ability to copy or paste sent messages.

4. No ability to create line breaks in messages, leading to long messages being cut off at smaller window sizes.

# TEST GAPS
While the current test checks if the App component renders, it does not check for the nested components. The tests also do not list Watchman as a dependancy. I've included some Javascript tests to check for the rendering of the nested components, along with positive and negative tests using Selenium and Python to check for standard HTTP response status codes. 

# MANUAL TESTS   
### PERFORMED
1. Manual entry of message, sending by pressing Enter
2. Manual entry of message, sending by clicking Send button
3. Hovering over message field to verify hover message
4. Manual test of character limit for message field 
5. Manually attempting to copy message
6. Manually attempting to paste message
7. Manual check of all spelling and grammar 
8. Manual check of all interactive elements 
9. Manual check of resizing window 

### WOULD LIKE TO PERFORM
1. Test Login functionality and logging in manually
2. Test Logout functionality and logging out manually

# FAILED TESTS
### The following tests are currently failing. While they most likely would not fail in a real world app, I've left them in as a showcase of features I would like to test. Please find more detailed explanations below.
1. `test_message_more_than_140_chars` 
   * The purpose of this test is to send a POST request including a message that is over 140 characters. The expected result is a 400 error; however a 200 is returned, likely because there is currently no validation on the /posts POST method 
2. `test_post_400`
   * The purpose of this test is to send an invalid post request to verify that the proper error code is returned. The expected result is a 400 error; however a 200 is returned, likely because there is currently no validation on the /posts POST method

# CLOSING THOUGHTS
  Overall the exercise was enjoyable to complete. One difficulty I ran into was the requirement of Watchman being installed on your system. Running npm test without Watchman installed would return the following error: `Error: fsevents unavailable (this watcher can only be used on Darwin)`. This error was fixed after using brew to install Watchman, but seeing as it cannot be installed as a project dependency it may cause potential usability issues for others attempting to run similar tests. Other errors such as failing tests were easily traced and remedied. It would also be helpful if I would receive some kind of response back when an invalid POST request is sent. 