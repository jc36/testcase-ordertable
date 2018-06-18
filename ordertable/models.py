from django.db import models


class Table(models.Model):
    number = models.IntegerField(primary_key=True)
    count_place = models.IntegerField()
    shape = models.CharField(default='rectangular', max_length=30)
    coord_h = models.IntegerField()
    coord_v = models.IntegerField()
    size_h = models.IntegerField()
    size_v = models.IntegerField()

    def __str__(self):
        return str(self.number) + '(' + str(self.count_place) + ')'


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    table = models.ManyToManyField(Table)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)
    description = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.date) + ': reserve by ' + self.name + ' tables: ' + str(self.table.all()) + str(self.active)
