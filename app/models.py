from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
('Béni Mellal-Khénifra', 'Béni Mellal-Khénifra'),
('Casablanca-Settat', 'Casablanca-Settat'),
('Dakhla-Oued Ed-Dahab', 'Dakhla-Oued Ed-Dahab'),
('Drâa-Tafilalet', 'Drâa-Tafilalet'),
('Fès-Meknès', 'Fès-Meknès'),
('Guelmim-Oued Noun', 'Guelmim-Oued Noun'),
('Laâyoune-Sakia alHamra', 'Laâyoune-Sakia alHamra'),
('orientale', 'orientale'),
('Marrakech-Safi', 'Marrakech-Safi'),
('Rabat-Salé-Kénitra', 'Rabat-Salé-Kénitra'),
('Souss-Massa', 'Souss-Massa'),
('Tanger-Tétouan-Al Hoceima', 'Tanger-Tétouan-Al Hoceima'),
)

CATEGORY_CHOICES=( 
    ('AD','art'), 
    ('LP','santé'),
    ('GM','informatique'), 
    ('TP','economie'), 
    ('TV','entreprise'), 
    ('TB','enfants'), 
    ('SH','Science'), 
)




class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    caractéristiques = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    quantity_stock = models.IntegerField(default=10)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
       return self.quantity * self.product.discounted_price 





    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)




    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_cost = models.FloatField(default=40)
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    nbrJour = models.PositiveIntegerField(default=1)

    
class Dossier(models.Model):
    nom = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)  # يتم تحديد التاريخ عند الإنشاء
    date_modification = models.DateTimeField(auto_now=True)  # يتم تحديث التاريخ تلقائيًا عند التعديل

    def __str__(self):
        return self.nom

