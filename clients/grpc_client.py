import grpc
import signals_pb2
import signals_pb2_grpc


url = "meowmetry-grpc.dev1.mnt.group:50051"

# Create the gRPC channel to the server
channel = grpc.insecure_channel(url)

# The stub & the request is generated from .proto file (inside signals_pb2_grpc & signals_pb2 files)

# Create the stub, which is the client-side interface for the remote service / method (the remote service: SignalStream)
stub = signals_pb2_grpc.SignalStreamStub(channel)

# Create the request 
request = signals_pb2.SubscribeRequest()

# The actual gRPC call (call the remote method using stub with this(request) and return its response stream that match .proto definition)
signals = stub.Subscribe(request)


for signal in signals:
    print(signal)