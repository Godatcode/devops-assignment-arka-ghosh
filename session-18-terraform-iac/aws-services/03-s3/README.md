# S3: storage

Amazon S3 stores objects inside buckets. An object has a key and data; a bucket name is globally unique. Storage classes trade access time and price, so a lifecycle policy can move old objects to a cheaper class or expire them. Versioning keeps previous object versions and helps recover from accidental overwrite or deletion. Encryption protects stored data; bucket policies and IAM policies control access.

In the Terraform lab, the bucket has versioning, server-side AES256 encryption, and a public access block. Common uses are backups, logs, static assets, and build artifacts. A bucket is not a filesystem: applications should use S3 APIs rather than expecting POSIX file locking.
