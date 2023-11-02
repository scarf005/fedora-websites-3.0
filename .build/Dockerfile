FROM docker.io/library/node:18 as build
RUN apt-get update && apt-get install -y translate-toolkit python3-gnupg python3-yaml python3-requests git && rm -rf /var/lib/apt/lists/*
ADD . /websites
WORKDIR /websites
# Update submodules to the latest version available
RUN git submodule update --remote && git submodule status
RUN .build/load_gpg.sh
# Uncomment this if you want to fetch Cloud AMIs list at build time
# RUN python3 .build/fetch_amis.py content/release.yml content/editions/cloud/ami_list.yml
RUN npm install
RUN NODE_OPTIONS=--max_old_space_size=8192 npm run generate
# override default 404 error page with the custom one
RUN cp -v .output/public/404/index.html .output/public/404.html

FROM quay.io/fedora/fedora:38
RUN dnf -y install s3cmd  && dnf clean all
COPY --from=build /websites/.output/public /output
