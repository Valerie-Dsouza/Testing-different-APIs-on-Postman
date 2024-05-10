from concurrent import futures
import grpc
from assetproto.employee_pb2_grpc import add_EmployeeServiceServicer_to_server
from assetproto.designation_pb2_grpc import add_DesignationServiceServicer_to_server
from assetproto.web_pb2_grpc import add_WebServiceServicer_to_server



from assetserver.controller.employeecontroller import EmployeeController
from assetserver.controller.designationcontroller import DesignationController
from assetserver.controller.webcontroller import WebController



def server_start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_EmployeeServiceServicer_to_server(EmployeeController(), server)
    add_DesignationServiceServicer_to_server(DesignationController(), server)
    add_WebServiceServicer_to_server(WebController(), server)


    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

    
if __name__ == '__main__':
    server_start()      