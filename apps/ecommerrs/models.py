from django.contrib.postgres.fields import ArrayField
from django.core.files import images
from django.db.models import CharField, ImageField, SlugField, IntegerField, DecimalField, IntegerChoices, ForeignKey, \
    SET_NULL, ManyToManyField, CASCADE, Model
from django.utils.text import slugify

from apps.sharing.models import BaseModel


class Category(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(CharField(max_length=255), unique=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1

        while Category.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('-created_at',)
        db_table = 'Categorys'


class Product(BaseModel):
    class Rating(IntegerChoices):
        WORSE = 1
        BAD = 2
        AVERAGE = 3
        GOT = 4
        EXCELLENT = 5

    title = CharField(max_length=255)
    teg = ArrayField(CharField(max_length=255), )
    price = DecimalField(max_digits=9, decimal_places=1)
    discount = ImageField()
    rating = IntegerField(choices=Rating.choices, default=Rating.AVERAGE)
    created_by = ForeignKey('auth.User', SET_NULL, 'created', null=True, blank=True)
    updated_at = ForeignKey('auth.User', SET_NULL, 'updated', null=True, blank=True)
    wishlist = ManyToManyField('auth.User', 'wishlist')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-created_at',)
        db_table = 'products'


class ProductImages(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ImageField(upload_to='images/', verbose_name='Image')
