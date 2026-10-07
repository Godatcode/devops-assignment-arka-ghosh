# Session 4: Networking commands

| Command | What I checked | What it means |
|---|---|---|
| `ifconfig` or `ip addr` | Interface addresses | Local IP address and interface status |
| `ping -c 2 example.com` | ICMP reachability | Replies show a route, but firewalls may block ICMP |
| `dig example.com` | DNS answer | Separates name resolution from HTTP |
| `traceroute example.com` | Route hops | Shows routers that respond to TTL expiry |
| `netstat -rn` or `ip route` | Route table | Default gateway and local routes |
| `curl -I https://example.com` | HTTP headers | Tests the application layer after DNS and TCP/TLS |
| `lsof -iTCP -sTCP:LISTEN -n -P` or `ss -ltn` | Listening ports | Shows which local process accepts connections |

I first check the local address and route, then DNS, then a direct connection. This order helps identify which layer failed. The file [`command-output.md`](command-output.md) contains captured output from this machine.
