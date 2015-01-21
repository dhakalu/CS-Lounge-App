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
    def by_id(cls, session_id):
      return TutorSession.get_by_id(session_id)
      
    @classmethod
    def by_tutor(cls, tutor):
      return TutorSession.all().filter('tutor =', tutor)
      
    @classmethod
    def by_subject(cls, subject):
      return TutorSession.all().filter('subject =', subject)
