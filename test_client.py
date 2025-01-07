import test_pb2_grpc
import test_pb2
import time
import grpc

class TestServicer(test_pb2_grpc.TestServicer):
    def SayCool(self, request, context):
        print("SayCool Request Made:")
        print(request)
        hello_reply = test_pb2.CoolReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply