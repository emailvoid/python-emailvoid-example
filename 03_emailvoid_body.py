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
        self._apikey = "b8818f4c8594021a9ca1489d135a2540d726f855767496788c6f1d76f2f5917d"
        self._client = EmailVoidClient(apikey=self._apikey)


    def runTest(self):
        """ Receive message body to continue processing (parse body, ...)
        """
        # Step 0. Define const
        username = 'support'
        # Step 1. Check message count
        msg_count = self._client.msg_count(username)
        #self.__log.debug(msg_count)
        # Step 2. Search our message
        #if msg_count > 0:
        #    items = c.msg_search(user)
        #    for item in items:
        #        self.__log.debug(item)
        #        msgid = item.get_msgid()
        # Step 3. Fetch message body
        #body = c.msg_content(msgid=msgid)
        #self.__log.debug(body)


    def tearDown(self):
        """ Dispose clisent
        """
        if self._client:
            self._client.dispose()
            self._client = None



if __name__ == "__main__":
    basicConfig(filename="03_emailvoid_body.log", level=DEBUG)
    main()
