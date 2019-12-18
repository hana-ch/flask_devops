/* Database test creation */

/* Create App flask user */
CREATE USER userapp WITH ENCRYPTED PASSWORD 'password';

/* Create Database */ 
CREATE DATABASE appdb OWNER userapp;

/* Granting all rights to pi */
GRANT ALL PRIVILEGES ON DATABASE appdb TO userapp;

