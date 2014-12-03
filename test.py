
from bounce_check import check

import unittest

class TestCheck(unittest.TestCase):

    def setUp(self):
        self.mail_string="""Return-Path: <double-bounce@mail.emiau.com.br>
X-Original-To: bounces@emiau.com.br
Delivered-To: bounces@emiau.com.br
Received: by mail.emiau.com.br (Postfix)
    id 3BFAC2773E; Wed,  3 Dec 2014 17:43:06 -0200 (BRST)
Date: Wed,  3 Dec 2014 17:43:06 -0200 (BRST)
From: MAILER-DAEMON@mail.emiau.com.br (Mail Delivery System)
Subject: Postmaster Copy: Undelivered Mail
To: bounces@emiau.com.br
Auto-Submitted: auto-generated
MIME-Version: 1.0
Content-Type: multipart/report; report-type=delivery-status;
    boundary="F29B627500.1417635786/mail.emiau.com.br"
Message-Id: <20141203194306.3BFAC2773E@mail.emiau.com.br>

This is a MIME-encapsulated message.

--F29B627500.1417635786/mail.emiau.com.br
Content-Description: Notification
Content-Type: text/plain; charset=us-ascii


<thebounced@setentaequatroumdoistresquatro.com.br>: Host or domain name not
    found. Name service error for name=setentaequatroumdoistresquatro.com.br
    type=A: Host not found

--F29B627500.1417635786/mail.emiau.com.br
Content-Description: Delivery report
Content-Type: message/delivery-status

Reporting-MTA: dns; mail.emiau.com.br
X-Postfix-Queue-ID: F29B627500
X-Postfix-Sender: rfc822; marly@soeta.com.br
Arrival-Date: Wed,  3 Dec 2014 17:43:05 -0200 (BRST)

Final-Recipient: rfc822; thebounced@setentaequatroumdoistresquatro.com.br
Original-Recipient: rfc822;thebounced@setentaequatroumdoistresquatro.com.br
Action: failed
Status: 5.4.4
Diagnostic-Code: X-Postfix; Host or domain name not found. Name service error
    for name=setentaequatroumdoistresquatro.com.br type=A: Host not found

--F29B627500.1417635786/mail.emiau.com.br
Content-Description: Undelivered Message Headers
Content-Type: text/rfc822-headers

Return-Path: <marly@soeta.com.br>
Received: from [127.0.0.1] (unknown [10.0.0.70])
    by mail.emiau.com.br (Postfix) with ESMTP id F29B627500
    for <thebounced@setentaequatroumdoistresquatro.com.br>; Wed,  3 Dec 2014 17:43:05 -0200 (BRST)
Content-Type: multipart/mixed; boundary="===============7736281935899896060=="
MIME-Version: 1.0
From: <marly@soeta.com.br>
To: thebounced@setentaequatroumdoistresquatro.com.br
Date: Wed, 03 Dec 2014 17:43:05 -0200
Subject: asdasdasd
MID: 1690872
Message-Id: <20141203194305.F29B627500@mail.emiau.com.br>

--F29B627500.1417635786/mail.emiau.com.br--
"""

    def test_bouncecheck(self):
        # make sure the shuffled sequence does not lose any elements
        resp=check(self.mail_string)
        self.assertEqual(resp['isbounce'], True)
        self.assertEqual(resp['status'], '5.4.4')

if __name__ == '__main__':
    unittest.main()