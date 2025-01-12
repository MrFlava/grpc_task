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

        rpc_call = input("Which rpc you like to make: ")

        if rpc_call == "1":
            pass
            add_request = task_pb2.AddItemRequest(id="test1", description="test")
            add_response = stub.AddItem(add_request)
            print("Addr Response Received:")
            print(add_response)
        elif rpc_call == "2":
            search_items_request = task_pb2.SearchItemsRequest(query="test")
            search_items_response = stub.SearchItems(search_items_request)

            print("Search Items Response Received:")
            print(search_items_response)
        elif rpc_call == "3":
            pass
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