# -*- coding: utf-8 -*-
__author__ = 'florije'
from tornado.httpclient import HTTPRequest, HTTPClient


def send_request(self, url, args="", body="", method="GET"):
    # forms = forms.encode("gb2312")
    headers = {"Connection": "Keep-alive"}
    request = HTTPRequest(url=url + "?" + args, method=method, body=body, connect_timeout=10, request_timeout=30,
                          headers=headers)
    httpclient = HTTPClient()
    response = httpclient.fetch(request)
    resData = response.body
    return resData