from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import session, engine
import backend.database_model as database_model
from backend.models import Product
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173"
        ],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)

database_model.Base.metadata.create_all(bind=engine)

@app.get('/')
def greet():
    return "Hello, welcome !!!"

def get_db():
    db = session()
    try:
        yield db
    except Exception as e:
        raise e
    finally:
        db.close()

# def init_db(): #initial data insertion
#     db = session()
#     count = db.query(database_model.Product).count()
#     if count == 0:
#         for product in products:
#             db.add(database_model.Product(**product.model_dump())) 
#     db.commit()
# init_db()

@app.get('/products')
def get_all_products(db : Session = Depends(get_db)):
    db_query = db.query(database_model.Product).all()
    return db_query

@app.get('/products/{id}')
def get_products_by_id(id : int, db : Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return "No product found with id {}".format(id)

@app.post('/products')
def add_product(product : Product, db : Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return product

@app.put('/products/{id}')
def update_products_by_id(id : int, product : Product, db : Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db_product.description = product.description
        db_product.quantity = product.quantity
        db.commit()
        return "product updated"
    return "No item found with id {}".format(id)

@app.delete('/products/{id}')
def delete_product_by_id(id : int, db : Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Deleted successfully"
    return "No item found with id {}".format(id)