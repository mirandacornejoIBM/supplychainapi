Python 3.13.5 (v3.13.5:6cb20a219a8, Jun 11 2025, 12:23:45) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from fastapi import FastAPI
>>> from pydantic import BaseModel
>>> import pandas as pd
>>> 
>>> app = FastAPI(title="Supply Chain & Sales", version="1.0.0")
>>> df = pd.read_csv("/Users/mirandacornejoahuja/Desktop/supplychaincoe.csv")
>>> class Product(BaseModel):
...      product_card_id: int
...      product_name:str
...      product_price:float
... 
...      
>>> class Product(BaseModel):
...      product_card_id: int
...      product_name:str
...      product_price:float
...      product_category_id: int
... 
...      
>>> class Customer(BaseModel):
...      customer_id:float
...      customer_city:str
...      customer_country:str
...      customer_segment:str | None=None
...      customer_state:str | None=None
...      customer_zipcode: str | None=None
... 
...      
>>> class Order(BaseModel):
...     order_id: str
...     order_customer_id: float
...     order_date: str
...     order_item_id: float
...     order_item_product_price: float
...     order_item_quantity: int
...     order_status: str
... 
    
class Shipment(BaseModel):
    shipping_date: str
    shipping_mode: str
    order_date_IsHoliday: bool
    shipping_date_IsHoliday: bool

    
@app.get("/products", response_model=list[Product])
def get_products():
    return df[["product_card_id", "product_category_id", "product_name", "product_price"]] \
        .dropna().drop_duplicates().to_dict(orient="records")

@app.get("/products/{product_card_id}", response_model=Product)
def get_product(product_card_id: int):
    record = df[df["product_card_id"] == product_card_id]
    if record.empty:
        return {"error": "Product not found"}
    return record.iloc[0][["product_card_id","product_category_id","product_name","product_price"]].to_dict()

@app.get("/customers", response_model=list[Customer])
def get_customers():
    return df[["customer_id","customer_city","customer_country","customer_segment","customer_state","customer_zipcode"]] \
        .dropna().drop_duplicates().to_dict(orient="records")

@app.get("/customers/{customer_id}", response_model=Customer)
def get_customer(customer_id: float):
    record = df[df["customer_id"] == customer_id]
    if record.empty:
        return {"error": "Customer not found"}
    return record.iloc[0][["customer_id","customer_city","customer_country","customer_segment","customer_state","customer_zipcode"]].to_dict()

@app.get("/orders", response_model=list[Order])
def get_orders():
    return df[["order_id","order_customer_id","order_date","order_item_id","order_item_product_price","order_item_quantity","order_status"]] \
        .dropna().drop_duplicates().to_dict(orient="records")

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str):
    record = df[df["order_id"] == order_id]
    if record.empty:
        return {"error": "Order not found"}
    return record.iloc[0][["order_id","order_customer_id","order_date","order_item_id","order_item_product_price","order_item_quantity","order_status"]].to_dict()

@app.get("/shipments", response_model=list[Shipment])
def get_shipments():
    return df[["shipping_date","shipping_mode","order_date_IsHoliday","shipping_date_IsHoliday"]] \
        .dropna().drop_duplicates().to_dict(orient="records")

