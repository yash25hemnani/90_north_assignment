from time import sleep
from channels.consumer import SyncConsumer, AsyncConsumer, async_to_sync
from channels.exceptions import StopConsumer
import json
from .models import ChatModel, GroupModel

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket Connected....', event)
        print('Channel Layer....', self.channel_layer)
        print('Channel Name....', self.channel_name)

        # Getting Group Name from URL
        self.group_name = self.scope['url_route']['kwargs']['groupName']

        # Adding Channels to a group - it is an async function so you can't use it directly
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({
            'type':'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('Message received from client: ', event['text'])
        print("User...", self.scope['user'])

        # Convert to python dict
        data = json.loads(event['text'])
        message = data['msg']

        # Get the Group
        group = GroupModel.objects.get(name = self.group_name)


        if self.scope['user'].is_authenticated:
            # Save the chats
            chat = ChatModel(
                content = data['msg'],
                group = group,
                sent_by = self.scope['user']
            )

            chat.save()

            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                'type': 'chat.message',
                'message': event['text'],
                'username': self.scope['user'].username,
            })
        else:
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({'msg':"Login Required"})
            })
    def chat_message(self, event):
        print('event...', event)
        print('Actual Data...', event['message'])
        self.send({
        'type': 'websocket.send',
        'text': json.dumps({
            'msg': event['message'],  
            'username': event['username'],  
        }),
    })


    def websocket_disconnect(self, event):
        print('Websocket Disconnected...', event)

        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

        raise StopConsumer()
    