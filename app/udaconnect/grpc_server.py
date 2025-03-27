import logging
import grpc
from concurrent import futures
import time
from app.udaconnect import person_pb2
from app.udaconnect import person_pb2_grpc

class PersonServiceGRPC(person_pb2_grpc.PersonServiceServicer):
    def GetPersons(self, request, context):
        persons = [
            person_pb2.PersonMessage(id=1, first_name="Alice", last_name="Smith", company_name="TechCorp"),
            person_pb2.PersonMessage(id=6, first_name="Bob", last_name="Johnson", company_name="SoftInc")
        ]
        return person_pb2.PersonMessageList(persons=persons)


def serve_grpc():
    print("Starting gRPC server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServiceGRPC(), server)
    server.add_insecure_port("[::]:5005")
    server.start()
    logging.info("gRPC server is running on port 5005...")
    server.wait_for_termination()