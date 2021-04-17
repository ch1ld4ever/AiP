-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Апр 17 2021 г., 11:12
-- Версия сервера: 8.0.22-0ubuntu0.20.04.2
-- Версия PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `soft0047_labrab`
--

-- --------------------------------------------------------

--
-- Структура таблицы `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `StudentName` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Rating` int NOT NULL,
  `Gender` tinyint(1) NOT NULL,
  `bday` date NOT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `students`
--

INSERT INTO `students` (`id`, `StudentName`, `Rating`, `Gender`, `bday`, `city`) VALUES
(46, 'Мишкин', 217, 1, '2002-08-23', 'Кунгур'),
(47, 'Бортич', 224, 0, '2002-06-03', 'Лысьва'),
(48, 'Деревянко', 182, 0, '2002-02-20', 'Оса'),
(49, 'Столбова', 194, 0, '2003-01-22', 'Кунгур'),
(50, 'Хомич', 205, 0, '2002-04-23', 'Кунгур'),
(51, 'Круглов', 191, 1, '2002-04-23', 'Березники'),
(52, 'Иванов', 192, 1, '2002-05-17', 'Кунгур'),
(53, 'Петров', 191, 1, '2002-11-25', 'Кунгур'),
(54, 'Сидоров', 196, 1, '2004-01-20', 'Кунгур'),
(55, 'Капустин', 196, 1, '2002-06-04', 'Кунгур'),
(56, 'Томатова', 201, 0, '2003-04-16', 'Кунгур'),
(57, 'Ежова', 214, 0, '2001-10-07', 'Лысьва'),
(58, 'Микова', 222, 0, '2001-10-07', 'Пермь'),
(59, 'Мамин', 199, 1, '2001-11-10', 'Пермь'),
(60, 'Комов', 195, 1, '2002-01-17', 'Пермь');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `students`
--
ALTER TABLE `students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
