class IcmpEcho(object):
    output_fields = (
        'saddr', 'saddr-raw', 'daddr', 'daddr-raw', 'ipid', 'ttl', 'type', 'code', 'icmp-id',
        'seq', 'classification', 'success', 'repeat', 'cooldown', 'timestamp-str', 'timestamp-ts', 'timestamp-us'
    )

    def __init__(self, saddr, saddr_raw, daddr, daddr_raw, ipid, ttl, _type, code, icmp_id, seq, classification,
                 success, repeat, cooldown, timestamp_str, timestamp_ts, timestamp_us):
        """

        :param saddr: source IP address of response
        :param saddr_raw: network order integer form of source IP address
        :param daddr: destination IP address of response
        :param daddr_raw: network order integer form of destination IP address
        :param ipid: IP identification number of response
        :param ttl: time-to-live of response packet
        :param _type: icmp message type
        :param code: icmp message sub type code
        :param icmp_id: icmp id number
        :param seq: icmp sequence number
        :param classification: probe module classification
        :param success: did probe module classify response as success
        :param repeat: Is response a repeat response from host
        :param cooldown: Was response received during the cooldown period
        :param timestamp_str:  timestamp of when response arrived in ISO8601 format.
        :param timestamp_ts: timestamp of when response arrived in seconds since Epoch
        :param timestamp_us:  microsecond part of timestamp (e.g. microseconds since 'timestamp-ts')
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
        self.classification = classification
        self.success = success
        self.repeat = repeat
        self.cooldown = cooldown
        self.timestamp_str = timestamp_str
        self.timestamp_ts = timestamp_ts
        self.timestamp_us = timestamp_us

    def __str__(self):
        return str(self.__dict__)


