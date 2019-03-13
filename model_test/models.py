from django.db import models

# Create your models here.
class Repoter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Repoter, on_delete=models.CASCADE)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('-headline',)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return '이름은 {} 입니다.'.format(self.name)

class Restaurant(models.Model):
    place = models.OneToOneField(Place,
        on_delete = models.CASCADE, primary_key=True)

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return '식당의 이름은 {}'.format(self.place.name)

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}, 근무자 : {}".format(self.restaurant, self.name)


