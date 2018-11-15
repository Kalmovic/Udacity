from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()
#This secret key will be used to create and verify your tokens
secret_key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
      s = Serializer(secret_key, expires_in = expiration)
      return s.dumps({'id': self.id })

    @staticmethod
    def verify_auth_token(token):
      s = Serializer(secret_key)
      try:
        data = s.loads(token)
      except SignatureExpired:
        #Valid Token, but expired
        return None
      except BadSignature:
        #Invalid Token
        return None
      user_id = data['id']
      return user_id


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
    __tablename__ = 'immobile'

    address =Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(100), nullable = False)
    squarefeet = Column(Integer(10) , nullable = False)
    bedrooms = Column(Integer(8), nullable = False)
    bathrooms = Column(Integer(8), nullable = False)
    city_id = Column(Integer,ForeignKey('city.id'))
    city = relationship(Immobile)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'address'         : self.address,
           'description'         : self.description,
           'id'         : self.id,
           'squarefeet'         : self.squarefeet,
           'bedrooms'         : self.bedrooms,
           'bathrooms'         : self.bathrooms,
       }



engine = create_engine('sqlite:///immobileswithusers.db')


Base.metadata.create_all(engine)
