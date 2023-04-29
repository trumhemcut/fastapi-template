You are a principal Python developer and you write the code based on the requirements. You can suggest multiple files. Firstly, you show the folder structure. Only show me the code when I request to.

1. Functional requirement:
    - Application: you build an application for a coffee shop to list drinks in the menu, and order the drinks. The application must have 2 services:
        * Drink service: this service is used to list drinks in the menu. The service must have 2 methods:
            + ListDrinks: list all drinks in the menu
            + GetDrink: get a drink by id
            + CreateDrink: create a drink
            + UpdateDrink: update a drink
            + DeleteDrink: delete a drink
        * Order service: this service is used to order drinks. The service must have 2 methods:
            + CreateOrder: create an order
            + GetOrder: get an order by id
            + ListOrders: list all orders
            + UpdateOrder: update an order
            + DeleteOrder: delete an order
    - The services must be implemented with AsyncIO, AsyncSession and located at "./services"
2. GRPC requirement:
    - The application must build on GRPC server, not using FastAPI, Flask neither AIOHTTP.
    - The proto files are located at "./protos"
    - There are 2 proto files: drink.proto and order.proto. You must show the content of proto files.
3. Data requirement:
    - ORM Framework: using SQLAlchemy as an ORM to design the models. Model validation is required such as max length, field description. The models are located at "./models".
    - Database design: You must use AsyncSession to connect to database server. You use PostgreSQL to store data with the table are described below:
        * Drink table’s fields: id, name, description, price. Please add description to the columns.
        * Order table’s fields: id, customer_name, customer_email, customer_phone, quantity, total_price, drink_id. Please add description to the columns. The drink_id is a foreign key to the Drink table.
    - Database migration: you must use Alembic to create migration files. Alembic configs and migration files are located at "./migrations". You have to build the mechanism to run migration at runtime. You don't need to show migration files.
4. Non-functional requirement:
    - No security is required
    - Caching is not required
    - Exception handling is required. You must handle all exceptions and return the correct error code and message to the client.
    - Logging: you must write the necessary logs. Default logging level is INFO. Logger configs are located at "./utils/logger.py"

6. Deployment: you create the files as below:
    - Dockerfile: The app would be deployed as Docker container, so a Dockerfile. You use the latest stable Python version.
    - docker-compose.yml: A Docker compose should have 2 services: app and database. Database should have a Docker volume to store data.
    - .dockerignore: It should have Docker ignore to ignore the built files. 

5. Documentation: You create a README.md at root folder and create a range of documents and store at ./docs folder:
    - You must write README.md and describe step by step to run the app. Please use grpcurl tool to help users connect to our app. You must show content of this README.md file.
    - Database design document: you must use ERD to design the database. The document is located at "./docs/database.md". ERD is generated from PlantUML. You must show the file name of this planuml file.
    - Architecture design document: you must use UML to design the architecture. The document is located at "./docs/architecture.md"
    - You generate a C4 diagram and store at "./docs/c4.dsl" plantuml format. The diagram must include:
        * A model includes: user to use our Software System, a software system that connect to a database
        * Views to show system context, containers

Finally, If the response is too long, I say “continue” and you continue with the showing the code. After I say “continue”, you show the code in a new code block where you left off. Once you finish, you say “Finished” so that I can know you’re done.
