from dotenv import load_dotenv
load_dotenv()


from app import app, db
from app.models import Pokemon, Item, Type


with app.app_context():
    db.drop_all()
    db.create_all()

    bul = Pokemon(number=1,image_url='https://cis3110fall2021pi.s3.us-west-1.amazonaws.com/Screenshot+2022-08-03+181306.png',name='Bulbasaur',attack=49,defense=49,type=Type.grass,moves='tackle',captured=True)
    ivy = Pokemon(number=2, image_url='/images/pokemon_snaps/2.svg', name='Ivysaur', attack=62,
                  defense=63, type=Type.grass, moves='vine whip', captured=True)
    item1 = Item(happiness=90, image_url='/images/pokemon_berry.svg', name='berry', price=100, pokemon_id=1)
    item2 = Item(happiness=99, image_url='/images/pokemon_egg.svg', name='egg', price=150, pokemon_id=2)
    item3 = Item(happiness=99, image_url='/images/pokemon_egg.svg', name='egg', price=150, pokemon_id=1)

    db.session.add(bul)
    db.session.add(ivy)
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
