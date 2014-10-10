FROM golang:1.3.3

RUN go get -v github.com/spf13/hugo
VOLUME /public
ADD . /src
WORKDIR /src
RUN hugo --theme=hyde-x
ENTRYPOINT sh copy.sh
