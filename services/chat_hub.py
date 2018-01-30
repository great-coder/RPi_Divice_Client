__author__ = 'Mohammad Dehghan'

from requests import Session
from signalr import Connection


# create new chat message handler
def print_received_message(data):
    print('received: ', data)


# create new chat topic handler
def print_topic(topic, user):
    print('topic: ', topic, user)


# create error handler
def print_error(error):
    print('error: ', error)


with Session() as session:
    # create a connection
    connection = Connection("http://localhost:51130/chat", session)

    # get chat hub
    chat = connection.register_hub('chat')

    # start a connection
    connection.start()

    # receive new chat messages from the hub
    chat.client.on('receiveMessage', print_received_message)

    # change chat topic
    # chat.client.on('topicChanged', print_topic)

    # process errors
    connection.error += print_error

    # start connection, optionally can be connection.start()
    with connection:
        # post new message
        chat.server.invoke('BroadcastMessage', 'Python is here')

        # change chat topic
        # chat.server.invoke('setTopic', 'Welcome python!')

        # invoke server method that throws error
        # chat.server.invoke('requestError')

        chat.server.invoke('SendMessage', 'johnsmith@outlook.com', 'From DIVICE')
        # post another message
        chat.server.invoke('send', 'Bye-bye!')

        # wait a second before exit
        connection.wait(1)
