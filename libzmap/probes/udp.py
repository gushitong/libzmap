class Udp(object):

    output_fields = (
        'saddr', 'saddr_raw', 'daddr', 'daddr_raw', 'ipid', 'ttl', 'classification', 'success', 'sport', 'dport',
        'icmp_responder', 'icmp_type', 'icmp_code', 'icmp_unreach_str', 'udp_pkt_size', 'data', 'repeat', 'cooldown',
        'timestamp_str', 'timestamp_ts', 'timestamp_us'
    )

    def __init__(self, saddr, saddr_raw, daddr, daddr_raw, ipid, ttl, classification, success, sport, dport,
                 icmp_responder, icmp_type, icmp_code, icmp_unreach_str, udp_pkt_size, data, repeat, cooldown,
                 timestamp_str, timestamp_ts, timestamp_us):
        """
        :param:  saddr           string: source IP address of response
        :param:  saddr-raw          int: network order integer form of source IP address
        :param:  daddr           string: destination IP address of response
        :param:  daddr-raw          int: network order integer form of destination IP address
        :param:  ipid               int: IP identification number of response
        :param:  ttl                int: time-to-live of response packet
        :param:  classification  string: packet classification
        :param:  success            int: is response considered success
        :param:  sport              int: UDP source port
        :param:  dport              int: UDP destination port
        :param:  icmp_responder  string: Source IP of ICMP_UNREACH message
        :param:  icmp_type          int: icmp message type
        :param:  icmp_code          int: icmp message sub type code
        :param:  icmp_unreach_str string: for icmp_unreach responses, the string version of icmp_code (e.g. network-unreach)
        :param:  udp_pkt_size       int: UDP packet length
        :param:  data            binary: UDP payload
        :param:  repeat             int: Is response a repeat response from host
        :param:  cooldown           int: Was response received during the cooldown period
        :param:  timestamp-str   string: timestamp of when response arrived in ISO8601 format.
        :param:  timestamp-ts       int: timestamp of when response arrived in seconds since Epoch
        :param:  timestamp-us       int: microsecond part of timestamp (e.g. microseconds since 'timestamp-ts')
        """

        self.saddr = saddr
        self.saddr_raw = saddr_raw
        self.daddr = daddr
        self.daddr_raw = daddr_raw
        self.ipid = ipid
        self.ttl = ttl
        self.classification = classification
        self.success = success
        self.sport = sport
        self.dport = dport
        self.icmp_responder = icmp_responder
        self.icmp_type = icmp_type
        self.icmp_code = icmp_code
        self.icmp_unreach_str = icmp_unreach_str
        self.udp_pkt_size = udp_pkt_size
        self.data = data
        self.repeat = repeat
        self.cooldown = cooldown
        self.timestamp_str = timestamp_str
        self.timestamp_ts = timestamp_ts
        self.timestamp_us = timestamp_us

    def __str__(self):
        return str(self.__dict__)

