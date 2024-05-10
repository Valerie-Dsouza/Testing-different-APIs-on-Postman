
from assetserver.service.EmployeeService import EmployeeService
from assetproto import employee_pb2_grpc

class EmployeeController(employee_pb2_grpc.EmployeeServiceServicer):
    def __init__(self):
        self.service=EmployeeService()


    def CreateEmployee(self,request , context):
        response=self.service.CreateEmployee(request)
        return response    
    
    def GetEmployee(self,request,context ):
        response=self.service.GetEmployee(request)
        return response 
    
    def UpdateEmployee(self,request,context):
        response=self.service.UpdateEmployee(request)
        return response 
    
    def DeleteEmployee(self,request,context):
        response=self.service.DeleteEmployee(request)
        return response 
    
    def SelectAllEmployee(self,request,context):
        response=self.service.SelectAllEmployee(request)
        return response 
    
    def SelectSalaryByRange(self,request,context):
        response=self.service.SelectSalaryByRange(request)
        return response 
    
    def GetRedisData(self,request,context):
        response=self.service.GetRedis(request)
        return response 
    
    def GetForm(self,request,context):
        response=self.service.GetForm(request)
        return response 
    
    # def WebApp(self,request,context):
    #     response=self.service.GetWebApp(request)
    #     return response