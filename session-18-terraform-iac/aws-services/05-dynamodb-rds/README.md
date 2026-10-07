# DynamoDB and RDS: database services

**DynamoDB** is a managed NoSQL database. Data is arranged in tables of items and attributes. Every item has a partition key; a sort key is optional and allows multiple items within one partition. Query access patterns should guide key design. It suits low-latency key-value and document workloads such as sessions, carts, and event metadata.

**RDS** runs managed relational engines such as PostgreSQL and MySQL. A DB instance supplies compute and storage. Security groups and authentication limit access; automated backups support recovery. Multi-AZ improves availability through a standby, while read replicas can serve read-heavy traffic and are not the same as a synchronous HA standby. RDS suits relational transactions, joins, and structured application data. For the final task board, moving SQLite to RDS would allow multiple app replicas to share one database.
