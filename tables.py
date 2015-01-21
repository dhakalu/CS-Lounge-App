from google.appengine.ext import db


class TutorSeesion(db.Model):
  tutor = db.StringProperty(required=True)
  subject = db.StringProperty(required=True)
  location = db.StringProperty(required=True)
  time = db.StringProperty(required=True)
  
  @classmethod
  def create_session(cls, tutor, subject, location, time):
    return TutorSession(tutor=tutor,
                        subject=subject,
                        location=location,
                        time=time
                        )
                        
    @classmethod
    def by_id(cls, sessionid):
      return TutorSession.
      
