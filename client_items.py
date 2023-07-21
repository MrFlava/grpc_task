import grpc

import item_pb2 as message
import item_pb2_grpc as service


class ServiceClient:
    def __init__(self):
        self.host = 'localhost'
        self.port = 50051

        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))

        self.stub = service.SimilaritySearchServiceStub(self.channel)

    def create_item(self, id, description):
        req = message.AddItemRequest(id="aaaaa", description="bbbb")
        self.stub.AddItem(req)
        print(self.stub.AddItem(req))


if __name__ == "__main__":
    service_client = ServiceClient()
    service_client.create_item(id="asdwqd2", description="11213213")
