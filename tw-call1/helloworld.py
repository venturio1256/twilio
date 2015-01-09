#!/usr/bin/env python
import cgi
import webapp2
from twilio import twiml
from twilio.rest import TwilioRestClient

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/sendsms" method="post">
      <div><input type="text" name="dest" placeholder="Send a text to"></div>
      <div><textarea name="content" rows="2" cols="70"></textarea></div>
      <div><input type="submit" value="Send SMS"></div>
    </form>
  </body>
</html>
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class SendSms(webapp2.RequestHandler):
    def post(self):
        try:
            account_sid = "AC568a8dbef442e66d2f8080af15a5c844"
            auth_token = "80fd00c4e685b165ca71825e1dda60ba"
            client = TwilioRestClient(account_sid, auth_token)
            message = client.messages.create(
                body=cgi.escape(self.request.get('content')),
                to=self.request.get('dest'),
                from_="+17205062175")
            self.response.headers['Content-Type'] = 'text/html'
            self.response.write('<html><body>Your message ID:<pre>')
            self.response.write(message.sid)
        except twilio.TwilioRestException as e:
            self.response.write(e)

class InboundCall(webapp2.RequestHandler):
    def post(self):
        r = twiml.Response()
        r.say("Hi!! Welcome to Venturio.")
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(str(r))
 
class InboundSms(webapp2.RequestHandler):
    def post(self):
        r = twiml.Response()
        r.sms("Hi! Thank you for your interest. Team Venturio.")
        self.response.headers['Content-Type'] = 'text/xml'
        self.response.write(str(r))
 
application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sendsms', SendSms),
    ('/incall', InboundCall),
    ('/insms',InboundSms)
    ], debug=True)


