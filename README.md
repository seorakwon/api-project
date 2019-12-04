# api-project

**Description:** The aim of this project is to analyze `public` chat messages from different chats and create sentiment metrics
of the different people on your team. Hence, it would be possible to analyze the conversations and see if the participants are happy 😃.
 
In this project the following tools will be used:
- API (bottle)
- NLTK sentiment analysis


## Project Goals

**Main goal**: Analyze the conversations coming from a chat

- (L1🧐) Write an API in bottle just to store chat messages in a database like mongodb or mysql.
- (L2🥳) Extract sentiment from chat messages and perform a report over a whole conversation


## TODO's - API Endpoints

An API was created with the following endpoints:

### 1. User endpoints
- (POST) `/user/create` 
  - **Purpose:** Create a user and save into DB
  - **Params:** `username` the user name
  - **Returns:** `user_id`

### 2. Chat endpoints:
- (GET) `/chat/create` 
  - **Purpose:** Create a conversation to load messages
  - **Params:** An array of users ids `[user_id]`
  - **Returns:** `chat_id`
- (GET) `/chat/<chat_id>/adduser` 
  - **Purpose:** Add a user to a chat, this is optional just in case you want to add more users to a chat after it's creation.
  - **Params:** `user_id`
  - **Returns:** `chat_id`
- (POST) `/chat/<chat_id>/addmessage` 
  - **Purpose:** Add a message to the conversation. Help: Before adding the chat message to the database, check that the incoming user is part of this chat id. If not, raise an exception.
  - **Params:**
    - `chat_id`: Chat to store message
    - `user_id`: the user that writes the message
    - `text`: Message text
  - **Returns:** `message_id`
- (GET) `/chat/<chat_id>/list` 
  - **Purpose:** Get all messages from `chat_id`
  - **Returns:** json array with all messages from this `chat_id`
- (GET) `/chat/<chat_id>/sentiment` 
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat

### 3. Instructions

- @get("/"): returns all the conversations
- @get("/<username>"): returns all the conversation lines of the user
- @get("/chat/<chat_id>/list"): returns the conversation lines per chat
- @get('/chat/<chat_id>/sentiment'): returnschat sentiment per chat(you can get the sentiment per line of conversation and the compound and average
- @post('/user/create'): creates a new user
- @post('/adduser'): adds new user with message with new chat
- @post('/chat/create'): creates new chat
- @post('/chat/<idChat>/adduser'): adds user to existing chat with their their text
- @post("/chat/<chat_id>/addmessage"): add message to existing conversation

--> this is shown in the file api1.py (execute it from the terminal)


## Links - API dev in python
- [https://bottlepy.org/docs/dev/]
- [https://www.getpostman.com/]

## Links - NLP & Text Sentiment Analysis
- [https://www.nltk.org/]
- [https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386]
- [https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk]

