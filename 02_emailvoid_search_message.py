#!/usr/bin/python

from __future__ import print_function

from logging import getLogger, basicConfig, DEBUG
from unittest import TestCase, main
from emailvoid import EmailVoidClient


class Test39189(TestCase):
    def setUp(self):
        """ Precondition
        """
        self.__log = getLogger('Test39189')
        self._apikey = "4f016ffc-437e-4750-8b2d-d0dbc89de7fc"
        self._client = EmailVoidClient(apikey=self._apikey)


    def runTest(self):
        """ Search message on server
        """
        # Step 0. Define const
        domain = 'emailvoid.com'
        # Step 2. Search messages
        items = self._client.msg_search(domain=domain)
        for item in items:
            self.__log.debug("item = {item!r}".format(item=item))
            #msgid = item.get_msgid()


    def tearDown(self):
        """ Dispose clisent
        """
        if self._client:
            self._client.dispose()
            self._client = None



if __name__ == "__main__":
    basicConfig(filename="02_emailvoid_search_message.log", level=DEBUG)
    main()
