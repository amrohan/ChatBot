import re


def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response)
    return [score, response]


def get_response(message):
    # Add your custom responses here
    response_list = [
        process_message(message, ['hello', 'hi', 'hey','sup'], 'Hello there, your AI companion is here to serve you.\nYou can talk normally or Type (cmd) to get started '),
        
        process_message(message, ['bye', 'goodbye'], 'Please don\'t go!'),
        process_message(message, ['cmd', 'type cmd'], 'click me /help'),
        
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        #new
        process_message(message, ['how', 'you', 'created'], 'I was created by using python and got deployed on server Herkou'),
        
        #Name
        process_message(message, ['your', 'name'], 'My name is Rohan\'s Bot, nice to meet you!'), 
        #Help
        process_message(message, ['help', 'please'], 'I will do my best to assist you!'),
        #Website
        process_message(message, ['link','links',], 'website https://rohan.ml'),
        
        #Song
        process_message(message, ['play','song',], 'https://youtu.be/edzt82nC45k'),
        
        #Notes
        process_message(message, ['notes','note',], 'Soon, notes will be available'),
        
        #Nude Joke Lol
        process_message(message, ['nude','nudes',], 'I just took a screenshot, and I\'m sending your photo to @amrohan right now, you lil horny ass😏'),
                
        #When Querry
        process_message(message, ['when','?','query','question','inform','developer'], 'Inquire with the developer about this. @amrohan'),
            
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response