FROM ubuntu:16.04

WORKDIR /mydir
RUN apt update && apt install -y curl
COPY curl-script .
CMD ["./curl-script"]
