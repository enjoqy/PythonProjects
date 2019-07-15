#!/usr/bin/env python 
# -*- coding:utf-8 -*-

sql_tmp = "CREATE TABLE `china_job` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `province` varchar(255) DEFAULT NULL COMMENT '省份',  `job_title` varchar(255) DEFAULT NULL COMMENT '职位',  `company_name` varchar(255) DEFAULT NULL COMMENT '公司名称',  `working_place` varchar(255) DEFAULT NULL COMMENT '工作地点',  `salary` varchar(255) DEFAULT NULL COMMENT '薪资',  `release_time` varchar(255) DEFAULT NULL COMMENT '发布时间',  `district` varchar(255) DEFAULT NULL COMMENT '行政区',  `work_exp` varchar(255) DEFAULT NULL COMMENT '工作经验要求',  `degree` varchar(255) DEFAULT NULL COMMENT '学历要求',  `hiring_number` varchar(255) DEFAULT NULL COMMENT '招聘人数',  PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;"

province_name = '1111'
row = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
aa = "INSERT INTO china_job (province, job_title, company_name, working_place, salary, release_time, district, work_exp, degree, hiring_number) " \
     " VALUES " \
     "(\"" + province_name + "\",\"" + row[0] + "\",\"" + row[1] + "\",\"" + row[2] + "\",\"" + row[3] + "\",\"" + \
     row[4] + "\",\"" + row[5] + "\",\"" + row[6] + "\",\"" + row[7] + "\",\"" + row[8] + "\");"

# 错误的示范，这样的多行字符串，会使其中的参数失去意义
bb = '''
     INSERT INTO china_job (province, job_title, company_name, working_place, salary, release_time, district, work_exp, degree, hiring_number)
     VALUES 
     (\" + province_name + \",\" + row[0] + \",\" + row[1] + \",\" + row[2] + \",\" + row[3] + \",\" 
     row[4] + \",\" + row[5] + \",\" + row[6] + \",\" + row[7] + \",\" + row[8] + \" );
     '''

print(bb)

print('111111111')
print(aa)
