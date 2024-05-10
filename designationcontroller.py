
# import sys
# import os 
# sys.path.insert(0 , os.path.abspath('../'))
from assetserver.service.DesignationService import DesignationService
from assetproto import designation_pb2_grpc

class DesignationController(designation_pb2_grpc.DesignationServiceServicer):
    def __init__(self):
        self.service=DesignationService()

    def CreateDesignation(self,request,context):
        response=self.service.CreateDesignation(request)
        return response    
    
    def GetDesignation(self,request,context):
        response=self.service.GetDesignation(request)
        return response 