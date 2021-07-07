from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import reverse
from django.utils.text import slugify


class User(AbstractUser):
    slug = models.SlugField(max_length=150, verbose_name="Slug")
    age = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)], blank=True, null=True,
        verbose_name='Age'
    )
    image = models.ImageField(
        upload_to='images/users/',
        null=True,
        blank=True,
        verbose_name='User image'
    )
    gender = models.CharField(max_length=6, choices=(
        ('male', 'male'), ('female', 'female')))
    country = CountryField()
    raiting = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Raiting',
        default=0
    )

    class Meta(AbstractUser.Meta):
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.pk:
            self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='Title')
    slug = models.SlugField(
        max_length=25, verbose_name='Slug', default='No category')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("by_category", kwargs={"slug": self.slug})


class Test(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    slug = models.SlugField(max_length=50, verbose_name='Slug')
    category = models.ForeignKey(
        Category,
        verbose_name='Category',
        on_delete=models.SET_NULL,
        related_name='tests',
        null=True
    )
    description = models.TextField(
        max_length=250,
        verbose_name='Description',
        validators=[MinLengthValidator(100)]
    )
    author = models.ForeignKey(
        User,
        verbose_name='Author',
        on_delete=models.SET_NULL,
        related_name='tests',
        null=True
    )
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Difficulty'
    )
    raiting = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Raiting'
    )
    image = models.ImageField(
        upload_to='images/tests/%Y/%m/%d/', verbose_name='Test image')
    likes = models.PositiveIntegerField(verbose_name='Likes')
    dislikes = models.PositiveIntegerField(verbose_name='Dislikes')

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'tests'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('test_detail', kwargs={'slug': self.slug})


class Question(models.Model):
    title = models.CharField(max_length=25, verbose_name='Question')
    image = models.ImageField(
        upload_to='images/questions/%Y/%m/%d/', verbose_name='Question image')
    test = models.ForeignKey(
        Test,
        verbose_name='Test',
        on_delete=models.CASCADE,
        related_name='questions'
    )
    true_answer = models.CharField(max_length=20, verbose_name='True answer')
    false_answers = ArrayField(
        models.CharField(max_length=20, blank=True),
        size=6,
        verbose_name='False Answers'
    )
    clarification_to_answer = models.CharField(
        max_length=100,
        verbose_name='Clarification to answer'
    )

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.title
