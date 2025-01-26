FROM ubuntu:latest
LABEL authors="vladyslavsirenko"

ENTRYPOINT ["top", "-b"]