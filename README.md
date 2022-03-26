# My-Simple-Scalable-Server

Currently, this project encompasses a microservice architecture using Docker Compose.

The following containers exist:

* mysql: Database that *should* persist between runs. TODO: Verify this behavior; implement security for data saved to local host and password protections.
* web: The Django backend
* playground: A python container. TBD what this will be used for.
* adminer: A troubleshooting tool to access the mysql 
database.

## How to Run:

CLI options exist, but we'll only operate in VSCode for convenience. I'm assuming VSCode, Docker extension, and Docker Engine/Docker Desktop are installed.

* Using VSCode, open web folder in container. This will run the Docker Compose commands.

## References

* [docker mysql](https://hub.docker.com/_/mysql)
* [docker compose django](https://docs.docker.com/samples/django/)
* [VSCode Create Dev Container](https://code.visualstudio.com/docs/remote/create-dev-container)


## TODOs

A lot! Provide project direction. What's the goal?

* Fix the CLRF end-of-line issue. Whenever I start a Docker container, it rewrites files with different line endings. This will move from obnoxious to disruptive as the project scales.
* Add black, isort, and flake8 precommit hooks in each container.
* Implmement commit-triggered automated testing.
