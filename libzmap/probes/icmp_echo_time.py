class IcmpEchoTime(object):
    output_fields = (
        'saddr', 'saddr_raw', 'daddr', 'daddr_raw', 'ipid', 'ttl', 'type', 'code', 'icmp_id', 'seq',
        'sent_timestamp_ts', 'sent_timestamp_us', 'dst_raw', 'classification', 'success', 'repeat',
        'cooldown', 'timestamp_str', 'timestamp_ts', 'timestamp_us'
    )

    def __init__(self, saddr, saddr_raw, daddr, daddr_raw, ipid, ttl, _type, code, icmp_id, seq, sent_timestamp_ts,
                 sent_timestamp_us, dst_raw, classification, success, repeat, cooldown, timestamp_str, timestamp_ts,
                 timestamp_us):
        """
        :param:  saddr           string: source IP address of response
        :param:  saddr-raw          int: network order integer form of source IP address
        :param:  daddr           string: destination IP address of response
        :param:  daddr-raw          int: network order integer form of destination IP address
        :param:  ipid               int: IP identification number of response
        :param:  ttl                int: time-to-live of response packet
        :param:  type               int: icmp message type
        :param:  code               int: icmp message sub type code
        :param:  icmp-id            int: icmp id number
        :param:  seq                int: icmp sequence number
        :param:  sent-timestamp-ts    int: timestamp of sent probe in seconds since Epoch
        :param:  sent-timestamp-us    int: microsecond part of sent timestamp
        :param:  dst-raw            int: raw destination IP address of sent probe
        :param:  classification  string: probe module classification
        :param:  success            int: did probe module classify response as success
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
        self.type = _type
        self.code = code
        self.icmp_id = icmp_id
        self.seq = seq
        self.sent_timestamp_ts = sent_timestamp_ts
        self.sent_timestamp_us = sent_timestamp_us
        self.dst_raw = dst_raw
        self.classification = classification
        self.success = success
        self.repeat = repeat
        self.cooldown = cooldown
        self.timestamp_str = timestamp_str
        self.timestamp_ts = timestamp_ts
        self.timestamp_us = timestamp_us

    def __str__(self):
        return str(self.__dict__)



