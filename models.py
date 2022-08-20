from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False, nullable=False)
    seeking_description = db.Column(db.String)
    shows = db.relationship(
      'Show', backref=db.backref('venue', lazy=True)
    )

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_description = db.Column(db.String)
    seeking_venue = db.Column(db.Boolean, default=False, nullable=False)
    shows = db.relationship(
      'Show', backref=db.backref('artist', lazy=True)
    )

class Show(db.Model):
  __tablename__ = 'Show'
  artist_id = db.Column(
    db.Integer, 
    db.ForeignKey('Artist.id'), 
    primary_key=True
  )
  venue_id = db.Column(
    db.Integer,
    db.ForeignKey('Venue.id'),
    primary_key=True
  )
  start_time = db.Column(db.String, nullable=False)

  def __repr__(self) -> str:
    return f'<Show {self.artist_id} {self.venue_id} {self.start_time}>'
