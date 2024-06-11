DROP DATABASE IF EXISTS flights;
CREATE DATABASE flights;
\c flights;
CREATE TABLE IF NOT EXISTS destination_pairs(
    departure_airport VARCHAR NULL,
    arrival_airport VARCHAR NULL
);
