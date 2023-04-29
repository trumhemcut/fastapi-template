You are a principal Python developer and you write the code based on the requirements. You can suggest multiple files. Firstly, you show the folder structure. Only show the code, no explanation. Every files in the folder structure must be shown explicitly.

1. Functional requirement:
    - Application: you build an application for a coffee shop to list drinks in the menu, and order the drinks. The application must have 2 services:
        * Drink service: this service is used to list drinks in the menu. The service must have 2 methods:
            + ListDrinks: list all drinks in the menu
            + GetDrink: get a drink by id
            + CreateDrink: create a drink
            + UpdateDrink: update a drink
        * Order service: this service is used to order drinks. The service must have 2 methods:
            + CreateOrder: create an order
            + GetOrder: get an order by id
            + ListOrders: list all orders
            + UpdateOrder: update an order
            + DeleteOrder: delete an order
    - The services must be implemented with AsyncIO and located at "./services"
2. GRPC requirement:
    - The application must build on GRPC server, not using FastAPI, Flask neither AIOHTTP.
    - The proto files are located at "./protos"
2. Data requirement:
    - ORM Framework: using SQLAlchemy as an ORM to design the models. Model validation is required such as max length, field description
    - Database design: You must use AsyncSession to connect to database server. You use PostgreSQL to store data with the table are described below:
        * Drink table’s fields: id, name, description, price. Please add description to the columns.
        * Order table’s fields: id, customer_name, customer_email, customer_phone, quantity, total_price, drink_id. Please add description to the columns. The models are located at "./models".
    - Database migration: you must use Alembic to create migration files. Alembic configs and migration files are located at "./migrations". You have to build the mechanism to run migration at runtime.
2. Non-functional requirement:
    - No security is required
    - Caching is not required
    - Exception handling is required.
    - Logging: you must write the necessary logs. Default logging level is INFO. Logger configs are located at "./utils/logger.py"
3. Other requirement:
    - You must write README.md and describe step by step to run the app. Please use grpcurl tool to help users connect to our app.
    - The app would be deployed as Docker container, so a Dockerfile and Docker Compose file are required.

Finally, If the response is too long, I say “continue” and you continue with the showing the code. After I say “continue”, you say “(continued”) and then show the code in a new code block. Once you finish, you say “Finished” so that I can know you’re done.
