# IAM: governance

AWS Identity and Access Management controls who can call which AWS APIs. A **user** represents a person or application identity; a **group** collects users; a **role** grants temporary permissions to a trusted principal such as an EC2 instance or GitHub OIDC session. A **policy** is a JSON document of allowed or denied actions on resources, optionally under conditions. Permissions are the effective result of identity policies, resource policies, boundaries, and organization controls.

Least privilege means granting only the actions and resources actually needed. For a CI pipeline that uploads one artifact, grant write access to one bucket prefix, not `s3:*` on all buckets. Prefer roles and short-lived credentials to long-lived access keys, enable MFA for people, review unused permissions, and separate administrator from daily access. Typical uses include letting EC2 read S3, allowing a deploy job to push images, and giving auditors read-only access.
