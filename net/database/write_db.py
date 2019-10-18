import ast
import csv

from sqlalchemy import exists

from net.database.db import data_db as db
from net.move.models import Company, Country, Genre, Move


def get_obj_from_json(json_list, model_name):
    models = {
        'production_companies': Company,
        'genres': Genre,
        'production_countries': Country
    }
    model = models[model_name]
    name_list = [i['name'] for i in ast.literal_eval(json_list)]
    model_objects = db.Session.query(model).filter(model.name.in_(name_list))
    return model_objects


def write_data_to_move_meta_table(path):
    def add_new_obj_to_session(row, model_type):
        models = {
            'production_companies': Company,
            'genres': Genre,
            'production_countries': Country
        }
        if not model_type in ['production_companies', 'genres', 'production_countries']:
            return

        if row.get(model_type, None):
            try:
                model = models[model_type]
                for i in ast.literal_eval(row[model_type]):
                    if not db.Session.query(exists().where(model.name == i['name'])).scalar() and i['name'] != '':
                        db.Session.add(model(
                            name=i['name'],
                            slug='-'.join(i['name'].split(' ')),
                        ))
            except Exception as e:
                print('error ', e)
                return

    with open(path, 'rt') as f:
        spamreader = csv.DictReader(f, quotechar='\"')
        db.migrate()

        for row in spamreader:
            add_new_obj_to_session(row, 'production_companies')
            add_new_obj_to_session(row, 'production_countries')
            add_new_obj_to_session(row, 'genres')
            db.Session.commit()


def write_data_to_move_table(path):
    with open(path, 'rt') as f:
        spamreader = csv.DictReader(f, quotechar='\"')

        for row in spamreader:
            if db.Session.query(exists().where(Move.title == row['original_title'])).scalar():
                continue

            move = Move(
                adult=row['adult'] == 'True',
                belongs_to_collection=row['belongs_to_collection'],
                budget=int(row['budget']),
                homepage=row['homepage'],
                idd=row['id'],
                imdb_id=row['imdb_id'],
                original_language=row['original_language'],
                original_title=row['original_title'],
                overview=row['overview'],
                popularity=row['popularity'],
                poster_path=row['poster_path'],
                release_date=row['release_date'],
                revenue=row['revenue'],
                runtime=row['runtime'],
                spoken_languages=row['spoken_languages'],
                status=row['status'],
                tagline=row['tagline'],
                title=row['original_title'],
                video=row['video'],
                vote_average=row['vote_average'],
                vote_count=row['vote_count'],
            )
            try:
                genres, companies, countries = (
                    get_obj_from_json(row['genres'], model_name='genres'),
                    get_obj_from_json(row['production_companies'], model_name='production_companies'),
                    get_obj_from_json(row['production_countries'], model_name='production_countries')
                )
            except Exception as e:
                print('error ', e)
                continue

            for genre, company, country in zip(genres, companies, countries):
                move.genres.append(genre)
                move.production_companies.append(company)
                move.production_countries.append(country)

            db.Session.add(move)
            db.Session.commit()
