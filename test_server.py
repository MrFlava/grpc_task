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


    def SimonClientSaysHello(self, request_iterator, context):
        print("SimonClientSaysHello Request Made:")
        delayed_reply = test_pb2.DelayedCoolReply()
        for request in request_iterator:
            print("in cycle:")
            print(request)
            delayed_reply.request.append(request)

        delayed_reply.message = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServicer_to_server(TestServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()