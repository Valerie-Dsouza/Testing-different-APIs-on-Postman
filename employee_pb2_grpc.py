# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from assetproto import employee_pb2 as employee__pb2


class EmployeeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEmployee = channel.unary_unary(
                '/employees.EmployeeService/CreateEmployee',
                request_serializer=employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
                response_deserializer=employee__pb2.CreateUpdateEmployeeRequest.FromString,
                )
        self.GetEmployee = channel.unary_unary(
                '/employees.EmployeeService/GetEmployee',
                request_serializer=employee__pb2.GetDeleteEmployeeRequest.SerializeToString,
                response_deserializer=employee__pb2.CreateUpdateEmployeeRequest.FromString,
                )
        self.DeleteEmployee = channel.unary_unary(
                '/employees.EmployeeService/DeleteEmployee',
                request_serializer=employee__pb2.GetDeleteEmployeeRequest.SerializeToString,
                response_deserializer=employee__pb2.DeleteEmployeeResponse.FromString,
                )
        self.UpdateEmployee = channel.unary_unary(
                '/employees.EmployeeService/UpdateEmployee',
                request_serializer=employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
                response_deserializer=employee__pb2.CreateUpdateEmployeeRequest.FromString,
                )
        self.SelectAllEmployee = channel.unary_unary(
                '/employees.EmployeeService/SelectAllEmployee',
                request_serializer=employee__pb2.SelectColumnsRequest.SerializeToString,
                response_deserializer=employee__pb2.SelectAllEmployeeResponse.FromString,
                )
        self.SelectSalaryByRange = channel.unary_unary(
                '/employees.EmployeeService/SelectSalaryByRange',
                request_serializer=employee__pb2.SelectSalaryByRangeRequest.SerializeToString,
                response_deserializer=employee__pb2.SelectAllEmployeeResponse.FromString,
                )
        self.GetRedisData = channel.unary_unary(
                '/employees.EmployeeService/GetRedisData',
                request_serializer=employee__pb2.GetRedisRequest.SerializeToString,
                response_deserializer=employee__pb2.GetRedisResponse.FromString,
                )
        self.GetForm = channel.unary_unary(
                '/employees.EmployeeService/GetForm',
                request_serializer=employee__pb2.GetFormRequest.SerializeToString,
                response_deserializer=employee__pb2.SelectAllEmployeeResponse.FromString,
                )


class EmployeeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectAllEmployee(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectSalaryByRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRedisData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetForm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmployeeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEmployee,
                    request_deserializer=employee__pb2.CreateUpdateEmployeeRequest.FromString,
                    response_serializer=employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
            ),
            'GetEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEmployee,
                    request_deserializer=employee__pb2.GetDeleteEmployeeRequest.FromString,
                    response_serializer=employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
            ),
            'DeleteEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteEmployee,
                    request_deserializer=employee__pb2.GetDeleteEmployeeRequest.FromString,
                    response_serializer=employee__pb2.DeleteEmployeeResponse.SerializeToString,
            ),
            'UpdateEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEmployee,
                    request_deserializer=employee__pb2.CreateUpdateEmployeeRequest.FromString,
                    response_serializer=employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
            ),
            'SelectAllEmployee': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectAllEmployee,
                    request_deserializer=employee__pb2.SelectColumnsRequest.FromString,
                    response_serializer=employee__pb2.SelectAllEmployeeResponse.SerializeToString,
            ),
            'SelectSalaryByRange': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectSalaryByRange,
                    request_deserializer=employee__pb2.SelectSalaryByRangeRequest.FromString,
                    response_serializer=employee__pb2.SelectAllEmployeeResponse.SerializeToString,
            ),
            'GetRedisData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRedisData,
                    request_deserializer=employee__pb2.GetRedisRequest.FromString,
                    response_serializer=employee__pb2.GetRedisResponse.SerializeToString,
            ),
            'GetForm': grpc.unary_unary_rpc_method_handler(
                    servicer.GetForm,
                    request_deserializer=employee__pb2.GetFormRequest.FromString,
                    response_serializer=employee__pb2.SelectAllEmployeeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'employees.EmployeeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EmployeeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/CreateEmployee',
            employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
            employee__pb2.CreateUpdateEmployeeRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/GetEmployee',
            employee__pb2.GetDeleteEmployeeRequest.SerializeToString,
            employee__pb2.CreateUpdateEmployeeRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/DeleteEmployee',
            employee__pb2.GetDeleteEmployeeRequest.SerializeToString,
            employee__pb2.DeleteEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/UpdateEmployee',
            employee__pb2.CreateUpdateEmployeeRequest.SerializeToString,
            employee__pb2.CreateUpdateEmployeeRequest.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectAllEmployee(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/SelectAllEmployee',
            employee__pb2.SelectColumnsRequest.SerializeToString,
            employee__pb2.SelectAllEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectSalaryByRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/SelectSalaryByRange',
            employee__pb2.SelectSalaryByRangeRequest.SerializeToString,
            employee__pb2.SelectAllEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRedisData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/GetRedisData',
            employee__pb2.GetRedisRequest.SerializeToString,
            employee__pb2.GetRedisResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetForm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/employees.EmployeeService/GetForm',
            employee__pb2.GetFormRequest.SerializeToString,
            employee__pb2.SelectAllEmployeeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
