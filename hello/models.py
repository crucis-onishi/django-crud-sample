from django.db import models

# Article クラスを定義
class Article(models.Model):
    # content カラムを定義
    content = models.CharField(max_length=140)

    def __str__(self):
        return self.content
