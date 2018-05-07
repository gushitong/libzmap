python-libzmap
==============

ZMap is an open-source network scanner that enables researchers to easily perform Internet-wide network studies. 
python-libzmap is a zmap-python binding, with full scan option support(tcp_synscan, icmp_echoscan, icmp_echo_time, udp, ntp, upnp)

Dependencies
------------

Make sure you have `zmap` installed: https://github.com/zmap/zmap


Install
--------

```bash
git clone https://github.com/gushitong/python-libzmap
```

```bash
cd python-libzmap && python setup.py install
```


Use case
-------

```bash
>>> from libzmap import ZmapProcess
>>> 
>>> proc = ZmapProcess(targets='101.200.188.97/20', options='-B 100M', probe_module='icmp_echoscan')
>>> for obj in proc.run():
...     print obj
... 
{'daddr': '172.30.8.34', 'code': '0', 'timestamp_ts': '1524630534', 'classification': 'echoreply', 'seq': '0', 'timestamp_us': '196136\n', 'saddr': '101.200.178.99', 'success': '1', 'icmp_id': '50011', 'saddr_raw': '1672661093', 'repeat': '0', 'ttl': '52', 'ipid': '20469', 'daddr_raw': '570957484', 'type': '0', 'cooldown': '1', 'timestamp_str': '2018-04-25T12:28:54.196+0800'}
{'daddr': '172.30.8.34', 'code': '0', 'timestamp_ts': '1524630534', 'classification': 'echoreply', 'seq': '0', 'timestamp_us': '196183\n', 'saddr': '101.200.176.161', 'success': '1', 'icmp_id': '25116', 'saddr_raw': '2712717413', 'repeat': '0', 'ttl': '52', 'ipid': '38111', 'daddr_raw': '570957484', 'type': '0', 'cooldown': '1', 'timestamp_str': '2018-04-25T12:28:54.196+0800'}
{'daddr': '172.30.8.34', 'code': '0', 'timestamp_ts': '1524630534', 'classification': 'echoreply', 'seq': '0', 'timestamp_us': '196199\n', 'saddr': '101.200.188.190', 'success': '1', 'icmp_id': '9652', 'saddr_raw': '3200043109', 'repeat': '0', 'ttl': '52', 'ipid': '45756', 'daddr_raw': '570957484', 'type': '0', 'cooldown': '1', 'timestamp_str': '2018-04-25T12:28:54.196+0800'}
{'daddr': '172.30.8.34', 'code': '0', 'timestamp_ts': '1524630534', 'classification': 'echoreply', 'seq': '0', 'timestamp_us': '196216\n', 'saddr': '101.200.177.21', 'success': '1', 'icmp_id': '59041', 'saddr_raw': '363972709', 'repeat': '0', 'ttl': '52', 'ipid': '63177', 'daddr_raw': '570957484', 'type': '0', 'cooldown': '1', 'timestamp_str': '2018-04-25T12:28:54.196+0800'}
...
```

ZmapProcess Args
------------------
* targets: ip address wildcard. (eg: `101.200.188.97/20`)
* port: target port. (eg: `80`)
* probe_module: zmap probe_module supported. (`tcp_synscan`, `icmp_echoscan`, `icmp_echo_time`,  `udp`, `upnp`)
* options: zmap scan params. (eg: `-B 100M`)
* fqp: path to zmap binary. (eg: `zmap`)
* yield_raw: if `True`, will yield raw zmap output(type `str`) instead of packed object. For debug purpose.


Python Support
--------------

The libnmap code is tested against the following python interpreters:

- Python 2.7 (Test on ubuntu-15.10 with zmap-2.1.0);


About me
------------

gushitong@gmail.com, Welcome to pull requests! 
