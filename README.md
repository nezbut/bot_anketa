# Bot Anketa

In this project, I'm just practicing connecting a Python project with Docker/Docker Compose. And so, the bot itself only collects information about the user and saves his profile to the database. Redis acts as FSMStorage here, and PostgreSQL acts as a database.

## Project Launch

#### With Docker

1. Replace the environment variables in the docker-compose.yml on your own.
2. Launch docker compose:
```bash
docker compose up
```

#### Without Docker

To run a project without Docker, follow these steps:

1. Install and run PostgreSQL and Redis
2. Set environment variables in the console:

```bash
export TG_BOT_TOKEN="TG BOT TOKEN @BotFather"
export DATABASE_URI="postgresql+asyncpg://USERNAME:PASSWORD@localhost:5432/bot_anketa"
export KV_DATABASE_URI="redis://localhost:6379/4"
```

3. Apply Migrations:

```bash
alembic -c bot_anketa/src/alembic.ini upgrade head
```

4. Create a file in the project start.sh and copy everything from there start.example.sh and change the environment variables to your own, as mentioned above
5. Run the file start.sh