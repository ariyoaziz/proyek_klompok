-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Jan 2024 pada 16.20
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_peminjaman`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('c312e4d909d5');

-- --------------------------------------------------------

--
-- Struktur dari tabel `loan`
--

CREATE TABLE `loan` (
  `loan_id` bigint(20) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `jumlah_pinjaman` float NOT NULL,
  `jangka_waktu_peminjaman` int(11) NOT NULL,
  `tanggal_pinjaman` datetime DEFAULT NULL,
  `tanggal_jatuh_tempo` datetime NOT NULL,
  `status_pinjaman` varchar(50) NOT NULL,
  `bunga_pinjaman` float NOT NULL,
  `total_pembayaran` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `loan`
--

INSERT INTO `loan` (`loan_id`, `user_id`, `jumlah_pinjaman`, `jangka_waktu_peminjaman`, `tanggal_pinjaman`, `tanggal_jatuh_tempo`, `status_pinjaman`, `bunga_pinjaman`, `total_pembayaran`) VALUES
(1, 22666232, 5000, 12, '2024-01-01 14:08:30', '2024-01-13 21:08:30', 'Active', 5, 8000),
(2, 22666232, 5000, 12, '2024-01-01 14:20:46', '2024-01-13 21:20:46', 'Active', 5, 8000),
(3, 22666233, 5000, 12, '2024-01-01 14:20:51', '2024-01-13 21:20:51', 'Active', 5, 8000),
(4, 22666234, 50000000, 12, '2024-01-01 14:20:55', '2024-01-13 21:20:55', 'Aktif', 5, 80000000),
(6, 22666234, 50000000, 12, '2024-01-01 14:21:08', '2024-01-13 21:21:08', 'Aktif', 5, 80000000),
(7, 22666231, 75000000, 24, '2024-01-01 14:25:51', '2024-01-25 21:25:51', 'Lunas', 7.5, 210000000),
(8, 22666231, 75000000, 24, '2024-01-01 14:25:53', '2024-01-25 21:25:53', 'Lunas', 7.5, 210000000),
(9, 22666231, 75000000, 24, '2024-01-01 14:25:55', '2024-01-25 21:25:55', 'Lunas', 7.5, 210000000),
(10, 22666234, 50000000, 12, '2024-01-01 14:51:41', '2024-01-13 21:51:41', 'Aktif', 5, 80000000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `payment`
--

CREATE TABLE `payment` (
  `payment_id` bigint(20) NOT NULL,
  `loan_id` bigint(20) DEFAULT NULL,
  `jumlah_pengembalian` float NOT NULL,
  `tanggal_pengembalian` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `payment`
--

INSERT INTO `payment` (`payment_id`, `loan_id`, `jumlah_pengembalian`, `tanggal_pengembalian`) VALUES
(1, 1, 1000, '2024-01-01 22:08:28'),
(2, 1, 600000, '2024-01-01 22:19:43'),
(4, 1, 1000, '2024-01-01 22:16:55');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `name` varchar(230) NOT NULL,
  `email` varchar(120) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `update_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `name`, `email`, `phone`, `password`, `created_at`, `update_at`) VALUES
(22666231, 'Ariyo Aziz Pratama', 'ariyoaziz.pratama@gmail.com', '08533330000', 'ariyo123', '2023-12-20 21:03:31', '2023-12-20 21:03:31'),
(22666232, 'Agus Purwanto ', 'aguspurwanto@gmail.com', '082199991111', 'agus123', '2023-12-20 21:03:31', '2023-12-20 21:03:31'),
(22666233, 'Kurnia Rahman', 'kurniarahman@gmail.com', '085800001111', 'kurnia123', '2023-12-20 21:07:40', '2023-12-20 21:07:40'),
(22666234, 'Muhammad Gazali', 'muhammadgazali@gmail.com', '081266669999', 'gazali123', '2023-12-20 21:07:40', '2023-12-20 21:07:40'),
(22666236, 'contoh', 'contoh@gmail.com', '987654321', 'scrypt:32768:8:1$2PaksC5DWiKzEgDy$f13686ad74ab1adb89a14a7589a3c6693eec44eb4e73560eeb2a98f0d778b075f2a65d7c0a443799b33f5698c66af4', '2023-12-31 07:40:18', '2023-12-31 07:40:18');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indeks untuk tabel `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`loan_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indeks untuk tabel `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `loan_id` (`loan_id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `ix_user_email` (`email`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `loan`
--
ALTER TABLE `loan`
  MODIFY `loan_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT untuk tabel `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `loan`
--
ALTER TABLE `loan`
  ADD CONSTRAINT `loan_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Ketidakleluasaan untuk tabel `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`loan_id`) REFERENCES `loan` (`loan_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
