#!/usr/bin/python

from __future__ import print_function

from logging import getLogger, basicConfig, DEBUG
from unittest import TestCase, main
from emailvoid import EmailVoidClient


class Test39190(TestCase):
    def setUp(self):
        """ Precondition
        """
        self.__log = getLogger('Test39190')
        self._apikey = "4f016ffc-437e-4750-8b2d-d0dbc89de7fc"
        self._client = EmailVoidClient(apikey=self._apikey)


    def runTest(self):
        """ Receive message body to continue processing (parse body, ...)
        """
        # Step 0. Define const
        domain = 'emailvoid.com'
        # Step 1. Search message
        items = self._client.msg_search(domain=domain)
        msgid = None
        for item in items:
            #if item 
            msgid = item.msgid
        # Step 2. Fetch message body by msgid
        self.assertIsNotNone(msgid, msg="No messages on server")
        #
        body = self._client.msg_content(domain=domain, msgid=msgid)
        self.__log.debug("body = {body!r}".format(body=body))


    def tearDown(self):
        """ Dispose clisent
        """
        if self._client:
            self._client.dispose()
            self._client = None



if __name__ == "__main__":
    basicConfig(filename="03_emailvoid_body.log", level=DEBUG)
    main()
