FROM docker.io/library/node:18 as build
RUN apt-get update && apt-get install -y translate-toolkit python3-gnupg python3-yaml python3-requests && rm -rf /var/lib/apt/lists/*
ADD . /websites
WORKDIR /websites
RUN .build/load_gpg.sh
# Uncomment this if you want to fetch Cloud AMIs list at build time
# RUN python3 .build/fetch_amis.py content/release.yml content/editions/cloud/ami_list.yml
RUN npm install
RUN npm run generate

FROM quay.io/fedora/fedora:37
RUN dnf -y install s3cmd  && dnf clean all
COPY --from=build /websites/.output/public /output
