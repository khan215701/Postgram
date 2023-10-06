from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
import uuid
import datetime

class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            print("checking instance")
            instance = self.get(public_id=public_id)
            print(instance)
            return instance
        except (ObjectDoesNotExist, TypeError, ValueError):
            return Http404
        


class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = AbstractManager()
    
    class Meta:
        abstract = True
    