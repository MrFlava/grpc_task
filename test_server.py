from concurrent import futures
import time

import grpc
import test_pb2
import test_pb2_grpc

class TestServicer(test_pb2_grpc.TestServicer):
    def SayCool(self, request, context):
        print("SayCool Request Made:")
        print(request)
        hello_reply = test_pb2.CoolReply()
        hello_reply.message = f"{request.greeting} {request.name}"

        return hello_reply

    def SimonSayHello(self, request, context):
        print("SimonSayHello Request Made:")
        print(request)

        for i in range(3):
            hello_reply = test_pb2.CoolReply()
            hello_reply.message = f"{request.greeting} {request.name} {i + 1}"
            yield hello_reply
            time.sleep(3)


    def ChattyClientSayHello(self, request_iterator, context):
        print("ChattyClientSayHello Request Made:")
        delayed_reply = test_pb2.DelayedCoolReply()
        for request in request_iterator:
            print("in cycle:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply
