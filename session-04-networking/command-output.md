# Networking command output

Captured on 7 October 2026 from this machine. DNS addresses and timing can change.

```text
$ dig example.com +short
172.66.147.243
104.20.23.154

$ ping -c 2 example.com
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 64.610/70.127/75.645/5.517 ms

$ curl -IsS https://example.com
HTTP/2 200
content-type: text/html; charset=utf-8
server: cloudflare

$ netstat -rn
default route present on en0
loopback route present on lo0
```

`dig` showed that the hostname resolved; `ping` showed ICMP replies; `curl` confirmed a successful HTTPS response. A route table includes a default route and local loopback route. Private gateway details are omitted.
