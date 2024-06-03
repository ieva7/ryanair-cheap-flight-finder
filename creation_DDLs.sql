CREATE DATABASE IF NOT EXISTS finder;
CREATE SCHEMA IF NOT EXISTS flight_info;
CREATE TABLE IF NOT EXISTS destination_pairs (
    departure_airport VARCHAR NULL,
    arrival_airport VARCHAR NULL
);
