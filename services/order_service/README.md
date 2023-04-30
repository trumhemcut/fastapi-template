python -m grpc_tools.protoc -I ./protos --python_out=./app/services/protos --pyi_out=./app/services/protos --grpc_python_out=./app/services/protos ./protos/drink.proto


python -m grpc_tools.protoc -I ./protos --python_out=./app/services/protos --pyi_out=./app/services/protos --grpc_python_out=./app/services/protos ./protos/helloworld.proto


uvicorn app.server --reload --port 50051