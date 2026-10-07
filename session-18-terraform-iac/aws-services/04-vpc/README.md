# VPC: networking

A VPC is an isolated AWS network with a CIDR range, such as `10.42.0.0/16`. Subnets divide that range. A route table decides where traffic goes; an Internet Gateway provides an internet route for a public subnet, while a NAT Gateway can allow outbound internet access from private subnets without making instances directly reachable. A subnet is public when it has a route to an Internet Gateway; simply assigning a public IP is not enough.

Security groups are stateful instance-level rules. Network ACLs are stateless subnet-level rules. The Session 19 project creates a public subnet, route to the Internet Gateway, a security group permitting HTTP, and an EC2 instance. A production design would put databases in private subnets and limit inbound access further.
