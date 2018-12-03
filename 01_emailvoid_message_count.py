#!/usr/bin/python

from __future__ import print_function

from logging import getLogger, basicConfig, DEBUG
from unittest import TestCase, main
from emailvoid import EmailVoidClient


class Test39188(TestCase):
    def setUp(self):
        """ Precondition
        """
        self.__log = getLogger('Test39188')
        self._apikey = "4f016ffc-437e-4750-8b2d-d0dbc89de7fc"
        self._client = EmailVoidClient(apikey=self._apikey)


    def runTest(self):
        """ Receive message count on emailvoid.com server
        """
        # Step 0. Define const
        domain = 'emailvoid.com'
        # Step 1. Check message count
        msg_count = self._client.msg_count(domain=domain)
        self.__log.debug("msg_count = {msg_count!r}".format(msg_count=msg_count))


    def tearDown(self):
        """ Dispose clisent
        """
        if self._client:
            self._client.dispose()
            self._client = None



if __name__ == "__main__":
    basicConfig(filename="01_emailvoid_message_count.log", level=DEBUG)
    main()
