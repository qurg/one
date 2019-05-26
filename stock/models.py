from django.conf import settings
from django.db import models


# Create your models here.

class Index(models.Model):
    name = models.CharField('名称', max_length=255)
    code = models.CharField('代码', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '指数'
        verbose_name_plural = '指数'


class IndexList(models.Model):
    ACT_ITEMS = {
        (1, '买入'),
        (2, '卖出'),
        (3, '保持'),
    }

    index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='指数')
    value = models.FloatField('数值')
    pe = models.FloatField('市盈率')
    target = models.FloatField('PE标杆', blank=True,null=True)
    act = models.IntegerField(choices=ACT_ITEMS, verbose_name='行动', blank=True,null=True)
    summary = models.CharField('小结', max_length=1000, blank=True,null=True)
    create_date = models.DateField('日期')
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, verbose_name='创建人', default=settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = '指数记录'
        verbose_name_plural = '指数记录'
