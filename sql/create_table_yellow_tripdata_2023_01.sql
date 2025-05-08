-- Athena table definition for Yellow Taxi January 2023
-- S3 bucket is private and requires AWS credentials to access

CREATE DATABASE IF NOT EXISTS taxi_project;

CREATE EXTERNAL TABLE IF NOT EXISTS taxi_project.yellow_tripdata_2023_01 (
  vendor_id string,
  tpep_pickup_datetime timestamp,
  tpep_dropoff_datetime timestamp,
  passenger_count int,
  trip_distance double,
  rate_code_id int,
  store_and_fwd_flag string,
  pu_location_id int,
  do_location_id int,
  payment_type int,
  fare_amount double,
  extra double,
  mta_tax double,
  tip_amount double,
  tolls_amount double,
  improvement_surcharge double,
  total_amount double,
  congestion_surcharge double
)
STORED AS PARQUET
LOCATION 's3://strath-nyc-taxi/raw/2023/01/'
