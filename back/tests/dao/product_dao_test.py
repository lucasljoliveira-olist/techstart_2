import sys
sys.path.append('.')
from back.dao.product_dao import ProductDao
from back.dao.base_dao import BaseDao
from back.models.product_model import Product
import pytest


class TestProductDao:
    __dao = ProductDao()

    @pytest.fixture
    def create_instance(self):
        product = Product('Nome', 'Descricao', 1.99, 5)
        return product

    def test_product_dao_instance(self):
        assert isinstance(self.__dao, ProductDao)
        assert isinstance(self.__dao, BaseDao)

    def test_product_dao_save(self, create_instance):
        product = self.__dao.save(create_instance)
        assert product.id_ is not None
        self.__dao.delete(product)

    def test_product_dao_not_save(self):
        with pytest.raises(TypeError):
            product = self.__dao.save('product')

    def test_product_dao_read_by_id(self, create_instance):
        product = self.__dao.save(create_instance)
        product_readed = self.__dao.read_by_id(product.id_)
        assert isinstance(product_readed, Product)
        assert product_readed is not None
        self.__dao.delete(product_readed)

    def test_product_dao_not_read_by_id(self):
        with pytest.raises(TypeError):
            product = self.__dao.read_by_id('product')

    def test_product_dao_read_all(self):
        products = self.__dao.read_all()
        assert isinstance(products, list)
        assert all(isinstance(item, Product) for item in products)

    def test_product_dao_delete(self, create_instance):
        product = self.__dao.save(create_instance)
        product_readed = self.__dao.read_by_id(product.id_)
        self.__dao.delete(product_readed)
        product_readed = self.__dao.read_by_id(product.id_)
        assert product_readed is None

    def test_product_dao_not_delete(self):
        with pytest.raises(TypeError):
            self.__dao.delete('product')
