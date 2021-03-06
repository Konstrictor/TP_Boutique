from django.db import models
from django.utils import timezone

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)
	qtt = models.IntegerField(default=0)
	unite = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.name}({self.qtt})"

class Music(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)
	descr = models.CharField(max_length=32)
	file = models.FileField(upload_to="music")

	def __str__(self):
		return f"{self.name}"

class Prix(models.Model):
	id = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
	prix_achat = models.IntegerField()
	prix_vente = models.IntegerField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f"{self.product}(achat:{self.prix_achat} vente:{self.prix_vente})"

class Vente(models.Model):
	id = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
	qtt = models.IntegerField(default=0)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.product.name}({self.qtt})"

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		produit = self.product
		produit.qtt -= self.qtt
		produit.save()

class Achat(models.Model):
	id = models.AutoField(primary_key=True)
	product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
	qtt = models.IntegerField(default=0)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.product.name}({self.qtt})"

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		produit = self.product
		produit.qtt += self.qtt
		produit.save()



