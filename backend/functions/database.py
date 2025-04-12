import os
import json
import random

# save messages from retrieval later on
def get_recent_messages():

    # define the file name
    file_name = "stored_data.json"
    learn_instruction = {"role": "system",
                         "content": "You are a customer service agent at Raiffeisen bank. The website to get bank products is https://www.raiffeisen.ch/rch/de.html or https://www.raiffeisen.ch/rch/de/ueber-uns/raiffeisen-group-for-investors/our-services.html. "
    "You are extremely knowledgeable to conduct customer feedback. You understand that asking the right questions is "
    "the key to getting insightful and actionable answers from your surveys and polls. Success depends on recommending "
    "bank products and services, using neutral answer options, ensuring that your surveys have a balanced set of answer "
    "options. You avoid asking for two things at once, using a diverse set of questions. Ask questions more relevant to "
    "the conversation. You go by the name Raif. Answer in Swiss German and then translate in English. Keep your answers concise."}

    # initialize messages
    messages = []

    # add random element
    x = random.uniform(0, 1)
    if x < 0.2:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will have some sense of empathy if the customer is angry. "
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include an interesting new fact about Switzerland to make customers happy. "

    # Append instruction to message
    messages.append(learn_instruction)

    # get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # append last 5 rows of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except:
        pass

    #return messages
    return messages


# save messages for retrieval later on
def store_messages(request_message, response_message):

    # define the file name
    file_name = "stored_data.json"

    # get recent messages
    messages = get_recent_messages()[1:]

    # add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # sae the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


# save messages to json file
def reset_messages():

    file_name = "stored_data.json"

    # write an empty file
    open(file_name, "w")

# to api
#def message_to_api():

#    file_name = "stored_data.json"

#    f = open(file_name)
#    data = json.loads(f)
#    print(data)