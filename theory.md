## WHAT IS LB?
LB is a device (either a software or a hardware) that is used to route the incoming requests to one of the servers from the available pool.
So, it can be thought of as a traffic cop that directs traffic to the proper lane to reduce congestion.

## WHAT IS ITS NEED?
LB becomes important when we have multiple users accessing our servers and we need to ensure proper utilisation of the server resources.

## SOME ADVANTAGES?
- Improves the resources utilisation
- Helps in scaling of the servers according to demand
- Overall, it reduces the downtime of the servers
- Can help with session persistence (users are reconnected to the same server, ensuring efficient utilisation of cache)

## HARDWARE VS SOFTWARE?
The choice between both is more a question of the requirements of the users
- Hardware LB are more robust in the sense that they are not directly dependent on the OS of the system, whereas Software LB is sensitive to the changes in environment.
- Hardware LB can't be upgraded directly and we need to get a new one in case our requirements exceed the current device, whereas Software LB are much more flexible.

## LOCATION IN SEVEN LAYER OSI MODEL?
Load balancing can be performed at various levels.
- Layer 7 is more CPU intensive than Layer 4. 
- Layer 7 allows for more smarter decisions and optimisations as compared to Layer 4.