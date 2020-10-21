from flask.cli import AppGroup
from model import db
import os, urllib.request, click

db_cli = AppGroup('db')
@db_cli.command('create')
def db_create():
    db.create_all()
@db_cli.command('drop')
def db_drop():
    db.drop_all()

translate_cli = AppGroup('translate')
@translate_cli.command('download')
@click.argument('lang')
def translate_download(lang):
    try:
        urllib.request.urlretrieve(
            'https://dl.fbaipublicfiles.com/arrival/vectors/wiki.multi.{}.vec'.format(lang),
            os.getcwd()+'/../data/wiki.multi.{}.vec'.format(lang))
    except Exception as ex:
        print(ex)
