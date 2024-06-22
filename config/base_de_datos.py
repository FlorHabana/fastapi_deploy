import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

fichero = "../datos.sqlite"
#leemos el directorio actual del archivo de base de datos
directorio = os.path.dirname(os.path.realpath(__file__))
#direccion bd uniendo las 2 variables anteriores
ruta = f"sqlite:///{os.path.join(directorio,fichero)}"
#creamos el motor 
motor = create_engine(ruta,echo=True)
#creamos la sesión  pasandole el motor
sesion = sessionmaker(bind=motor)
#crear base para manejar las tablas
base = declarative_base()