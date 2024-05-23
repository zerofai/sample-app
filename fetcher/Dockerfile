# Use apline as base image
FROM alpine:latest

# Download and install glibc
RUN apk add --no-cache bash curl

# Change WORKDIR
WORKDIR /fetcher

COPY ./fetcher.sh /fetcher/fetcher.sh

RUN chmod -R 765 /fetcher

# Set the entrypoint command
CMD ["./fetcher.sh"]