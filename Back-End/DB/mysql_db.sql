CREATE DATABASE phongkhamptit;
USE phongkhamptit;

CREATE TABLE PhongChucNang (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    chucNang VARCHAR(255),
    moTa TEXT
);

CREATE TABLE BacSi (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ten VARCHAR(255),
    sdt VARCHAR(15),
    chucvu VARCHAR(255),
    phongID INT,
    FOREIGN KEY (phongID) REFERENCES PhongChucNang(ID)
);

CREATE TABLE BenhNhan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ten VARCHAR(255),
    sdt VARCHAR(15),
    quequan VARCHAR(255),
    cccd VARCHAR(20) UNIQUE
);

CREATE TABLE LichHen (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    bacsiID INT,
    benhnhanID INT,
    thoigianhen DATETIME,
    FOREIGN KEY (bacsiID) REFERENCES BacSi(ID),
    FOREIGN KEY (benhnhanID) REFERENCES BenhNhan(id)
);

CREATE TABLE PhieuKham (
    id INT PRIMARY KEY AUTO_INCREMENT,
    trieuchung TEXT,
    chuandoan TEXT,
    thongsoxetnghiem TEXT,
    ngaykham DATETIME,
    sohuthu INT,
    benhnhanID INT,
    bacsiID INT,
    tienkham FLOAT,
    FOREIGN KEY (benhnhanID) REFERENCES BenhNhan(id),
    FOREIGN KEY (bacsiID) REFERENCES BacSi(ID)
);

CREATE TABLE Thuoc (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ten VARCHAR(255),
    mota TEXT,
    nsx DATE,
    hsd DATE,
    dongia FLOAT
);

CREATE TABLE DonThuoc (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    ngaymua DATETIME,
    benhnhanID INT,
    bacsiID INT,
    tonggia FLOAT,
    FOREIGN KEY (benhnhanID) REFERENCES BenhNhan(id),
    FOREIGN KEY (bacsiID) REFERENCES BacSi(ID)
);

CREATE TABLE ChiTietDonThuoc (
    id INT PRIMARY KEY AUTO_INCREMENT,
    donthuocID INT,
    thuocID INT,
    soluong INT,
    gia FLOAT,
    FOREIGN KEY (donthuocID) REFERENCES DonThuoc(ID),
    FOREIGN KEY (thuocID) REFERENCES Thuoc(id)
);
