"""Defines handler paths and initializes the app."""
import webapp2

import home 

app = webapp2.WSGIApplication([('/', home.Handler)], debug=False)
