# Ports snapshot (2025-09-04 00:22:11 UTC)

## Listening (ss -ltnp)
```
State  Recv-Q Send-Q  Local Address:Port  Peer Address:PortProcess                                                         
LISTEN 0      511         127.0.0.1:44723      0.0.0.0:*    users:(("node",pid=602053,fd=21))                              
LISTEN 0      4096    127.0.0.53%lo:53         0.0.0.0:*                                                                   
LISTEN 0      5             0.0.0.0:8080       0.0.0.0:*    users:(("python3",pid=409,fd=3))                               
LISTEN 0      50            0.0.0.0:4002       0.0.0.0:*    users:(("twistd",pid=562947,fd=12))                            
LISTEN 0      100           0.0.0.0:4010       0.0.0.0:*    users:(("python3",pid=630644,fd=6))                            
LISTEN 0      4096          0.0.0.0:22         0.0.0.0:*                                                                   
LISTEN 0      50            0.0.0.0:4100       0.0.0.0:*    users:(("twistd",pid=562947,fd=11))                            
LISTEN 0      50            0.0.0.0:4105       0.0.0.0:*    users:(("twistd",pid=562947,fd=13))                            
LISTEN 0      1000   10.255.255.254:53         0.0.0.0:*                                                                   
LISTEN 0      100           0.0.0.0:5101       0.0.0.0:*    users:(("python3",pid=564320,fd=6))                            
LISTEN 0      2048          0.0.0.0:5100       0.0.0.0:*    users:(("python3",pid=784425,fd=3),("python3",pid=566121,fd=3))
LISTEN 0      4096        127.0.0.1:2019       0.0.0.0:*                                                                   
LISTEN 0      4096          0.0.0.0:631        0.0.0.0:*                                                                   
LISTEN 0      50          127.0.0.1:4115       0.0.0.0:*    users:(("twistd",pid=566043,fd=11))                            
LISTEN 0      50          127.0.0.1:4106       0.0.0.0:*    users:(("twistd",pid=562947,fd=10))                            
LISTEN 0      4096       127.0.0.54:53         0.0.0.0:*                                                                   
LISTEN 0      4096                *:80               *:*                                                                   
LISTEN 0      4096             [::]:22            [::]:*                                                                   
LISTEN 0      4096             [::]:631           [::]:*                                                                   
LISTEN 0      511                 *:5443             *:*    users:(("node",pid=754579,fd=22))                              
LISTEN 0      511                 *:5644             *:*    users:(("node",pid=603750,fd=22))                              
```

## Common Mistwood ports (4010, 5100–5199)
```
LISTEN 0      100           0.0.0.0:4010       0.0.0.0:*    users:(("python3",pid=630644,fd=6))                            
LISTEN 0      100           0.0.0.0:5101       0.0.0.0:*    users:(("python3",pid=564320,fd=6))                            
LISTEN 0      2048          0.0.0.0:5100       0.0.0.0:*    users:(("python3",pid=784425,fd=3),("python3",pid=566121,fd=3))
```
