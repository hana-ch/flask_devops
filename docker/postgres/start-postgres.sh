#!/bin/bash


mkdir -p ./postgres-data
mkdir -p ./pgadmin-data

# Execution of postgres
echo "Start PostgreSQL and PGAdmin container"
docker-compose -f docker-compose.yaml up -d

sleep 5

docker exec -it flask-postgres rm /var/lib/postgresql/data/postgresql.conf /var/lib/postgresql/data/postgresql.auto.conf
docker exec -it flask-postgres cp /etc/postgres-conf/postgresql.conf /var/lib/postgresql/data/postgresql.conf
docker exec -it flask-postgres chown postgres: /var/lib/postgresql/data/postgresql.conf
docker exec -it flask-postgres runuser -l postgres -c '/usr/lib/postgresql/11/bin/pg_ctl reload -D /var/lib/postgresql/data'

# Init database
echo "Initialise database"
docker exec -it flask-postgres /scripts_sql/createSchema.sh

# Import data
#rm -f scripts_sql/import/*.sql
#rm -f scripts_sql/import/treated/*.sql
#rm -f scripts_sql/import/failed/*.sql
#cp ImportUserFile/*.sql scripts_sql/import 

# Import User
#docker exec -it postgres /scripts_sql/importUser.sh
