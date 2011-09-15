from django.db import models

from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200)
    hourly_rate = models.DecimalField(decimal_places=2, max_digits=6)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'sub categories'

    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.TextField()
    hours = models.IntegerField()
    category = models.ForeignKey(Category, related_name="tasks")
    sub_category = models.ForeignKey(SubCategory, blank=True, null=True,
                                     related_name="sub_tasks")

    class Meta:
        ordering = ('category', 'sub_category', 'hours')

    def __unicode__(self):
        return '{0} ({1} hours)'.format(self.name, self.hours)


class Quote(models.Model):
    creation_date = models.DateField(default=datetime.now)
    tasks = models.ManyToManyField(Task)
    locked_price = models.DecimalField(decimal_places=2, max_digits=12,
                                       blank=True, null=True)

    class Meta:
        ordering = ('creation_date',)

    def __unicode__(self):
        return str(self.creation_date)

    def current_estimate(self):
        if self.locked_price:
            return self.locked_price
        else:
            return self.new_estimate()

    def new_estimate(self):
        values = self.tasks.values_list('hours', 'category__hourly_rate')
        return sum([h * r for h, r in values])

    def lock_price(self):
        self.locked_price = self.new_estimate()
