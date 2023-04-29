You are a principal Python developer and you write the code based on the requirements. You can suggest multiple files. Firstly, you show the folder structure. Secondly you show all the code.

1. Functional requirement:
    - Application: you build an application for a coffee shop to list drinks in the menu, and order the drinks. The application must have 2 services:
        * Drink service: this service is used to list drinks in the menu. All methods are using async await, AsyncSession. The service must have these methods:
            + ListDrinks: list all drinks in the menu, use SqlModel to get all drinks
            + GetDrink: get a drink by id, use SqlModel to get a drink
            + CreateDrink: create a drink
            + UpdateDrink: update a drink
            + DeleteDrink: delete a drink
        * Order service: this service is used to order drinks. All methods are using async await, AsyncSession. The service must have these methods:
            + CreateOrder: create an order
            + GetOrder: get an order by id, use SqlModel package to get an order
            + ListOrders: list all orders, use SqlModel package to get all orders
            + UpdateOrder: update an order
            + DeleteOrder: delete an order
    - The services must be implemented with AsyncIO, AsyncSession and located at "./app/services"
2. GRPC requirement:
    - The application must build on GRPC server, not using FastAPI, Flask neither AIOHTTP. The GRPC server is located at "./app/server.py" using aio. You have to write log to track the status.
    - The proto files are located at "./protos"
    - There are 2 proto files: drink.proto and order.proto. You must show the content of proto files.
3. Data requirement:
    - ORM Framework: using SQLAlchemy as an ORM to design the models. Model validation is required such as max length, field description. The models are located at "./app/models".
    - Database design: You must use AsyncSession to connect to database server. You use PostgreSQL to store data with the table are described below:
        * Drink table’s fields: id is uuid type, name, description, price. Please add description to the columns.
        * Order table’s fields: id  is uuid type, customer_name, customer_email, customer_phone, quantity, total_price, drink_id. Please add description to the columns. The drink_id is a foreign key to the Drink table.
    - Database migration: you must use Alembic to create migration files. Alembic configs and migration files are located at "./app/migrations". You have to build the mechanism to run migration at runtime. You don't need to show migration files.
    - A database connection is located at "./app/database.py" to get a AsyncSession. The connection string is located at "./app/config.py"
4. Non-functional requirement:
    - No security is required
    - Caching is not required
    - Exception handling is required. You must handle all exceptions and return the correct error code and message to the client.
    - Logging: you must write the necessary logs. Default logging level is INFO. You get log config at "./app/utils/logger.py"
    - Config: 
        * Using pydantic library.
        * It should have a config file to store configs located at "./app/config.py"
        * It can read from environment variables. 
        * All config names must be in uppercase. 
        * .env file is located at "./.env" store environment variables:
            + DATABASE_URL: database connection string postgresql+asyncpg format.
            + LOG_LEVEL: logging level

5. Deployment: you create the files as below:
    - Dockerfile: The app would be deployed as Docker container, so a Dockerfile is required at ./Dockerfile. You use the latest stable Python version.
    - docker-compose.yml: A Docker compose should have 2 services: app and database. Database should have a Docker volume to store data. This file is at ./docker-compse.yml
    - .dockerignore is at ./.dockerignore

6. Testing: you create the testing as follows:
    - Test files are located at "./tests"
    - test_drink_service.py: test drink service, mock SQLAlchemy session
    - test_order_service.py: test order service, mock SQLAlchemy session
    - test_server.py: test GRPC server

7. Documentation: You create a README.md at root folder and create a range of documents and store at ./docs folder:
    - You must write README.md and describe step by step to run the app. Please use grpcurl tool to help users connect to our app. You must show content of this README.md file. The file is at ./README.md.
    - Database design document: you must use ERD to design the database. The document is located at "./docs/database.md". ERD is generated from PlantUML. You must show the file name of this planuml file.
    - Architecture design document: you must use UML to design the architecture. The document is located at "./docs/architecture.md"
    - You generate a C4 diagram and store at "./docs/c4.dsl" plantuml format. The diagram must include:
        * A model includes: user to use our Software System, a software system that connect to a database
        * Views to show system context, containers

