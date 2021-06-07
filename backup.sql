/*
SQLyog Ultimate v10.00 Beta1
MySQL - 8.0.21 : Database - exampool
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`exampool` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `exampool`;

/*Table structure for table `bank_modern_history` */

DROP TABLE IF EXISTS `bank_modern_history`;

CREATE TABLE `bank_modern_history` (
  `id` int NOT NULL,
  `chap` int DEFAULT NULL,
  `stem` varchar(256) DEFAULT NULL,
  `option_A` varchar(128) DEFAULT NULL,
  `option_B` varchar(128) DEFAULT NULL,
  `option_C` varchar(128) DEFAULT NULL,
  `option_D` varchar(128) DEFAULT NULL,
  `answer` varchar(5) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `bank_modern_history` */

insert  into `bank_modern_history`(`id`,`chap`,`stem`,`option_A`,`option_B`,`option_C`,`option_D`,`answer`,`type`) values (1,1,'鸦片战争前中国封建社会的主要矛盾是','地主阶级和农民阶级的矛盾','帝国主义和中华民族的矛盾','资产阶级和工人阶级的矛盾','封建主义和资本主义的矛盾','A','Single4'),(2,1,'中国封建社会产生过诸多“盛世”，出现在清代的是','文景之治','贞观之治','开元之治','康乾盛世','D','Single4'),(3,1,'将中国领土台湾割让给日本的不平等条约是','《南京条约》','《北京条约》','《马关条约》','《瑗珲条约》','C','Single4'),(4,1,'西方列强对中国的侵略，首先和主要的是','政治控制','军事侵略','经济掠夺','文化渗透','B','Single4'),(5,1,'1839年组织编写成《四洲志》，向中国人介绍西方情况的是','林则徐','魏源','马建忠','郑观应','A','Single4'),(6,1,'19世纪末，在帝国主义列强瓜分中国的狂潮中提出“门户开放”政策的国家是','俄国','日本','美国','德国','C','Single4'),(7,1,'19世纪初，大肆向中国走私鸦片的主要国家是','美国','英国','日本','俄国','B','Single4'),(8,1,'1840年鸦片战争前，中国社会的性质是','奴隶社会','封建社会','半殖民地半封建社会','资本主义社会','B','Single4'),(9,1,'早在1836年就扬言要用武力打开中国国门的是','英国驻华商务监督义律','美国驻华公使田贝','德国传教士郭士立','法国传教士孟振生','A','Single4'),(10,1,'第一次鸦片战争后，清政府被迫与法国签订的不平等条约是','《南京条约》','《望厦条约》','《黄埔条约》','《北京条约》','C','Single4'),(11,1,'外国列强对近代中国进行资本输出最早出现在','第一次鸦片战争后','第二次鸦片战争后','中日甲午战争后','八国联军侵华战争后','B','Single4'),(12,1,'在中国近代史上，人民群众第一次反侵略的武装斗争是','三元里人民的抗英斗争','太平天国抗击洋枪队的斗争','台湾人民的抗日斗争','义和团抗击八国联军的斗争','A','Single4'),(13,1,'日本在甲午战争后迫使清政府签订了','《天津条约','《北京条约》','《马关条约》','《辛丑条约》','C','Single4'),(14,1,'1860年洗劫和烧毁圆明园的侵略军是','日本侵略军','俄国侵略军','英法联军','八国联军','C','Single4'),(15,1,'1895年签订的将中国领土台湾割让给日本的不平等条约是','《南京条约》','《北京条约》','《天津条约》','《马关条约》','D','Single4'),(16,1,'近代中国睁眼看世界的第一人是','魏源','林则徐','龚自珍','洪仁玕','B','Single4'),(17,1,'第一次鸦片战争结束后，美国迫使清政府订立的不平等条约是','《南京条约》','《望厦条约》','《黄埔条约》','《瑷珲条约》','B','Single4'),(18,2,'最先对洋务运动的指导思想做出比较完整表述的是','冯桂芬','薛福成','曾国藩','张之洞','A','Single4'),(19,2,'洋务运动时期兴办的第一个规模较大的兵工厂是','马尾船政局','金陵机器局','天津机器局','江南制造总局','D','Single4'),(20,2,'戊戌维新时期，梁启超曾任主笔的报纸是','《时务报》','《万国公报》','《国闻报》','《湘报》','A','Single4'),(21,2,'1898年3月，张之洞发表的对抗维新变法的代表作是','《新学伪经考》','《孔子改制考》','《人类公理》','《劝学篇》','D','Single4'),(22,2,'20世纪初，在民主革命思想传播中发表《警世钟》的是','章炳麟','邹容','陈天华','孙中山','C','Single4'),(23,2,'太平天国农民起义爆发的时间是','1851年','1853年','1856年','1864年','A','Single4'),(24,2,'太平天国由盛而衰的转折点是','永安建制','北伐失利','天京事变','洪秀全病逝','C','Single4'),(25,2,'洋务运动时期最早创办的翻译学堂是','同文馆','广方言馆','译书局','译书馆','A','Single4'),(26,2,'1898年发表《劝学篇》一文，对抗维新变法的洋务派官僚是','李鸿章','左宗棠','张之洞','刘坤一','C','Single4'),(27,2,'戊戌维新时期，维新派在上海创办的影响较大的报刊是','《时务报》','《国闻报》','《湘报》','《万国公报》','A','Single4'),(28,2,'魏源在1843年编纂的《海国图志》中提出的重要思想是','中学为体、西学为用','物竞天择、适者生存','救亡图存','师夷长技以制夷','D','Single4'),(29,2,'太平天国在1853年颁布的纲领性文件是','《十款天条》','《原道觉世训》','《天朝田亩制度》','《资政新篇》','C','Single4'),(30,2,'19世纪60年代，洋务派最早从事的洋务事业是','举办民用工业','创立新式学堂','派遣留学生','开设军用工业','D','Single4'),(31,2,'在中国近代史上，资产阶级思想与封建主义思想的第一次正面交锋是','维新派与守旧派的论战','洋务派与维新派的论战','革命派与改良派的论战','洋务派与顽固派的论战','A','Single4'),(32,2,'洪秀全在广西发动金田起义的时间是','1851年','1853年','1856年','1864年','A','Single4'),(33,2,'中国近代史上第一个具有资本主义色彩的改革方案是','《海国图志》','《救亡决论》','《天朝天田制度》','《资政新篇》','D','Single4'),(34,2,'19世纪60年代，清朝统治集团中倡导洋务的首领人物是','奕䜣(xīn)','桂良','曾国藩','李鸿章','A','Single4'),(35,2,'19世纪60年代到90年代，洋务派兴办洋务事业的指导思想是','师夷长技以制夷','中学为体，西学为用','物竞天择，适者生存','变法维新，救亡图存','B','Single4'),(36,2,'严复1898年翻译出版的《天演论》所宣传的思想是','师夷长技以制夷','中学为体、西学为用','振兴中华','物竞天择、适者生存','D','Single4'),(37,2,'太平天国农民战争爆发的标志是','金田起义','永安建制','长沙战役','南京定都','A','Single4'),(38,2,'太平天国运动后期，提出《资政新篇》这一带有资本主义色彩改革方案的是','洪秀全','洪仁玕','石达开','李秀成','B','Single4'),(39,2,'洋务派建成的新式海军中的主力是','福建水师','广东水师','南洋水师','北洋水师','D','Single4'),(40,2,'1861年，清政府设立的掌管洋务的机关是','江南制造总局','京师同文馆','总理各国事务衙门','外务部','C','Single4'),(41,2,'19世纪末，梁启超撰写的宣传变法维新主张的著作是','《新学伪经考》','《人类公理》','《仁学》','《变法通义》','D','Single4'),(42,2,'1904年至1905年，为了争夺在华利益而在中国东北进行战争的帝国主义国家是','美国与俄国','美国与英国','英国与日本','日本与俄国','D','Single4'),(43,2,'我国的科举制度正式废除于','1905年','1906年','1907年','1908年','B','Single4'),(44,2,'太平天国由盛而衰的转折点是','永安建制','长沙战役','北伐失利','天京事变','D','Single4'),(45,3,'20世纪初，在民主革命思想传播中发表《驳康有为论革命书》的是','邹容','章炳麟','陈天华','严复','B','Single4'),(46,3,'近代中国历史上第一个全国性的资产阶级革命政党是','兴中会','中国同盟会','中华革命党','中国国民党','B','Single4'),(47,3,'武昌起义前夕，在保路运动中规模最大、斗争最激烈的省份是','湖南','湖北','广东','四川','D','Single4'),(48,3,'中国历史上第一部具有资产阶级共和国宪法性质的法典是','《中华民国宪法》','《钦定宪法大纲》','《中华民国约法》','《中华民国临时约法》','D','Single4'),(49,3,'为反对袁世凯刺杀宋教仁和“善后大借款”，孙中山在1913年领导革命党人发动了','二次革命','护国战争','护法战争','北伐战争','A','Single4'),(50,3,'1914年7月，孙中山在东京正式成立了','兴中会','中国同盟会','中华革命党','中国国民党','C','Single4'),(51,3,'武昌义胜利后被推举为湖北军政府都督的是','黄兴','黎元洪','孙中山','章太炎','B','Single4'),(52,3,'1894年，孙中山在檀香山建立的资产阶级革命组织是','兴中会','华兴会','光复会','岳王会','A','Single4'),(53,3,'1905年，中国同盟会成立后的机关报是','《时务报》','《国闻报》','《新民丛报》','《民报》','D','Single4'),(54,3,'1911年夏，湖北、湖南、广东和四川爆发的民众运动是','拒俄运动','拒法运动','保路运动','立宪运动','C','Single4'),(55,3,'1911年10月，资产阶级革命派发动了将辛亥革命推向高潮的','惠州起义','河口起义','广州起义','武昌起义','D','Single4'),(56,3,'标志着中国民族资产阶级开始登上政治舞台的运动是','洋务运动','戊戌维新运动','国会请愿运动','保路运动','B','Single4'),(57,3,'1905年至1907年，资产阶级革命派与改良派论战的焦点是','要不要打倒列强','要不要实行共和','要不要以革命手段推翻清政府','要不要废科举，兴学堂','C','Single4'),(58,3,'1905年，中国同盟会创办的机关报是','《民报》','《新民丛报》','《时务报》','《国闻报》','A','Single4'),(59,3,'1911年，标志辛亥革命达到高潮的起义是','惠州起义','河口赶义','广州起义','武昌起义','D','Single4'),(60,3,'袁世凯窃夺辛亥革命成果后，于1914年5月炮制了','《戒严法》','《中华民国约法》','《钦定宪法大纲》','《暂行新刑律》','B','Single4'),(61,3,'中国资产阶级领导的旧民主主义革命终结的标志是','二次革命的失败','护国运动的失败','第一次护法运动的失败','第二次护法运动的失败','D','Single4'),(62,4,'1920年8月，陈独秀等领导建立的中国最早的地方共产党组织是','北京共产主义小组','上海共产主义小组','武汉共产主义小组','广州共产主义小组','B','Single4'),(63,4,'1919年，发表《我的马克思主义观》一文的是','陈独秀','李大钊','蔡和森','杨匏安','B','Single4'),(64,4,'1922年7月，中共二大第一次明确提出了','反帝反封建的民主革命纲领','实现共产主义的最高纲领','新民主主义革命总路线','土地革命总路线','A','Single4'),(65,4,'1923年2月，中国共产党领导的工人罢工斗争是','香港海员罢工','安源路矿工人罢工','京汉铁路工人罢工','省港工人罢工','C','Single4'),(66,4,'中国共产党确定第一次国共合作和建立革命统一战线方针的会议是','中共三大','中共四大','中共五大','中共六大','A','Single4'),(67,4,'1915年9月在上海创办《青年》杂志的是','胡适','鲁迅','李大钊','陈独秀','D','Single4'),(68,4,'中国新民主主义革命的伟大开端是','戊戌变法运动','保路运动','新文化运动','五四运动','D','Single4'),(69,4,'1922年召开的中共二大第一次明确提出了','实现共产主义的最高纲领','新民主主义革命总路线','反帝反封建的民主革命纲领','土地革命总路线','C','Single4'),(70,4,'中国共产党领导的中国工人运动第一个高潮的起点是','香港海员罢工','安源路矿工人罢工','京汉铁路工人罢工','省港工人罢工','A','Single4'),(71,4,'第一次国共合作的政治基础是','三民主义','新三民主义','新民主主义','社会主义','B','Single4'),(72,4,'在俄国十月革命影响下，中国率先举起马克思主义旗帜的是','陈独秀','李大钊','陈望道','毛泽东','B','Single4'),(73,4,'1921年8月，中国共产党成立的领导工人运动的专门机关是','职工运动委员会','中国劳动组合书记部','中华全国总工会','省港罢工委员','B','Single4'),(74,4,'1924年，国民革命统一战线正式形成的标志是','中国国民党一大的召开','中国国民党二大的召开','中国共产党三大的召开','中国共产党四大的召开','A','Single4'),(75,4,'1920年，陈独秀等建立的中国共产党早期组织是','北京共产主义小组','上海共产主义小组','武汉共产主义小组','广州共产主义小组','B','Single4'),(76,4,'中国共产党第一次明确提出反帝反封建民主革命纲领的会议是','中共一大','中共二大','中共三大','中共四大','B','Single4'),(77,4,'新文化运动的主要内容是','提倡民主和科学','宣传俄国十月革命','主张社会革命','反对外来侵略','A','Single4'),(78,4,'1918年5月，鲁迅发表的第一篇白话文小说是','《阿Q正传》','《狂人日记》','《药》','《孔乙己》','B','Single4'),(79,4,'中国新民主主义革命的开端是','五卅运动','五四运动','一二一运动','一二二九运动','B','Single4'),(80,4,'1920年10月，李大钊发赶成立的中国共产党早期组织是','上海共产主义小组','武汉共产主义小组','北京共产主义小组','共产主义小组','C','Single4'),(81,4,'1921年8月，中国共产党成立的领导工人运动的机关是','上海机器工会','北京长辛店工人俱乐部','中华全国总工会','中国劳动组合书记部','C','Single4'),(82,4,'中国共产党领导建立的第一个农民协会是在','浙江省萧山县','广东省海丰县','福建省上杭县','湖南省湘潭县','A','Single4'),(83,4,'五四运动爆发的直接导火线是','北洋军阀接受日本提出的“二十一条','北洋军阀与日本签订“西原借款”合同','巴黎和会上中国外交的失败','华盛顿会议上中国外交的受挫','C','Single4'),(84,4,'1924年11月，出任黄埔军校政治部主任是','周恩来','廖仲恺','邓演达','聂荣臻','A','Single4'),(85,4,'1925年至1926年间，中国工人坚持16个月之久的罢工斗争是','香港海员罢工','安源路矿工人罢工','京汉铁路工人罢工','省港罢工','D','Single4'),(86,4,'1928年12月，在东北宣布“改易旗帜”、归顺南京国民政府的是','孙传芳','张学良','吴佩孚','张作霖','B','Single4'),(87,5,'1928年，毛泽东主持制定的中国共产党历史上第一个土地法是','《井冈山土地法》','《兴国土地法》','《关于清算、减租及土地问题的指示》','《中国土地法大纲》','A','Single4'),(88,5,'1927年毛泽东在中共八七会议上提出的著名论断是','“须知政权是由枪杆子中取得的”','“没有调查就没有发言权”','“兵民是胜利之本”','“一切反动派都是纸老虎”','A','Single4'),(89,5,'从1930年到1931年，红一方面军在三次反“围剿”斗争胜利的基础上开辟了','鄂豫皖革命根据地','左右江革命根据地','湘鄂西革命根据地','中央革命根据地','D','Single4'),(90,5,'1931年11月当选为中华苏维埃共和国临时中央政府主席的是','毛泽东','周恩来','张国焘','王稼祥','A','Single4'),(91,5,'《义勇军进行曲》的词作者是','田汉','聂耳','鲁迅','瞿秋白','A','Single4'),(92,5,'1928年，毛泽东主持制定中国共产党第一个土地法是在','井冈山','瑞金','古田','永新','A','Single4'),(93,5,'1927年，中共八七会议确定的总方针是','推翻北洋军阀的黑暗统治','开辟农村革命根据地','开展土地革命和武装反抗国民党反动派','建立工农民主统一战线','C','Single4'),(94,5,'中国共产党独立领导革命战争和创建人民军队的开端是','秋收起义','南昌起义','平江起义','广州起义','B','Single4'),(95,5,'1930年1月，毛泽东进一步阐农村包围城市、武装夺取政权理论的文章是','《中国的红色政权为什么能够存在》','《星星之火，可以燎原》','《井冈山的斗争》','《中国革命战争的战略问题》','B','Single4'),(96,5,'1927年，中国共产党确定土地革命和武装反抗国民党反动派方针的会议是','八七会议','古田会议','赣南会议','十二月会议','A','Single4'),(97,5,'1930年成立的中国国民党临时行动委员会(又称第三党)，其主要领导人是','梁漱溟','黄炎培','张君劢(mài)','邓演达','D','Single4'),(98,5,'1930年1月，毛泽东进一步从理论上阐逋农村包围城市、武装夺取政权理论的文章是','《中国的红色政权为什么能够存在》','《星星之火，可以燎原》','《井冈山的斗争》','《中国革命战争的战略问题》','B','Single4'),(99,5,'1928年12月，毛泽东主持制定的中国共产党历史上第一个土地法是','《井冈山土地法》','《兴国土地法》','《关于清算、减租及土地问题的指示》','《中国土地法大纲》','A','Single4'),(100,5,'国民党四大家族官僚资本的性质是','私人垄断资本主义','封建的买办的国家垄断资本主义','私人资本主义','国家资本主义','B','Single4'),(101,5,'1936年10月，中国工农红军第一、二、四方面军胜利会师于','陕北保安地区','陕北洛川地区','陕北瓦窑堡地区','甘肃会宁、静宁地区','D','Single4'),(102,5,'遵义会议后，中共中央政治局成立了新的三人团负责红军的军事行动，其成员是','毛泽东、朱德、周恩来','毛泽东、朱德、王稼祥','毛泽东、周恩来、王稼祥','毛泽东、张闻天、周恩来','C','Single4'),(103,5,'1927年，蒋介石在上海制造了捕杀共产党员和革命群众的','中山舰事件','整理党务案','四一二政变','七一五政变','C','Single4'),(104,5,'国民党在全国的统治建立后，官僚资本的垄断活动首先和主要是从','重工业方面开始的','商业方面开始的','轻工业方面开始的','金融业方面开始的','D','Single4'),(105,5,'1927年大革命失败后，中国共产党召开的确定土地革命和武装斗争方针的会议是','八七会议','古田会议','遵义会议','洛川会议','A','Single4'),(106,5,'1931年1月至1935年1月，中国共产党内出现的主要错误倾向是','“左”倾盲动主义','“左”倾教条主义','右倾保守主义','右倾投降主义','B','Single4'),(107,5,'1931年，日本帝国主义制造了侵略中国的','九一八事变','一二八事变','华北事变','卢沟桥事变','A','Single4'),(108,5,'第一次国共合作的政治基础是','三民主义','新民主主义','新三民主义','社会主义','C','Single4'),(109,5,'1927年，汪精卫在武汉制造了屠杀共产党人和革命群众的','中山舰事件','整理党务案事件','四一二事变','七一五事变','D','Single4'),(110,5,'中国共产党独立领导革命战争和创建人民军队的开端是','南昌起义','秋收起义','平江起义','百色起义','A','Single4'),(111,5,'1927年，中共八七会议确定的总方针是','推翻北洋军阀黑暗统治','开辟农村革命根据地','开展土地革命和武装斗争','建立工农民主统一战线','C','Single4'),(112,5,'1930年1月，毛泽东论述中国革命“以乡村为中心”思想的著作是','《井冈山的斗争》','《星星之火，可以燎原》','《反对本本主义》','《中国革命和中国共产党》','B','Single4'),(113,5,'1930年到1931年，在红一方面军三次反“围剿”斗争胜利的基础上形成了','鄂豫皖革命根据地','左右江革命根据地','湘鄂西革命根据地','中央革命根据地','D','Single4'),(114,5,'抗日战争进入相持阶段后，日本帝国主义对国民党改府采取的政策是','以军事打击为主，政治诱降为辅','以政治诱降为主，军事打击为辅','军事打击和政治诱降并重','速战速决，武力征服','B','Single4'),(115,5,'1935年1月，中国共产党在红军长征途中召开了具有历史转折意义的','古田会议','遵义会议','两河口会议','瓦窑堡会议','B','Single4'),(116,5,'中国近代史上第一次彻底反帝反封建的革命运动是','辛亥革命','五四运动','五卅运动','国民革命','B','Single4'),(117,5,'以第一次国共合作为基础的国民革命统一战线正式形成的标志是','中共二大的召开','中共三大的召开','中国国民党一大的召开','中国国民党二大的召开','C','Single4'),(118,5,'1928年10月，国民党中央常务委员会通过了','《中华民国临时约法》','《中华民国约法》','《军政纲领》','《训政纲领》','D','Single4'),(119,5,'1928年12月，在东北宣布“服从国民政府，改易旗帜”的是','张学良','张作霖','冯国璋','冯玉祥','A','Single4'),(120,5,'1934年中国工农红军第五次反“围剿”斗争失败后，率先开始战略转移的是','红十五军团','红一方面军','红二方面军','红四方面军','B','Single4'),(121,5,'1935年1月，中国共产党在遵义会议上解决的主要问题是','军事和组织问题','思想和作风问题','政治和军事问题','筹款和征兵问题','A','Single4'),(122,5,'1933年11月，国民党爱国将领蔡廷锴和蒋光鼐发动了抗日反蒋的','北京事变','福建事变','西安事变','皖南事变','B','Single4'),(123,5,'1920年10月，李大钊发起成立的中国共产党早期组织是','上海共产主义小组','武汉共产主义小组','北京共产主义小组','广州共产主义小组','C','Single4'),(124,5,'1921年8月，中国共产党成立的领导工人运动的机关是','上海机器工会','北京长辛店工人俱乐部','中华全国总工会','中国劳动组合书记部','D','Single4'),(125,5,'中国共产党领导建立的第一个农民协会是在','浙江省萧山县','广东省海丰县','福建省上杭县','湖南省湘潭县','A','Single4'),(126,6,'1938年5至6月间，毛泽东系统阐述抗日战争的特点、前途和发展规律的重要讲演是','《抗日救国十大纲领》','《论持久战》','《中国革命和中国共产党》','《新民主主义论》','B','Single4'),(127,6,'1935年12月，中国共产党确定抗日民族统一战线政策的会议是','遵义会议','瓦窑堡会议','洛川会议','晋绥干部会议','B','Single4'),(128,6,'在抗日战争的战略防御阶段，国民党军队在正面战场上取得胜利的战役是','台儿庄战役','桂南战役','枣宜战役','中条山战役','A','Single4'),(129,6,'毛泽东在《论持久战》中指出，中国抗日战争取得胜利最关键的阶段是','战略防御阶段','战略相持阶段','战略反攻阶段','战略决战阶段','B','Single4'),(130,6,'1933年11月，在福州发动抗日反蒋事变的国民党爱国将领是','马占山和李杜','冯玉祥和吉鸿昌','蔡廷锴(kǎi)和蒋光鼐(nài)','张学良和杨虎','C','Single4'),(131,6,'1941年3月，在大后方抗日民主运动中诞生的民主党派是','中华民族解放行动委员','中国民主建国会','中国民主促进会','中国民主政团同盟','D','Single4'),(132,6,'抗日战争全面爆发后，中国军队取得第一次重大胜利的战役是','平型关战役','雁门关战役','阳明堡战役','台儿庄战役','A','Single4'),(133,6,'1945年8月，发表《对日寇的最后一战》声明的是','朱德','毛泽东','彭德怀','刘伯承','B','Single4'),(134,6,'1937年，出任新四军军长的是','朱德','刘伯承','叶挺','陈毅','C','Single4'),(135,6,'1937年，在淞沪会战中率领“八百壮士”孤守上海四行仓库的爱国将领是','佟麟阁','赵登禹','戴安澜','谢晋元','D','Single4'),(136,6,'从1937年卢沟桥事变到1938年10月广州、武汉失守，中国抗日战争处于','战略防御阶段','战略相持阶段','战略反攻阶段','战略决战阶','A','Single4'),(137,6,'1933年，冯玉祥在张家口领导成立的抗日武装力量是','东北抗日义勇军','东北抗日联军','察哈尔抗日义勇军','察哈尔抗日同盟军','D','Single4'),(138,6,'1935年，中共北平临时工作委员会领导发动的抗日救亡运动是','一二九运动','一二一运动','一二三〇运动','五二〇运动','A','Single4'),(139,6,'1945年8月，中共中央在《对目前时局的宣言》中提出的口号是','和平、民主、团结','打倒蒋介石，解放全中国','向北发展，向南防御','将革命进行到底','A','Single4'),(140,6,'1935年12月，中国共产党召开的确定抗日民族统一战线新政策的会议是','西湖会议','八七会议','瓦窑堡会议','洛川会议','C','Single4'),(141,6,'1938年5月、6月间，毛泽东发表的系统论逋抗日战争特点、前途和发展规律的著作是','《论发对日本帝国主义的策略》','《抗日救国十大纲领》','《论持久战》','《对日寇的最后一战》','C','Single4'),(142,6,'1945年4月，包括解放区代表董必武在内的中国代表团出席了','开罗会议','德黑兰会议','雅尔塔会议','联合国制宪会议','D','Single4'),(143,6,'1935年，北平学生举行的抗日救亡运动是','五四运动','一二九运动','五卅运动','一二三〇运动','B','Single4'),(144,6,'1938年3月，国民党军队在抗日战争正面战场取得胜利的战役是','平型关战役','桂南战役','台儿庄战役','枣宜战役','C','Single4'),(145,6,'941年，在缅北对日作战中以身殉国的中国远征军将领是','佟麟阁','谢晋元','张自忠','戴安澜','D','Single4'),(146,6,'1937年8月，中国共产党制定《抗日救国十大纲领》的重要会议是','瓦窑堡会议','洛川会议','中共六届六中全会','中共六届七中全会','B','Single4'),(147,6,'1940年，八路军对华北日军发动的大规模进攻战役是','平型关战役','雁门关战役','阳明堡战役','百团大战','D','Single4'),(148,7,'1945年10月10日，国共双方签署了','《国共重庆谈判纪要》','《国共重庆谈判协定》','《政府与中共代表会谈协定》','《政府与中共代表会谈纪要》','D','Single4'),(149,7,'1948年4月，毛泽东完整地提出新民主主义革命总路线的著作是','《新民主主义论》','《目前形势和我们的任务》','《在晋绥干部会议上的讲话》','《将革命进行到底》','C','Single4'),(150,7,'中国人民解放军在1949年4月21日发起的重大战役是','辽沈战役','淮海战役','平津战役','渡江战役','D','Single4'),(151,7,'1947年在国统区爆发的大规模爱国学生运动是','一二九运动','五·二〇运动','一二一运动','一二三〇运动','B','Single4'),(152,7,'《中国人民政治协商会议共同纲领》最基本、最核心的内容是规定了新中国的','基本民族政策','国体和政体','经济工作方针','外交工作原则','B','Single4'),(153,7,'在抗美援朝战争中担任中国人民志愿军总司令兼政治委员的是','朱德','彭德怀','陈毅','刘伯承','B','Single4'),(154,7,'1945年4月，出席联合国制宪会议中国代表团中的解放区代表是','周恩来','刘少奇','董必武','王若飞','C','Single4'),(155,7,'抗日战争胜利后，国共双方通过重庆谈判签订《政府与中共代表会谈纪要》的时间是','1945年8月','1945年9月','1945年10月','1945年11月','C','Single4'),(156,7,'1946年6月全面内战爆发时，国民党军队首先进攻的地区是','中原解放区','东北解放区','山东解放区','陕甘宁解放区','A','Single4'),(157,7,'新中国建立初期通过没收官僚资本建立了','合作社经济','国家资本主义经济','国营经济','民族资本主义经济','C','Single4'),(158,7,'1950年6月，中国共产党为争取国家财政经济状况的基本好转而召开的重要会议是','中共七届二中全会','中共七届三中全会','中共七届四中全会','中共七届五中全会','B','Single4'),(159,7,'1955年，毛泽东总结农业合作化运动基本经验的报告是','《关于农业生产互助合作的决议(草案)》','《关于发展农业生产合作社的决议》','《关于农业合作化问题》','《关于人民公社若干问题的决议》','C','Single4'),(160,7,'我国对资本主义工商业进行社会主义改造所实行的高级形式的国家资本主义是','加工订货','统购统销','经销代销','公私合营','D','Single4'),(161,7,'1956年召开的中共八大指出，党和全国人民当前的主要任务是','正确处理人民内部矛盾','实现社会主义四个现代化','把我国推进到社会主义社会','把我国从落后的农业国变为先进的工业国','D','Single4'),(162,7,'1948年4月，毛泽东完整地提出新民主主义革命总路线的著作是','《中国革命和中国共产党》','《目前形势和我们的任务》','《在晋绥干部会议上的讲话》','《<共产党人>发刊词》','C','Single4'),(163,7,'1946年6月，国名党当局制造了镇压上海人民团体和平请愿团的','五卅惨案','校场口惨案','下关惨案','五二〇惨案','C','Single4'),(164,7,'1947年10月10日，《中国人民解放军总部宣言》正式提出的口号是','和平、民主、团结','打倒蒋介石，解放全中国','将革命进行到底','打过长江去，解放全中国','B','Single4'),(165,8,'中国进入新民主主义社会后，在经济上处于领导地位的是','私人资本主义经济','国营经济','国家资本主义经济','合作社经济','B','Single4'),(166,8,'中国大陆基本解放和实现统一的标志是','1949年中华人民共和国的成立','1950年中共七届三中全会的召开','1951年西藏的和平解放','1952年土地改革的完成','C','Single4'),(167,8,'中共中央正式提出过渡时期总路线是在','1949年','1952年','1953年','1956年','C','Single4'),(168,8,'1955年，毛泽东发表全面总结农业合作化运动经验的报告是','《关于农业生产互助合作的决议(草案)》','《关于发展农业生产合作社的决议》','《关于农业合作化问题》','《关于人民公社若千问题的决议》','C','Single4'),(169,8,'1959年，在中共中央召开的庐山会议上受到错误批判的是','刘少奇','彭德怀','周恩来','邓小平','B','Single4'),(170,8,'1966年至1976年间在我国发生的全局性、长时间的“左”倾严重错误是','“大跃进”','人民公社运动','反右派斗争扩大化','“文化大革命”','D','Single4'),(171,8,'1962年1月，中共中央召开总结经验教训、明确工作方向的会议是','“七千人大会”','中共八届九中全会','第一次郑州会议','中共八届十中全会','A','Single4'),(172,8,'1951年底到1952年春，中国共产党在党政机构工作人员中开展了','肃反运动','整风、整党运动','“三反”运动','“五反”运动','C','Single4'),(173,8,'中国共产党在过渡时期总路线的主体是实现','国家的社会主义工业化','国家对农业的社会主义改造','国家对手工业的社会主义改造','国家对资本主义工商业的社会主义改造','A','Single4'),(174,8,'新中国开始实行发展国民经济的第一个五年计划是在','1950年','1951年','1952年','1953年','D','Single4'),(175,8,'中国进入社会主义社会的主要标志是','中华人民共和国的成立','过渡时期总路线的提出','第一届全国人民代表大会的召开','社会主义三大改造的完成','D','Single4'),(176,8,'1949年3月，中国共产党在西柏坡召开的重要会议是','中共六大','中共六届六中全会','中共七大','中共七届二中全会','D','Single4'),(177,8,'中华人民共和国的成立标志着中国进入','资本主义社会','社会主义初级阶段','新民主主义社会','社会主义中级阶段','C','Single4'),(178,8,'我国对资本主义工商业的社会主义改造所实行的政策是','无偿没收','有偿征用','公私合营','和平赎买','D','Single4'),(179,8,'毛泽东在1957年指出，我国国家改治生活的主题是正确处理','敌我矛盾','人民内部矛盾','生产关系与生产力的矛盾','上层建筑与经济基础的矛盾','B','Single4'),(180,8,'1947年，台湾人民举行了反对国民党黑暗统治的','黑旗军起义','抗暴运动','二二八起义','五二〇运动','C','Single4'),(181,8,'1949年4月21日，中国人民解放军发起的重大战役是','辽沈战役','淮海战役','平津战役','渡江战役','D','Single4'),(182,8,'1947年11月，在香港成立的中国民主党派是','中国民主同盟','中国国民党革命委员会','中国民主促进会','国农工民主党','B','Single4'),(183,8,'中国共产党为总结经验教训，明确工作方向召开的“七千人大会”是在','1958年','1959年','1962年','1963年','C','Single4'),(184,8,'我国对资本主义工商业进行社会主义改造的政策是','无偿没收','有偿征用','和平赎买','限制发展','C','Single4'),(185,8,'新中国发展国民经济的第一个五年计划规定，集中主要力量发展','重工业','轻工业','农业','交通运输业','A','Single4'),(186,9,'毛泽东在《论十大关系》中提出的中国社会主义建设的基本方针是','不要四面出击','调整、巩固、充实、提高','积极引导、稳步前进','调动一切积极因素为社会主义事业服务','D','Single4'),(187,9,'“文化大革命”的导火线是','《评新编历史剧<海润罢官>》的发表','上海“一月革命”夺权斗争','围困中南海事件','《炮打司令部————我的一张大字报》的发表','A','Single4'),(188,9,'“文化大革命”结束的标志是','\"一月风暴”的兴起','林彪反革命集团的覆灭','\"天安门事件”的爆发','江青反革命集团的垮台','D','Single4'),(189,9,'1964年，新中国取得重大科技成就是','第一颗原子弹试验成功','第一颗氢弹试验成功','第一台万吨水压机试制成','第一颗人造卫星发射成功','A','Single4'),(190,9,'1949年6月，毛泽东发表的系统论逋中国共产党建国主张的著作是','《新民主主义论》','《目前形势和我们的任务》','《论联合政府》','《论人民民主专政》','D','Single4'),(191,9,'1948年秋，中国人民解放军进行战略决战的第一个战役是','辽沈战役','淮海战役','平津战役','渡江战役','A','Single4'),(192,9,'1950年6月，中共七届三中全会确定的中心任务是','迅速消灭国民党残余势力','完成新解放区土地改革','统一全国财政经济','争取国家财政经济状况的基本好转','D','Single4'),(193,9,'新中国成立后，社会主义国营经济建立的主要途径是','没收帝国主义在华企业','没收官僚资本','没收民族资本','没收地主阶级的土地和财产','B','Single4'),(194,9,'1951年底到1952年春，中国共产党在党政机关中开展的“三反”运动是','反贪污、反浪费、反官僚主义','反主观主义、反宗派主义、反党八股','反贪污、反受贿、反自由主义','反浪费、反行贿、反形式主','A','Single4'),(195,9,'我国进入社会主义社会的最主要标志是','中华人民共和国的成立','发展国民经济第一个五年计划的制定','第一届全国人民代表大会的召开','社会主义改造的基本完成','D','Single4'),(196,9,'1956年，在中共八大上提出“三个主体，三个补充”思想的是','陈云','毛泽东','周恩来','邓小平','A','Single4'),(197,9,'新中国第一颗原子弹试验成功是在','1964年10月','1966年10月','1967年6月','1970年4月','A','Single4'),(198,9,'新中国恢复在联合国合法席位的时间是','1949年','1966年','1971年','1978年','C','Single4'),(199,10,'毛泽东指出，在社会主义改造完成后我国改治生活的主题是正确处理','生产关系与生产力之间的矛盾','上层建筑与经济基础之间的矛盾','敌我矛盾','人民内部矛盾','D','Single4'),(200,10,'中共中央通过《关于建国以来党的若干历史问题的决议》的会议是','十一届三中全会','十一届六中全会','十二届三中全会','十二届六中全会','B','Single4'),(201,10,'新中国第一颗人造地球卫星的成功发射是在','1964年10月','1966年10月','1967年4月','1970年4月','D','Single4'),(202,10,'1978年，我国开展的一场马克思主义思想解放运动是','揭批“四人帮”','关于真理标准问题的大讨论','平反冤假错案','关于社会主义市场经济问题的大讨论','D','Single4'),(203,10,'中国共产党将“三个代表”重要思想作为党的指导思想写入党章是在','中共十四大','中共十五大','中共十六大','中共十七大','C','Single4'),(204,10,'1971年10月，新中国在外交上取得的重大成果是','恢复了在联合国的合法席位','恢复了在世界卫生组织的合法席位','实现了中日关系正常化','实现了中法关系正常化','A','Single4'),(205,10,'20世纪70年代，毛泽东、周恩来抓住时机发起了改善中美关系的','“篮球外交”','“乒乓外交”','“网球外交”','“围棋外交”','B','Single4'),(206,10,'中国共产党第一次比较系统地阐述社会主义初级阶段理论是在','中共十二大','中共十三大','中共十四大','中共十五大','B','Single4'),(207,10,'1990年3月，中共十三届六中全会通过了','《关于科学技术体制改革的决定》','《关于教育体制改革的决定》','《关于加强党同人民群众联系的决定》','《关于加强党的执政能力建设的决定》','C','Single4'),(208,10,'1979年，邓小平在中央理论工作务虚会上首次明确提出，必须坚持','拨乱反正','四项基本原则','解放思想','以经济建设为中','B','Single4'),(209,10,'1988年，中共中央和国务院决定建立的经济特区是','珠海经济特区','汕头经济特区','厦门经济特区','海南经济特区','D','Single4'),(210,10,'中共十三大比较系统地阐述了','社会主义本质理论','社会主义市场经济理论','社会主义初级阶段理论','“三个有利于”标准的理论','C','Single4'),(211,10,'中国对香港恢复行使主权的时间是','1997年7月1日','1997年12月20日','1999年7月1日','1999年12月20日','A','Single4'),(212,10,'1995年，江泽民关于发展海峡两岸关系的重要讲话是','《告台湾同胞书》','《为促进祖国统一大业的完成而继续奋斗》','《一个国家，两种制度》','《实现两岸和平统一的九项方针》','B','Single4'),(213,11,'2004年9月，中共十六届四中全会提出的战略任务是','构建社会主义和谐社会','全面建设小康社会','建设社会主义新农村','建立社会主义市场经济体制潼','A','Single4'),(214,11,'中共十七大报告指出，我国社会主义现代化建设新时期最鲜明的特点是','与时俱进','快速发展','改革开放','以人为本','C','Single4'),(215,11,'中国加入世界贸易组织的时间是','1999年|2月','2000年12月','2001年12月','2002年12月','C','Single4'),(216,11,'中国共产党第一次完整地概括社会主义初级阶段基本路线的会议是','中共十三大','中共十四大','中共十五大','中共十六大','A','Single4'),(217,11,'中共十四大明确提出，我国经济体制改革的目标是建立','社会主义市场经济体制','市场为主、计划为辅的经济体制','社会主义计划经济体制','社会主义有计划的商品经济体制','A','Single4'),(218,11,'1998年，中共中央决定在县级以上党政领导班子和领导干部中深入开展','讲政治、讲经济、讲文化的教育','讲思想、讲作风、讲文明的教育','讲理想、讲觉悟、讲正气的教育','讲学习、讲政治、讲正气的教育','D','Single4'),(219,11,'2005年，我国通过《反分裂国家法》的会议是','十届全国人大二次会议','十届全国人大三次会议','十届全国人大四次会议','十届全国人大五次会议','B','Single4'),(220,11,'2005年3月，十届全国人大三次会议通过的法律是','《反分裂国家法》','《国家安全法》','《香港特别行政区基本法','《澳门特别行政区基本法》','A','Single4');

/*Table structure for table `bank_test` */

DROP TABLE IF EXISTS `bank_test`;

CREATE TABLE `bank_test` (
  `id` int NOT NULL,
  `chap` int DEFAULT NULL,
  `stem` varchar(256) DEFAULT NULL,
  `option_A` varchar(128) DEFAULT NULL,
  `option_B` varchar(128) DEFAULT NULL,
  `option_C` varchar(128) DEFAULT NULL,
  `option_D` varchar(128) DEFAULT NULL,
  `option_E` varchar(128) DEFAULT NULL,
  `answer` varchar(5) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `bank_test` */

insert  into `bank_test`(`id`,`chap`,`stem`,`option_A`,`option_B`,`option_C`,`option_D`,`option_E`,`answer`,`type`) values (1,1,'示例题干（4选项单选）','选项A','选项B','选项C','选项D',NULL,'A','Single4'),(2,1,'示例题干（5选项单选）','选项A','选项B','选项C','选项D','选项E','A','Single5'),(3,1,'示例题干（4选项多选）','选项A','选项B','选项C','选项D',NULL,'AB','Multiple4'),(4,1,'示例题干（5选项多选）','选项A','选项B','选项C','选项D','选项E','AB','Multiple5');

/*Table structure for table `banks` */

DROP TABLE IF EXISTS `banks`;

CREATE TABLE `banks` (
  `bank_name` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `CN` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`bank_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `banks` */

insert  into `banks`(`bank_name`,`CN`) values ('bank_modern_history','近代史'),('bank_test','测试题库');

/*Table structure for table `records` */

DROP TABLE IF EXISTS `records`;

CREATE TABLE `records` (
  `Uid` bigint NOT NULL,
  `time` datetime NOT NULL,
  `bank_name` varchar(64) DEFAULT NULL,
  `mode` varchar(3) DEFAULT NULL,
  `record` varchar(1024) DEFAULT NULL,
  `wrong_questions` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`Uid`,`time`),
  KEY `bank_name` (`bank_name`),
  CONSTRAINT `records_ibfk_1` FOREIGN KEY (`Uid`) REFERENCES `user` (`Uid`),
  CONSTRAINT `records_ibfk_2` FOREIGN KEY (`bank_name`) REFERENCES `banks` (`bank_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `records` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `Uid` bigint NOT NULL AUTO_INCREMENT,
  `stuID` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(16) DEFAULT NULL,
  `nickname` varchar(20) DEFAULT NULL,
  `invite_code` varchar(6) DEFAULT NULL,
  `inviter_code` varchar(6) DEFAULT NULL,
  `authority` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Uid`,`stuID`)
) ENGINE=InnoDB AUTO_INCREMENT=100007 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`Uid`,`stuID`,`password`,`nickname`,`invite_code`,`inviter_code`,`authority`) values (100000,'00000000','123456','Administrator','NJMU',NULL,'admin');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
