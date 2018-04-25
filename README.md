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

```python
from libzmap import ZmapProcess

proc = ZmapProcess(targets='101.200.188.97/20', options='-B 100M', probe_module='icmp_echoscan')
for obj in proc.run():
    print vars(obj)
```


Python Support
--------------

The libnmap code is tested against the following python interpreters:

- Python 2.7 (Test on ubuntu-15.10 with zmap-2.1.0);


About me
------------

gushitong@gmail.com, Welcome to pull requests! 
