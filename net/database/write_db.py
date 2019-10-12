import csv
from database.db import data_db as db
from net.move.models import Move

def write_data_to_move_table():
    with open('datasets/movies_metadata.csv', 'rt') as f:
        spamreader = csv.DictReader(f, quotechar='\"')
        db.migrate()
        for row in spamreader:
            db.Session.add(Move(
                adult= row['adult'] == 'True',
                belongs_to_collection=row['belongs_to_collection'],
                budget=int(row['budget']),
                genres=row['genres'],
                homepage=row['homepage'],
                idd=row['id'],
                imdb_id=row['imdb_id'],
                original_language=row['original_language'],
                original_title=row['original_title'],
                overview=row['overview'],
                popularity=row['popularity'],
                poster_path=row['poster_path'],
                production_companies=row['production_companies'],
                production_countries=row['production_countries'],
                release_date=row['release_date'],
                revenue=row['revenue'],
                runtime=row['runtime'],
                spoken_languages=row['spoken_languages'],
                status=row['status'],
                tagline=row['tagline'],
                title=row['title'],
                video=row['video'],
                vote_average=row['vote_average'],
                vote_count=row['vote_count'],       
            ))
            db.Session.commit()
