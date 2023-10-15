# Postmortem
![Attck Meme](ddos-packets.webp)
# Postmortem
## Summary
Global outage of payment service from 9th October 2023 at 8:00 am EAT to 15th October 2023 at 6:00 pm EAT affecting all users and caused by Distributed Denial-of-Service (DDOS) attacks.
The issue affected the availability of payment service causing customer attrition and loss of revenue. It was marked as a critical incident level. There were persistent complaints from customers that they were not able to make payments through the service. Monitoring alerts kept coming from the monitoring tools indicating that there was increased load on the servers. 

## Timeline
- The issue was detected on 9th October 2023 at 8:00 am, through monitoring alerts and Customer complaints. 
- At 8:15 am the Firewalls and gateway were configured to restrict access to the systems to limit traffic from DDOS attack
- A misleading debugging/investigation path included increasing server capacity through scaling with the thinking that the servers were being overwhelmed with genuine traffic
- The incident was escalated to the security team since it was an attack
- The incident was resolved through the application of firewall rules and gateway

## Root cause
- The main cause of the incident was a DDOS attack from unknown malicious hackers.
- Unknown hackers kept sending traffic in a coordinated attack from several clients. This greatly affected the performance of the application and servers and made the service inaccessible throughout the incident duration. 
- With firewall rules and the gateway, the security team enforced system access restrictions to limit the traffic from the same IP address per second.
- A Web Application Firewall (WAF) and application gateway were used for rate-limiting requests based on some parameters. These configurations throttled the requests when the number exceeded certain limits


## Corrective and preventative measures
- (Stricter) Firewall rules were put in place to limit traffic from suspicious IP addresses and rate-limiting of traffic was applied to prevent the reoccurrence of the incident.
- Server redundancy was also put in place to make it difficult for hackers to attack all servers at the same time. This ensures that the service remains accessible if attackers launch DDOS attack on one of the server.
- Tasks done to address the issue included:
  1. Updating firewall rules to enforce rate-limiting
  2. Setting up the Application gateway to mitigate DDOS attacks by throttling the requests that exceed certain set parameters
  3. Setting up intrusion detection systems to automatically detect anomalies before impacting customers.
