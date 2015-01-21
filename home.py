"""Contains handler for writing out the homepage."""
import base


class Handler(base.Handler):

  def get(self):
    self._WriteTemplate('index.html', {})
  
  def post(self):
    subject = self.request.get("subject")
    tutor = self.request.get("tutor")
    time = self.request.get("time")
    location = sle.request.get("location")
    if not subject or not tutor or not time or not location:
      output_json['status'] = 'ERR'
      output_json['error'] = 'All the fields are required fields.'
    else:
      tables.TutorSession.create(subject=subject,
                                 tutor=tutor,
                                 time=time,
                                 location=location
                                 )
                                 
