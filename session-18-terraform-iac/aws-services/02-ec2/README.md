# EC2: compute

Amazon EC2 supplies virtual servers. An **AMI** is the machine image; an **instance type** sets CPU, memory, and network capacity. A **key pair** can be used for SSH login, while a **security group** is a stateful virtual firewall. **EBS** is block storage attached to instances. A public IP can be reached through an internet gateway if routes and security rules allow it; a private IP is for VPC communication.

An instance goes from pending to running, then may be stopped, started, or terminated. Stopping keeps EBS root storage but compute billing stops; terminating deletes the instance and may delete root volume according to configuration. Uses include web servers, batch workers, and self-managed services. The Session 19 example creates a `t3.micro` without opening SSH, exposing only port 80 for the networking exercise.
