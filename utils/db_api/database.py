from gino import Gino
from data.config import DB_HOST, DB_NAME, DB_PASS,DB_USER
db = Gino()

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer,primary_key = True)
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String)
    price = db.Column(db.Float)
    date_timee = db.Column(db.String)

class DB_Commands:
    async def getcategories(self):
        categories = await Category.query.gino.all()
        return categories

async def create_db():
    # await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    # await db.set_bind(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")
    await db.gino.create_all()
    # await db.gino.drop_all()