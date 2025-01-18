from concurrent import futures

import grpc

import task_pb2
import task_pb2_grpc
from utils import config, mongo_connector

class SimilaritySearchServiceServicer(task_pb2_grpc.SimilaritySearchServiceServicer):
    def AddItem(self, request, context):
        print("Adding item request")
        print(request)
        item = {"itemID": request.id, "description": request.description}

        mongo = mongo_connector()

        try:
            item_id = mongo.add_item(db_name=config["DB_NAME"], collection_name="items", item=item)
            add_item_reply = task_pb2.AddItemResponse()
            add_item_reply.status = 200
            add_item_reply.message = f"Item with description {item.get('description')} created with id {item_id}"

        except Exception as e:
            add_item_reply = task_pb2.AddItemResponse()
            add_item_reply.status = 400
            add_item_reply.message = f"An error occurred: {e}"
            return add_item_reply

        return add_item_reply

    def SearchItems(self, request, context):
        print("Searching items request")
        print(request)

        mongo = mongo_connector()
        try:
            search_item_reply = task_pb2.SearchItemsResponse()
            search_item_reply.search_id = 'test-id'

        except Exception as e:
            search_item_reply = task_pb2.SearchItemsResponse()
            search_item_reply.search_id = 'not found'
            return search_item_reply

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
    server.add_insecure_port(f'{config["HOST"]}:{config["LOCAL_PORT"]}')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()