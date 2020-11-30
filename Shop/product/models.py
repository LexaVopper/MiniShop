from django.db import models


class Product (models.Model):
    name = models.CharField(max_length=30, blank=True)
    price = models.FloatField(max_length=30, blank=True)
    status = models.CharField(max_length=30, blank=True)
    sale = models.FloatField(blank=True, default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.price = int(self.price * (100 - self.sale) / 100)
        super(Product, self).save(*args, **kwargs)

    def first_price(self):
        first_price = self.price
        first_price += int(self.price * self.sale / (100 - self.sale))
        return first_price

    def __str__(self):
        return "%s, %s" % (self.name, self.price)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media/products_images/')
    is_main = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
