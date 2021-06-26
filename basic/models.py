from django.db import models


class User(models.Model):
    """ユーザー"""
    id = models.UUIDField('ユーザーID', primary_key=True)
    name = models.CharField("ユーザー名", max_length=32)

    def __str__(self) -> str:
        return self.name
