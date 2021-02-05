from flask_restful import marshal_with, fields
from back.resources.base_resource import BaseResource
from back.dao.product_dao import ProductDao
from back.models.product_model import Product


class ProductResource(BaseResource):
    field_base = {
        "id_": fields.Integer,
        "name": fields.String,
        "description": fields.String,
        "price": fields.Float,
        "amount": fields.Integer
    }

    def __init__(self) -> None:
        self.__dao = ProductDao()
        self.__model_type = Product
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(field_base)
    def get(self, id_: int = None):
        return super().get(id_)

    @marshal_with(field_base)
    def post(self):
        return super().post()

    @marshal_with(field_base)
    def put(self, id_: int):
        return super().put(id_)