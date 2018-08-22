# myIndex
一个由django框架的个人网站主页

主页分为5个结构：主页，博客，个人作品，关于我的，联系。

代码结构清晰。

后台为/admin,上传作品，查看留言、评论，以及写博客都在后台写。

博客以及关于我的页面 主体文字 后台编写均为tinymce 富文本。

下载代码后请修改数据库文件 /myblog/setting.py，并且本地mysql数据库创建同'NAME'数据库

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',  
        'NAME':'myblog',
        'USER':'root',  
        'PASSWORD':'密码',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

进入代码根目录

python manage.py createsuperuser 创建管理员用户

python manage.py migrate 自动创建数据库表

python manage.py runserver 开启服务

请先后台编写数据 查看效果

#django版本为2.0，Python版本为3.6

个人网站：www.siyang.site
