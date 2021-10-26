import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json

#AAAAAAAAAAAAAAAAAAAAAD9WEgEAAAAAOpUZ7etqOM2j1tAcWPwodbmG1Mw%3DtrBiZeIdKzOFSnu3r9vSDJyfnHUx5Fg9WQFld6bQor6bj6gy1i
# Set up your credentials
consumer_key='XRe59TnfhDODaEdG20pKdGeDA'
consumer_secret='NzTGdk9DmJTddwNty63l0sSbO7zStzfLvaBpyCFCEFimd5ONiK'
access_token ='705037096340226049-FQGj1JJWSaVoGMaD8gtBoT4KhmVQMMz'
access_secret='UkJYwHCV1vgvx4dbd5op0OqKukBgLXoWBTjqJPKTnlUgl'


class TweetsListener(StreamListener):

  def __init__(self, csocket):
      self.client_socket = csocket

  def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True

  def on_error(self, status):
      print(status)
      return True

def sendData(c_socket):
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket))
  twitter_stream.filter(track=['ether'])

if __name__ == "__main__":
  s = socket.socket()         # Create a socket object
  host = "127.0.0.1"     # Get local machine name
  port = 5554                 # Reserve a port for your service.
  s.bind((host, port))        # Bind to the port

  print("Listening on port: %s" % str(port))

  s.listen(5)                 # Now wait for client connection.
  c, addr = s.accept()        # Establish connection with client.

  print( "Received request from: " + str( addr ) )

  sendData( c )