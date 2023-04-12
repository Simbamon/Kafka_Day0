# Apache Kafka

## What is Apache Kafka
Apache Kafka is a Distributed Event Streaming solution  

* Kafka can efficiently manages billions of events:
    - Publish and subscribe to streams of records
    - Quickly scale up with minimal downtime
    - Process streams of records in real-time  

* Ideal for streaming applications:
    - Geolocation Data (Uber, Lyft, etc.)
    - Log Processing (Spotify, Netflix, etc.)
    - Big Data (Real-time) Analytics (Cloudflare, etc.)  

* Kafka Server (Broker):
    - Kafka server, also known as Kafka Broker, handles incoming requests to write messages to a topic
    - Kafka broekr allows consumers to fetch messages by topic  

* Kafka Topic:
    - A topic is a category/feed name to which recordes are stored and published
    - All Kafka records are organized into topics. Producer applications write data to topics and consumer applications read from topics

## Logical Replication 
* PostgreSQL Logical Replication (pgoutput):
    - Logical replication is a method of replicating data objects and their changes, based upon their replication identity (usually a primary key)
    - Logical replication uses a publish and subscribe model (Pub/Sub)
    - Pub/Sub provides a framework for exchanging messages between publishers and subscribers

* Debezium Postgres Connector:
    - Debezium PostgreSQL connector captures row-level changes in the schemas of a PostgreSQL database
    - Connector subscribe to Postgres Replication logs
    - Stream database changes to a Kafka Topic

## Debezium connector user permissions
- User must have Replication privileges in the database to add the table to a publication
- User must have CREATE privileges on the database to add publications
- User must have SELECT privileges on the tables to copy the initial table data
- A publication is essentially a group of tables whose data changes are intended to be replicated through logical replication

## Process
Postgres wal_level configuration  
wal_level determines how much information is written to the wal  
the default value is `replica`, which writes enough data to wal archiving and replication  
`logical` adds additional information necessary to support logical decoding  
1. In pgAdmin, type this query
    ```sql
    select * from pg_settings where name = 'wal_level';
    ```
2. Go to `postgresql.conf` to change the wal_level from replica to logical
    * If you are using PostgreSQL in a docker container, run
    ```sql
    ALTER SYSTEM SET wal_level = logical;
    ```
3. After change the config, go to Services and restart the `postgresql-x64-15` service
4. rerun the sql query to see the difference in wal_level setting
5. Make a user under postgres account with admin access

