#!/bin/bash


# Delete postgres and pgadmin container 
docker container rm flask-postgres flask-pgadmin --force

# Delete network
# docker network rm bdd_backend

# Delete volumes
docker volume rm postgres_flask-pgadmin-data postgres_flask-postgres-data postgres_flask-scripts_sql postgres_flask-postgres-conf

# Delete data
sudo chown -R ${USER}:${USER} postgres-data
#rm -rf postgres-data/*
