from .probes import *


class ZmapParser(object):
    def __init__(self, probe_module_name):
        """

        :param probe_module_name:
        """
        self.probe_module_name = probe_module_name

    def parse_line(self, line):
        """
        parse streamline
        :param line:
        :return:
        """
        qs = line.split(',')
        if any(k in self.loginfo for k in qs):
            return None
        if any(k in self.progressinfo for k in qs):
            return None
        if any(k in self.zmapkeywords for k in qs):
            return None
        return self.probe_module(*tuple(qs))
    def parse_csv(self):
        pass

    @property
    def probe_module(self):
        if self.probe_module_name == 'tcp_synscan':
            return TcpSyn
        elif self.probe_module_name == 'icmp_echoscan':
            return IcmpEcho
        elif self.probe_module_name == 'icmp_echo_time':
            return IcmpEchoTime
        elif self.probe_module_name == 'udp':
            return Udp
        elif self.probe_module_name == 'upnp':
            return Upnp
        else:
            raise RuntimeError(1, 'Unsupported zmap probe module %s' % self.probe_module_name)

    @property
    def output_fields(self):
        return self.probe_module.output_fields

    @property
    def loginfo(self):
        return ('CRITICAL', 'DEBUG', 'ERROR', 'FATAL', 'INFO', 'WARN', 'WARNING',
                'critical', 'debug', 'error', 'fatal', 'info', 'warn', 'warning')

    @property
    def progressinfo(self):
        return ('send', 'recv', 'done', 'drops', 'hitrate')

    @property
    def zmapkeywords(self):
        return (
            'saddr', 'saddr_raw', 'daddr', 'daddr_raw', 'ipid', 'ttl', 'classification', 'success', 'sport', 'dport',
            'icmp_responder', 'icmp_type', 'icmp_code', 'icmp_unreach_str', 'udp_pkt_size', 'data', 'repeat',
            'cooldown',
            'timestamp_str', 'timestamp_ts', 'timestamp_us'
        )
