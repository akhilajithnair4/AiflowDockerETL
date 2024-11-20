FROM quay.io/astronomer/astro-runtime:12.4.0
USER root

# Install system dependencies required for pandas
RUN apt-get update && apt-get install -y --fix-missing \
    gcc \
    g++ \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    && apt-get clean

USER astro