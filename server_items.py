from concurrent import futures

import grpc
import item_pb2 as message
import item_pb2_grpc as service
from db import Session, engine
from models import Item


class ItemService(service.SimilaritySearchService):

    def create_item(self, request, context):
        with Session(autoflush=False, bind=engine) as db:
            new_item = Item(id=request.id, description=request.description)

            db.add(new_item)
            db.commit()

        return message.AddItemResponse(status=200, message="aaaaa")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service.add_SimilaritySearchServiceServicer_to_server(ItemService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
