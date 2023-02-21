FROM docker.io/library/node:18 as build
RUN apt-get update && apt-get install -y translate-toolkit python3-gnupg python3-yaml && rm -rf /var/lib/apt/lists/*
ADD . /websites
WORKDIR /websites
RUN .build/load_gpg.sh
RUN npm install
RUN npm run generate

FROM quay.io/fedora/fedora:37
RUN dnf -y install s3cmd  && dnf clean all
COPY --from=build /websites/.output/public /output
