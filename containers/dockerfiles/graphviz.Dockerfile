# Use an official Ubuntu base image
FROM ubuntu:latest

# Install Graphviz
RUN apt-get update && apt-get install -y graphviz

# Set the working directory
WORKDIR /data

# Default command uses the `dot` tool to process a graph file
ENTRYPOINT ["dot"]
CMD ["-Tpng", "-o", "output.png"]  # Default command if no argument is provided
