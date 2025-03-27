from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print(f'Message Received From Client: {event['text']}')

        for i in range(10):
            self.send({
                "type": "websocket.send",
                "text": str(i),
            })
            sleep(1)

    def websocket_disconnect(self, event):
        raise StopConsumer()