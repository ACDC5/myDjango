**python 3.5.1**
**django 2.2.6**
**virtualenv 16.4.3**
**postgresql**

#models
- 1、python manage.py makemigrations命令:使models中的类和变量转换成数据库执行的脚本
- 2、python manage.py migrate命令：在数据库中根据models的内容生成表和字典


#App
- 在Django中的app我认为就是一个功能模块,将不能功能放在不同的app中, 方便代码的复用

- python manage.py runserver   #启动Django中的开发服务器


这里进入Django的shell和python内置的shell是非常类似的

>>> from article.models import Article
	from 应用名.models import 类名
>>> #create数据库增加操作
>>> Article.objects.create(title = 'Hello World', category = 'Python', content = '我们来做一个简单的数据库增加操作')
<Article: Article object>
>>> Article.objects.create(title = 'Django Blog学习', category = 'Python', content = 'Django简单博客教程')
<Article: Article object>

>>> #all和get的数据库查看操作
>>> Article.objects.all()  #查看全部对象, 返回一个列表, 无对象返回空list
[<Article: Article object>, <Article: Article object>]
>>> Article.objects.get(id = 1)  #返回符合条件的对象
<Article: Article object>

>>> #update数据库修改操作
>>> first = Article.objects.get(id = 1)  #获取id = 1的对象
>>> first.title
'Hello World'
>>> first.date_time
datetime.datetime(2014, 12, 26, 13, 56, 48, 727425, tzinfo=<UTC>)
>>> first.content
'我们来做一个简单的数据库增加操作'
>>> first.category
'Python'
>>> first.content = 'Hello World, How are you'
>>> first.content  #再次查看是否修改成功, 修改操作就是点语法
'Hello World, How are you'

>>> #delete数据库删除操作
>>> first.delete()
>>> Article.objects.all()  #此时可以看到只有一个对象了, 另一个对象已经被成功删除
[<Article: Article object>]  

Blog.objects.all()  # 选择全部对象
Blog.objects.filter(caption='blogname')  # 使用 filter() 按博客题目过滤
Blog.objects.filter(caption='blogname', id="1") # 也可以多个条件
#上面是精确匹配 也可以包含性查询
Blog.objects.filter(caption__contains='blogname')

Blog.objects.get(caption='blogname') # 获取单个对象 如果查询没有返回结果也会抛出异常

#数据排序
Blog.objects.order_by("caption")
Blog.objects.order_by("-caption")  # 倒序

#如果需要以多个字段为标准进行排序（第二个字段会在第一个字段的值相同的情况下被使用到），使用多个参数就可以了
Blog.objects.order_by("caption", "id")

#连锁查询
Blog.objects.filter(caption__contains='blogname').order_by("-id")

#限制返回的数据
Blog.objects.filter(caption__contains='blogname')[0]
Blog.objects.filter(caption__contains='blogname')[0:3]  # 可以进行类似于列表的操作

#创建超级用户
python manage.py createsuperuser

#使用第三方插件
示例使用bootstrap
安装 pip install bootstrap-admin
部署插件:
	INSTALLED_APPS = (
    'bootstrap_admin',  #一定要放在`django.contrib.admin`前面
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
	)

