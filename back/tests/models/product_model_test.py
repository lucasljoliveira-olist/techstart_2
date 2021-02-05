import sys
sys.path.append('.')
from back.models.base_model import BaseModel
from back.models.product_model import Product
import pytest

class TestProductModel:
    def test_product_instance(self):
        product = Product('Prod', 'Desc', 10.50, 5)
        assert isinstance(product, Product)
        assert isinstance(product, BaseModel)

    @pytest.mark.parametrize('name', ['Teste', 'T'*100, 'T'])
    def test_product_name_type(self, name):
        product = Product(name, 'Desc', 10.50, 5)
        assert isinstance(product.name, str)

    @pytest.mark.parametrize('description', ['Teste', 'T'*255, 'T', ''])
    def test_product_description_type(self, description):
        product = Product('Name', description, 10.50, 5)
        assert isinstance(product.description, str)

    @pytest.mark.parametrize('price', [1.0, 100.0, 10.5])
    def test_product_price_type(self, price):
        product = Product('Name', 'Desc', price, 5)
        assert isinstance(product.price, float)

    @pytest.mark.parametrize('amount', [0, 100, 10])
    def test_product_amount_type(self, amount):
        product = Product('Name', 'Desc', 10.50, amount)
        assert isinstance(product.amount, int)

    @pytest.mark.parametrize('name', [1, True, 10.5])
    def test_product_name_type_error(self, name):
        with pytest.raises(TypeError):
            product = Product(name, 'Desc', 10.50, 5)

    @pytest.mark.parametrize('description', [1, True, 10.5])
    def test_product_description_type_error(self, description):
        with pytest.raises(TypeError):
            product = Product('Name', description, 10.50, 5)

    @pytest.mark.parametrize('price', ['', 10])
    def test_product_price_type_error(self, price):
        with pytest.raises(TypeError):
            product = Product('Name', 'Desc', price, 5)

    @pytest.mark.parametrize('amount', ['', [], 10.5])
    def test_product_amount_type_error(self, amount):
        with pytest.raises(TypeError):
            product = Product('Name', 'Desc', 10.5, amount)

    def test_product_name_len_error(self):
        with pytest.raises(ValueError):
            product = Product('T'*101, '', 10.5, 10)

    def test_product_name_empty_error(self):
        with pytest.raises(ValueError):
            product = Product('', '', 10.5, 10)

    def test_product_description_len_error(self):
        with pytest.raises(ValueError):
            product = Product('Name', 'T'*256, 10.5, 10)

    @pytest.mark.parametrize('price', [0.0, -1.0, -100.0])
    def test_product_price_greatter_than_error(self, price):
        with pytest.raises(ValueError):
            product = Product('Name', 'Desc', price, 10)

    @pytest.mark.parametrize('amount', [-1, -10, -100])
    def test_product_price_greatter_than_error(self, amount):
        with pytest.raises(ValueError):
            product = Product('Name', 'Desc', 10.0, amount)