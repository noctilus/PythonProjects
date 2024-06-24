# Port redirection on the same firewall - Linux

<https://serverfault.com/questions/238563/can-i-use-ufw-to-setup-a-port-forward>

#### First way

Let's say you want to forward requests going to 80 to a server listening on port 8080.

Note that you will need to make sure port 8080 is allowed,
otherwise ufw will block the requests that are redirected to 8080.

```
sudo ufw allow 8080/tcp
```

There are no ufw commands for setting up the port forwards, so it must be done via configuraton files. Add the lines below to /etc/ufw/before.rules, before the filter section, right at the top of the file:

\*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
COMMIT

Then restart and enable ufw to start on boot:

sudo ufw enable

#### Other way?

Since ufw 0.34 ufw supports forward rules.

example: sudo ufw route allow in on eth0 out on eth1 to 10.0.0.0/8 port 8080 from 192.168.0.0/16 port 80

You also need to make sure you have the sysctl net.ipv4.ip_forward enabled. For most distributions, that's done by editing /etc/sysctl.conf and running sysctl -p or rebooting.

ufw doesn't support NAT through it's easy interface, though.
