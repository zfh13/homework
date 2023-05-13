# homework
本项目实现了注册登录功能（不过没实现表单验证），当然也没有实现过期功能

首先你需要git clone 
然后调用数据库迁移命令
#### 1. 生成迁移文件

`python manage.py makemigrations`

#### 2. 同步到数据库中

`python manage.py migrate`
然后启动访问就行了。
