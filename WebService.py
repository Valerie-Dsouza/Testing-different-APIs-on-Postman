from assetproto import web_pb2
from assetserver.models.WebDetailsSchema import WebDetailsSchema,WebDetailsTable
from assetserver.packages.base import base


class WebService(base):
    def GetWebApp(self,request):
        user=request.user
        message=request.message 
        self.StartConnection(user,message)
        with self.session_obj as session:
           web = self.webd.webd.insert().values(user=request.user,message=request.message)
           session.execute(web)
           session.commit()
        return web_pb2.WebAppRequest(user=user,message=message)
        

    def StartConnection(self,user,message):
        self.hub_connection.send("SendMessage", [user, message])
      