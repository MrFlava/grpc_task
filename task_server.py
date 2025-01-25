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
            item_data = mongo.search_item(
                db_name=config["DB_NAME"],
                collection_name="items",
                query={"description": request.query},
            )

            search_item_reply = task_pb2.SearchItemsResponse()
            search_item_reply.search_id = item_data["itemID"]

        except Exception as e:
            print(e)
            search_item_reply = task_pb2.SearchItemsResponse()
            search_item_reply.search_id = 'not found'
            return search_item_reply

        return search_item_reply

    def GetSearchResults(self, request, context):
        print("Getting search results request")
        print(request)

        mongo = mongo_connector()
        try:
            found_items = mongo.search_items(
                db_name=config["DB_NAME"],
                collection_name="items",
                query={"itemID": request.search_id},
            )
            print(found_items)
            search_result_list_reply = []
            for found_item in found_items:
                print(found_item)
                search_result = task_pb2.SearchResult()
                search_result.id = found_item.get("itemID")
                search_result.description = found_item.get("description")
                search_result_list_reply.append(search_result)

            search_results_reply = task_pb2.GetSearchResultsResponse(results=search_result_list_reply)

        except Exception as e:
            print(e)
            search_result_not_found = task_pb2.SearchResult()
            search_result_not_found.id = '-'
            search_result_not_found.description = '-'
            search_results_reply = task_pb2.GetSearchResultsResponse(results=[search_result_not_found])

        return search_results_reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_pb2_grpc.add_SimilaritySearchServiceServicer_to_server(SimilaritySearchServiceServicer(), server)
    server.add_insecure_port(f'{config["HOST"]}:{config["LOCAL_PORT"]}')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()