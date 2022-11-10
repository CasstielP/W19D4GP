from dotenv import load_dotenv
load_dotenv()


from app import app, db
from app.models import Pokemon, Item


with app.app_context():
    db.drop_all()
    db.create_all()

    bul = Pokemon(number=1,image_url='./images/pokemon_snaps/1.svg',name='Bulbasaur',attack=49,defense=49,type='grass',moves=['tackle','vine whip'],captured=True)
    ivy = Pokemon(number=2,image_url='./images/pokemon_snaps/2.svg',name='Ivysaur',attack=62,defense=63,type='grass',moves=['tackle','vine whip','razor leaf'],captured=True)
    item1 = Item(happiness=90, image_url='./images/pokemon_berry.svg', name='berry', price=100, pokemon_id=1)
    item2 = Item(happiness=99, image_url='./images/pokemon_egg.svg', name='egg', price=150, pokemon_id=2)

    db.session.add(bul)
    db.session.add(ivy)
    db.session.add(item1)
    db.session.add(item2)
    db.session.commit()
