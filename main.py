from flask import Flask, request, Response
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage

from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest

app = Flask(__name__)
viber = Api(BotConfiguration(
    name='Kupujem Prodajem Notifikator',
    avatar='',
    auth_token='512edd0b5b67e619-d5fc49f747cf8646-91bb1c406d02b4e4'
))

@app.route('/', methods=['POST'])
def incoming():
    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        # lets echo back
        viber.send_messages(viber_request.sender.id, [
            TextMessage(text="Your id is: " + str(viber_request.sender.id))
        ])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="Hvala što ste se prijavili na ovu uslugu!")
        ])

    return Response(status=200)

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=80, debug=True)
