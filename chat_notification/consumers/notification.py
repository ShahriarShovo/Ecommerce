import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer


# AsyncWebsocketConsumer
# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.group_name = 'public_room'
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )

#     async def send_notification(self, event):
#         print("send Notification-------", event['message'])
#         await self.send(text_data=json.dumps({ 'message': event['message'] }))



#AsyncJsonWebsocketConsumer
class NotificationConsumer(AsyncJsonWebsocketConsumer):

    # async def connect(self):
    #     self.user = self.scope['user']
    #     if not self.user or  not self.user.is_authenticated:
    #         await self.close()
    #     else:
    #         self.group_name='notification'
    #         try:
    #             await self.channel_layer.group_add(self.group_name, self.channel_name)
    #         except Exception as e:
    #             print(f"Error adding channel to group: {e}")
    #             await self.close()
    #         else:
    #             await self.accept()

    async def connect(self):
        print("Connnected..")
        self.user = self.scope['user']
        if not self.user or not self.user.is_authenticated:
            await self.close()
        else:
            self.group_name = 'notification'
            try:
                await self.channel_layer.group_add(self.group_name, self.channel_name)
            except Exception as e:
                print(f"Error adding channel to group: {e}")
                await self.close()
            else:
                await self.accept()



    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name,self.channel_name)
    
    async def send_notification(self, event):
        await self.send_json({
            'notification':event['notification']
            })

