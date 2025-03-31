import grpc
import sys
from concurrent import futures
from app.udaconnect import person_pb2
from app.udaconnect import person_pb2_grpc
from app.udaconnect.models import Person
import logging

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PersonServiceGRPC(person_pb2_grpc.PersonServiceServicer):
    def GetPersons(self, request, context):

        from app import create_app
        from app import db

        # Set application context
        app = create_app()
        with app.app_context():
            # Database query
            persons_from_db = db.session.query(Person).all()

            # Convert into gRPC objects
            persons = [
                person_pb2.PersonMessage(
                    id=person.id,
                    first_name=person.first_name,
                    last_name=person.last_name,
                    company_name=person.company_name
                )
                for person in persons_from_db
            ]

            return person_pb2.PersonMessageList(persons=persons)


def serve_grpc():
    print("Starting gRPC server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServiceGRPC(), server)
    server.add_insecure_port("[::]:5005")
    server.start()
    logger.info("gRPC server is running on port 5005...")
    server.wait_for_termination()