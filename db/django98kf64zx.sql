-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: django98kf64zx
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `django98kf64zx`
--

/*!40000 DROP DATABASE IF EXISTS `django98kf64zx`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `django98kf64zx` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `django98kf64zx`;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(100) DEFAULT NULL COMMENT '配置参数值',
  `url` varchar(500) DEFAULT NULL COMMENT 'url',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='配置文件';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES (1,'picture1','upload/picture1.jpg',NULL),(2,'picture2','upload/picture2.jpg',NULL),(3,'picture3','upload/picture3.jpg',NULL);
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monthlysalesofcarmodels`
--

DROP TABLE IF EXISTS `monthlysalesofcarmodels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monthlysalesofcarmodels` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `year` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '年份',
  `month` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '月份',
  `ranking` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '排名',
  `model` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '车型',
  `shareofsales` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '厂商',
  `manufacturer` int(11) DEFAULT NULL COMMENT '销量(辆)',
  `sales` int(11) DEFAULT NULL COMMENT '售价(万元)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1740216073629 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='车型每月销量';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthlysalesofcarmodels`
--

LOCK TABLES `monthlysalesofcarmodels` WRITE;
/*!40000 ALTER TABLE `monthlysalesofcarmodels` DISABLE KEYS */;
INSERT INTO `monthlysalesofcarmodels` VALUES (1740216073450,'2025-02-22 09:21:13','2022','1','1','轩逸','东风日产',61170,9),(1740216073454,'2025-02-22 09:21:13','2022','2','2','朗逸','上汽大众',45524,10),(1740216073457,'2025-02-22 09:21:13','2022','3','3','宏光MINIEV','上汽通用五菱',37048,11),(1740216073460,'2025-02-22 09:21:13','2022','4','4','哈弗H6','长城汽车',35570,12),(1740216073463,'2025-02-22 09:21:13','2022','5','5','长安CS75 PLUS','长安汽车',33590,13),(1740216073466,'2025-02-22 09:21:13','2022','6','6','Model Y','特斯拉中国',33297,14),(1740216073469,'2025-02-22 09:21:13','2022','7','7','长安CS55PLUS','长安汽车',30316,15),(1740216073472,'2025-02-22 09:21:13','2022','8','8','凯美瑞','广汽丰田',28023,16),(1740216073475,'2025-02-22 09:21:13','2022','9','9','Model 3','特斯拉中国',26548,17),(1740216073478,'2025-02-22 09:21:13','2022','10','10','速腾','一汽-大众',26341,18),(1740216073481,'2025-02-22 09:21:13','2022','11','11','秦PLUS','比亚迪',25535,19),(1740216073484,'2025-02-22 09:21:13','2022','12','12','逍客','东风日产',24732,20),(1740216073487,'2025-02-22 09:21:13','2022','1','13','红旗HS5','一汽红旗',24451,21),(1740216073491,'2025-02-22 09:21:13','2022','2','14','本田CR-V','东风本田',24293,22),(1740216073494,'2025-02-22 09:21:13','2022','3','15','逸动','长安汽车',21883,23),(1740216073497,'2025-02-22 09:21:13','2022','4','16','宋PLUS新能源','比亚迪',20722,24),(1740216073500,'2025-02-22 09:21:14','2022','5','17','宝马5系','华晨宝马',20579,25),(1740216073502,'2025-02-22 09:21:14','2022','6','18','雷凌','广汽丰田',19485,26),(1740216073506,'2025-02-22 09:21:14','2022','7','19','宝马3系','华晨宝马',18841,27),(1740216073509,'2025-02-22 09:21:14','2022','8','20','宝来','一汽-大众',18521,28),(1740216073511,'2025-02-22 09:21:14','2022','9','21','奥迪A4L','一汽-大众奥迪',18444,29),(1740216073514,'2025-02-22 09:21:14','2022','10','22','缤智','广汽本田',18395,30),(1740216073517,'2025-02-22 09:21:14','2022','11','23','奔驰GLC','北京奔驰',18211,31),(1740216073521,'2025-02-22 09:21:14','2022','12','24','帝豪','吉利汽车',18129,32),(1740216073524,'2025-02-22 09:21:14','2022','1','25','别克GL8','上汽通用别克',17859,33),(1740216073527,'2025-02-22 09:21:14','2022','2','26','途观L','上汽大众',17768,34),(1740216073530,'2025-02-22 09:21:14','2022','3','27','本田XR-V','东风本田',17614,35),(1740216073533,'2025-02-22 09:21:14','2022','4','28','雅阁','广汽本田',17601,36),(1740216073535,'2025-02-22 09:21:14','2022','5','29','天籁','东风日产',17571,37),(1740216073538,'2025-02-22 09:21:14','2022','6','30','宝马X3','华晨宝马',17101,38),(1740216073541,'2025-02-22 09:21:14','2022','7','31','威兰达','广汽丰田',16982,39),(1740216073544,'2025-02-22 09:21:14','2022','8','32','缤越','吉利汽车',16976,40),(1740216073546,'2025-02-22 09:21:14','2022','9','33','长安欧尚X5','长安汽车',16400,41),(1740216073549,'2025-02-22 09:21:14','2022','10','34','瑞虎8','奇瑞汽车',16240,42),(1740216073552,'2025-02-22 09:21:14','2022','11','35','博越','吉利汽车',16107,43),(1740216073555,'2025-02-22 09:21:14','2022','12','36','思域','东风本田',16019,44),(1740216073557,'2025-02-22 09:21:14','2022','1','37','迈腾','一汽-大众',15991,45),(1740216073560,'2025-02-22 09:21:14','2022','2','38','帕萨特','上汽大众',14668,46),(1740216073563,'2025-02-22 09:21:14','2022','3','39','RAV4荣放','一汽丰田',13654,47),(1740216073565,'2025-02-22 09:21:14','2022','4','40','传祺GS4','广汽乘用车',13523,48),(1740216073568,'2025-02-22 09:21:14','2022','5','41','奔驰E级','北京奔驰',13460,49),(1740216073570,'2025-02-22 09:21:14','2022','6','42','MG5','上汽名爵',13416,50),(1740216073573,'2025-02-22 09:21:14','2022','7','43','汉兰达','广汽丰田',13189,51),(1740216073575,'2025-02-22 09:21:14','2022','8','44','马自达3 昂克赛拉','长安马自达',13157,52),(1740216073579,'2025-02-22 09:21:14','2022','9','45','红旗H5','一汽红旗',13137,53),(1740216073582,'2025-02-22 09:21:14','2022','10','46','汉','比亚迪',12781,54),(1740216073585,'2025-02-22 09:21:14','2022','11','47','卡罗拉','一汽丰田',12564,55),(1740216073588,'2025-02-22 09:21:14','2022','12','48','亚洲龙','一汽丰田',8000,5600),(1740216073590,'2025-02-22 09:21:14','2022','1','49','理想ONE','理想',12268,57),(1740216073594,'2025-02-22 09:21:14','2022','2','50','T-ROC探歌','一汽-大众',12187,58),(1740216073597,'2025-02-22 09:21:14','2022','3','51','星瑞','吉利汽车',12109,59),(1740216073600,'2025-02-22 09:21:14','2022','4','52','荣威RX5','上汽集团',12074,60),(1740216073602,'2025-02-22 09:21:14','2022','5','53','奥迪Q5L','一汽-大众奥迪',11699,61),(1740216073605,'2025-02-22 09:21:14','2022','6','54','奥迪A3','一汽-大众奥迪',11664,62),(1740216073608,'2025-02-22 09:21:14','2022','7','55','五菱星辰','上汽通用五菱',10000,12000),(1740216073610,'2025-02-22 09:21:14','2022','8','56','星越L','吉利汽车',11492,64),(1740216073613,'2025-02-22 09:21:14','2022','9','57','瑞虎7','奇瑞汽车',11138,65),(1740216073615,'2025-02-22 09:21:14','2022','10','58','皓影','广汽本田',11071,66),(1740216073618,'2025-02-22 09:21:14','2022','11','59','荣威i5','上汽集团',10940,67),(1740216073621,'2025-02-22 09:21:14','2022','12','60','宝马X1','华晨宝马',10904,6800),(1740216073625,'2025-02-22 09:21:14','2022','1','61','海豚','比亚迪',10602,69),(1740216073628,'2025-02-22 09:21:14','2022','1','62','科鲁泽','上汽通用雪佛兰',100,70);
/*!40000 ALTER TABLE `monthlysalesofcarmodels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monthlysalesofcarmodelsforecast`
--

DROP TABLE IF EXISTS `monthlysalesofcarmodelsforecast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monthlysalesofcarmodelsforecast` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `month` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '月份',
  `model` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '车型',
  `shareofsales` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '厂商',
  `sales` int(11) DEFAULT NULL COMMENT '售价(万元)',
  `manufacturer` int(11) DEFAULT NULL COMMENT '需求量(辆)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='销量预测';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthlysalesofcarmodelsforecast`
--

LOCK TABLES `monthlysalesofcarmodelsforecast` WRITE;
/*!40000 ALTER TABLE `monthlysalesofcarmodelsforecast` DISABLE KEYS */;
INSERT INTO `monthlysalesofcarmodelsforecast` VALUES (1,'2025-02-22 09:19:51','月份1','车型1','厂商1',1,1),(2,'2025-02-22 09:19:51','月份2','车型2','厂商2',2,2),(3,'2025-02-22 09:19:51','月份3','车型3','厂商3',3,3),(4,'2025-02-22 09:19:51','月份4','车型4','厂商4',4,4),(5,'2025-02-22 09:19:51','月份5','车型5','厂商5',5,5),(6,'2025-02-22 09:19:51','月份6','车型6','厂商6',6,6),(7,'2025-02-22 09:19:52','月份7','车型7','厂商7',7,7),(8,'2025-02-22 09:19:52','月份8','车型8','厂商8',8,8);
/*!40000 ALTER TABLE `monthlysalesofcarmodelsforecast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monthlysalesofmanufacturers`
--

DROP TABLE IF EXISTS `monthlysalesofmanufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monthlysalesofmanufacturers` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `year` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '年份',
  `month` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '月份',
  `ranking` int(11) DEFAULT NULL COMMENT '排行',
  `shareofsales` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '厂商',
  `manufacturer` int(11) DEFAULT NULL COMMENT '销量(辆)',
  `shareofsalesvolume` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '占销量份额',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1740216064042 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='厂商每月销售';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monthlysalesofmanufacturers`
--

LOCK TABLES `monthlysalesofmanufacturers` WRITE;
/*!40000 ALTER TABLE `monthlysalesofmanufacturers` DISABLE KEYS */;
INSERT INTO `monthlysalesofmanufacturers` VALUES (1740216063880,'2025-02-22 09:21:04','2023','1',1,'比亚迪',133317,'10.29%'),(1740216063888,'2025-02-22 09:21:04','2023','2',2,'长安汽车',90067,'6.95%'),(1740216063890,'2025-02-22 09:21:04','2023','3',3,'上汽大众',78000,'6'),(1740216063894,'2025-02-22 09:21:04','2023','4',4,'一汽-大众',70004,'5.41%'),(1740216063897,'2025-02-22 09:21:04','2023','5',5,'吉利汽车',67479,'5.21%'),(1740216063900,'2025-02-22 09:21:04','1990','6',6,'广汽丰田',61105,'4.72%'),(1740216063903,'2025-02-22 09:21:04','1991','7',7,'华晨宝马',56765,'4.38%'),(1740216063906,'2025-02-22 09:21:04','1992','8',8,'上汽通用五菱',46922,'3.62%'),(1740216063909,'2025-02-22 09:21:04','1993','9',9,'一汽丰田',43787,'3.38%'),(1740216063912,'2025-02-22 09:21:04','1994','10',10,'北京奔驰',42357,'3.27%'),(1740216063914,'2025-02-22 09:21:04','1995','1',11,'广汽本田',40259,'3.11%'),(1740216063917,'2025-02-22 09:21:04','1996','2',12,'东风日产',40243,'3.11%'),(1740216063920,'2025-02-22 09:21:04','1997','3',13,'上汽通用别克',35007,'2.7%'),(1740216063922,'2025-02-22 09:21:04','1998','4',14,'一汽-大众奥迪',30900,'2.39%'),(1740216063925,'2025-02-22 09:21:04','1999','5',15,'长城汽车',28450,'2.2%'),(1740216063927,'2025-02-22 09:21:04','2000','6',16,'特斯拉中国',26843,'2'),(1740216063930,'2025-02-22 09:21:04','2001','7',17,'东风本田',23713,'1.83%'),(1740216063933,'2025-02-22 09:21:04','2002','8',18,'一汽红旗',22077,'1.7%'),(1740216063935,'2025-02-22 09:21:04','2003','9',19,'奇瑞汽车',21255,'1.64%'),(1740216063938,'2025-02-22 09:21:04','2004','10',20,'北京现代',20075,'1.55%'),(1740216063940,'2025-02-22 09:21:04','2005','11',21,'广汽乘用车',19688,'1.52%'),(1740216063943,'2025-02-22 09:21:04','2006','12',22,'长安汽车',18371,'1.42%'),(1740216063945,'2025-02-22 09:21:04','2007','1',23,'上汽集团',15765,'1.22%'),(1740216063947,'2025-02-22 09:21:04','2008','2',24,'理想',15141,'1.17%'),(1740216063950,'2025-02-22 09:21:04','2009','3',25,'领克',10816,'0.84%'),(1740216063952,'2025-02-22 09:21:04','2010','4',26,'奇瑞汽车',10746,'0.83%'),(1740216063955,'2025-02-22 09:21:04','2011','5',27,'一汽-大众捷达',10531,'0.81%'),(1740216063958,'2025-02-22 09:21:04','2012','6',28,'上汽通用雪佛兰',10508,'0.81%'),(1740216063961,'2025-02-22 09:21:04','2013','7',29,'广汽埃安',10206,'0.79%'),(1740216063964,'2025-02-22 09:21:04','2014','8',30,'沃尔沃亚太',9710,'0.75%'),(1740216063966,'2025-02-22 09:21:04','2015','9',31,'通用凯迪拉克',9507,'0.73%'),(1740216063969,'2025-02-22 09:21:04','2016','10',32,'长安福特',9406,'0.73%'),(1740216063971,'2025-02-22 09:21:04','2017','11',33,'东风乘用车',9246,'0.71%'),(1740216063974,'2025-02-22 09:21:04','2018','12',34,'蔚来',8506,'0.66%'),(1740216063976,'2025-02-22 09:21:04','2019','1',35,'上汽名爵',8201,'0.63%'),(1740216063979,'2025-02-22 09:21:04','2020','2',36,'腾势汽车',6438,'0.5%'),(1740216063981,'2025-02-22 09:21:04','2021','3',37,'起亚',6202,'0.48%'),(1740216063984,'2025-02-22 09:21:04','2022','4',38,'深蓝汽车',6137,'0.47%'),(1740216063986,'2025-02-22 09:21:04','2023','5',39,'合众汽车',6016,'0.46%'),(1740216063988,'2025-02-22 09:21:04','2024','6',40,'长城汽车',5795,'0.45%'),(1740216063991,'2025-02-22 09:21:04','2025','7',41,'长安林肯',5301,'0.41%'),(1740216063993,'2025-02-22 09:21:04','1997','8',42,'小鹏汽车',5218,'0.4%'),(1740216063996,'2025-02-22 09:21:04','1998','9',43,'江汽集团',4720,'0.36%'),(1740216063998,'2025-02-22 09:21:04','1999','10',44,'东风日产',4606,'0.36%'),(1740216064000,'2025-02-22 09:21:04','2000','11',45,'赛力斯汽车',4469,'0.35%'),(1740216064003,'2025-02-22 09:21:04','2001','12',46,'奇瑞新能源',4175,'0.32%'),(1740216064005,'2025-02-22 09:21:04','2002','1',47,'长安马自达',4024,'0.31%'),(1740216064008,'2025-02-22 09:21:04','2003','2',48,'东风小康',3669,'0.28%'),(1740216064010,'2025-02-22 09:21:04','2004','3',49,'吉利几何',3271,'0.25%'),(1740216064014,'2025-02-22 09:21:04','2005','4',50,'smart',3170,'0.24%'),(1740216064016,'2025-02-22 09:21:04','2006','5',51,'一汽奔腾',3131,'0.24%'),(1740216064019,'2025-02-22 09:21:04','2007','6',52,'极氪',3116,'0.24%'),(1740216064021,'2025-02-22 09:21:04','2008','7',53,'东风风行',3090,'0.24%'),(1740216064024,'2025-02-22 09:21:04','2009','8',54,'凯翼汽车',3050,'0.24%'),(1740216064027,'2025-02-22 09:21:04','2010','9',55,'BEIJING汽车',3020,'0.23%'),(1740216064029,'2025-02-22 09:21:04','2011','10',56,'江铃福特',2962,'0.23%'),(1740216064031,'2025-02-22 09:21:04','2012','11',57,'SWM斯威汽车',2918,'0.23%'),(1740216064034,'2025-02-22 09:21:04','2013','12',58,'长城新能源',2493,'0.19%'),(1740216064036,'2025-02-22 09:21:04','2014','1',59,'东风雪铁龙',2390,'0.18%'),(1740216064039,'2025-02-22 09:21:04','2015','1',60,'奇瑞捷豹路虎',2302,'0.18%'),(1740216064041,'2025-02-22 09:21:04','2016','1',61,'吉利新能源',2053,'0.16%');
/*!40000 ALTER TABLE `monthlysalesofmanufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `overallsalesofcars`
--

DROP TABLE IF EXISTS `overallsalesofcars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `overallsalesofcars` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `time` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '时间',
  `manufacturer` int(11) DEFAULT NULL COMMENT '销量(辆)',
  `yearonyear` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '同比',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='汽车总体销量';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `overallsalesofcars`
--

LOCK TABLES `overallsalesofcars` WRITE;
/*!40000 ALTER TABLE `overallsalesofcars` DISABLE KEYS */;
INSERT INTO `overallsalesofcars` VALUES (1,'2025-02-22 09:19:51','时间1',1,'同比1'),(2,'2025-02-22 09:19:51','时间2',2,'同比2'),(3,'2025-02-22 09:19:51','时间3',3,'同比3'),(4,'2025-02-22 09:19:51','时间4',4,'同比4'),(5,'2025-02-22 09:19:51','时间5',5,'同比5'),(6,'2025-02-22 09:19:51','时间6',6,'同比6'),(7,'2025-02-22 09:19:51','时间7',7,'同比7'),(8,'2025-02-22 09:19:51','时间8',8,'同比8');
/*!40000 ALTER TABLE `overallsalesofcars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `image` varchar(200) DEFAULT NULL COMMENT '头像',
  `role` varchar(100) DEFAULT '管理员' COMMENT '角色',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='管理员表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin','upload/image1.jpg','管理员','2025-02-22 09:19:52');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-10 17:40:16
