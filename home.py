"""Contains handler for writing out the homepage."""
import base


class Handler(base.Handler):

  def get(self):
    self._WriteTemplate('index.html', {})
