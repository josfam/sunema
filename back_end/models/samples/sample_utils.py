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
    select_attrs = ('id', 'title', 'poster_path', 'vote_average', 'release_date')

    for sample_film in sample_films.values():
        film = SampleFilm(**sample_film)
        db.session.add(film)
    db.session.commit()

sample_collections = {
    19968: {
        'adult': False,
        'backdrop_path': '/4fobpKsoeNrJ8BtbYiHP4AdSVjU.jpg',
        'genre_ids': [35, 10752],
        'id': 19968,
        'original_language': 'en',
        'original_title': 'No Time for Sergeants',
        'overview': 'Georgia farm boy Will Stockdale is about to bust with '
        "pride. He's been drafted. Will's ready. But is Uncle Sam "
        'ready for Will?',
        'popularity': 3.695,
        'poster_path': '/yCoIRzy6C5TCXN0ibD2IqEqqOgl.jpg',
        'release_date': '1958-07-05',
        'title': 'No Time for Sergeants',
        'video': False,
        'vote_average': 7.22,
        'vote_count': 50,
    },
    406169: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [53],
        'id': 406169,
        'original_language': 'en',
        'original_title': 'Adult Fun',
        'overview': 'A young London City-worker inadvertently becomes '
        'involved in the world of crime.',
        'popularity': 1.095,
        'poster_path': '/bMVbE5iZD5B3UbRPZFsWTJLFBVJ.jpg',
        'release_date': '1972-11-29',
        'title': 'Adult Fun',
        'video': False,
        'vote_average': 7.0,
        'vote_count': 3,
    },
    845157: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [27],
        'id': 845157,
        'original_language': 'en',
        'original_title': 'Soft Teeth',
        'overview': 'A man with throbbing mouth pain suffers the '
        'consequences of ignoring the world around him.',
        'popularity': 0.245,
        'poster_path': '/pP5TwwlVESTd2BzKPSupS5ZZLEQ.jpg',
        'release_date': '2022-07-01',
        'title': 'Soft Teeth',
        'video': False,
        'vote_average': 10.0,
        'vote_count': 1,
    },
    856926: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [9648, 80, 10770],
        'id': 856926,
        'original_language': 'en',
        'original_title': "Ellery Queen: Don't Look Behind You",
        'overview': 'Detective Ellery Queen has to solve a series of murders '
        'where the victims were killed in numerically descending '
        'ages, the male victims were strangled with blue cords '
        'and the female victims with pink ones.',
        'popularity': 0.631,
        'poster_path': '/6SpHSoSetgG2Y885yVbc8j8BkVX.jpg',
        'release_date': '1971-11-19',
        'title': "Ellery Queen: Don't Look Behind You",
        'video': False,
        'vote_average': 8.0,
        'vote_count': 1,
    },
    954854: {
        'adult': False,
        'backdrop_path': '/8daz0LOlaA3ZLC5CMxfXOHEIppb.jpg',
        'genre_ids': [18, 80],
        'id': 954854,
        'original_language': 'ja',
        'original_title': '鬼平犯科帳スペシャル 引き込み女',
        'overview': 'Edo town thief called "Acrobatics boy" has been rampant '
        'in town, just that time, spy, Goro of Otaki will see a '
        'woman who had been an inside contact of the Yataro by '
        'chance. Also, Heizo is worried about the child of Inoue '
        "Tatsuizumi, who decided to ask for help for Gen'an.",
        'popularity': 2.877,
        'poster_path': '/coca0yycujVfYeSIHhp7qQLHX1q.jpg',
        'release_date': '2008-10-17',
        'title': 'Onihei Crime Files: The Inside Woman',
        'video': False,
        'vote_average': 8.0,
        'vote_count': 1,
    },
    1302485: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [9648, 80, 18],
        'id': 1302485,
        'original_language': 'en',
        'original_title': 'Darius Lockwood and the Murder For Truth',
        'overview': 'A victorian Detective and his faithful companion must '
        'solve a murder, but in doing so they uncover a much '
        'deeper, darker secret.',
        'popularity': 0.319,
        'poster_path': '/uuwAFtyLzQv9g9GLUnMuMaBm1he.jpg',
        'release_date': '2024-05-30',
        'title': 'Darius Lockwood and the Murder For Truth',
        'video': False,
        'vote_average': 10.0,
        'vote_count': 1,
    },
    260569: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [28],
        'id': 260569,
        'original_language': 'ja',
        'original_title': '女囚さそり 殺人予告',
        'overview': 'A woman who, disguised as a beggar, turns out to be a '
        'formidable assassin, is charged by a warden to '
        "infiltrate a women's prison, to run the one that took "
        'his eye with a wooden spoon carved from a knife - a '
        'woman named Nami Matsushima, known within the walls '
        'under the nickname of Scorpion.',
        'popularity': 3.216,
        'poster_path': '/ZfG1jtuo7iJBEWw10mufIguFUR.jpg',
        'release_date': '1991-05-17',
        'title': 'Scorpion Woman Prisoner: Death Threat',
        'video': False,
        'vote_average': 10.0,
        'vote_count': 1,
    },
    302326: {
        'adult': False,
        'backdrop_path': '/81lZCne8NJpdGcpZkqdZr1VDPvC.jpg',
        'genre_ids': [10751, 16],
        'id': 302326,
        'original_language': 'en',
        'original_title': 'The Enormous Crocodile',
        'overview': 'When the Enormous Crocodile boasts that he is going to '
        'eat a child for his lunch, the other jungle animals '
        'decide to foil his dastardly plot. Children of all ages '
        'will delight in the exploits of Humpy Rumpy - the '
        'hippopotamus, Muggle Wump - the monkey and the amazing '
        'antics of the Roly-Poly bird.',
        'popularity': 2.958,
        'poster_path': '/6s8nDBbE16fTNnlOK2vhng89qcV.jpg',
        'release_date': '1990-01-02',
        'title': 'The Enormous Crocodile',
        'video': False,
        'vote_average': 7.0,
        'vote_count': 2,
    },
    441130: {
        'adult': False,
        'backdrop_path': '/yeJhRNtE4XW2lOoVVFO9iuDr3AL.jpg',
        'genre_ids': [16, 10751, 12, 14],
        'id': 441130,
        'original_language': 'en',
        'original_title': 'Wolfwalkers',
        'overview': 'In a time of superstition and magic, when wolves are '
        'seen as demonic and nature an evil to be tamed, a young '
        'apprentice hunter comes to Ireland with her father to '
        'wipe out the last pack. But when she saves a wild '
        'native girl, their friendship leads her to discover the '
        'world of the Wolfwalkers and transform her into the '
        'very thing her father is tasked to destroy.',
        'popularity': 22.564,
        'poster_path': '/53VE3Iv9NiCOJfFMWwQuRUQMaXZ.jpg',
        'release_date': '2020-10-26',
        'title': 'Wolfwalkers',
        'video': False,
        'vote_average': 8.224,
        'vote_count': 1164,
    },
    809526: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [878],
        'id': 809526,
        'original_language': 'en',
        'original_title': 'parabiosis: neurolibidinal induction complex',
        'overview': 'Parabiosis: neurolibidinal induction complex is a '
        'program specially designed to produce iatrogenic '
        'interlock in target neurologies. It delivers its '
        'effects via deep audiovisual stimulation. Informatic '
        'overlays reproduce a signal which induces '
        'intensification of pre-existing tendencies in such '
        'neurologies.',
        'popularity': 0.035,
        'poster_path': '/noQ76TcYOoXY7pqdZ73gEjzUYla.jpg',
        'release_date': '',
        'title': 'parabiosis: neurolibidinal induction complex',
        'video': False,
        'vote_average': 8.0,
        'vote_count': 1,
    },
    1089263: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [35, 12],
        'id': 1089263,
        'original_language': 'tr',
        'original_title': 'Tatil Belası',
        'overview': '',
        'popularity': 0.508,
        'poster_path': '/7KK2t2ZcvkpzfaB60p3OhAtFe8J.jpg',
        'release_date': '1997-01-01',
        'title': 'Tatil Belası',
        'video': False,
        'vote_average': 9.0,
        'vote_count': 1,
    },
    1111889: {
        'adult': False,
        'backdrop_path': '/ndOa8B63Jh3pkbGDTF1gbw38gr2.jpg',
        'genre_ids': [35, 99],
        'id': 1111889,
        'original_language': 'en',
        'original_title': 'Carol Burnett: 90 Years of Laughter + Love',
        'overview': 'Paying tribute to a beloved national icon for her '
        'birthday, NBC celebrates Carol Burnett’s illustrious '
        'career with a star-studded event featuring an A-list '
        'lineup of musical performances and special guests who '
        'come together to share their love for one of the most '
        'cherished comediennes in television history.',
        'popularity': 2.45,
        'poster_path': '/2MKglxLcNgKE7GFxWD7k3ZReOuQ.jpg',
        'release_date': '2023-04-26',
        'title': 'Carol Burnett: 90 Years of Laughter + Love',
        'video': False,
        'vote_average': 8.429,
        'vote_count': 7,
    },
    205358: {
        'adult': False,
        'backdrop_path': '/1F3rhBh35uG5S2pCvcrxqaWlZ0L.jpg',
        'genre_ids': [18, 28],
        'id': 205358,
        'original_language': 'ja',
        'original_title': '獣たちの熱い眠り',
        'overview': 'A star tennis player takes revenge on the blackmailers '
        'out to ruin his athletic career.',
        'popularity': 4.176,
        'poster_path': '/ayxdqkSK0XClMf2fo9UwwHcABu6.jpg',
        'release_date': '1981-09-12',
        'title': 'The Hidden Trail of the Beasts',
        'video': False,
        'vote_average': 7.0,
        'vote_count': 2,
    },
    364759: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [878, 18, 53, 9648, 14, 27],
        'id': 364759,
        'original_language': 'en',
        'original_title': 'Home Sweet Home',
        'overview': "Ben's not as sharp as he once was. Thank god he's got "
        "his wife around to look out for him. But something's "
        'not right. Something seems to be lurking in the shadows '
        "and this time it's up to him to figure it out.",
        'popularity': 0.663,
        'poster_path': None,
        'release_date': '2015-02-21',
        'title': 'Home Sweet Home',
        'video': False,
        'vote_average': 7.2,
        'vote_count': 2,
    },
    413164: {
        'adult': False,
        'backdrop_path': '/aB6cqsQyfAWWHFqyKPAa66qm5qG.jpg',
        'genre_ids': [16, 14, 28, 10402, 12, 35, 10751],
        'id': 413164,
        'original_language': 'ja',
        'original_title': '映画 プリキュアオールスターズ みんなで歌う 奇跡の魔法！',
        'overview': 'Mirai and Rico come to the human world to play, but are '
        'separated when the witch Sorcierre and her servant '
        'Trauuma suddenly appear. Their aim is to acquire the '
        'tears of the 44 Precure girls, using them for her Most '
        'Evil Magic. Only the friendship of all 44 Precure girls '
        'will allow them to protect the world.',
        'popularity': 2.974,
        'poster_path': '/de8pcCDwgQ6Mne5Z0NxsQr2D943.jpg',
        'release_date': '2016-03-19',
        'title': 'Pretty Cure All Stars Movie: Everybody Sing! Miraculous '
        'Magic!',
        'video': False,
        'vote_average': 7.4,
        'vote_count': 8,
    },
    950833: {
        'adult': False,
        'backdrop_path': '/lUstCnFLmOa5xvku0bxAs50ZBiV.jpg',
        'genre_ids': [16],
        'id': 950833,
        'original_language': 'fr',
        'original_title': 'The Record',
        'overview': 'A traveller gives an antiques dealer a magic vinyl '
        'record: "It reads your mind and plays your lost '
        'memories". Obsessed by this endless record, he listens '
        'to it again and again.',
        'popularity': 0.962,
        'poster_path': '/ndy78Ev3RxpAtQ0AZbWwF4hLWGo.jpg',
        'release_date': '2022-06-13',
        'title': 'The Record',
        'video': False,
        'vote_average': 7.833,
        'vote_count': 3,
    },
    1175075: {
        'adult': False,
        'backdrop_path': '/2UYUojn45G06tk2gTbQc20DQGCm.jpg',
        'genre_ids': [35],
        'id': 1175075,
        'original_language': 'es',
        'original_title': 'Menudas piezas',
        'overview': 'Candela, the headmistress of an elite school, after a '
        'traumatic divorce, returns to her old high school to '
        'lead a group of rebellious students through chess. '
        'There she will learn that in chess, and in life, it '
        "doesn't matter if you are a king or a pawn, because "
        'everyone ends up in the same box.',
        'popularity': 16.582,
        'poster_path': '/epxMmvLaQmInLeRNOIMfRaJrhSZ.jpg',
        'release_date': '2024-04-12',
        'title': 'Checkmates',
        'video': False,
        'vote_average': 7.148,
        'vote_count': 43,
    },
    1299215: {
        'adult': False,
        'backdrop_path': None,
        'genre_ids': [12, 878, 16, 28, 10752],
        'id': 1299215,
        'original_language': 'en',
        'original_title': 'Battle of the Brick: Built for Combat',
        'overview': 'The blue and red teams fight on the shores of Zanzibar '
        'in a brutal game of capture the flag.',
        'popularity': 1.776,
        'poster_path': None,
        'release_date': '2011-12-01',
        'title': 'Battle of the Brick: Built for Combat',
        'video': False,
        'vote_average': 9.0,
        'vote_count': 1,
    },
}
