# Bot Anketa

In this project, I'm just practicing connecting a Python project with Docker/Docker Compose. And so, the bot itself only
collects information about the user and saves his profile to the database. Redis acts as FSMStorage here, and PostgreSQL
acts as a database.

## Project Launch

#### With Docker

1. Replace the environment variables in the docker-compose.yml on your own.
2. Launch docker compose:

```bash
docker compose up
```

#### With Kubernetes/Helm

1. Go to the k8s folder

```bash
cd k8s/
```

2. Start k8s cluster
3. Share your secrets: secrets/dev/secrets.my, secrets/prod/secrets.yml
4. Create a GPG key and put it in secrets/dev/.sops.yaml and secrets/prod/.sops.yaml
5. Install [sops](https://github.com/getsops/sops)
6. Install Helm plugin: [helm-secrets](https://github.com/jkroepke/helm-secrets)

```bash
helm plugin install https://github.com/jkroepke/helm-secrets
```

7. Install Helm Chart

```bash
helm secrets install bot-anketa-release-dev bot_anketa/ -f secrets/dev/secrets.yml
```

or

```bash
helm secrets install bot-anketa-release-prod bot_anketa/ -f secrets/prod/secrets.yml
```

#### Standard Launch

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

4. Create a file in the project start.sh and copy everything from there start.example.sh and change the environment
   variables to your own, as mentioned above
5. Run the file start.sh