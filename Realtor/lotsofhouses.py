from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, City, Immobile, User

engine = create_engine('sqlite:///immobileswithusers.db')


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

city1 = City(name = "Rio de Janeiro")

session.add(city1)
session.commit()

immobileDetails1 = Immobile(address = "Street Ituverava, 1033",
                           description = "House",
                           squarefeet = "1323 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city1)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Henrique de Novais, 155",
                           description = "Apartment",
                           squarefeet = "839 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathroom",
                           city = city1)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Caruso, 19",
                           description = "House",
                           squarefeet = "4305 squarefeet",
                           bedrooms = "7 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city1)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Professor Gabiso, 135",
                           description = "House",
                           squarefeet = "4187 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city1)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street Franco Zampari, 111",
                           description = "Apartment",
                           squarefeet = "796 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city1)

session.add(immobileDetails5)
session.commit()

city2 = City(name = "Sao Paulo")

session.add(city2)
session.commit()

immobileDetails1 = Immobile(address = "Street Sao Joao Cabral, 48",
                           description = "House",
                           squarefeet = "1808 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city2)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Camburiu, 413",
                           description = "Apartment",
                           squarefeet = "721 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city2)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Dr. Joao Jorge Sabino, 270",
                           description = "House",
                           squarefeet = "1216 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city2)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Avenue Escragnolle Doria, 322",
                           description = "House",
                           squarefeet = "1453 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city2)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street Jose Cola Grossi",
                           description = "House",
                           squarefeet = "3993 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city2)

session.add(immobileDetails5)
session.commit()

city3 = City(name = "Belo Horizonte")

session.add(city3)
session.commit()

immobileDetails1 = Immobile(address = "Street Coronel Emilio Martins, 140",
                           description = "House",
                           squarefeet = "2271 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city3)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Purus",
                           description = "House",
                           squarefeet = "624 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city3)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Deputado Gregoriano Canedo, 698",
                           description = "House",
                           squarefeet = "968 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city3)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Heitor Socrates Cardoso, 587",
                           description = "House",
                           squarefeet = "1937 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city3)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street Jaime Petiti da Silva, 196",
                           description = "House",
                           squarefeet = "3875 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city3)

session.add(immobileDetails5)
session.commit()

city4 = City(name = "Porto Alegre")

session.add(city4)
session.commit()

immobileDetails1 = Immobile(address = "Street General Rondon, 123",
                           description = "House",
                           squarefeet = "3552 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city4)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Conselheiro Xavier da Costa, 2431",
                           description = "House",
                           squarefeet = "5920 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "5 bathrooms",
                           city = city4)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Dona Augusta, 244 ",
                           description = "House",
                           squarefeet = "1399 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city4)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Pedro Carneiro Pereira, 65",
                           description = "House",
                           squarefeet = "3993 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city4)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Avenue Vicente Monteggia, 586",
                           description = "House",
                           squarefeet = "3444 squarefeet",
                           bedrooms = "7 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city4)

session.add(immobileDetails5)
session.commit()

city5 = City(name = "Vitoria")

session.add(city5)
session.commit()

immobileDetails1 = Immobile(address = "Avenue Desembargador Alfredo Cabral, 870",
                           description = "House",
                           squarefeet = "12916 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "6 bathrooms",
                           city = city5)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Avenue Antonio Borges, 186",
                           description = "House",
                           squarefeet = "9343 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "5 bathrooms",
                           city = city5)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Fortunato Abreu Gagno",
                           description = "House",
                           squarefeet = "2690 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city5)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Manoel Gomes de Almeida",
                           description = "House",
                           squarefeet = "8880 squarefeet",
                           bedrooms = "5 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city5)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street General Camara, 96",
                           description = "House",
                           squarefeet = "2368 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city5)

session.add(immobileDetails5)
session.commit()

city6 = City(name = "Curitiba")

session.add(city6)
session.commit()

immobileDetails1 = Immobile(address = "Street Capitao Tenente Maris de Barros, 313",
                           description = "Apartment",
                           squarefeet = "753 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city6)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Rua Antonio Gasparin, 4911",
                           description = "Apartment",
                           squarefeet = "1140 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city6)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Avenue Rep. Argentina, 2524",
                           description = "Apartment",
                           squarefeet = "678 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city6)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Dona Alice Tibirica, 611",
                           description = "Apartment",
                           squarefeet = "1593 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "5 bathrooms",
                           city = city6)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street Gago Coutinho, 45",
                           description = "Apartment",
                           squarefeet = "1022 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city6)

session.add(immobileDetails5)
session.commit()

city7 = City(name = "Florianopolis")

session.add(city7)
session.commit()

immobileDetails1 = Immobile(address = "Servidao Belo Horizonte, 390",
                           description = "House",
                           squarefeet = "645 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "1 bathrooms",
                           city = city7)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Manoel Pedro Teixeira, 1",
                           description = "House",
                           squarefeet = "753 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "1 bathrooms",
                           city = city7)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Servidao Sotero Jose de Farias, 429",
                           description = "House",
                           squarefeet = "2152 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city7)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Joao Jose Adriano, 188",
                           description = "House",
                           squarefeet = "2820 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city7)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Servidao Bons Amigos, 300",
                           description = "House",
                           squarefeet = "1237 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city7)

session.add(immobileDetails5)
session.commit()

city8 = City(name = "Salvador")

session.add(city8)
session.commit()

immobileDetails1 = Immobile(address = "Street Rua das Azaleias, 184",
                           description = "House",
                           squarefeet = "4413 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "5 bathrooms",
                           city = city8)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Avenida Alphaville, 100",
                           description = "House",
                           squarefeet = "3821 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "6 bathrooms",
                           city = city8)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Alameda das Samambaias, 620",
                           description = "House",
                           squarefeet = "1345 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city8)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Ramalho Ortigao, 51",
                           description = "House",
                           squarefeet = "4305 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "5 bathrooms",
                           city = city8)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Avenue Dorival Caymmi, 63",
                           description = "House",
                           squarefeet = "914 squarefeet",
                           bedrooms = "2 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city8)

session.add(immobileDetails5)
session.commit()

city9 = City(name = "Gramado")

session.add(city9)
session.commit()

immobileDetails1 = Immobile(address = "Street Leopoldo Geier, 174",
                           description = "House",
                           squarefeet = "1087 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city9)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Joao Alfredo Schneider, 792",
                           description = "House",
                           squarefeet = "3552 squarefeet",
                           bedrooms = "6 bedrooms",
                           bathrooms = "5 bathrooms",
                           city = city9)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Nereu Ramos, 223",
                           description = "House",
                           squarefeet = "1829 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "3 bathrooms",
                           city = city9)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Nereu Ramos, 333",
                           description = "House",
                           squarefeet = "2475 squarefeet",
                           bedrooms = "5 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city9)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street Sao Marcos, 30",
                           description = "House",
                           squarefeet = "1614 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city9)

session.add(immobileDetails5)
session.commit()

city10 = City(name = "Recife")

session.add(city10)
session.commit()

immobileDetails1 = Immobile(address = "Street Ipiniras, 118",
                           description = "House",
                           squarefeet = "893 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "1 bathrooms",
                           city = city10)

session.add(immobileDetails1)
session.commit()

immobileDetails2 = Immobile(address = "Street Capitao Araujo Miranda, 178",
                           description = "House",
                           squarefeet = "1808 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city10)

session.add(immobileDetails2)
session.commit()

immobileDetails3 = Immobile(address = "Street Jader de Andrade, 125",
                           description = "House",
                           squarefeet = "4305 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "4 bathrooms",
                           city = city10)

session.add(immobileDetails3)
session.commit()

immobileDetails4 = Immobile(address = "Street Ambrosio Machado, 210",
                           description = "House",
                           squarefeet = "753 squarefeet",
                           bedrooms = "3 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city10)

session.add(immobileDetails4)
session.commit()

immobileDetails5 = Immobile(address = "Street Itacaja, 66",
                           description = "House",
                           squarefeet = "4574 squarefeet",
                           bedrooms = "4 bedrooms",
                           bathrooms = "2 bathrooms",
                           city = city10)

session.add(immobileDetails5)
session.commit()

print "address added!!"