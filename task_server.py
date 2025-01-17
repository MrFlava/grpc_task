from concurrent import futures

import grpc

import task_pb2
import task_pb2_grpc
from db import db

class SimilaritySearchServiceServicer(task_pb2_grpc.SimilaritySearchServiceServicer):
    def AddItem(self, request, context):
        print("Adding item request")
        print(request)
        add_item = {"itemID": request.id, "description": request.description}

        add_item_reply = task_pb2.AddItemResponse()
        add_item_reply.status = 200
        add_item_reply.message = f"Item with description {add_item.get('description')} created"

        return add_item_reply

    def SearchItems(self, request, context):
        print("Searching items request")
        print(request)

        search_item_reply = task_pb2.SearchItemsResponse()
        search_item_reply.search_id = 'test-id'

        return search_item_reply

    def GetSearchResults(self, request, context):
        print("Getting search results request")
        print(request)

        search_result1 = task_pb2.SearchResult()
        search_result1.id = 'test-id'
        search_result1.description = 'test-description'
        search_results_reply = task_pb2.GetSearchResultsResponse(results=[search_result1])
        return search_results_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_SimilaritySearchServiceServicer_to_server(SimilaritySearchServiceServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()