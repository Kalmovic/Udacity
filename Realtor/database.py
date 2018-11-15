from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'user_id'      : self.user_id
       }

class Immobile(Base):
    __tablename__ = 'info'

    address =Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(100), nullable = False)
    squarefeet = Column(Integer(10) , nullable = False)
    bedrooms = Column(Integer(8), nullable = False)
    bathrooms = Column(Integer(8), nullable = False)
    immobile_id = Column(Integer,ForeignKey('immobile.id'))
    immobile = relationship(Immobile)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'course'         : self.course,
       }



engine = create_engine('sqlite:///restaurantmenuwithusers.db')


Base.metadata.create_all(engine)