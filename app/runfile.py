#runfile.py
from models import engine, Base
from sqlalchemy.orm import sessionmaker
from models import Band, Venue,Concert


Base.metadata.create_all(engine)
    
Session= sessionmaker(bind=engine)
session = Session()

def create_cases():
    band1 = Band(name="Taylor Swift", hometown="Pennsylvania")
    band2 = Band(name="Depeche Mode", hometown="Basildon")
    band3 = Band(name="Doja Cat", hometown="Carlifonia")
    band4 = Band(name="Lana Del Rey", hometown="New York")
    band5 = Band(name="Lenny Kravitz", hometown="New York")

    venue1 = Venue(title="La Defense Arena", city="Paris")
    venue2 = Venue(title="Royal Arena", city="Copenhagen")
    venue3 = Venue(title="Ziggo Dome", city="Amsterdam")
    venue4 = Venue(title="Mediolanum Forum", city="Milan")
    venue5 = Venue(title="Tauron Arena", city="Krakow")

    concert1 = Concert(date="2024-05-09", band=band1, venue=venue1)
    concert2 = Concert(date="2024-02-08", band=band2, venue=venue2)
    concert3 = Concert(date="2024-06-19", band=band4, venue=venue5)

    session.add_all([band1, band2, band3, band4, band5, venue1, venue2, venue3, venue4, venue5, concert1, concert2, concert3])
    session.commit()

def queries():
    most_performances = Band.most_performances(session)
    if most_performances:
        print(f"Band with the most performances: {most_performances.name}")

    concert = session.query(Concert).first()
    if concert:
        print(concert.introduction())
        
if __name__ == '__main__':
    create_cases()
    queries()        