import os
import platform
import shlex
import subprocess
from threading import Thread

from .parser import ZmapParser


class ZmapProcess(Thread):
    def __init__(self, targets='127.0.0.1', port=80, probe_module=None, options=None, fqp=None, yield_raw=False):
        """

        :param targets:
        :param port:
        :param options:
        :param fqp:
        :param yield_raw:
        """
        Thread.__init__(self)
        self.__zmap_targets = targets
        self.__zmap_port = port
        self.__zmap_options = options
        self.__zmap_proc = None
        self.__starttime = 0
        self.__endtime = 0
        self.__stdout = ''
        self.__stderr = ''
        self.__zmap_command_line = ''
        self.__zmap_rc = 0
        self.__zmap_binary_name = 'zmap'
        self.__zmap_binary = None
        self.__zmap_probe_module = probe_module if probe_module else 'tcp_synscan'
        self.__zmap_parser = ZmapParser(self.__zmap_probe_module)
        self.__yield_raw = yield_raw

        # more reliable than just using os.name() (cygwin)
        self.__is_windows = platform.system() == 'Windows'

        (self.DONE, self.READY, self.RUNNING,
         self.CANCELLED, self.FAILED) = range(5)

        self.__state = self.RUNNING

        if fqp:
            if os.path.isfile(fqp) and os.access(fqp, os.X_OK):
                self.__zmap_binary = fqp
            else:
                raise EnvironmentError(1, "wrong path or not executable", fqp)
        else:
            self.__zmap_binary_name = 'zmap'
            self.__zmap_binary = self._whereis(self.__zmap_binary_name)

    def _whereis(self, program):

        """
        Protected method enabling the object to find the full path of a binary
        from its PATH environment variable.

        :param program: name of a binary for which the full path needs to
        be discovered.

        :return: the full path to the binary.

        :todo: add a default path list in case PATH is empty.
        """
        split_char = ';' if self.__is_windows else ':'
        program = program + '.exe' if self.__is_windows else program
        for path in os.environ.get('PATH', '').split(split_char):
            if (os.path.exists(os.path.join(path, program)) and not
            os.path.isdir(os.path.join(path, program))):
                return os.path.join(path, program)
        return None

    def get_commandline(self):
        """

        :return:
        """
        output_fields = self.parser.output_fields
        args = [self.__zmap_binary, '-M', self.__zmap_probe_module, '-p', self.__zmap_port, '-f',
                ','.join(output_fields), self.__zmap_options, self.__zmap_targets]
        args = [str(item) for item in args]
        return ' '.join(args)

    def run(self):
        cmdline = self.get_commandline()
        try:
            self.__zmap_proc = subprocess.Popen(args=shlex.split(cmdline), stdout=subprocess.PIPE,
                                                stderr=subprocess.PIPE,
                                                universal_newlines=True, bufsize=0)
        except OSError, e:
            print(e)
            raise EnvironmentError(1, "zmap is not installed or could not be found in system path")

        while self.__zmap_proc.poll() is None:
            for streamline in iter(self.__zmap_proc.stdout.readline, ''):
                if self.__yield_raw:
                    yield streamline
                else:
                    obj = self.parser.parse_line(streamline)
                    if obj:
                        yield obj

        self.__stderr += self.__zmap_proc.stderr.read()
        # print self.__stderr
        self.__zmap_rc = self.__zmap_proc.poll()
        if self.rc is None:
            self.__state = self.CANCELLED
        elif self.rc == 0:
            self.__state = self.DONE
        else:
            self.__state = self.FAILED

    def run_background(self):
        """
        run zmap scan in background as a thread.
        For privileged scans, consider ZmapProcess.sudo_run_background()
        """
        self.__state = self.RUNNING
        super(ZmapProcess, self).start()

    def is_running(self):
        """
        Checks if zmap is still running.

        :return: True if zmap is still running
        """
        return self.state == self.RUNNING

    def has_terminated(self):
        """
        Checks if zmap has terminated. Could have failed or succeeded

        :return: True if zmap process is not running anymore.
        """
        return (self.state == self.DONE or self.state == self.FAILED or
                self.state == self.CANCELLED)

    def has_failed(self):
        """
        Checks if zmap has failed.

        :return: True if zmap process errored.
        """
        return self.state == self.FAILED

    def is_successful(self):
        """
        Checks if zmap terminated successfully.

        :return: True if zmap terminated successfully.
        """
        return self.state == self.DONE

    def stop(self):
        """
        Send KILL -15 to the zmap subprocess and gently ask the threads to
        stop.
        """
        self.__state = self.CANCELLED
        if self.__zmap_proc.poll() is None:
            self.__zmap_proc.kill()

    @property
    def command(self):
        """
        return the constructed zmap command or empty string if not
        constructed yet.

        :return: string
        """
        return self.__zmap_command_line or ''

    @property
    def targets(self):
        """
        Provides the list of targets to scan

        :return: list of string
        """
        return self.__zmap_targets

    @property
    def rc(self):
        return self.__zmap_rc

    @property
    def state(self):
        return self.__state

    @property
    def parser(self):
        return self.__zmap_parser


def main():
    proc = ZmapProcess(targets='101.200.188.97/20', options='-B 100M', probe_module='icmp_echoscan')
    for obj in proc.run():
        print vars(obj)


if __name__ == '__main__':
    main()
