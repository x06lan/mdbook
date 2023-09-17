# docker

## Docker Image
Images are typically created from a base image (like a Linux distribution) and can be customized by adding your application code, configurations, and dependencies.

## Docker Container
A Docker container is a running instance of a Docker image. It encapsulates the application code, libraries, and dependencies defined in the image, along with an isolated file system, network stack, and process space.
## command

### Working with Images:
```bash
docker images                               # List all locally available Docker images.
docker pull <image>                         # Download an image from a registry (e.g., Docker Hub).
docker build -t <tag> <path_to_Dockerfile>  # Build a new Docker image from a Dockerfile.
docker rmi <image>                          # Remove a Docker image.
```

### Working with Containers:

```bash
docker run [options] <image>             # Create and start a new container based on the specified image.
docker ps                                # List all running containers.
docker ps -a                             # List all containers (including stopped ones).
docker start <container>                 # Start a stopped container.
docker stop <container>                  # Stop a running container.
docker restart <container>               # Restart a container.
docker exec -it <container> <command>    # Execute a command inside a running container.
```

### Managing Docker Compose (for multi-container applications):

```bash
docker-compose up            # Create and start containers defined in a docker-compose.yml file.
docker-compose down          # Stop and remove containers created 
```
### Networking:

```bash
docker network ls                                # List all Docker networks.
docker network create <name>                     # Create a new Docker network.
docker network connect <network> <container>     # Connect a container to a network.
docker network disconnect <network> <container>  # Disconnect a container from a n
```