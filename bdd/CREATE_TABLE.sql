-- phpMyAdmin SQL Dump
-- version 4.0.8
-- http://www.phpmyadmin.net
--
-- Client: mysql.imerir.com
-- Généré le: Ven 13 Novembre 2015 à 11:08
-- Version du serveur: 5.1.73
-- Version de PHP: 5.3.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `parcevaux3a05`
--

-- --------------------------------------------------------

--
-- Structure de la table `BELBIN`
--

CREATE TABLE IF NOT EXISTS `BELBIN` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Contenu de la table `BELBIN`
--

INSERT INTO `BELBIN` (`id`, `name`) VALUES
(1, 'Organisateur'),
(2, 'Président'),
(3, 'Faiseur'),
(4, 'Créatif'),
(5, 'Eclaireur'),
(6, 'Evaluateur'),
(7, 'Coéquipier'),
(8, 'Finisseur');

-- --------------------------------------------------------

--
-- Structure de la table `GROUP`
--

CREATE TABLE IF NOT EXISTS `GROUP` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;


-- --------------------------------------------------------

--
-- Structure de la table `PROJECT`
--

CREATE TABLE IF NOT EXISTS `PROJECT` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Contenu de la table `PROJECT`
--

INSERT INTO `PROJECT` (`id`, `name`) VALUES
(1, 'Management');

-- --------------------------------------------------------

--
-- Structure de la table `SKILL`
--

CREATE TABLE IF NOT EXISTS `SKILL` (
  `id_skill` int(11) NOT NULL AUTO_INCREMENT,
  `name_skill` text NOT NULL,
  PRIMARY KEY (`id_skill`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Contenu de la table `SKILL`
--

INSERT INTO `SKILL` (`id_skill`, `name_skill`) VALUES
(1, 'Web'),
(2, 'BDD'),
(3, 'Programmation'),
(4, 'Métier'),
(5, 'Marketing');

-- --------------------------------------------------------

--
-- Structure de la table `UNCOMPATIBILITY`
--

CREATE TABLE IF NOT EXISTS `UNCOMPATIBILITY` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_id_uncompatibility` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `id_2` (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=9 ;


-- --------------------------------------------------------

--
-- Structure de la table `USER`
--

CREATE TABLE IF NOT EXISTS `USER` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` text COLLATE latin1_general_ci NOT NULL,
  `nickname` text COLLATE latin1_general_ci NOT NULL,
  `mail` text COLLATE latin1_general_ci NOT NULL,
  `password` text COLLATE latin1_general_ci NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=10 ;



-- --------------------------------------------------------

--
-- Structure de la table `USER_BELBIN`
--

CREATE TABLE IF NOT EXISTS `USER_BELBIN` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `belbin_id` int(11) NOT NULL,
  `value` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 COLLATE=latin1_general_ci AUTO_INCREMENT=16 ;


-- --------------------------------------------------------

--
-- Structure de la table `USER_GROUP`
--

CREATE TABLE IF NOT EXISTS `USER_GROUP` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;



-- --------------------------------------------------------

--
-- Structure de la table `USER_SKILL`
--

CREATE TABLE IF NOT EXISTS `USER_SKILL` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `skill_id` int(11) NOT NULL,
  `value` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;



/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
