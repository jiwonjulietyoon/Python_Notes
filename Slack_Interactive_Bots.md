# Interactive Slack Bots with Python and Flask



##### NOTES

- Setting up
  - Slack Bot & tokens => environment variables
    - enable interactivity, add event subscriptions
  - Ngrok to run python app.py
- Overall flow
  - No interactivity
    1. bot is mentioned in channel
    2. bot answers in the same channel
  - With interactivity
    1. bot is mentioned in channel
    2. bot answers and offers buttons/dropdown list for user to choose from
    3. user selects an option
    4. bot gives follow-up answer according to selected option