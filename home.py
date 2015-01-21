"""Contains handler for writing out the homepage."""
import base


class Handler(base.Handler):

  def get(self):
    self._WriteTemplate('index.html', {})
  
  def post(self):
    subject = self.request.get("subject")
    tutor = self.request.get("tutor")
