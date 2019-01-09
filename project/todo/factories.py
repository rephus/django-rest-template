import uuid 
import factory
from faker import Factory as FakerFactory
from todo import models


fake = FakerFactory.create('en_GB')
fake.seed(13337)

"""
By using DjangoModelFactory, the object is inserted in DB 
when TaskFactory() is mentioned, otherwise you can use factory.Factory
"""
class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Task

    #id = factory.LazyAttribute(lambda a: uuid.uuid4() )
    title = factory.LazyAttribute(lambda a: fake.name())
    description = factory.LazyAttribute(lambda a: fake.text())
    completed = factory.LazyAttribute(lambda a: fake.boolean())
    due = factory.LazyAttribute(lambda a: fake.date_time(tzinfo=None, end_datetime=None))

