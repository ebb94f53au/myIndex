from django.db import models

# Create your models here.
class Wheel(models.Model):
    #主页滚动图
    text=models.CharField(max_length=255,verbose_name='主页滚动句★')
    #将上传的图片定为'static/media/images/wheel'下
    img=models.ImageField(upload_to='images/wheel',verbose_name='主页背景图★')
    isDelete=models.BooleanField(default=False,verbose_name='是否逻辑删除')
    class Meta:
        verbose_name='主页滚动图'
        verbose_name_plural='主页滚动图'
class ViewsNum(models.Model):
    #浏览量
    todayNum=models.IntegerField(verbose_name='当日点击量')
    date = models.DateField(verbose_name='时间')
    sumNum=models.IntegerField(verbose_name='总点击量')
    isDelete = models.BooleanField(default=False, verbose_name='是否逻辑删除')

    class Meta:
        verbose_name='浏览量'
        verbose_name_plural='浏览量'
        ordering = ['-sumNum']
    def addToday(self):
        self.todayNum+=1
        self.save(update_fields=['todayNum'])
    def addSum(self):
        self.sumNum += 1
        self.save(update_fields=['sumNum'])
    @classmethod
    def create(cls,date,sumNum):
        num=cls(todayNum=0,date=date,sumNum=sumNum)
        num.save()