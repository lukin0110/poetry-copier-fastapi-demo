[![Lint and Test](https://github.com/lukin0110/poetry-copier-fastapi-demo/actions/workflows/test.yml/badge.svg)](https://github.com/lukin0110/poetry-copier-fastapi-demo/actions)

# Marty McFly

An example of a FastAPI app that was scaffolded with Poetry Copier.

## 🚀 Using

<details>
<summary>Prerequisites</summary>

<details>
<summary>1. Install Docker</summary>

1. Go to [Docker](https://www.docker.com/get-started), download and install docker.
2. [Configure Docker to use the BuildKit build system](https://docs.docker.com/build/buildkit/#getting-started). On macOS and Windows, BuildKit is enabled by default in Docker Desktop.

</details>


</details>

To serve this FastAPI app, run:
```bash
# Inside a DevContainer (when using VSCode)
poe serve --dev
```
```bash
# or, outside a DevContainer (when using PyCharm)
docker compose up app
```
and open [localhost:8000](https://localhost:8000) in your browser, [Swagger API docs](https://swagger.io/) available on [localhost:8000/docs](https://localhost:8000/docs).


## ✨ Setup VSCode

Open this repo with VSCode, *build DevContainer* and *Dev Containers: Reopen in Container*.

## ✨ Setup PyCharm

Open this repo with PyCharm, and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote) with the `dev` service.

## 🧑‍💻 Contributing

The following commands can be used inside a DevContainer.

#### Run linters
```bash
poe lint
```

#### Run tests
```bash
poe test
```

#### Update poetry lock file
```bash
poetry lock --no-update
```

<details>
<summary>Outside a DevContainer</summary>

1. Run linters
```bash
docker compose run devcontainer poe lint
```
2. Run tests
```bash
docker compose run devcontainer poe test
```
3. Update poetry lock file
```bash
docker compose run devcontainer poetry lock --no-update
# Update the docker image with the new lock file
docker compose build
```
4. Open a shell in docker
```bash
docker compose run devcontainer
```
</details>
<details>
<summary>Shortcuts outside a DevContainer</summary>

1. `make lint`
2. `make test`
3. `make lock`
4. `make shell`
</details>

---
️⚡️ Scaffolded with [Poetry Copier](https://github.com/lukin0110/poetry-copier/)\
🛠️ [Open an issue](https://github.com/lukin0110/poetry-copier/issues/new) if you have any questions or suggestions.
