# homework
本项目来自于南京信息工程大学大三下学期的实践课《信息系统设计与实现》，实现了注册登录功能（不过没实现表单验证），当然也没有实现过期功能（太菜了。。。）
下面是如何启动这个项目：

首先你需要git clone https://github.com/zfh13/homework
然后调用数据库迁移命令
#### 1. 生成迁移文件

`python manage.py makemigrations`

#### 2. 同步到数据库中

`python manage.py migrate`
然后启动访问就行了。
对了，致我可爱(baipiao)的队友们，记得给我右上角star点赞
