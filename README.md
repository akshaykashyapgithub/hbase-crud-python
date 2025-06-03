# HBase CRUD with Python and Docker

This project demonstrates how to perform basic CRUD operations (Create, Read, Update, Delete) on Apache HBase using Python. The setup uses Docker to run HBase and the `happybase` library to connect via the Thrift interface.

## Project Description

Apache HBase is a distributed, scalable, big data store that works on top of Hadoop HDFS. This project sets up HBase locally in a Docker container and uses Python to interact with it using the Thrift interface.

The Python script performs the following operations:
- Creates an HBase table with a column family
- Inserts a row into the table
- Reads the inserted row
- Updates the row by modifying a column
- Deletes the row

## How It Works

1. **Docker Setup**  
   The HBase Docker container is started using a `docker-compose.yml` file. It exposes necessary ports including 16010 for the HBase UI and 9090 for the Thrift server used by the Python client.

2. **Python Client (happybase)**  
   The Python script connects to HBase using the `happybase` library, which communicates over the Thrift protocol. The script handles all the CRUD operations programmatically.

3. **Create Table**  
   A new table is created with a column family (e.g., `cf1`) if it doesn’t already exist.

4. **Insert Data**  
   Data is inserted into the table using a unique row key.

5. **Read Data**  
   The script reads the row using the row key and displays the column values.

6. **Update Data**  
   A new value is inserted using the same row key to simulate an update operation.

7. **Delete Data**  
   The row is deleted from the table.

## Requirements

- Docker and Docker Compose
- Python 3.x
- happybase Python package

## Setup Instructions

1. Start the HBase container using Docker Compose.
2. Run the `hbase_crud.py` script to perform the operations.

## Notes

- The HBase Web UI is accessible at `http://localhost:16010`.
- Ensure that the Thrift server (port 9090) is running inside the container.
- The Python script assumes HBase is accessible on `localhost` and port `9090`.
