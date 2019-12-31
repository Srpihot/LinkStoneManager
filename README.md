# 墨石协会用户管理系统

#### V0.1 datetime:2019.12.31

编译环境 : Python3.7.0  Windows10 sqlserver2017

第三方库:

1. wxpython 4.0.7.post2

2. mssql  2.1.4



#### 数据库关系模式：

Student(学号，姓名，代号，性别，年龄,出生日期，籍贯，年级，专业编号)
ConnectStu（学号，电话，qq号，电子邮箱）
College（学院id，学院名）
Mojar（专业id，专业名）
Mojar2College（专业id，学院id）
Management（学号，部门id，职位名）
Departmentlist（部门id，部门名）
Permissionby（学号，密码）
PermissionList（学号，权限）
Course（科目编号，科目名，最高成绩，科目描述）
StuGrade（id,学号，科目编号，获得成绩）
LinkStoneStu（学号，ctf平台昵称，个人介绍，题解数量，正确答题数量，答题错误数量，正在作答题目，积分，金币，排名）
Financial（id,状态，金钱额，备注）
ActivityList(id，活动名称，活动负责人，开始时间，结束时间，计划书url，总花费，活动总结url)



#### 权限：

Permissionby表存账号信息  PermissionList存权限

权限1，2代表管理员权限 权限3代表普通成员权限 权限4代表未注册协会成员

管理员权限具有增删改查协会成员信息，协会活动，财务管理，课程信息等

普通成员具有查看个人信息与课程信息等

非注册协会成员注册后成为普通成员





#### V0.1版本开发GUI管理界面

后期将开发为python后端 对接墨石CTF平台。

Ps:窗口跳转使用os.systemz所以python3环境需要添加环境变量 python.exe
测试可直接打开LinkStone.exe即可。
sqlserver.sql为建库代码。