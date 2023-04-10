# Apache Kafka

## What is Apache Kafka
Apache Kafka is a Distributed Event Streaming solution  
Kafka can efficiently manages billions of events:
- Publish and subscribe to streams of records
- Quickly scale up with minimal downtime
- Process streams of records in real-time

Ideal for streaming applications:
- Geolocation Data (Uber, Lyft, etc.)
- Log Processing (Spotify, Netflix, etc.)
- Big Data (Real-time) Analytics (Cloudflare, etc.)

## Logical Replication 
PostgreSQL Logical Replication (pgoutput):
- Logical replication is a method of replicating data objects and their changes, based upon their replication identity (usually a primary key)
- Logical replication uses a publish and subscribe model (Pub/Sub)
- Pub/Sub provides a framework for exchanging messages between publishers and subscribers

Debezium Postgres Connector:
- Debezium PostgreSQL connector captures row-level changes in the schemas of a PostgreSQL database
- Connector subscribe to Postgres Replication logs
- Stream database changes to a Kafka Topic