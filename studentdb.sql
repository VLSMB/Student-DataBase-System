/*
 Navicat MySQL Data Transfer

 Source Server         : VLSMB
 Source Server Type    : MySQL
 Source Server Version : 50735
 Source Host           : localhost:3306
 Source Schema         : studentdb

 Target Server Type    : MySQL
 Target Server Version : 50735
 File Encoding         : 65001

 Date: 08/02/2022 23:05:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `userName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `userPwd` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`userPwd`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('VLSMB', 'VLSMB');
INSERT INTO `admin` VALUES ('admin', 'admin');
INSERT INTO `admin` VALUES ('test', '1234');
INSERT INTO `admin` VALUES ('Har', 'monia');
INSERT INTO `admin` VALUES ('Rei', 'Shiona');
INSERT INTO `admin` VALUES ('v', 'L');

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `classID` int(11) NOT NULL,
  `gradeID` int(11) NOT NULL,
  `className` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`classID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (1, 1, '高一一班');
INSERT INTO `class` VALUES (2, 1, '高一二班');
INSERT INTO `class` VALUES (15, 2, '高二十五班');
INSERT INTO `class` VALUES (28, 3, '高三二十八班');
INSERT INTO `class` VALUES (90, 5, 'KEY班');
INSERT INTO `class` VALUES (12, 4, '高四十二班');

-- ----------------------------
-- Table structure for examkinds
-- ----------------------------
DROP TABLE IF EXISTS `examkinds`;
CREATE TABLE `examkinds`  (
  `kindID` int(11) NOT NULL,
  `kindName` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`kindID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of examkinds
-- ----------------------------
INSERT INTO `examkinds` VALUES (1, '第一次月考');
INSERT INTO `examkinds` VALUES (2, '期中考试');
INSERT INTO `examkinds` VALUES (3, '期末考试A');
INSERT INTO `examkinds` VALUES (4, '八省联考');

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `gradeID` int(11) NOT NULL,
  `gradeName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`gradeID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES (1, '高一');
INSERT INTO `grade` VALUES (2, '高二');
INSERT INTO `grade` VALUES (3, '高三');
INSERT INTO `grade` VALUES (4, '高四');
INSERT INTO `grade` VALUES (5, 'KEY年');

-- ----------------------------
-- Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS `result`;
CREATE TABLE `result`  (
  `ID` int(11) NOT NULL,
  `stuID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `kindID` int(11) NOT NULL,
  `subID` int(11) NOT NULL,
  `result` double NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of result
-- ----------------------------
INSERT INTO `result` VALUES (1, 'KEY01001', 4, 1, 119);
INSERT INTO `result` VALUES (3, 'KEY02002', 1, 1, 88);
INSERT INTO `result` VALUES (24, 'KEY02001', 2, 4, 150);
INSERT INTO `result` VALUES (6, 'KEY01002', 3, 2, 105.25);
INSERT INTO `result` VALUES (7, 'HH00000', 1, 1, 90.65);
INSERT INTO `result` VALUES (2, 'KEY02001', 2, 4, 94.65);
INSERT INTO `result` VALUES (4, 'KEY03001', 2, 2, 97.3);
INSERT INTO `result` VALUES (8, 'HH00001', 1, 1, 90.65);
INSERT INTO `result` VALUES (9, 'KEY01001', 1, 1, 90.65);
INSERT INTO `result` VALUES (10, 'KEY02001', 2, 1, 94.65);
INSERT INTO `result` VALUES (11, 'KEY02002', 1, 1, 88);
INSERT INTO `result` VALUES (12, 'KEY03001', 4, 2, 97.3);
INSERT INTO `result` VALUES (26, 'HH00001', 1, 2, 150);
INSERT INTO `result` VALUES (14, 'KEY01002', 3, 5, 105.25);
INSERT INTO `result` VALUES (15, 'HH00000', 1, 1, 90.65);
INSERT INTO `result` VALUES (16, 'HH00001', 1, 1, 90.65);
INSERT INTO `result` VALUES (17, 'KEY01001', 1, 1, 90.65);
INSERT INTO `result` VALUES (18, 'KEY02001', 2, 1, 94.65);
INSERT INTO `result` VALUES (19, 'KEY02002', 1, 1, 88);
INSERT INTO `result` VALUES (20, 'KEY03001', 4, 2, 97.3);
INSERT INTO `result` VALUES (22, 'KEY01002', 3, 5, 105.25);
INSERT INTO `result` VALUES (23, 'HH00000', 1, 1, 90.65);
INSERT INTO `result` VALUES (25, 'KEY01002', 3, 2, 100.25);
INSERT INTO `result` VALUES (27, 'HH00001', 3, 2, 0);
INSERT INTO `result` VALUES (28, 'KEY02001', 2, 5, 150);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stuID` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stuName` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `classID` int(11) NOT NULL,
  `gradeID` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `sex` char(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`stuID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('KEY01001', '神尾观铃', 90, 5, 16, '女', '1008611', 'AIR小镇');
INSERT INTO `student` VALUES ('KEY02001', '汐奈', 1, 1, 256, '女', '1008611', 'Harmonia小镇');
INSERT INTO `student` VALUES ('KEY02002', '黎', 2, 1, 16, '男', '1008611', 'Harmonia小镇');
INSERT INTO `student` VALUES ('KEY03001', '枣恭介', 12, 4, 17, '男', '1008611', '神北私立高等中学');
INSERT INTO `student` VALUES ('KEY03009', '直枝理树', 90, 5, 16, '男', '1008611', '神北私立高等中学');
INSERT INTO `student` VALUES ('KEY01002', '国崎往人', 90, 5, 20, '男', '1008611', 'AIR小镇');
INSERT INTO `student` VALUES ('HH00000', 'VLSMB', 90, 5, 17, '女', '1008611', '地球');
INSERT INTO `student` VALUES ('HH00001', '贴吧楼主', 28, 3, 10, '男', '1008611', '火星');
INSERT INTO `student` VALUES ('HH05001', '？？？', 15, 2, 18, '男', '1000111', '金星');

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject`  (
  `subID` int(11) NOT NULL,
  `subName` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`subID`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of subject
-- ----------------------------
INSERT INTO `subject` VALUES (1, '语文');
INSERT INTO `subject` VALUES (2, '理科数学');
INSERT INTO `subject` VALUES (3, '英语');
INSERT INTO `subject` VALUES (4, '物理');
INSERT INTO `subject` VALUES (5, '信息技术');

SET FOREIGN_KEY_CHECKS = 1;
