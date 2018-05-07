class TcpSyn(object):

    output_fields = (
        'saddr-raw', 'daddr', 'daddr-raw', 'ipid', 'ttl', 'sport', 'dport', 'seqnum', 'acknum', 'window',
        'classification', 'success', 'repeat', 'cooldown', 'timestamp-str', 'timestamp-ts', 'timestamp-us'
    )

    def __init__(self, saddr, saddr_raw, daddr, daddr_raw, ipid, ttl, sport, dport, seqnum, acknum, window, classification,
                 success, repeat, cooldown, timestamp_str, timestamp_ts, timestamp_us):
        """
        :param saddr: string: source IP address of response
        :param saddr_raw: int: network order integer form of source IP address
        :param daddr: string: destination IP address of response
        :param daddr_raw: string: destination IP address of response
        :param ipid: int: IP identification number of response
        :param ttl: int: time-to-live of response packet
        :param sport: int: TCP source port
        :param dport: int: TCP destination port
        :param seqnum: int: TCP sequence number
        :param acknum: int: TCP acknowledgement number
        :param window:  int: TCP window
        :param classification: string: packet classification
        :param success: string: is response considered success
        :param repeat: int: Is response a repeat response from host
        :param cooldown: int: int: Was response received during the cooldown period
        :param timestamp_str: string: timestamp of when response arrived in ISO8601 format.
        :param timestamp_ts: int: timestamp of when response arrived in seconds since Epoch
        :param timestamp_us: int: microsecond part of timestamp (e.g. microseconds since 'timestamp-ts')
        :return:
        """
        self.saddr = saddr
        self.saddr_raw = saddr_raw
        self.daddr = daddr
        self.daddr_raw = daddr_raw
        self.ipid = ipid
        self.ttl = ttl
        self.sport = sport
        self.dport = dport
        self.seqnum = seqnum
        self.acknum = acknum
        self.window = window
        self.classification = classification
        self.success = success
        self.repeat = repeat
        self.cooldown = cooldown
        self.timestamp_str = timestamp_str
        self.timestamp_ts = timestamp_ts
        self.timestamp_us = timestamp_us

    def __str__(self):
        return str(self.__dict__)
