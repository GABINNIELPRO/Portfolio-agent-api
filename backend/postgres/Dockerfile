FROM postgres:15

# Installer pgvector depuis apt
RUN apt-get update && \
    apt-get install -y postgresql-15-pgvector && \
    rm -rf /var/lib/apt/lists/*

# Expose
EXPOSE 5432
