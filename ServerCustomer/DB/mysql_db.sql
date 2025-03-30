-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th3 30, 2025 lúc 04:14 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `phongkhamptit`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `bacsi`
--

CREATE TABLE `bacsi` (
  `id` int(11) NOT NULL,
  `ten` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `chuyenmon` varchar(255) NOT NULL,
  `hocvan` varchar(100) NOT NULL,
  `kinhnghiem` varchar(100) NOT NULL,
  `img` varchar(250) NOT NULL,
  `phongID` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `bacsi`
--

INSERT INTO `bacsi` (`id`, `ten`, `dob`, `chuyenmon`, `hocvan`, `kinhnghiem`, `img`, `phongID`, `username`, `password`) VALUES
(1, 'Ngọ Văn Trọng', '2003-07-16', 'Chuẩn đoán não bộ', 'Bác Sĩ Chuyên Khoa I', '2 năm làm việc tại Bệnh Viện Bạch Mai', 'http://192.168.43.20:5000/static/bacsi/2.jpg', 1, 'ngovantrong1607', '123'),
(2, 'Bùi Anh Tú', '2003-08-13', 'Bệnh não', 'Thủ Khoa Tốt Nghiệp Đại Học Y Hà Nội Năm 2025. ', '3 năm làm khám não tại bệnh viện Việt Đức', 'http://192.168.43.20:5000/static/bacsi/1.jpg', 1, 'anhtu', '123'),
(3, 'Cam Hải Đăng', '2003-07-16', 'Bệnh Phổi', 'Bác sĩ nội trú Y Thái Nguyên', '4 Năm làm việc tại bệnh viên 108 trong điều trị bệnh phổi', 'http://192.168.43.20:5000/static/bacsi/3.jpg', 2, 'haidang', '123'),
(4, 'Trương Vĩnh Tiến', '2003-04-16', 'Điều trị tim mạch', 'Á khoa đầu ra,tốt nghiệp bằng xuất sắc đại học Y Hà Nội', '3 năm làm việc tại bệnh viện trung ương quân đội 108', 'http://192.168.43.20:5000/static/bacsi/4.jpg', 3, 'vinhtien', '123');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `benhnhan`
--

CREATE TABLE `benhnhan` (
  `id` int(11) NOT NULL,
  `ten` varchar(255) NOT NULL,
  `sdt` varchar(15) NOT NULL,
  `quequan` varchar(255) NOT NULL,
  `cccd` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `img` varchar(250) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `benhnhan`
--

INSERT INTO `benhnhan` (`id`, `ten`, `sdt`, `quequan`, `cccd`, `dob`, `img`, `username`, `password`) VALUES
(1, 'Nguyễn Hoàng Hải', '0904708498', 'Hàm Rồng', '03820302253', '2025-03-01', 'http://192.168.43.20:5000/static/uploads/55a5dd25-e263-46e3-b9b2-0a5d29db8535_photo_1740151322518.jpg', 'hai123', '1234567'),
(2, 'Nguyễn Huynh', '0903456789', 'Quảng Xương', '123455778', '2003-03-12', 'http://192.168.43.20:5000/static/uploads/ccd95960-05c7-4357-af69-92b71ce7f934_photo_1740151178266.jpg', 'huynhngao', '123'),
(4, 'Trọng', '0904708498', 'ttt', '03820302252', '2003-07-15', 'http://192.168.43.20:5000/static/uploads/d690230e-c943-4842-a604-dbbe1b896d6a_photo_1740148399260.jpg', 'trong', '123'),
(5, 'Ngọ Văn Trọng', '0352987324', 'Thăng Bình', '012345678912', '2003-07-16', 'http://192.168.43.20:5000/static/uploads/36c14809-9703-460b-ba3e-8a27f1f78910_photo_1740147525501.jpg', 'vantrong', '123'),
(6, 'Phạm Thị Nga', '0352987324', 'Ngọ Hạ, Thăng Bình', '123456781234', '1972-10-10', 'http://192.168.43.20:5000/static/uploads/45792f93-293a-4682-bf14-a1bda5872357_photo_1740151316390.jpg', 'nga', '123456'),
(7, 'Ngọ Thứ', '0904708498', 'Nhà 22 thôn ngọ hạ', '987654321234', '2025-01-01', 'http://192.168.43.20:5000/static/uploads/577ee7db-31d7-4c79-b4da-16f46a03221e_IMG_20220529_002041.jpg', 'Thu', '123');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietdonthuoc`
--

CREATE TABLE `chitietdonthuoc` (
  `id` int(11) NOT NULL,
  `donthuocID` int(11) DEFAULT NULL,
  `thuocID` int(11) DEFAULT NULL,
  `soluong` int(11) DEFAULT NULL,
  `gia` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `chitietdonthuoc`
--

INSERT INTO `chitietdonthuoc` (`id`, `donthuocID`, `thuocID`, `soluong`, `gia`) VALUES
(1, 1, 1, 2, 100000),
(2, 1, 2, 2, 50000),
(3, 2, 1, 3, 100000),
(4, 2, 2, 3, 50000),
(5, 3, 1, 3, 100000),
(6, 3, 2, 1, 50000),
(7, 4, 2, 3, 50000),
(8, 4, 1, 3, 100000),
(9, 5, 1, 3, 100000),
(10, 5, 2, 1, 50000),
(11, 6, 3, 3, 200000),
(12, 6, 4, 1, 50000),
(13, 6, 1, 1, 100000),
(14, 6, 2, 1, 50000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `donthuoc`
--

CREATE TABLE `donthuoc` (
  `ID` int(11) NOT NULL,
  `ngaymua` datetime DEFAULT NULL,
  `benhnhanID` int(11) DEFAULT NULL,
  `bacsiID` int(11) DEFAULT NULL,
  `tonggia` float DEFAULT NULL,
  `mota` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `donthuoc`
--

INSERT INTO `donthuoc` (`ID`, `ngaymua`, `benhnhanID`, `bacsiID`, `tonggia`, `mota`) VALUES
(1, '2025-03-23 00:00:00', 1, 1, 300000, 'nhớ uống mạnh lên'),
(2, '2025-03-23 00:00:00', 1, 1, 450000, 'uống cho bớt ngáo'),
(3, '2025-03-23 00:00:00', 2, 1, 350000, 'uống nhiều là ngáo'),
(4, '2025-03-28 00:00:00', 2, 1, 450000, 'uống ít thôi'),
(5, '2025-03-29 00:00:00', 1, 1, 350000, 'chơi game ít thôi uống thuốc nhiều lên'),
(6, '2025-03-29 00:00:00', 1, 1, 800000, 'uống nhiều lên nhá');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lichhen`
--

CREATE TABLE `lichhen` (
  `ID` int(11) NOT NULL,
  `bacsiID` int(11) NOT NULL,
  `benhnhanID` int(11) NOT NULL,
  `thoigianhen` datetime NOT NULL,
  `ghichu` varchar(100) DEFAULT NULL,
  `trangthai` varchar(100) NOT NULL DEFAULT 'Chưa duyệt'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `lichhen`
--

INSERT INTO `lichhen` (`ID`, `bacsiID`, `benhnhanID`, `thoigianhen`, `ghichu`, `trangthai`) VALUES
(1, 1, 1, '2025-03-22 02:52:20', 'khẩn cấp', 'Đã duyệt'),
(2, 1, 2, '2025-03-22 02:52:20', 'nhanh nhá', 'Đã duyệt'),
(3, 1, 6, '2025-03-29 09:53:00', 'vui lòng khám gấp nhé', 'Đã duyệt'),
(4, 2, 4, '2025-03-30 16:01:00', 'đau đầu quá, cần khám gấp!', 'Chưa duyệt');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieukham`
--

CREATE TABLE `phieukham` (
  `id` int(11) NOT NULL,
  `trieuchung` text DEFAULT NULL,
  `chandoan` text NOT NULL,
  `thongsoxetnghiem` text DEFAULT NULL,
  `anhxetnghiem` varchar(255) DEFAULT NULL,
  `ngaykham` datetime NOT NULL,
  `benhnhanID` int(11) NOT NULL,
  `bacsiID` int(11) NOT NULL,
  `tienkham` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phieukham`
--

INSERT INTO `phieukham` (`id`, `trieuchung`, `chandoan`, `thongsoxetnghiem`, `anhxetnghiem`, `ngaykham`, `benhnhanID`, `bacsiID`, `tienkham`) VALUES
(1, 'oke', 'oke', 'oke', 'oke', '2025-03-22 00:00:00', 1, 1, 100000),
(2, 't', 't', 'tt', 't', '2025-03-22 00:00:00', 1, 1, 200),
(3, 'hhh', 'hhh', 'hhh', 'hhh', '2025-03-22 00:00:00', 1, 1, 300),
(4, 'h', 'h', 'h', 'h', '2025-03-22 00:00:00', 2, 1, 400),
(5, 'Không', 'Huyết áp cao', 'Huyết áp:180/180', 'Không', '2025-03-22 00:00:00', 2, 1, 100000),
(6, 'Sốt', 'Sốt virus', 'nhiệt độ cao: 40 độ C', 'không', '2025-03-23 00:00:00', 1, 1, 50000),
(7, 'Đau mỏi vai gáy', 'Hạ đường huyết', 'Đường huyết giảm', 'C:\\fakepath\\194170344_2592925137669395_2318511476495343916_n.jpg', '2025-03-23 00:00:00', 1, 1, 1000000),
(8, 'Đau mỏi vai gáy', 'Hạ đường huyết', 'Đường huyết giảm', 'C:\\fakepath\\Tr-gl_0015.jpg', '2025-03-23 00:00:00', 1, 1, 1000000),
(9, 'Đau bụng', 'Đau ruột thừa', 'Thiếu máu các chi', 'C:\\fakepath\\Tr-gl_0015.jpg', '2025-03-23 00:00:00', 1, 1, 5000000),
(10, 'Đau bụng', 'U thần kinh đệm', 'Thoát vị đĩa đệm', 'C:\\fakepath\\Tr-gl_0015.jpg', '2025-03-23 00:00:00', 1, 1, 2000000),
(11, 'Đau bụng', 'U màng não', 'Đường huyết giảm', 'C:\\fakepath\\8a.jpg', '2025-03-23 00:00:00', 1, 1, 5000000),
(12, 'Không', 'huyết áp thấp', 'Huyết áp : 160/180', '', '2025-03-23 00:00:00', 1, 1, 50000),
(13, 'oke', 'Sốt virus', 'oke', '', '2025-03-23 00:00:00', 2, 1, 400),
(14, 'Đau đầu', 'U thần kinh đệm', 'Chỉ số máu: xấu', 'C:\\fakepath\\Tr-gl_0020.jpg', '2025-03-23 00:00:00', 1, 1, 500000),
(15, 'Không', 'h', 'oke', '', '2025-03-23 00:00:00', 1, 1, 400),
(16, 'Không', 'oke', 'oke', '', '2025-03-23 00:00:00', 2, 1, 100000),
(17, 'Không', 'oke', 'oke', '', '2025-03-23 00:00:00', 2, 1, 100000),
(18, 'ngáo', 'oke', 'oke', '', '2025-03-23 00:00:00', 2, 1, 100000),
(19, 'hâm', 'hâm', 'hâm', '', '2025-03-23 00:00:00', 1, 1, 500000),
(20, 'hâm', 'hâm', 'hâm', '', '2025-03-23 00:00:00', 1, 1, 500000),
(21, 'ngáo', 'ngáo', 'ngáo', '', '2025-03-23 00:00:00', 1, 1, 100000),
(22, 'ngáo', 'U thần kinh đệm', 'ngáo đét', 'C:\\fakepath\\Tr-gl_0020.jpg', '2025-03-23 00:00:00', 2, 1, 500000),
(23, 'oke', 'oke', 'oke', NULL, '2025-03-27 00:00:00', 1, 1, 300000),
(24, 'Ho, đau đầu, nôn mửa', 'ung thư', '- Máu: 100/ml\n- Nồng độ cồn:100...\n- Huyết áp: 180/180', NULL, '2025-03-28 00:00:00', 1, 1, 300000),
(25, 'ho', 'mỡ máu', 'choles', NULL, '2025-03-28 00:00:00', 2, 1, 300000),
(26, 'no', 'hâm', 'no', NULL, '2025-03-28 00:00:00', 1, 1, 300000),
(27, 'no', 'hâm', 'no', NULL, '2025-03-28 00:00:00', 1, 1, 300000),
(28, 'hâm', 'ngáo', 'ngáo', NULL, '2025-03-28 00:00:00', 2, 1, 300000),
(29, 'đau đầu dai dẳng', 'do chơi game nhiều', 'huyết áp 1000/180', NULL, '2025-03-29 00:00:00', 1, 1, 300000),
(30, 'đau tim', 'nhồi máu cơ tim', 'nhịp tim: 230km/h', NULL, '2025-03-29 00:00:00', 1, 1, 300000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phongchucnang`
--

CREATE TABLE `phongchucnang` (
  `ID` int(11) NOT NULL,
  `chucNang` varchar(255) DEFAULT NULL,
  `moTa` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `phongchucnang`
--

INSERT INTO `phongchucnang` (`ID`, `chucNang`, `moTa`) VALUES
(1, 'Phòng Khám Não Bộ', 'Các bác sĩ khám não bộ hàng đầu VN'),
(2, 'Phòng khám phổi', 'hàng đầu VN'),
(3, 'Phòng khám Tim mạch', 'hàng đầu châu á');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `thuoc`
--

CREATE TABLE `thuoc` (
  `id` int(11) NOT NULL,
  `ten` varchar(255) DEFAULT NULL,
  `mota` text DEFAULT NULL,
  `nsx` date DEFAULT NULL,
  `hsd` date DEFAULT NULL,
  `dongia` float DEFAULT NULL,
  `img` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `thuoc`
--

INSERT INTO `thuoc` (`id`, `ten`, `mota`, `nsx`, `hsd`, `dongia`, `img`) VALUES
(1, 'Hoạt huyết nhất nhất', 'điều trị huyết áp thấp', '2025-03-01', '2025-03-15', 100000, 'http://192.168.43.20:5000/static/thuoc/1.jpg'),
(2, 'Hoạt huyết dưỡng não', 'trị thiếu máu não', '2024-12-31', '2025-03-15', 50000, 'http://192.168.43.20:5000/static/thuoc/2.jpg'),
(3, 'Bổ phế nam hà', 'Trị ho, bổ phổi', '2025-03-01', '2025-09-25', 200000, 'http://192.168.43.20:5000/static/thuoc/5.jpg'),
(4, 'Thuốc ho Bảo Thanh', 'Trị rát họng ho có đờm', '2022-03-01', '2025-03-01', 50000, 'http://192.168.43.20:5000/static/thuoc/6.jpg'),
(5, 'Ích tâm khang', 'thuốc bổ tim', '2024-03-01', '2025-03-01', 120000, 'http://192.168.43.20:5000/static/thuoc/4.jpg'),
(6, 'Bổ não thông huyết', 'tăng cường máu lên não', '2023-03-09', '2025-03-21', 180000, 'http://192.168.43.20:5000/static/thuoc/3.jpg');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `bacsi`
--
ALTER TABLE `bacsi`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `phongID` (`phongID`);

--
-- Chỉ mục cho bảng `benhnhan`
--
ALTER TABLE `benhnhan`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `cccd` (`cccd`);

--
-- Chỉ mục cho bảng `chitietdonthuoc`
--
ALTER TABLE `chitietdonthuoc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `donthuocID` (`donthuocID`),
  ADD KEY `thuocID` (`thuocID`);

--
-- Chỉ mục cho bảng `donthuoc`
--
ALTER TABLE `donthuoc`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `benhnhanID` (`benhnhanID`),
  ADD KEY `bacsiID` (`bacsiID`);

--
-- Chỉ mục cho bảng `lichhen`
--
ALTER TABLE `lichhen`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `bacsiID` (`bacsiID`),
  ADD KEY `benhnhanID` (`benhnhanID`);

--
-- Chỉ mục cho bảng `phieukham`
--
ALTER TABLE `phieukham`
  ADD PRIMARY KEY (`id`),
  ADD KEY `benhnhanID` (`benhnhanID`),
  ADD KEY `bacsiID` (`bacsiID`);

--
-- Chỉ mục cho bảng `phongchucnang`
--
ALTER TABLE `phongchucnang`
  ADD PRIMARY KEY (`ID`);

--
-- Chỉ mục cho bảng `thuoc`
--
ALTER TABLE `thuoc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `bacsi`
--
ALTER TABLE `bacsi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `benhnhan`
--
ALTER TABLE `benhnhan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `chitietdonthuoc`
--
ALTER TABLE `chitietdonthuoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT cho bảng `donthuoc`
--
ALTER TABLE `donthuoc`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `lichhen`
--
ALTER TABLE `lichhen`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT cho bảng `phieukham`
--
ALTER TABLE `phieukham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT cho bảng `phongchucnang`
--
ALTER TABLE `phongchucnang`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `thuoc`
--
ALTER TABLE `thuoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `bacsi`
--
ALTER TABLE `bacsi`
  ADD CONSTRAINT `bacsi_ibfk_1` FOREIGN KEY (`phongID`) REFERENCES `phongchucnang` (`ID`);

--
-- Các ràng buộc cho bảng `chitietdonthuoc`
--
ALTER TABLE `chitietdonthuoc`
  ADD CONSTRAINT `chitietdonthuoc_ibfk_1` FOREIGN KEY (`donthuocID`) REFERENCES `donthuoc` (`ID`),
  ADD CONSTRAINT `chitietdonthuoc_ibfk_2` FOREIGN KEY (`thuocID`) REFERENCES `thuoc` (`id`);

--
-- Các ràng buộc cho bảng `donthuoc`
--
ALTER TABLE `donthuoc`
  ADD CONSTRAINT `donthuoc_ibfk_1` FOREIGN KEY (`benhnhanID`) REFERENCES `benhnhan` (`id`),
  ADD CONSTRAINT `donthuoc_ibfk_2` FOREIGN KEY (`bacsiID`) REFERENCES `bacsi` (`id`);

--
-- Các ràng buộc cho bảng `lichhen`
--
ALTER TABLE `lichhen`
  ADD CONSTRAINT `lichhen_ibfk_1` FOREIGN KEY (`bacsiID`) REFERENCES `bacsi` (`id`),
  ADD CONSTRAINT `lichhen_ibfk_2` FOREIGN KEY (`benhnhanID`) REFERENCES `benhnhan` (`id`);

--
-- Các ràng buộc cho bảng `phieukham`
--
ALTER TABLE `phieukham`
  ADD CONSTRAINT `phieukham_ibfk_1` FOREIGN KEY (`benhnhanID`) REFERENCES `benhnhan` (`id`),
  ADD CONSTRAINT `phieukham_ibfk_2` FOREIGN KEY (`bacsiID`) REFERENCES `bacsi` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
