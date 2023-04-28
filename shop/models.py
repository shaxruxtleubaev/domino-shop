from django.db.models import *
from django.urls import reverse
from ckeditor.fields import *


#main model - product
class Product(Model):
	product_name = CharField('Наименование*', max_length=512)
	description = RichTextField('Описание*')

	main_img = ImageField('Главное фото*', upload_to='product-images/')
	image1 = ImageField('Фотография 1', upload_to='product-images/', blank=True, null=True)
	image2 = ImageField('Фотография 2', upload_to='product-images/', blank=True, null=True)
	image3 = ImageField('Фотография 3', upload_to='product-images/', blank=True, null=True)

	price = FloatField('Ценник(сум)', default=0)

	trend = BooleanField('Тренд*', default=True)
	stock = BooleanField('Наличие*', default=True)

	made = ForeignKey('Country', verbose_name='Изготовление*', on_delete=CASCADE)

	category = ForeignKey('Category', on_delete=CASCADE, verbose_name='Категория*')
	size = ManyToManyField('Size', verbose_name='Размер*')
	color = ManyToManyField('Color', verbose_name='Цвет*')

	brand = ForeignKey('Brand', on_delete=CASCADE, verbose_name='Бренд*')

	date = DateTimeField('Дата и время', auto_now_add=True)

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


'''--------------------------------------------------'''


#model of category
class Category(Model):
	category_name = CharField('Название', max_length=512)
	category_img = ImageField('Картинка', upload_to='category-img/')
	category_desc = RichTextField('Описание*')

	slug = SlugField('URL категории', null=False)

	def __str__(self) -> str:
		return self.category_name
	
	class Meta:
	     verbose_name = 'Категория'
	     verbose_name_plural = 'Категории'

	def get_absolute_url(self):
		return reverse(
	    	'categories',
	    	kwargs={
	    		'category_slug': self.slug,
	     	}
		)


#model of color
class Color(Model):
	color_name = CharField('Цвет', max_length=512)

	def __str__(self) -> str:
		return self.color_name
	
	class Meta:
		verbose_name = 'Цвет'
		verbose_name_plural = 'Цвета'


#model of size
class Size(Model):
	size_name = CharField('Размер', max_length=512)

	def __str__(self) -> str:
		return self.size_name
	
	class Meta:
		verbose_name = 'Размер'
		verbose_name_plural = 'Размеры'


#model of country
class Country(Model):
	country_name = CharField('Государство', max_length=512)

	def __str__(self) -> str:
		return self.country_name
	
	class Meta:
		verbose_name = 'Страна производства'
		verbose_name_plural = 'Странаы производства'


#model of brand
class Brand(Model):
	brand_name = CharField('Бренд', max_length=512)

	def __str__(self) -> str:
		return self.brand_name
	
	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'