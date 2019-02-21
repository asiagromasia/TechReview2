from django.test import TestCase
from .models import Product, ProductType
from django.urls import reverse

# Create your tests here.
#  # model tests

class ProductTest(TestCase):
    def test_stringOutput(self):
        product=Product(productname='Lenovo laptop')
        self.assertEqual(str(product), product.productname)

    def test_tablename(self):
        self.assertEqual(str(Product._meta.db_table), 'product')    

#testing a view 
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))   
        self.assertEqual(response.status_code, 200)     

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'techapp/index.html')    

# from .models import TechProduct, TechType, TechReview
# from .forms import TechProductForm, TechReviewForm
# from datetime import datetime
# from django.urls import reverse

# # Create your tests here.
# # model tests

# class TechProductTest(TestCase):
#     def test_stringOutput(self):
#         techproduct=TechProduct(productname='Lenovo Laptop')
#         self.assertEqual(str(techproduct), techproduct.productname)

#     def test_tablename(self):
#         self.assertEqual(str(TechProduct._meta.db_table), 'techproduct')

# class TechTypeTest(TestCase):
#     def test_stringOutput(self):
#         techtype=TechType(typename='Laptop')
#         self.assertEqual(str(techtype), techtype.typename)

#     def test_tablename(self):
#         self.assertEqual(str(TechType._meta.db_table), 'techtype')

# class TechReviewTest(TestCase):
#     def test_stringOutput(self):
#         techreview=TechReview(reviewtitle='Lenovo Laptop')
#         self.assertEqual(str(techreview), techreview.reviewtitle)

#     def test_tablename(self):
#         self.assertEqual(str(TechReview._meta.db_table), 'techreview')


# class TestIndex(TestCase):
    
#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
        
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'reviews/index.html')

# class TestGetProduct(TestCase):


#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('/reviews/products')
#         self.assertEqual(response.status_code, 200)

#     def test_view_url_accessible_by_name(self):
#         response = self.client.get(reverse('getProducts'))
#         self.assertEqual(response.status_code, 200)
        
#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('getProducts'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'reviews/products.html')
