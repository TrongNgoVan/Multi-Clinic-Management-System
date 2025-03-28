-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th3 20, 2025 lúc 03:08 AM
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
  `img` varchar(100) NOT NULL,
  `phongID` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `bacsi`
--

INSERT INTO `bacsi` (`id`, `ten`, `dob`, `chuyenmon`, `hocvan`, `kinhnghiem`, `img`, `phongID`, `username`, `password`) VALUES
(1, 'Ngọ Văn Trọng', '2003-07-16', 'Chuẩn đoán não bộ', 'Bác Sĩ Chuyên Khoa I', '2 năm làm việc tại Bệnh Viện Bạch Mai', 'chưa có', 1, 'ngovantrong1607', '123');

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
  `img` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lichhen`
--

CREATE TABLE `lichhen` (
  `ID` int(11) NOT NULL,
  `bacsiID` int(11) NOT NULL,
  `benhnhanID` int(11) NOT NULL,
  `thoigianhen` datetime NOT NULL,
  `trangthai` varchar(100) NOT NULL DEFAULT 'Chưa duyệt'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieukham`
--

CREATE TABLE `phieukham` (
  `id` int(11) NOT NULL,
  `trieuchung` text DEFAULT NULL,
  `chuandoan` text NOT NULL,
  `thongsoxetnghiem` text DEFAULT NULL,
  `anhxetnghiem` varchar(255) DEFAULT NULL,
  `ngaykham` datetime NOT NULL,
  `benhnhanID` int(11) NOT NULL,
  `bacsiID` int(11) NOT NULL,
  `tienkham` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(1, 'Phòng Khám Não Bộ', 'Các bác sĩ khám não bộ hàng đầu VN');

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
  `dongia` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `benhnhan`
--
ALTER TABLE `benhnhan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `chitietdonthuoc`
--
ALTER TABLE `chitietdonthuoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `donthuoc`
--
ALTER TABLE `donthuoc`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `lichhen`
--
ALTER TABLE `lichhen`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `phieukham`
--
ALTER TABLE `phieukham`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `phongchucnang`
--
ALTER TABLE `phongchucnang`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `thuoc`
--
ALTER TABLE `thuoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
  ADD CONSTRAINT `donthuoc_ibfk_2` FOREIGN KEY (`bacsiID`) REFERENCES `bacsi` (`ID`);

--
-- Các ràng buộc cho bảng `lichhen`
--
ALTER TABLE `lichhen`
  ADD CONSTRAINT `lichhen_ibfk_1` FOREIGN KEY (`bacsiID`) REFERENCES `bacsi` (`ID`),
  ADD CONSTRAINT `lichhen_ibfk_2` FOREIGN KEY (`benhnhanID`) REFERENCES `benhnhan` (`id`);

--
-- Các ràng buộc cho bảng `phieukham`
--
ALTER TABLE `phieukham`
  ADD CONSTRAINT `phieukham_ibfk_1` FOREIGN KEY (`benhnhanID`) REFERENCES `benhnhan` (`id`),
  ADD CONSTRAINT `phieukham_ibfk_2` FOREIGN KEY (`bacsiID`) REFERENCES `bacsi` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
