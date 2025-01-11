import task_pb2_grpc
import task_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("Please enter a name (or nothing to stop): ")

        if name == "":
            break

        time.sleep(1)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = task_pb2_grpc.SimilaritySearchServiceStub(channel)
        print("1. Add item")
        print("2. Search items")
        print("3. Get search results")

        # rpc_call = input("Which rpc you like to make: ")

        # if rpc_call == "1":
        #     hello_request = test_pb2.CoolRequest(greeting = "Bonjour", name = "You")
        #     hello_reply = stub.SayCool(hello_request)
        #     print("SayCool Response Received:")
        #     print(hello_reply)
        # elif rpc_call == "2":
        #     hello_request = test_pb2.CoolRequest(greeting = "Bonjour", name = "Youuu")
        #     hello_replies = stub.SimonSaysHello(hello_request)
        #
        #     for hello_reply in hello_replies:
        #         print("SimonSaysHello Response Received:")
        #         print(hello_reply)
        # elif rpc_call == "3":
        #     delayed_reply = stub.SimonClientSaysHello(get_client_stream_requests())
        #
        #     print("SimonClientSaysHello Response Received:")
        #     print(delayed_reply)
        # elif rpc_call == "4":
        #     responses = stub.InteractingSimonHello(get_client_stream_requests())
        #
        #     for response in responses:
        #         print("InteractingSimonHello Response Received: ")
        #         print(response)

if __name__ == "__main__":
    run()