# 4、项目基本设置

除了数据库配置外，我们还需要进行一些其他配置。

## 4.1 应用设置

我们根据项目模块，创建了四个应用并全部置于apps包下：cart购物车、goods商品、order订单、user用户。

它们均需在settings里进行注册：

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 下面是一些自定义添加的第三方应用和项目应用
    'tinymce',  # django-tinymce 富文本编辑器
    'haystack',  # 全文检索的框架
    # 'djcelery', # 将耗时的程序放到celery中执行
    # 'celery_tasks',

    # 项目应用
    'apps.cart',  # 购物车  cart
    'apps.goods',  # 商品
    'apps.order',  # 订单
    'apps.user',  # 用户
)
```

## 4.2 模板路径配置

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 配置模板文件路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## 4.3 静态文件配置

```python
# 配置静态文件目录
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

## 4.4 URLconf根文件配置

```python
ROOT_URLCONF = 'dailyfresh.urls'
```

## 4.5 后台管理本地化语言配置

```python
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'
```

其他settings文件配置会在开发模块功能中遇到时再添加配置。

## 4.6 dailyfresh.urls配置

我们设计各模块对应的URL路径如下：

```python
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search', include('haystack.urls')), # 全文检索框架
    url(r'^tinymce/', include('tinymce.urls')),  # 富文本编辑器url
    
    url(r'^user/', include('apps.user.urls', namespace='user')), # 用户模块 user.urls
    url(r'^cart/', include('apps.cart.urls', namespace='cart')), # 购物车模块
    url(r'^order/', include('apps.order.urls', namespace='order')), # 订单模块
    url(r'^', include('apps.goods.urls', namespace='goods')), # 商品模块
]
```

可以看到，我们将网页首页默认放在了goods模块路径下，其他模块URL路径均与其模块名相同。这样分解URL配置，有利于各模块的URL管理。但需注意，URL层级不能过长，一般最多控制在3级左右。