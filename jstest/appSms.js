#!/usr/bin/env node
var twilio = require('twilio');
// Load configuration information from system environment variables.
var TWILIO_ACCOUNT_SID = process.env.TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN = process.env.TWILIO_AUTH_TOKEN,
    TWILIO_NUMBER = process.env.TWILIO_NUMBER;
    
// Create an authenticated client to access the Twilio REST API
var client = twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN);

client.messages.create({
  to:'+16512223344',
  from:'+17205062175',
  body:'Ahoy from Twilio!'
}, function(error, message) {
  if (error) {
    console.log(error.message);
  } else {
  process.stdout.write(message.sid);
  }
});
