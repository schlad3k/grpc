import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.ElectionServiceStub(channel)

        # Create ElectionData
        election_data = helloworld_pb2.ElectionData(
            regionID=30711,
            regionName="Maria Ellend",
            regionAddress="Kulturplatz 1",
            regionPostalCode=2402,
            federalState="Austria",
            timestamp="2024-12-10",
            countingData=[
                helloworld_pb2.Party(
                    partyID="OEVP",
                    amountVotes=1000,
                    preferedVotes=[
                        helloworld_pb2.Candidate(listnumber=1, name="Karner Gerhard", votes=500),
                        helloworld_pb2.Candidate(listnumber=2, name="Tanner Klaudia", votes=250),
                        helloworld_pb2.Candidate(listnumber=3, name="Servus Harald", votes=250),
                    ]
                ),
                helloworld_pb2.Party(
                    partyID="SPOE",
                    amountVotes=750,
                    preferedVotes=[
                        helloworld_pb2.Candidate(listnumber=1, name="Silvan Rudolf", votes=250),
                        helloworld_pb2.Candidate(listnumber=2, name="Kumpan-Takacs Silvia", votes=250),
                        helloworld_pb2.Candidate(listnumber=3, name="Laimer Robert", votes=250),
                    ]
                )
            ]
        )

        # Send the ElectionData
        response = stub.SendElectionData(election_data)

        # Print the server response
        print(f"Response from server: {response.confirmation}")


if __name__ == '__main__':
    run()
