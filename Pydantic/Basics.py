
# Pydantic is a Python library used for data validation and data parsing using Python type hints.
# It allows you to define the structure and expected types of data, and Pydantic automatically checks whether the provided data follows those rules.


# from pydantic import BaseModel

# # class User(BaseModel):
# #     id: int
# #     name : str
# #     is_active : bool

# # input_data = {'id': 101, 'name':"Chaicode", 'is_active':"true"}

# # user = User(**input_data) # the star-star annotation here unpacks the whole input_data dictionary that we are passing 
# # print(user)

# # Another example _________________________________________________________________________________________________________________


# # from pydantic import BaseModel

# class Products(BaseModel):
#     id:int
#     name:str
#     type:str
#     price:float
#     in_stock:bool = True # in this case we are giving a default true value here if we doesn't get any values from the user or we are not passing any values



# product_one = Products(id=1, name="milk", type= "liquid", price=45, in_stock=True )


# product_two = Products(id=2, name="Grain", type= "solid", price=35, in_stock=False )



# # Another example _______________________________________________________________________________


# # Typing and Pydantic 


# from pydantic import BaseModel
# from typing import List , Dict , Optional

# class Cart(BaseModel):
#     user_id: int
#     items: List[str] # here we used list because items me hum ni use kr skte just a string and a object 
#     quantities : Dict[str, int] # key is str and value is int 


# class BlogPost(BaseModel):
#     title: str
#     content: str 
#     image_url : Optional[str] = None # here the none would be the default value 


# cart_data = {
#     "user_id": 123,
#     "items": ["item1", "item2", "item3"],
#     "quantities": {"item1": 2, "item2": 1, "item3": 5}
# }


# cart = Cart(**cart_data) # here the star-star annotation is used to unpack the cart_data dictionary and pass its contents as keyword arguments to the Cart model. This allows Pydantic to validate and create an instance of the Cart model based on the provided data.
# print(cart)






# Fields


# from typing import Optional
# from pydantic import BaseModel, Field

# class Employee(BaseModel):
#     id: int = Field(..., description="The unique identifier for the employee") #here the triple dots are used to indicate that the field is required and must be provided when creating an instance of the Employee model.
#     name: str = Field(..., min_length=1, max_length=50, description="The name of the employee")
#     age: Optional[int] = Field(None, ge=18, le=65, description="The age of the employee (must be between 18 and 65)")
#     department: str = Field(..., description="The department the employee belongs to")
#     salary: float = Field(..., description="The salary is required here", ge=100000)



# Field and modal validators ______________________________________________________________________________________________________________________________________________________________________________________


# COMPUTED FIELD 

from pydantic import BaseModel, computed_field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field #computed_field → tells Pydantic that a value is calculated from other fields and should be included when the model is serialized.
    @property #this property decorator allows us to use the values 
    def total_price(self) -> float:
        return self.price * self.quantity



product = Product(price=45, quantity=3)
print(product.total_price)