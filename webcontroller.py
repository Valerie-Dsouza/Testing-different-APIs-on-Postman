from assetserver.service.WebService import WebService
from assetproto import web_pb2_grpc

class WebController(web_pb2_grpc.WebServiceServicer):
     def __init__(self):
        self.service=WebService()

     def WebApp(self,request,context):
        response=self.service.GetWebApp(request)
        return response