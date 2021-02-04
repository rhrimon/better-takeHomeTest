# BUGS
1. When user sends a message by clicking the send button the character counter does not automatically reset to 140, instead only resetting when user types something new into the message field.
This issue is not present when user sends message by pressing Enter.

2. "what's happening" text in message field not properly capitalized.

3. Hardcoded messages in data.json file can easily surpass 140 characters, manipulation of data possible. [all tests should check if message is <=140 characters]

# USABILITY
1. Upon hovering over any message, the entire message is obstructed by the "Last Active" text. This prevents user from seeing the message and also clicking any potential links (ie. the cornwall.jpg link sent by @baratunde). "Last Active" text should not obstruct message and would perhaps be better positioned as a small text hover above/under message or showing on some sort of profile page when user avatar is clicked.

2. "data.json" file has a "verified" boolean yet user verified status is not reflected in app.

3. No ability to copy or paste sent messages.

4. No ability to create line breaks in messages, leading to long messages being cut off at smaller window sizes.

# MANUAL TESTS   
### PERFORMED
1. Manual entry of message, sending by pressing Enter
2. Manual entry of message, sending by clicking Send button
3. Hovering over message field to verify hover message
4. Manual test of character limit for message field

### WOULD LIKE TO PERFORM
1. 

# FAILED TESTS
1. 

# CLOSING THOUGHTS
- would be helpful if i would receive some responses back 