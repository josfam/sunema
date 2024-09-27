"""Utility functions for working with the sample films"""

from back_end.models.engine.database import db
from back_end.models.samples.sample_film import SampleFilm


def sample_films_exist() -> bool:
    """Returns whether sample films exist in the sample database"""
    query = db.select(SampleFilm)
    films = db.session.execute(query).scalars().first()
    # print(f'films :::: {films}')
    return True if films else False


def save_films_to_db(sample_films: dict):
    """Extracts films from the provided dictionary, and adds them to the sample
    database"""
    select_attrs = (
        'id',
        'title',
        'poster_path',
        'vote_average',
        'release_date',
    )

    for sample_film in sample_films.values():
        film = SampleFilm(**sample_film)
        db.session.add(film)
    db.session.commit()


sample_collections = {
    137: {
        'adult': False,
        'backdrop_path': '/ttBydD0SynC0TMkW3AcnmsySkLp.jpg',
        'belongs_to_collection': None,
        'budget': 14600000,
        'genres': [
            {'id': 10749, 'name': 'Romance'},
            {'id': 14, 'name': 'Fantasy'},
            {'id': 18, 'name': 'Drama'},
            {'id': 35, 'name': 'Comedy'},
        ],
        'homepage': '',
        'id': 137,
        'imdb_id': 'tt0107048',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Groundhog Day',
        'overview': 'A narcissistic TV weatherman, along with his '
        'attractive-but-distant producer, and his mawkish '
        'cameraman, is sent to report on Groundhog Day in the small '
        'town of Punxsutawney, where he finds himself repeating the '
        'same day over and over.',
        'popularity': 26.941,
        'poster_path': '/h1ZEBoi0waPwtAPU1cnSZifdqZh.jpg',
        'production_companies': [
            {
                'id': 5,
                'logo_path': '/71BqEFAF4V3qjjMPCpLuyJFB9A.png',
                'name': 'Columbia Pictures',
                'origin_country': 'US',
            }
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '1993-02-11',
        'revenue': 71100000,
        'runtime': 101,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'French', 'iso_639_1': 'fr', 'name': 'Français'},
            {'english_name': 'Italian', 'iso_639_1': 'it', 'name': 'Italiano'},
        ],
        'status': 'Released',
        'tagline': 'He’s having the worst day of his life… Over and over again.',
        'title': 'Groundhog Day',
        'video': False,
        'vote_average': 7.61,
        'vote_count': 7885,
    },
    389: {
        'adult': False,
        'backdrop_path': '/qqHQsStV6exghCM7zbObuYBiYxw.jpg',
        'belongs_to_collection': None,
        'budget': 397751,
        'genres': [{'id': 18, 'name': 'Drama'}],
        'homepage': '',
        'id': 389,
        'imdb_id': 'tt0050083',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': '12 Angry Men',
        'overview': 'The defense and the prosecution have rested and the jury '
        'is filing into the jury room to decide if a young '
        'Spanish-American is guilty or innocent of murdering his '
        'father. What begins as an open and shut case soon becomes '
        "a mini-drama of each of the jurors' prejudices and "
        'preconceptions about the trial, the accused, and each '
        'other.',
        'popularity': 49.821,
        'poster_path': '/ow3wq89wM8qd5X7hWKxiRfsFf9C.jpg',
        'production_companies': [
            {
                'id': 60,
                'logo_path': '/1SEj4nyG3JPBSKBbFhtdcHRaIF9.png',
                'name': 'United Artists',
                'origin_country': 'US',
            },
            {
                'id': 10212,
                'logo_path': None,
                'name': 'Orion-Nova Productions',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '1957-04-10',
        'revenue': 4360000,
        'runtime': 97,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Life is in their hands — Death is on their minds!',
        'title': '12 Angry Men',
        'video': False,
        'vote_average': 8.546,
        'vote_count': 8525,
    },
    603: {
        'adult': False,
        'backdrop_path': '/icmmSD4vTTDKOq2vvdulafOGw93.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/bRm2DEgUiYciDw3myHuYFInD7la.jpg',
            'id': 2344,
            'name': 'The Matrix Collection',
            'poster_path': '/bV9qTVHTVf0gkW0j7p7M0ILD4pG.jpg',
        },
        'budget': 63000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': 'http://www.warnerbros.com/matrix',
        'id': 603,
        'imdb_id': 'tt0133093',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'The Matrix',
        'overview': 'Set in the 22nd century, The Matrix tells the story of a '
        'computer hacker who joins a group of underground '
        'insurgents fighting the vast and powerful computers who '
        'now rule the earth.',
        'popularity': 86.778,
        'poster_path': '/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg',
        'production_companies': [
            {
                'id': 79,
                'logo_path': '/at4uYdwAAgNRKhZuuFX8ShKSybw.png',
                'name': 'Village Roadshow Pictures',
                'origin_country': 'US',
            },
            {
                'id': 372,
                'logo_path': None,
                'name': 'Groucho II Film Partnership',
                'origin_country': '',
            },
            {
                'id': 1885,
                'logo_path': '/xlvoOZr4s1PygosrwZyolIFe5xs.png',
                'name': 'Silver Pictures',
                'origin_country': 'US',
            },
            {
                'id': 174,
                'logo_path': '/zhD3hhtKB5qyv7ZeL4uLpNxgMVU.png',
                'name': 'Warner Bros. Pictures',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '1999-03-31',
        'revenue': 463517383,
        'runtime': 136,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'The fight for the future begins.',
        'title': 'The Matrix',
        'video': False,
        'vote_average': 8.2,
        'vote_count': 25441,
    },
    797: {
        'adult': False,
        'backdrop_path': '/sj2aZDetPE8RoOCAm5QJitCNfLr.jpg',
        'belongs_to_collection': None,
        'budget': 0,
        'genres': [{'id': 18, 'name': 'Drama'}],
        'homepage': '',
        'id': 797,
        'imdb_id': 'tt0060827',
        'origin_country': ['SE'],
        'original_language': 'sv',
        'original_title': 'Persona',
        'overview': 'A young nurse, Alma, is put in charge of Elisabeth Vogler: '
        'an actress who is seemingly healthy in all respects, but '
        'will not talk. As they spend time together, Alma speaks to '
        'Elisabeth constantly, never receiving any answer.',
        'popularity': 13.491,
        'poster_path': '/cl0HEZT8UfzLqaMrYTvGNHOfPYj.jpg',
        'production_companies': [
            {
                'id': 6181,
                'logo_path': '/eaQ7or8IoEmPfgmQiU2C5lVZkxS.png',
                'name': 'SF Studios',
                'origin_country': 'SE',
            }
        ],
        'production_countries': [{'iso_3166_1': 'SE', 'name': 'Sweden'}],
        'release_date': '1966-10-18',
        'revenue': 0,
        'runtime': 83,
        'spoken_languages': [
            {'english_name': 'Swedish', 'iso_639_1': 'sv', 'name': 'svenska'}
        ],
        'status': 'Released',
        'tagline': "Ingmar Bergman's most personal and original film",
        'title': 'Persona',
        'video': False,
        'vote_average': 8.183,
        'vote_count': 2101,
    },
    1124: {
        'adult': False,
        'backdrop_path': '/xBDE2d6HM1aBKQRu4IT7SfPD9fs.jpg',
        'belongs_to_collection': None,
        'budget': 40000000,
        'genres': [
            {'id': 18, 'name': 'Drama'},
            {'id': 9648, 'name': 'Mystery'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': 'http://wwws.warnerbros.de/theprestige/',
        'id': 1124,
        'imdb_id': 'tt0482571',
        'origin_country': ['US', 'GB'],
        'original_language': 'en',
        'original_title': 'The Prestige',
        'overview': 'A mysterious story of two magicians whose intense rivalry '
        'leads them on a life-long battle for supremacy -- full of '
        'obsession, deceit and jealousy with dangerous and deadly '
        'consequences.',
        'popularity': 63.384,
        'poster_path': '/tRNlZbgNCNOpLpbPEz5L8G8A0JN.jpg',
        'production_companies': [
            {
                'id': 174,
                'logo_path': '/zhD3hhtKB5qyv7ZeL4uLpNxgMVU.png',
                'name': 'Warner Bros. Pictures',
                'origin_country': 'US',
            },
            {
                'id': 9195,
                'logo_path': '/ou5BUbtulr6tIt699q6xJiEQTR9.png',
                'name': 'Touchstone Pictures',
                'origin_country': 'US',
            },
            {
                'id': 28,
                'logo_path': '/xsSP0FwltGUvLthuSdXAcZqOWa6.png',
                'name': 'Newmarket Films',
                'origin_country': 'US',
            },
            {
                'id': 9996,
                'logo_path': '/3tvBqYsBhxWeHlu62SIJ1el93O7.png',
                'name': 'Syncopy',
                'origin_country': 'GB',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'GB', 'name': 'United Kingdom'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2006-10-17',
        'revenue': 109676311,
        'runtime': 130,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Are You Watching Closely?',
        'title': 'The Prestige',
        'video': False,
        'vote_average': 8.2,
        'vote_count': 15850,
    },
    2501: {
        'adult': False,
        'backdrop_path': '/kJaRWmy1BGq3pHyE94LOTteiHer.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/vA5xMglyZv7yzDTj1qUTU4OvelV.jpg',
            'id': 31562,
            'name': 'The Bourne Collection',
            'poster_path': '/q0ma8ozYaaol1IvdGjBvj3KllyL.jpg',
        },
        'budget': 60000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 18, 'name': 'Drama'},
            {'id': 9648, 'name': 'Mystery'},
            {'id': 53, 'name': 'Thriller'},
        ],
        'homepage': 'http://www.universalstudiosentertainment.com/the-bourne-identity/',
        'id': 2501,
        'imdb_id': 'tt0258463',
        'origin_country': ['DE', 'US', 'CZ'],
        'original_language': 'en',
        'original_title': 'The Bourne Identity',
        'overview': 'Wounded to the brink of death and suffering from amnesia, '
        'Jason Bourne is rescued at sea by a fisherman. With '
        'nothing to go on but a Swiss bank account number, he '
        'starts to reconstruct his life, but finds that many '
        'people he encounters want him dead. However, Bourne '
        'realizes that he has the combat and mental skills of a '
        'world-class spy—but who does he work for?',
        'popularity': 95.526,
        'poster_path': '/aP8swke3gmowbkfZ6lmNidu0y9p.jpg',
        'production_companies': [
            {
                'id': 33,
                'logo_path': '/8lvHyhjr8oUKOOy2dKXoALWKdp0.png',
                'name': 'Universal Pictures',
                'origin_country': 'US',
            },
            {
                'id': 7384,
                'logo_path': None,
                'name': 'Hypnotic',
                'origin_country': 'US',
            },
            {
                'id': 7385,
                'logo_path': None,
                'name': 'Kalima Productions',
                'origin_country': 'DE',
            },
            {
                'id': 11345,
                'logo_path': '/xhnnHfsqEimD4r0QeUz3GSvcv73.png',
                'name': 'Stillking Films',
                'origin_country': 'CZ',
            },
            {
                'id': 862,
                'logo_path': '/vdK6ZhC2CSW36j0VPEavRxOpbEg.png',
                'name': 'The Kennedy/Marshall Company',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'},
            {'iso_3166_1': 'DE', 'name': 'Germany'},
            {'iso_3166_1': 'CZ', 'name': 'Czech Republic'},
        ],
        'release_date': '2002-06-14',
        'revenue': 214034224,
        'runtime': 119,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'French', 'iso_639_1': 'fr', 'name': 'Français'},
            {'english_name': 'German', 'iso_639_1': 'de', 'name': 'Deutsch'},
            {'english_name': 'Dutch', 'iso_639_1': 'nl', 'name': 'Nederlands'},
            {'english_name': 'Italian', 'iso_639_1': 'it', 'name': 'Italiano'},
        ],
        'status': 'Released',
        'tagline': 'He was the perfect weapon until he became the target.',
        'title': 'The Bourne Identity',
        'video': False,
        'vote_average': 7.5,
        'vote_count': 9145,
    },
    9354: {
        'adult': False,
        'backdrop_path': '/d9xVUFkEKNxyOIihbpvAVdjzcL.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/sfT3NqSnjEDY1449qBgQRWOIcaq.jpg',
            'id': 72119,
            'name': 'Honey, I Shrunk the Kids Collection',
            'poster_path': '/xxIwqQARS0RZu5cIENahqZSRw2a.jpg',
        },
        'budget': 18000000,
        'genres': [
            {'id': 12, 'name': 'Adventure'},
            {'id': 35, 'name': 'Comedy'},
            {'id': 10751, 'name': 'Family'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': '',
        'id': 9354,
        'imdb_id': 'tt0097523',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Honey, I Shrunk the Kids',
        'overview': 'The scientist father of a teenage girl and boy '
        'accidentally shrinks his and two other neighborhood teens '
        'to the size of insects. Now the teens must fight '
        'diminutive dangers as the father searches for them.',
        'popularity': 20.346,
        'poster_path': '/1Xebz5V4UQchh49NXQ0n6FFLYQb.jpg',
        'production_companies': [
            {
                'id': 2,
                'logo_path': '/wdrCwmRnLFJhEoH8GSfymY85KHT.png',
                'name': 'Walt Disney Pictures',
                'origin_country': 'US',
            },
            {
                'id': 554,
                'logo_path': '/mN5HU5xYq9xtEs1X0Hu25A9y8lW.png',
                'name': 'Silver Screen Partners III',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '1989-06-23',
        'revenue': 222724172,
        'runtime': 93,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'The most astonishing, innovative, backyard adventure of '
        'all time!',
        'title': 'Honey, I Shrunk the Kids',
        'video': False,
        'vote_average': 6.3,
        'vote_count': 2991,
    },
    9602: {
        'adult': False,
        'backdrop_path': '/hP4PMoQfaofHbLDPIAXrirR7wSF.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/mgfXpEAnmuWCdSslqeoyTE7iqU9.jpg',
            'id': 647077,
            'name': 'Coming to America Collection',
            'poster_path': '/iIXHsGpnNxnujFMRwOQSLoxr7U5.jpg',
        },
        'budget': 30000000,
        'genres': [
            {'id': 35, 'name': 'Comedy'},
            {'id': 10749, 'name': 'Romance'},
        ],
        'homepage': '',
        'id': 9602,
        'imdb_id': 'tt0094898',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Coming to America',
        'overview': 'An African prince decides it’s time for him to find a '
        'princess... and his mission leads him and his most loyal '
        'friend to Queens, New York. In disguise as an '
        'impoverished immigrant, the pampered prince quickly finds '
        'himself a new job, new friends, new digs, new enemies and '
        'lots of trouble.',
        'popularity': 80.552,
        'poster_path': '/djRAvxyvvN2yqlJKDbT3uy4vOBw.jpg',
        'production_companies': [
            {
                'id': 30,
                'logo_path': None,
                'name': 'Eddie Murphy Productions',
                'origin_country': 'US',
            },
            {
                'id': 4,
                'logo_path': '/gz66EfNoYPqHTYI4q9UEN4CbHRc.png',
                'name': 'Paramount Pictures',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '1988-06-29',
        'revenue': 288752301,
        'runtime': 117,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'This summer, Prince Akeem discovers America.',
        'title': 'Coming to America',
        'video': False,
        'vote_average': 6.882,
        'vote_count': 4282,
    },
    10528: {
        'adult': False,
        'backdrop_path': '/veXdzn7LL0bFIDGmE7tTkvRg0qV.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/kT4Pz6QY29qHMVKULzNrVHg6Vwg.jpg',
            'id': 102322,
            'name': 'Sherlock Holmes Collection',
            'poster_path': '/oXzQIiGl3cZwF0R4Bq88Gf9fcMJ.jpg',
        },
        'budget': 90000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 12, 'name': 'Adventure'},
            {'id': 80, 'name': 'Crime'},
            {'id': 9648, 'name': 'Mystery'},
        ],
        'homepage': 'https://www.warnerbros.com/movies/sherlock-holmes/',
        'id': 10528,
        'imdb_id': 'tt0988045',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Sherlock Holmes',
        'overview': 'Eccentric consulting detective Sherlock Holmes and '
        'Doctor John Watson battle to bring down a new nemesis '
        'and unravel a deadly plot that could destroy England.',
        'popularity': 52.249,
        'poster_path': '/momkKuWburNTqKBF6ez7rvhYVhE.jpg',
        'production_companies': [
            {
                'id': 174,
                'logo_path': '/zhD3hhtKB5qyv7ZeL4uLpNxgMVU.png',
                'name': 'Warner Bros. Pictures',
                'origin_country': 'US',
            },
            {
                'id': 79,
                'logo_path': '/at4uYdwAAgNRKhZuuFX8ShKSybw.png',
                'name': 'Village Roadshow Pictures',
                'origin_country': 'US',
            },
            {
                'id': 1885,
                'logo_path': '/xlvoOZr4s1PygosrwZyolIFe5xs.png',
                'name': 'Silver Pictures',
                'origin_country': 'US',
            },
            {
                'id': 23202,
                'logo_path': None,
                'name': 'Wigram Productions',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2009-12-23',
        'revenue': 524028679,
        'runtime': 129,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'French', 'iso_639_1': 'fr', 'name': 'Français'},
        ],
        'status': 'Released',
        'tagline': 'Nothing escapes him.',
        'title': 'Sherlock Holmes',
        'video': False,
        'vote_average': 7.214,
        'vote_count': 13780,
    },
    11104: {
        'adult': False,
        'backdrop_path': '/8e6avmXiqurj5LHkmdHBq6rc5jm.jpg',
        'belongs_to_collection': None,
        'budget': 160000,
        'genres': [
            {'id': 18, 'name': 'Drama'},
            {'id': 35, 'name': 'Comedy'},
            {'id': 10749, 'name': 'Romance'},
        ],
        'homepage': '',
        'id': 11104,
        'imdb_id': 'tt0109424',
        'origin_country': ['HK'],
        'original_language': 'cn',
        'original_title': '重慶森林',
        'overview': 'Two melancholic Hong Kong policemen fall in love: one '
        'with a mysterious underworld figure, the other with a '
        'beautiful and ethereal server at a late-night '
        'restaurant.',
        'popularity': 35.524,
        'poster_path': '/43I9DcNoCzpyzK8JCkJYpHqHqGG.jpg',
        'production_companies': [
            {
                'id': 540,
                'logo_path': None,
                'name': 'Jet Tone Production',
                'origin_country': 'HK',
            },
            {
                'id': 1615,
                'logo_path': '/4eBmyaFkD9um04Weu6ybnLWNSVH.png',
                'name': 'Fortissimo Films',
                'origin_country': 'NL',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'HK', 'name': 'Hong Kong'},
            {'iso_3166_1': 'NL', 'name': 'Netherlands'},
        ],
        'release_date': '1994-07-14',
        'revenue': 0,
        'runtime': 103,
        'spoken_languages': [
            {
                'english_name': 'Cantonese',
                'iso_639_1': 'cn',
                'name': '广州话 / 廣州話',
            },
            {'english_name': 'Mandarin', 'iso_639_1': 'zh', 'name': '普通话'},
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'Hindi', 'iso_639_1': 'hi', 'name': 'हिन्दी'},
            {'english_name': 'Japanese', 'iso_639_1': 'ja', 'name': '日本語'},
            {'english_name': 'Punjabi', 'iso_639_1': 'pa', 'name': 'ਪੰਜਾਬੀ'},
            {'english_name': 'Urdu', 'iso_639_1': 'ur', 'name': 'اردو'},
        ],
        'status': 'Released',
        'tagline': 'What a difference a day makes.',
        'title': 'Chungking Express',
        'video': False,
        'vote_average': 8.0,
        'vote_count': 1755,
    },
    27205: {
        'adult': False,
        'backdrop_path': '/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg',
        'belongs_to_collection': None,
        'budget': 160000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 878, 'name': 'Science Fiction'},
            {'id': 12, 'name': 'Adventure'},
        ],
        'homepage': 'https://www.warnerbros.com/movies/inception',
        'id': 27205,
        'imdb_id': 'tt1375666',
        'origin_country': ['US', 'GB'],
        'original_language': 'en',
        'original_title': 'Inception',
        'overview': 'Cobb, a skilled thief who commits corporate espionage by '
        'infiltrating the subconscious of his targets is offered '
        'a chance to regain his old life as payment for a task '
        'considered to be impossible: "inception", the '
        "implantation of another person's idea into a target's "
        'subconscious.',
        'popularity': 73.934,
        'poster_path': '/ljsZTbVsrQSqZgWeep2B1QiDKuh.jpg',
        'production_companies': [
            {
                'id': 923,
                'logo_path': '/8M99Dkt23MjQMTTWukq4m5XsEuo.png',
                'name': 'Legendary Pictures',
                'origin_country': 'US',
            },
            {
                'id': 9996,
                'logo_path': '/3tvBqYsBhxWeHlu62SIJ1el93O7.png',
                'name': 'Syncopy',
                'origin_country': 'GB',
            },
            {
                'id': 174,
                'logo_path': '/zhD3hhtKB5qyv7ZeL4uLpNxgMVU.png',
                'name': 'Warner Bros. Pictures',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'GB', 'name': 'United Kingdom'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2010-07-15',
        'revenue': 825532764,
        'runtime': 148,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'French', 'iso_639_1': 'fr', 'name': 'Français'},
            {'english_name': 'Japanese', 'iso_639_1': 'ja', 'name': '日本語'},
            {
                'english_name': 'Swahili',
                'iso_639_1': 'sw',
                'name': 'Kiswahili',
            },
        ],
        'status': 'Released',
        'tagline': 'Your mind is the scene of the crime.',
        'title': 'Inception',
        'video': False,
        'vote_average': 8.368,
        'vote_count': 36309,
    },
    37165: {
        'adult': False,
        'backdrop_path': '/aCHn2TXYJfzPXQKA6r9mKPbMlUB.jpg',
        'belongs_to_collection': None,
        'budget': 60000000,
        'genres': [{'id': 35, 'name': 'Comedy'}, {'id': 18, 'name': 'Drama'}],
        'homepage': '',
        'id': 37165,
        'imdb_id': 'tt0120382',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'The Truman Show',
        'overview': 'Every second of every day, from the moment he was born, '
        'for the last thirty years, Truman Burbank has been the '
        'unwitting star of the longest running, most popular '
        'documentary-soap opera in history. The picture-perfect '
        'town of Seahaven that he calls home is actually a '
        "gigantic soundstage. Truman's friends and family - "
        'everyone he meets, in fact - are actors. He lives every '
        'moment under the unblinking gaze of thousands of hidden '
        'TV cameras.',
        'popularity': 77.151,
        'poster_path': '/vuza0WqY239yBXOadKlGwJsZJFE.jpg',
        'production_companies': [
            {
                'id': 4,
                'logo_path': '/gz66EfNoYPqHTYI4q9UEN4CbHRc.png',
                'name': 'Paramount Pictures',
                'origin_country': 'US',
            },
            {
                'id': 258,
                'logo_path': None,
                'name': 'Scott Rudin Productions',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '1998-06-04',
        'revenue': 264100000,
        'runtime': 103,
        'spoken_languages': [
            {'english_name': 'Spanish', 'iso_639_1': 'es', 'name': 'Español'},
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
        ],
        'status': 'Released',
        'tagline': 'On the air. Unaware.',
        'title': 'The Truman Show',
        'video': False,
        'vote_average': 8.1,
        'vote_count': 18120,
    },
    60243: {
        'adult': False,
        'backdrop_path': '/kcXBa2ru0PXcGI8U3JiInsG6FRR.jpg',
        'belongs_to_collection': None,
        'budget': 5000000,
        'genres': [{'id': 18, 'name': 'Drama'}],
        'homepage': 'https://www.sonyclassics.com/aseparation/',
        'id': 60243,
        'imdb_id': 'tt1832382',
        'origin_country': ['FR', 'IR'],
        'original_language': 'fa',
        'original_title': 'جدایی نادر از سیمین',
        'overview': 'A married couple are faced with a difficult decision - '
        'to improve the life of their child by moving to another '
        'country or to stay in Iran and look after a '
        "deteriorating parent who has Alzheimer's disease.",
        'popularity': 11.417,
        'poster_path': '/es4VftcjwOEGKbFWEY1hgu7Tesj.jpg',
        'production_companies': [
            {
                'id': 84797,
                'logo_path': None,
                'name': 'Asghar Farhadi Productions',
                'origin_country': 'IR',
            },
            {
                'id': 5162,
                'logo_path': '/ePS4wgTIC1hjOnnmxYJmYNEzAR.png',
                'name': 'Memento Films Production',
                'origin_country': 'FR',
            },
            {
                'id': 84798,
                'logo_path': None,
                'name': 'Dreamlab Films',
                'origin_country': 'FR',
            },
            {
                'id': 84799,
                'logo_path': None,
                'name': 'MPA APSA Academy Films',
                'origin_country': 'AU',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'AU', 'name': 'Australia'},
            {'iso_3166_1': 'FR', 'name': 'France'},
            {'iso_3166_1': 'IR', 'name': 'Iran'},
        ],
        'release_date': '2011-02-15',
        'revenue': 24426169,
        'runtime': 123,
        'spoken_languages': [
            {'english_name': 'Persian', 'iso_639_1': 'fa', 'name': 'فارسی'}
        ],
        'status': 'Released',
        'tagline': 'Ugly truth, sweet lies.',
        'title': 'A Separation',
        'video': False,
        'vote_average': 7.901,
        'vote_count': 1692,
    },
    76341: {
        'adult': False,
        'backdrop_path': '/gqrnQA6Xppdl8vIb2eJc58VC1tW.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/fhv3dWOuzeW9eXOSlr8MCHwo24t.jpg',
            'id': 8945,
            'name': 'Mad Max Collection',
            'poster_path': '/9U9QmbCDIBhqDShuIxOiS9gjKYz.jpg',
        },
        'budget': 150000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 12, 'name': 'Adventure'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': 'https://www.warnerbros.com/movies/mad-max-fury-road',
        'id': 76341,
        'imdb_id': 'tt1392190',
        'origin_country': ['AU', 'US'],
        'original_language': 'en',
        'original_title': 'Mad Max: Fury Road',
        'overview': 'An apocalyptic story set in the furthest reaches of our '
        'planet, in a stark desert landscape where humanity is '
        'broken, and most everyone is crazed fighting for the '
        'necessities of life. Within this world exist two rebels '
        'on the run who just might be able to restore order.',
        'popularity': 91.603,
        'poster_path': '/hA2ple9q4qnwxp3hKVNhroipsir.jpg',
        'production_companies': [
            {
                'id': 174,
                'logo_path': '/zhD3hhtKB5qyv7ZeL4uLpNxgMVU.png',
                'name': 'Warner Bros. Pictures',
                'origin_country': 'US',
            },
            {
                'id': 79,
                'logo_path': '/at4uYdwAAgNRKhZuuFX8ShKSybw.png',
                'name': 'Village Roadshow Pictures',
                'origin_country': 'US',
            },
            {
                'id': 28382,
                'logo_path': '/xqE1fjLynj3RaZca9chctZQyfzZ.png',
                'name': 'Kennedy Miller Mitchell',
                'origin_country': 'AU',
            },
            {
                'id': 41624,
                'logo_path': '/wzKxIeQKlMP0y5CaAw25MD6EQmf.png',
                'name': 'RatPac Entertainment',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'AU', 'name': 'Australia'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2015-05-13',
        'revenue': 378858340,
        'runtime': 121,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'The future belongs to the mad.',
        'title': 'Mad Max: Fury Road',
        'video': False,
        'vote_average': 7.614,
        'vote_count': 22414,
    },
    146233: {
        'adult': False,
        'backdrop_path': '/3RFmTz5h2UuFWEV4oH00XICBR9y.jpg',
        'belongs_to_collection': None,
        'budget': 46000000,
        'genres': [
            {'id': 18, 'name': 'Drama'},
            {'id': 53, 'name': 'Thriller'},
            {'id': 80, 'name': 'Crime'},
        ],
        'homepage': 'https://www.alconent.com/film/prisoners',
        'id': 146233,
        'imdb_id': 'tt1392214',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Prisoners',
        'overview': 'Keller Dover is facing every parent’s worst nightmare. '
        'His six-year-old daughter, Anna, is missing, together '
        'with her young friend, Joy, and as minutes turn to '
        'hours, panic sets in. The only lead is a dilapidated RV '
        'that had earlier been parked on their street.',
        'popularity': 60.775,
        'poster_path': '/uhviyknTT5cEQXbn6vWIqfM4vGm.jpg',
        'production_companies': [
            {
                'id': 1088,
                'logo_path': '/9WOE5AQUXbOtLU6GTwfjS8OMF0v.png',
                'name': 'Alcon Entertainment',
                'origin_country': 'US',
            },
            {
                'id': 18208,
                'logo_path': None,
                'name': '8:38 Productions',
                'origin_country': '',
            },
            {
                'id': 12199,
                'logo_path': '/gYYIgHpgRsyhyUkeFev1GnwBqHb.png',
                'name': 'Madhouse Entertainment',
                'origin_country': 'US',
            },
            {
                'id': 491,
                'logo_path': '/5LvDUt3KmvRnXQ4NrdWJYHeuA8J.png',
                'name': 'Summit Entertainment',
                'origin_country': 'US',
            },
            {
                'id': 174,
                'logo_path': '/zhD3hhtKB5qyv7ZeL4uLpNxgMVU.png',
                'name': 'Warner Bros. Pictures',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2013-09-19',
        'revenue': 122126687,
        'runtime': 153,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Every moment matters.',
        'title': 'Prisoners',
        'video': False,
        'vote_average': 8.099,
        'vote_count': 11613,
    },
    157336: {
        'adult': False,
        'backdrop_path': '/xJHokMbljvjADYdit5fK5VQsXEG.jpg',
        'belongs_to_collection': None,
        'budget': 165000000,
        'genres': [
            {'id': 12, 'name': 'Adventure'},
            {'id': 18, 'name': 'Drama'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': 'http://www.interstellarmovie.net/',
        'id': 157336,
        'imdb_id': 'tt0816692',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Interstellar',
        'overview': 'The adventures of a group of explorers who make use of '
        'a newly discovered wormhole to surpass the limitations '
        'on human space travel and conquer the vast distances '
        'involved in an interstellar voyage.',
        'popularity': 287.419,
        'poster_path': '/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
        'production_companies': [
            {
                'id': 923,
                'logo_path': '/8M99Dkt23MjQMTTWukq4m5XsEuo.png',
                'name': 'Legendary Pictures',
                'origin_country': 'US',
            },
            {
                'id': 9996,
                'logo_path': '/3tvBqYsBhxWeHlu62SIJ1el93O7.png',
                'name': 'Syncopy',
                'origin_country': 'GB',
            },
            {
                'id': 13769,
                'logo_path': None,
                'name': 'Lynda Obst Productions',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'GB', 'name': 'United Kingdom'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2014-11-05',
        'revenue': 701729206,
        'runtime': 169,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Mankind was born on Earth. It was never meant to die '
        'here.',
        'title': 'Interstellar',
        'video': False,
        'vote_average': 8.44,
        'vote_count': 35235,
    },
    244786: {
        'adult': False,
        'backdrop_path': '/vNXGrknx4GjWLgmuNTftWZluIUl.jpg',
        'belongs_to_collection': None,
        'budget': 3300000,
        'genres': [
            {'id': 18, 'name': 'Drama'},
            {'id': 10402, 'name': 'Music'},
        ],
        'homepage': 'https://www.sonyclassics.com/film/whiplash',
        'id': 244786,
        'imdb_id': 'tt2582802',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Whiplash',
        'overview': 'Under the direction of a ruthless instructor, a '
        'talented young drummer begins to pursue perfection at '
        'any cost, even his humanity.',
        'popularity': 126.783,
        'poster_path': '/7fn624j5lj3xTme2SgiLCeuedmO.jpg',
        'production_companies': [
            {
                'id': 2266,
                'logo_path': '/owzVs2mguyyJ3vIn7EbgowpUPnk.png',
                'name': 'Bold Films',
                'origin_country': 'US',
            },
            {
                'id': 3172,
                'logo_path': '/rzKluDcRkIwHZK2pHsiT667A2Kw.png',
                'name': 'Blumhouse Productions',
                'origin_country': 'US',
            },
            {
                'id': 32157,
                'logo_path': '/4hOCk25Ce8s242NItnwtV7aKRWY.png',
                'name': 'Right of Way Films',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2014-10-10',
        'revenue': 50027913,
        'runtime': 107,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'The road to greatness can take you to the edge.',
        'title': 'Whiplash',
        'video': False,
        'vote_average': 8.381,
        'vote_count': 14939,
    },
    263115: {
        'adult': False,
        'backdrop_path': '/9X7YweCJw3q8Mcf6GadxReFEksM.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/QtSxEuCwcZSfCTMZfER3nHDVsG.jpg',
            'id': 453993,
            'name': 'The Wolverine Collection',
            'poster_path': '/c18HVnKTybcAUYVQd8rOcdbqwY.jpg',
        },
        'budget': 97000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 18, 'name': 'Drama'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': 'https://www.20thcenturystudios.com/movies/logan',
        'id': 263115,
        'imdb_id': 'tt3315342',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Logan',
        'overview': 'In the near future, a weary Logan cares for an ailing '
        'Professor X in a hideout on the Mexican border. But '
        "Logan's attempts to hide from the world and his legacy "
        'are upended when a young mutant arrives, pursued by '
        'dark forces.',
        'popularity': 137.782,
        'poster_path': '/fnbjcRDYn6YviCcePDnGdyAkYsB.jpg',
        'production_companies': [
            {
                'id': 91797,
                'logo_path': None,
                'name': 'Hutch Parker Entertainment',
                'origin_country': 'US',
            },
            {
                'id': 431,
                'logo_path': '/6dcR1MbRqYgt3jUVYxkHe68GFnZ.png',
                'name': "The Donners' Company",
                'origin_country': 'US',
            },
            {
                'id': 28788,
                'logo_path': '/Aqomtf9oh5dKtxBNEagkdlp3aGv.png',
                'name': 'Genre Films',
                'origin_country': 'US',
            },
            {
                'id': 25,
                'logo_path': '/qZCc1lty5FzX30aOCVRBLzaVmcp.png',
                'name': '20th Century Fox',
                'origin_country': 'US',
            },
            {
                'id': 7505,
                'logo_path': '/837VMM4wOkODc1idNxGT0KQJlej.png',
                'name': 'Marvel Entertainment',
                'origin_country': 'US',
            },
            {
                'id': 22213,
                'logo_path': '/qx9K6bFWJupwde0xQDwOvXkOaL8.png',
                'name': 'TSG Entertainment',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2017-02-28',
        'revenue': 619021436,
        'runtime': 137,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'Spanish', 'iso_639_1': 'es', 'name': 'Español'},
        ],
        'status': 'Released',
        'tagline': 'His time has come.',
        'title': 'Logan',
        'video': False,
        'vote_average': 7.822,
        'vote_count': 19079,
    },
    438631: {
        'adult': False,
        'backdrop_path': '/lzWHmYdfeFiMIY4JaMmtR7GEli3.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/ygVSGv86R0BTOKJIb8RQ1sFxs4q.jpg',
            'id': 726871,
            'name': 'Dune Collection',
            'poster_path': '/lxIGYkpvYjLtYtZH684AQft0FhD.jpg',
        },
        'budget': 165000000,
        'genres': [
            {'id': 878, 'name': 'Science Fiction'},
            {'id': 12, 'name': 'Adventure'},
        ],
        'homepage': 'https://www.dunemovie.com/',
        'id': 438631,
        'imdb_id': 'tt1160419',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Dune',
        'overview': 'Paul Atreides, a brilliant and gifted young man born '
        'into a great destiny beyond his understanding, must '
        'travel to the most dangerous planet in the universe to '
        'ensure the future of his family and his people. As '
        'malevolent forces explode into conflict over the '
        "planet's exclusive supply of the most precious resource "
        'in existence-a commodity capable of unlocking '
        "humanity's greatest potential-only those who can "
        'conquer their fear will survive.',
        'popularity': 90.243,
        'poster_path': '/d5NXSklXo0qyIYkgV94XAgMIckC.jpg',
        'production_companies': [
            {
                'id': 923,
                'logo_path': '/8M99Dkt23MjQMTTWukq4m5XsEuo.png',
                'name': 'Legendary Pictures',
                'origin_country': 'US',
            }
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2021-09-15',
        'revenue': 407573628,
        'runtime': 155,
        'spoken_languages': [
            {'english_name': 'Mandarin', 'iso_639_1': 'zh', 'name': '普通话'},
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
        ],
        'status': 'Released',
        'tagline': 'It begins.',
        'title': 'Dune',
        'video': False,
        'vote_average': 7.785,
        'vote_count': 12425,
    },
    493922: {
        'adult': False,
        'backdrop_path': '/4DUoPZOHdPuROP4nyEIsPaMIiQl.jpg',
        'belongs_to_collection': None,
        'budget': 10000000,
        'genres': [
            {'id': 27, 'name': 'Horror'},
            {'id': 9648, 'name': 'Mystery'},
            {'id': 53, 'name': 'Thriller'},
        ],
        'homepage': 'https://a24films.com/films/hereditary',
        'id': 493922,
        'imdb_id': 'tt7784604',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Hereditary',
        'overview': 'Following the death of Ellen Leigh, the matriarch of '
        'their family, her daughter Annie and the rest of the '
        'family start to uncover disturbing secrets about their '
        'heritage.  Their daily lives are not only impacted, but '
        'they also become entangled in a chilling fate from '
        'which they cannot escape, driving them to the brink of '
        'madness.',
        'popularity': 92.408,
        'poster_path': '/p9fmuz2Oj3HtEJEqbIwkFGUhVXD.jpg',
        'production_companies': [
            {
                'id': 24277,
                'logo_path': '/mRSBVNNL2lZvJKVGjlxeUQVRc6X.png',
                'name': 'PalmStar Media',
                'origin_country': 'US',
            }
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2018-06-07',
        'revenue': 87825916,
        'runtime': 128,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Every family tree hides a secret.',
        'title': 'Hereditary',
        'video': False,
        'vote_average': 7.29,
        'vote_count': 7525,
    },
    496243: {
        'adult': False,
        'backdrop_path': '/8eihUxjQsJ7WvGySkVMC0EwbPAD.jpg',
        'belongs_to_collection': None,
        'budget': 11363000,
        'genres': [
            {'id': 35, 'name': 'Comedy'},
            {'id': 53, 'name': 'Thriller'},
            {'id': 18, 'name': 'Drama'},
        ],
        'homepage': 'https://www.parasite-movie.com/',
        'id': 496243,
        'imdb_id': 'tt6751668',
        'origin_country': ['KR'],
        'original_language': 'ko',
        'original_title': '기생충',
        'overview': "All unemployed, Ki-taek's family takes peculiar "
        'interest in the wealthy and glamorous Parks for their '
        'livelihood until they get entangled in an unexpected '
        'incident.',
        'popularity': 135.242,
        'poster_path': '/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg',
        'production_companies': [
            {
                'id': 4399,
                'logo_path': '/rk3kE5QX2dQtH0pPwCHV12qfebg.png',
                'name': 'Barunson E&A',
                'origin_country': 'KR',
            }
        ],
        'production_countries': [{'iso_3166_1': 'KR', 'name': 'South Korea'}],
        'release_date': '2019-05-30',
        'revenue': 257591776,
        'runtime': 133,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'German', 'iso_639_1': 'de', 'name': 'Deutsch'},
            {
                'english_name': 'Korean',
                'iso_639_1': 'ko',
                'name': '한국어/조선말',
            },
        ],
        'status': 'Released',
        'tagline': 'Act like you own the place.',
        'title': 'Parasite',
        'video': False,
        'vote_average': 8.5,
        'vote_count': 18051,
    },
    522627: {
        'adult': False,
        'backdrop_path': '/tintsaQ0WLzZsTMkTiqtMB3rfc8.jpg',
        'belongs_to_collection': None,
        'budget': 22000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 80, 'name': 'Crime'},
            {'id': 35, 'name': 'Comedy'},
        ],
        'homepage': 'https://www.miramax.com/movie/the-gentlemen',
        'id': 522627,
        'imdb_id': 'tt8367814',
        'origin_country': ['GB'],
        'original_language': 'en',
        'original_title': 'The Gentlemen',
        'overview': 'American expat Mickey Pearson has built a highly '
        'profitable marijuana empire in London. When word gets '
        'out that he’s looking to cash out of the business '
        'forever it triggers plots, schemes, bribery and '
        'blackmail in an attempt to steal his domain out from '
        'under him.',
        'popularity': 60.383,
        'poster_path': '/jtrhTYB7xSrJxR1vusu99nvnZ1g.jpg',
        'production_companies': [
            {
                'id': 14,
                'logo_path': '/m6AHu84oZQxvq7n1rsvMNJIAsMu.png',
                'name': 'Miramax',
                'origin_country': 'US',
            },
            {
                'id': 2900,
                'logo_path': None,
                'name': 'Toff Guy Films',
                'origin_country': 'GB',
            },
            {
                'id': 210118,
                'logo_path': None,
                'name': 'Coach Films',
                'origin_country': 'GB',
            },
            {
                'id': 47729,
                'logo_path': '/bAxh897TGgdR0Py6wdd0UuE147Z.png',
                'name': 'STXfilms',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'GB', 'name': 'United Kingdom'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2020-01-23',
        'revenue': 115171795,
        'runtime': 113,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Criminal. Class.',
        'title': 'The Gentlemen',
        'video': False,
        'vote_average': 7.679,
        'vote_count': 5656,
    },
    530385: {
        'adult': False,
        'backdrop_path': '/pYgj8e2Y6RufnSyOA6OnzmxFXxZ.jpg',
        'belongs_to_collection': None,
        'budget': 9000000,
        'genres': [
            {'id': 27, 'name': 'Horror'},
            {'id': 18, 'name': 'Drama'},
            {'id': 9648, 'name': 'Mystery'},
        ],
        'homepage': 'https://a24films.com/films/midsommar',
        'id': 530385,
        'imdb_id': 'tt8772262',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Midsommar',
        'overview': 'Several friends travel to Sweden to study as '
        'anthropologists a summer festival that is held every '
        'ninety years in the remote hometown of one of them. '
        'What begins as a dream vacation in a place where the '
        'sun never sets, gradually turns into a dark nightmare '
        'as the mysterious inhabitants invite them to '
        'participate in their disturbing festive activities.',
        'popularity': 41.601,
        'poster_path': '/7LEI8ulZzO5gy9Ww2NVCrKmHeDZ.jpg',
        'production_companies': [
            {
                'id': 39407,
                'logo_path': '/1ht2ayBUdGgKuLRCkTjyGVEY5VL.png',
                'name': 'B-Reel Films',
                'origin_country': 'SE',
            },
            {
                'id': 123620,
                'logo_path': '/ePRhZ3yb09Ya6WMzCCBYopwIYbE.png',
                'name': 'Square Peg',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'SE', 'name': 'Sweden'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2019-07-03',
        'revenue': 48015416,
        'runtime': 147,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'Swedish', 'iso_639_1': 'sv', 'name': 'svenska'},
        ],
        'status': 'Released',
        'tagline': 'Let the festivities begin.',
        'title': 'Midsommar',
        'video': False,
        'vote_average': 7.165,
        'vote_count': 6969,
    },
    545611: {
        'adult': False,
        'backdrop_path': '/ss0Os3uWJfQAENILHZUdX8Tt1OC.jpg',
        'belongs_to_collection': None,
        'budget': 25000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 12, 'name': 'Adventure'},
            {'id': 878, 'name': 'Science Fiction'},
        ],
        'homepage': 'https://a24films.com/films/everything-everywhere-all-at-once',
        'id': 545611,
        'imdb_id': 'tt6710474',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Everything Everywhere All at Once',
        'overview': 'An aging Chinese immigrant is swept up in an insane '
        "adventure, where she alone can save what's important to "
        'her by connecting with the lives she could have led in '
        'other universes.',
        'popularity': 47.378,
        'poster_path': '/rKvCys0fMIIi1X9rmJBxTPLAtoU.jpg',
        'production_companies': [
            {
                'id': 93105,
                'logo_path': '/asuzX794BM1gCettTxUoLxGNovd.png',
                'name': 'IAC Films',
                'origin_country': 'US',
            },
            {
                'id': 106544,
                'logo_path': '/psd84iF7PTGrKf4yFOStKj8JbAh.png',
                'name': 'AGBO',
                'origin_country': 'US',
            },
            {
                'id': 114130,
                'logo_path': '/4qWbeq1VqAH1RSCBFvCNkkY5Qi8.png',
                'name': 'Ley Line Entertainment',
                'origin_country': 'US',
            },
            {
                'id': 161506,
                'logo_path': None,
                'name': 'Year of the Rat',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2022-03-24',
        'revenue': 139200000,
        'runtime': 140,
        'spoken_languages': [
            {
                'english_name': 'Cantonese',
                'iso_639_1': 'cn',
                'name': '广州话 / 廣州話',
            },
            {'english_name': 'Mandarin', 'iso_639_1': 'zh', 'name': '普通话'},
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
        ],
        'status': 'Released',
        'tagline': 'The universe is so much bigger than you realize.',
        'title': 'Everything Everywhere All at Once',
        'video': False,
        'vote_average': 7.782,
        'vote_count': 6394,
    },
    546554: {
        'adult': False,
        'backdrop_path': '/4HWAQu28e2yaWrtupFPGFkdNU7V.jpg',
        'belongs_to_collection': {
            'backdrop_path': '/G7qYINSq5xyDd0I0zn3DpAssA0.jpg',
            'id': 722971,
            'name': 'Knives Out Collection',
            'poster_path': '/hAEATQo1enoasXMuSbeqw67E7N2.jpg',
        },
        'budget': 40000000,
        'genres': [
            {'id': 35, 'name': 'Comedy'},
            {'id': 80, 'name': 'Crime'},
            {'id': 9648, 'name': 'Mystery'},
        ],
        'homepage': 'https://www.lionsgate.com/movies/knives-out',
        'id': 546554,
        'imdb_id': 'tt8946378',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Knives Out',
        'overview': 'When renowned crime novelist Harlan Thrombey is found '
        'dead at his estate just after his 85th birthday, the '
        'inquisitive and debonair Detective Benoit Blanc is '
        "mysteriously enlisted to investigate. From Harlan's "
        'dysfunctional family to his devoted staff, Blanc sifts '
        'through a web of red herrings and self-serving lies to '
        "uncover the truth behind Harlan's untimely death.",
        'popularity': 89.882,
        'poster_path': '/pThyQovXQrw2m0s9x82twj48Jq4.jpg',
        'production_companies': [
            {
                'id': 1632,
                'logo_path': '/cisLn1YAUuptXVBa0xjq7ST9cH0.png',
                'name': 'Lionsgate',
                'origin_country': 'US',
            },
            {
                'id': 2531,
                'logo_path': '/9MfCJ2G6Nrf9yyRj4tAgPmMiDcn.png',
                'name': 'MRC',
                'origin_country': 'US',
            },
            {
                'id': 37871,
                'logo_path': '/aUOo1S2AabqQnRrXK6XuObWPDyK.png',
                'name': 'T-Street',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2019-11-27',
        'revenue': 312897920,
        'runtime': 131,
        'spoken_languages': [
            {'english_name': 'Spanish', 'iso_639_1': 'es', 'name': 'Español'},
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
        ],
        'status': 'Released',
        'tagline': 'Hell, any of them could have done it.',
        'title': 'Knives Out',
        'video': False,
        'vote_average': 7.848,
        'vote_count': 12195,
    },
    579974: {
        'adult': False,
        'backdrop_path': '/77GGKq6Ixq6ZiqBM6XcPZgQmiN2.jpg',
        'belongs_to_collection': None,
        'budget': 69000000,
        'genres': [{'id': 28, 'name': 'Action'}, {'id': 18, 'name': 'Drama'}],
        'homepage': '',
        'id': 579974,
        'imdb_id': 'tt8178634',
        'origin_country': ['IN'],
        'original_language': 'te',
        'original_title': 'రౌద్రం రణం రుధిరం',
        'overview': "A fictional history of two legendary revolutionaries' "
        'journey away from home before they began fighting for '
        'their country in the 1920s.',
        'popularity': 90.5,
        'poster_path': '/u0XUBNQWlOvrh0Gd97ARGpIkL0.jpg',
        'production_companies': [
            {
                'id': 68594,
                'logo_path': None,
                'name': 'DVV Entertainment',
                'origin_country': 'IN',
            },
            {
                'id': 103329,
                'logo_path': '/bjJ6phaG9F8cGm3RYBjly8wYuH5.png',
                'name': 'Pen Studios',
                'origin_country': 'IN',
            },
            {
                'id': 35124,
                'logo_path': '/clz3r0SYNudiGRB10yjvU9ZSgP8.png',
                'name': 'Lyca Productions',
                'origin_country': 'IN',
            },
        ],
        'production_countries': [{'iso_3166_1': 'IN', 'name': 'India'}],
        'release_date': '2022-03-24',
        'revenue': 160000000,
        'runtime': 185,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'Telugu', 'iso_639_1': 'te', 'name': 'తెలుగు'},
        ],
        'status': 'Released',
        'tagline': 'Rise, Roar, Revolt.',
        'title': 'RRR',
        'video': False,
        'vote_average': 7.754,
        'vote_count': 1258,
    },
    593643: {
        'adult': False,
        'backdrop_path': '/mSyQoValhBsJdq3JNGXJww2Q5yL.jpg',
        'belongs_to_collection': None,
        'budget': 35000000,
        'genres': [
            {'id': 35, 'name': 'Comedy'},
            {'id': 27, 'name': 'Horror'},
            {'id': 53, 'name': 'Thriller'},
        ],
        'homepage': 'https://searchlightpictures.com/the-menu',
        'id': 593643,
        'imdb_id': 'tt9764362',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'The Menu',
        'overview': 'A young couple travels to a remote island to eat at an '
        'exclusive restaurant where the chef has prepared a '
        'lavish menu, with some shocking surprises.',
        'popularity': 37.781,
        'poster_path': '/v31MsWhF9WFh7Qooq6xSBbmJxoG.jpg',
        'production_companies': [
            {
                'id': 125055,
                'logo_path': '/8iY66HqRqdQdwOjoS3sNvokcH9r.png',
                'name': 'Hyperobject Industries',
                'origin_country': 'US',
            },
            {
                'id': 127929,
                'logo_path': '/7DLKyL15ETI9645XSr9JcbMV79c.png',
                'name': 'Searchlight Pictures',
                'origin_country': 'US',
            },
            {
                'id': 4740,
                'logo_path': '/20IuOPEwlHRXnn0MTOsEmw0wcql.png',
                'name': 'Gary Sanchez Productions',
                'origin_country': 'US',
            },
            {
                'id': 22213,
                'logo_path': '/qx9K6bFWJupwde0xQDwOvXkOaL8.png',
                'name': 'TSG Entertainment',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2022-11-17',
        'revenue': 79628200,
        'runtime': 107,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'Spanish', 'iso_639_1': 'es', 'name': 'Español'},
        ],
        'status': 'Released',
        'tagline': 'Painstakingly prepared. Brilliantly executed.',
        'title': 'The Menu',
        'video': False,
        'vote_average': 7.184,
        'vote_count': 4758,
    },
    746036: {
        'adult': False,
        'backdrop_path': '/H5HjE7Xb9N09rbWn1zBfxgI8uz.jpg',
        'belongs_to_collection': None,
        'budget': 125000000,
        'genres': [{'id': 28, 'name': 'Action'}, {'id': 35, 'name': 'Comedy'}],
        'homepage': 'https://www.thefallguymovie.com',
        'id': 746036,
        'imdb_id': 'tt1684562',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'The Fall Guy',
        'overview': 'Fresh off an almost career-ending accident, stuntman '
        'Colt Seavers has to track down a missing movie star, '
        'solve a conspiracy and try to win back the love of his '
        'life while still doing his day job.',
        'popularity': 124.935,
        'poster_path': '/tSz1qsmSJon0rqjHBxXZmrotuse.jpg',
        'production_companies': [
            {
                'id': 121470,
                'logo_path': '/zvJFu1C6gB80A98n6IGXBvMtgVl.png',
                'name': '87North Productions',
                'origin_country': 'US',
            },
            {
                'id': 78984,
                'logo_path': '/vJLYh9YHQaEryuzu7GNUa1zwKG1.png',
                'name': 'Entertainment 360',
                'origin_country': 'US',
            },
            {
                'id': 33,
                'logo_path': '/8lvHyhjr8oUKOOy2dKXoALWKdp0.png',
                'name': 'Universal Pictures',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2024-04-24',
        'revenue': 181035480,
        'runtime': 126,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Fall hard.',
        'title': 'The Fall Guy',
        'video': False,
        'vote_average': 7.17,
        'vote_count': 2059,
    },
    799583: {
        'adult': False,
        'backdrop_path': '/s5znBQmprDJJ553IMQfwEVlfroH.jpg',
        'belongs_to_collection': None,
        'budget': 60000000,
        'genres': [
            {'id': 28, 'name': 'Action'},
            {'id': 35, 'name': 'Comedy'},
            {'id': 10752, 'name': 'War'},
        ],
        'homepage': 'https://www.theministryofungentlemanlywarfare.movie/',
        'id': 799583,
        'imdb_id': 'tt5177120',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'The Ministry of Ungentlemanly Warfare',
        'overview': 'During World War II, the British Army assigns a group '
        'of competent soldiers to carry out a mission against '
        'the Nazi forces behind enemy lines... A true story '
        'about a secret British WWII organization – the Special '
        'Operations Executive. Founded by Winston Churchill, '
        'their irregular warfare against the Germans helped to '
        'change the course of the war, and gave birth to modern '
        'black operations.',
        'popularity': 180.558,
        'poster_path': '/8aF0iAKH9MJMYAZdi0Slg77RYa2.jpg',
        'production_companies': [
            {
                'id': 130,
                'logo_path': '/c9dVHPOL3cqCr2593Ahk0nEKTEM.png',
                'name': 'Jerry Bruckheimer Films',
                'origin_country': 'US',
            },
            {
                'id': 22146,
                'logo_path': '/v37N1mFeXNQfvPankg3feBhVvM7.png',
                'name': 'Black Bear Pictures',
                'origin_country': 'US',
            },
            {
                'id': 2900,
                'logo_path': None,
                'name': 'Toff Guy Films',
                'origin_country': 'GB',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'GB', 'name': 'United Kingdom'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2024-04-18',
        'revenue': 27450915,
        'runtime': 120,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'German', 'iso_639_1': 'de', 'name': 'Deutsch'},
        ],
        'status': 'Released',
        'tagline': 'Discover the first special forces mission in history.',
        'title': 'The Ministry of Ungentlemanly Warfare',
        'video': False,
        'vote_average': 7.131,
        'vote_count': 1024,
    },
    937287: {
        'adult': False,
        'backdrop_path': '/4CcUgdiGe83MeqJW1NyJVmZqRrF.jpg',
        'belongs_to_collection': None,
        'budget': 55000000,
        'genres': [
            {'id': 10749, 'name': 'Romance'},
            {'id': 18, 'name': 'Drama'},
        ],
        'homepage': 'https://www.amazon.com/salp/challengers',
        'id': 937287,
        'imdb_id': 'tt16426418',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Challengers',
        'overview': 'Tennis player turned coach Tashi has taken her husband, '
        'Art, and transformed him into a world-famous Grand Slam '
        'champion. To jolt him out of his recent losing streak, '
        'she signs him up for a "Challenger" event — close to '
        'the lowest level of pro tournament — where he finds '
        'himself standing across the net from his former best '
        "friend and Tashi's former boyfriend.",
        'popularity': 151.494,
        'poster_path': '/H6vke7zGiuLsz4v4RPeReb9rsv.jpg',
        'production_companies': [
            {
                'id': 84041,
                'logo_path': '/nw4kyc29QRpNtFbdsBHkRSFavvt.png',
                'name': 'Pascal Pictures',
                'origin_country': 'US',
            },
            {
                'id': 226216,
                'logo_path': '/lVxgebv4lsM4mhgeJg9NUCahxIg.png',
                'name': 'Why Are You Acting? Productions',
                'origin_country': 'US',
            },
            {
                'id': 46344,
                'logo_path': '/qpSdIjnGHiz6UNIQWGIJkDnG79l.png',
                'name': 'Frenesy Film',
                'origin_country': 'IT',
            },
            {
                'id': 21,
                'logo_path': '/usUnaYV6hQnlVAXP6r4HwrlLFPG.png',
                'name': 'Metro-Goldwyn-Mayer',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'IT', 'name': 'Italy'},
            {'iso_3166_1': 'US', 'name': 'United States of America'},
        ],
        'release_date': '2024-04-18',
        'revenue': 94182533,
        'runtime': 132,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'},
            {'english_name': 'Romanian', 'iso_639_1': 'ro', 'name': 'Română'},
        ],
        'status': 'Released',
        'tagline': 'Her game. Her rules.',
        'title': 'Challengers',
        'video': False,
        'vote_average': 7.141,
        'vote_count': 1351,
    },
    945961: {
        'adult': False,
        'backdrop_path': '/9SSEUrSqhljBMzRe4aBTh17rUaC.jpg',
        'belongs_to_collection': None,
        'budget': 80000000,
        'genres': [
            {'id': 27, 'name': 'Horror'},
            {'id': 878, 'name': 'Science Fiction'},
            {'id': 28, 'name': 'Action'},
        ],
        'homepage': 'https://www.20thcenturystudios.com/movies/alien-romulus',
        'id': 945961,
        'imdb_id': 'tt18412256',
        'origin_country': ['US'],
        'original_language': 'en',
        'original_title': 'Alien: Romulus',
        'overview': 'While scavenging the deep ends of a derelict space '
        'station, a group of young space colonizers come face to '
        'face with the most terrifying life form in the '
        'universe.',
        'popularity': 622.593,
        'poster_path': '/b33nnKl1GSFbao4l3fZDDqsMx0F.jpg',
        'production_companies': [
            {
                'id': 127928,
                'logo_path': '/h0rjX5vjW5r8yEnUBStFarjcLT4.png',
                'name': '20th Century Studios',
                'origin_country': 'US',
            },
            {
                'id': 221347,
                'logo_path': '/6Ry6uNBaa0IbbSs1XYIgX5DkA9r.png',
                'name': 'Scott Free Productions',
                'origin_country': 'US',
            },
            {
                'id': 401,
                'logo_path': '/t7mM3DvQ9MwDT3YzMCBrkWpWiiz.png',
                'name': 'Brandywine Productions',
                'origin_country': 'US',
            },
        ],
        'production_countries': [
            {'iso_3166_1': 'US', 'name': 'United States of America'}
        ],
        'release_date': '2024-08-13',
        'revenue': 341521150,
        'runtime': 119,
        'spoken_languages': [
            {'english_name': 'English', 'iso_639_1': 'en', 'name': 'English'}
        ],
        'status': 'Released',
        'tagline': 'Everyone will hear you scream',
        'title': 'Alien: Romulus',
        'video': False,
        'vote_average': 7.1,
        'vote_count': 1075,
    },
}
