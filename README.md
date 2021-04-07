20210314:
1、创建项目工程、创建了README.md

2、接口测试流程
2.1 获取接口文档（1、开发 word/wiki文档库 2、charles抓包）
2.2 分析和理解接口文档上的接口业务功能
2.3 设计接口测试用例 == 评审
2.4 把设计的用例录入到接口测试框架执行 （postman/jmeter/线性代码框架）
2.5 定时自动化执行
2.6 生成测试报告通过邮件发送等...

3、构建接口测试框架
3.1 创建子包  common  testcases（存放用例） html_reports(html测试报告) ...
3.2 在testcases继续根据项目的不同模块建立子包，以接口为单位创建测试用例文件
3.3 编写接口的用例并保证单独执行成功（测试）
3.4 通过 HTMLTestReportCN.py 第三方模块构建测试报告
3.5 优化测试报告内部 测试用例名称 显示
3.6 在不同的模块下编写用例
3.7 增加配置文件 把主机地址作为全局配置（两种做法）
    3.7.1 py是脚本文件，可直接执行，固配置直接放在代码中 ==>common/config_utils.py
    3.7.2 配置放置在单独的ini配置文件中 == conf/config.ini
    备注：利用python包先做实例操作 --> 封装
3.8 所有的接口进行公共化  --> public_api_infos.py 
    函数实现 目的在于把请求方式、请求地址、请求参数的处理放在一起
    
20210317:
3.9 日志模块的使用 ： 自带的原始日志模块  、nb_log
    日志模块作用 1）方便调试框架日常过程中的错误 2）记录测试执行过程
    正常的操作流程一般使用debug或者info级别的日志
    需要进行异常处理的代码，一般使用error级别的日志

20210321:
3.10 由作业出发：接口业务用例录入到框架的流程
     1）对应的testscases子包创建接口测试模块如 tests_delete_user_tag_api.py
     2）编写好一个用例就用 if __name__=="__main__": 进行测试
     3) 尝试整体运行出结果（不做也可以）
     4）由于很多的接口测试方法都需要用户登录状态，故进行封装
        public_api_infos ==> get_access_token()
     5）发现用户登录的账号信息放在代码中不方便，调整为放置在配置文件中

3.11 引用邮件模块
    目的是为了把测试结果分发给测试部门其它同事查阅（建议，自动化测试报告不直接给开发发邮件）
    因为自动化测试偶尔会产生误报：
    