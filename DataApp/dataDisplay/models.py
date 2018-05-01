from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Creates the imports object and tries to self reference itself with json
class Sale(models.Model):
    ID = models.CharField(max_length=30)
    import_country = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    sold_by = models.CharField(max_length=50)
    sale_price = models.CharField(max_length=10)

    def to_json(self):
        return {
            'ID': self.ID,
            'import_country': self.import_country,
            'model': self.model,
            'make': self.make,
            'sold_by': self.sold_by,
            'sale_price': self.sale_price,
        }

    def __str__(self):
        return self.ID