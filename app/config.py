import os
from datetime import timedelta


class Config(object):

    SECRET_KEY = 'kaadfadfafafdafafadddddadfadadfaffddddddd'    
    # REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://armandosuazo:a1234567@armandosuazo.mysql.pythonanywhere-services.com/medical_db"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://armandosuazo:a1234567@armandosuazo.mysql.pythonanywhere-services.com/inspection_db"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@127.0.0.1/medic_consult_db'
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_MAX_OVERFLOW = 20
    SQLALCHEMY_POOL_TIMEOUT = 300

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True  
 
    #********MY PATHS ROUTES ------------****************************
    IMAGE_UPLOADS = 'C:/Users/UserGP/Documents/PROC_INSP/app/static/img/img_database'
    IMAGE_UPLOADS_PROFILE = 'C:/Users/UserGP/Documents/PROC_INSP/app/static/img/profile'
    SAVED_GRAPH_PNG = "C:/Users/UserGP/Documents/PROC_INSP/app/saved_graph"
   
    ALLOWED_IMAGE_EXTENSIONS = ['JPG','JPEG', 'PNG', 'GIF']
    MAX_IMAGE_FILESIZE = 1024 * 1024
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024


class Develop(object):

    SECRET_KEY = 'kaadfadfafafdafafadddddadfadadfaffddddddd'    
    # REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
    
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://armandosuazo:a1234567@armandosuazo.mysql.pythonanywhere-services.com/medical_db"
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://armandosuazo:a1234567@armandosuazo.mysql.pythonanywhere-services.com/inspection_db"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:''@127.0.0.1/inspection_db'
    # SQLALCHEMY_POOL_SIZE = 30
    # SQLALCHEMY_MAX_OVERFLOW = 20
    # SQLALCHEMY_POOL_TIMEOUT = 300

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True    

    #********MY PATHS ROUTES ------------****************************
    IMAGE_UPLOADS = 'C:/Users/UserGP/Documents/PROC_INSP/app/static/img/img_database'
    IMAGE_UPLOADS_PROFILE = 'C:/Users/UserGP/Documents/PROC_INSP/app/static/img/profile'
    SAVED_GRAPH_PNG = "C:/Users/UserGP/Documents/PROC_INSP/app/saved_graph"
   
    ALLOWED_IMAGE_EXTENSIONS = ['JPG','JPEG', 'PNG', 'GIF']
    MAX_IMAGE_FILESIZE = 1024 * 1024
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

