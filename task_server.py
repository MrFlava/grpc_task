from concurrent import futures
import time

import grpc
import task_pb2
import task_pb2_grpc

class SimilaritySearchServiceServicer(task_pb2_grpc.SimilaritySearchServiceServicer):
    def AddItem(self, request, context):
        print("Adding item request")
        print(request)

        add_item_reply = task_pb2.AddItemResponse()
        add_item_reply.status = 1
        add_item_reply.message = "created"

        return add_item_reply

    def SearchItems(self, request, context):
        print("Searching items request")
        print(request)

        search_item_reply = task_pb2.SearchItemsResponse()
        search_item_reply.search_id = 'test-id'

        return search_item_reply

    def GetSearchResults(self, request, context):
        pass