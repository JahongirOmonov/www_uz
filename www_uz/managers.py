from django.db import models



class WebsiteManager(models.Manager):

    def tasix(self):
        queryset = self.get_queryset()
        return queryset.filter(is_tasix = True)
