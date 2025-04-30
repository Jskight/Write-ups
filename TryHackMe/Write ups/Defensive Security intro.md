# Defensive Security intro

## The Scenario

Let us pretend you are a Security Operations Center (SOC) analyst responsible for protecting a bank. This bank's SOC uses a Security Information and Event Management (SIEM) tool, which gathers security-related information and events from various sources and presents them in one dashboard. If the SIEM finds something suspicious, an alert will be generated.

Not all alerts are malicious, however. It is up to the analyst to use their expertise in cyber security to investigate which ones are harmful.

For example, you may encounter an alert where a user has failed multiple login attempts. While suspicious, this kind of thing happens, especially if the user has forgotten their password and continues to try to log in. 

Additionally, there might be alerts related to connections from unknown IP addresses. An IP address is like a home address for your computer on the Internet—it tells other computers where to send the information you request. When these addresses are unknown, it could mean that someone new is trying to connect or someone is attempting unauthorized access.

![image](../Write%20ups/images/SIEM1.png)

In the image above we can see alert log. 

Lets take a look at that Unauthorized connection from ```143.110.250.149:22```

![image](../Write%20ups/images/SIEM2.png)

we want to take a closer look at the IP address making the unauthorized connection attempt, so we'll check it out on a site that contains a list on known malicious IPs.

![image](../Write%20ups/images/ipscan2.png)

Lets go ahead an escalate the issue to our Team Lead

![image](../Write%20ups/images/lead.png)

Our Team Lead advised that we have permission to Implement a block rule for the malicious IP

![image](../Write%20ups/images/block.png)
![image](../Write%20ups/images/block2.png)