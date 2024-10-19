Add to dhcpd.conf:
```
# Write logfile
on commit {
    set clip = binary-to-ascii(10, 8, ".", leased-address);
    set clhw = binary-to-ascii(16, 8, ":", substring(hardware, 1, 6));
    set ClientHost = pick-first-value(
        host-decl-name,
        option fqdn.hostname,
        option host-name,
        "none");
    execute("/etc/sh_cmd/dhcpd_eventlog.py", clip, clhw, ClientHost);
}
```

Each dhcp lease IP write to log file, for example /var/log/dhcpd/172.21.0.10.log contain:

>Commit IP: 172.21.0.10, with MAC: 60:22:32:26:84:22, and NAME: pc-01 DATE: 2023-06-20 16:56:55.990941<br />
>Commit IP: 172.21.0.10, with MAC: 60:22:32:26:84:22, and NAME: pc-01 DATE: 2023-06-20 17:02:01.570685<br />
>Commit IP: 172.21.0.10, with MAC: 60:22:32:26:84:22, and NAME: pc-01 DATE: 2023-06-20 17:06:03.487698<br />
>Commit IP: 172.21.0.10, with MAC: 60:22:32:26:84:22, and NAME: pc-01 DATE: 2023-06-20 17:15:26.171225<br />
>Commit IP: 172.21.0.10, with MAC: 60:22:32:26:84:22, and NAME: pc-01 DATE: 2023-06-20 17:20:26.847612<br />
