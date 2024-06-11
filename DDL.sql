DROP DATABASE IF EXISTS flights;
CREATE DATABASE flights;
\c flights;
CREATE SCHEMA IF NOT EXISTS flight_info;
SET search_path TO flight_info;
CREATE TABLE IF NOT EXISTS flight_info.destination_pairs(
    departure_airport VARCHAR NULL,
    arrival_airport VARCHAR NULL
);
