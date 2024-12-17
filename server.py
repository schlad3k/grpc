import grpc
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc


# Implementierung des ElectionService
class ElectionServiceServicer(helloworld_pb2_grpc.ElectionServiceServicer):
    def SendElectionData(self, request, context):
        # Log der empfangenen Daten
        print(f"Region: {request.regionName}, State: {request.federalState}")
        for party in request.countingData:
            print(f"Party: {party.partyID}, Votes: {party.amountVotes}")
            for candidate in party.preferedVotes:
                print(f"  Candidate: {candidate.name}, Votes: {candidate.votes}")

        # Bestätigung zurückgeben
        return helloworld_pb2.ElectionResponse(confirmation="Election data received successfully!")


# Server starten
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_ElectionServiceServicer_to_server(ElectionServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

