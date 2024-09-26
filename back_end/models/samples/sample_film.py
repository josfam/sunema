"""A model for a sample film in the samples database"""

from back_end.models.engine.database import db

class SampleFilm(db.Model):
    """A model for a sample film stored in samples.db"""

    __bind_key__ = 'film_samples'
    __tablename__ = 'sample_films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    poster_path = db.Column(db.String(120), nullable=True)
    vote_average = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.String(120), nullable=False)

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.poster_path = kwargs.get('poster_path')
        self.vote_average = kwargs.get('vote_average')
        self.release_date = kwargs.get('release_date')

    def __repr__(self):
        """Canonical string representation for a sample film"""
        return f'<Sample Film {self.title}>'

    def to_dict(self):
        """Returns the dictionary representation of this sample film"""
        return {
            self.id: {
            'id': self.id,
            'title': self.title,
            'poster_path': self.poster_path,
            'vote_average': self.vote_average,
            'release_date': self.release_date,
        }}
