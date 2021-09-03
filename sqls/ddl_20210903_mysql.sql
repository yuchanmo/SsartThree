-- SQLINES DEMO *** sktop version to convert large SQL scripts,
-- SQLINES DEMO *** ny issues with Online conversion.

-- SQLINES DEMO *** act us at support@sqlines.com/****** Object:  Table [dbo].[art_info_source]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE art_info_source(
	`art_info_source_id` int AUTO_INCREMENT NOT NULL,
	`art_source` nvarchar(100) NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_art_info_source` PRIMARY KEY 
(
	`art_info_source_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[art_infos]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE art_infos(
	`art_info_id` int AUTO_INCREMENT NOT NULL,
	`artist_id` int NULL,
	`art_info_source_id` int NULL,
	`make_year` date NULL,
	`title_kor` nvarchar(200) NULL,
	`title_eng` nvarchar(200) NULL,
	`unit_cd` nchar(10) NULL,
	`size_length` Double NULL,
	`size_height` Double NULL,
	`mix_cd` nchar(10) NULL,
	`mix_size` nchar(10) NULL,
	`canvas` nvarchar(50) NULL,
	`medium_eng` nvarchar(50) NULL,
	`medium_kor` nvarchar(50) NULL,
	`description` nvarchar(300) NULL,
	`edition` nvarchar(300) NULL,
	`image_name` nvarchar(300) NULL,
	`creat_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_art_info` PRIMARY KEY 
(
	`art_info_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[artist_search_logs]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE artist_search_logs(
	`artist_search_log_id` int AUTO_INCREMENT NOT NULL,
	`artist_id` int NULL,
	`user_id` int NULL,
	`search_date` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_artist_search_logs` PRIMARY KEY 
(
	`artist_search_log_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[artists]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE artists(
	`artist_id` int AUTO_INCREMENT NOT NULL,
	`artist_name_kor` nvarchar(255) NULL,
	`artist_name_eng` nvarchar(300) NULL,
	`artist_comment` nvarchar(500) NULL,
	`artist_image` nchar(10) NULL,
	`create_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK__artists__6CD040012159FA71` PRIMARY KEY 
(
	`artist_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[arts]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE arts(
	`art_id` int AUTO_INCREMENT NOT NULL,
	`auction_id` int NULL,
	`artist_id` int NULL,
	`lot_no` int NULL,
	`make_year` int NULL,
	`title_kor` nvarchar(500) NULL,
	`title_eng` nvarchar(500) NULL,
	`currency` nvarchar(30) NULL,
	`money` Double NULL,
	`unit_cd` nvarchar(30) NULL,
	`size_length` Double NULL,
	`size_width` Double NULL,
	`mix_cd` nvarchar(50) NULL,
	`mix_size` Double NULL,
	`canvas` Double NULL,
	`medium_eng` nvarchar(50) NULL,
	`medium_kor` nvarchar(50) NULL,
	`description` nvarchar(500) NULL,
	`estimate_high` Double NULL,
	`estimate_low` Double NULL,
	`edition` nvarchar(50) NULL,
	`image_name` nvarchar(500) NULL,
	`create_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK__arts__C4784F0087423838` PRIMARY KEY 
(
	`art_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[auction_arts]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE auction_arts(
	`auction_art_id` int AUTO_INCREMENT NOT NULL,
	`auction_id` int NULL,
	`art_info_id` int NULL,
	`lot_no` nchar(10) NULL,
	`currency` nvarchar(30) NULL,
	`price` Double NULL,
	`estimate_high` Double NULL,
	`estimate_low` Double NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_auction_arts` PRIMARY KEY 
(
	`auction_art_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[auctions]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE auctions(
	`auction_id` int AUTO_INCREMENT NOT NULL,
	`site_id` int NULL,
	`auction_url_num` int NULL,
	`auction_place` nvarchar(500) NULL,
	`auction_date` date NULL,
	`auction_cate` nvarchar(50) NULL,
	`create_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK__auctions__2FF78640C947DBD9` PRIMARY KEY 
(
	`auction_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[chat_messages]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE chat_messages(
	`chat_message_id` int AUTO_INCREMENT NOT NULL,
	`user_id` int NULL,
	`chat_room_id` int NULL,
	`message` Longtext NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_chat_message` PRIMARY KEY 
(
	`chat_message_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[chat_room_join]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE chat_room_join(
	`chat_room_join_id` int AUTO_INCREMENT NOT NULL,
	`user_id` int NULL,
	`chat_room_id` int NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_chat_room_join` PRIMARY KEY 
(
	`chat_room_join_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[chat_rooms]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE chat_rooms(
	`chat_room_id` int AUTO_INCREMENT NOT NULL,
	`chat_room_title` nvarchar(300) NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_chat_rooms` PRIMARY KEY 
(
	`chat_room_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[following_artists]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE following_artists(
	`following_artist_id` int AUTO_INCREMENT NOT NULL,
	`user_id` int NULL,
	`artist_id` int NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_following_artist` PRIMARY KEY 
(
	`following_artist_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[release_images]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE release_images(
	`release_image_id` int NULL,
	`release_id` int NULL,
	`release_image_name` nvarchar(300) NULL,
	`create_time` datetime(3) NULL DEFAULT now(3)
);
/* SQLINES DEMO *** le [dbo].[releases]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE releases(
	`release_id` int AUTO_INCREMENT NOT NULL,
	`art_info_id` int NULL,
	`price` Double NULL,
	`published_on` nvarchar(200) NULL,
	`published_on_url` nvarchar(200) NULL,
	`release_date` datetime(3) NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_release` PRIMARY KEY 
(
	`release_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[sell_infos]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE sell_infos(
	`sell_info_id` int AUTO_INCREMENT NOT NULL,
	`art_info_id` int NULL,
	`user_id` int NULL,
	`hope_price` Double NULL,
	`currency` nvarchar(30) NULL,
	`status` nchar(10) NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_sell_info` PRIMARY KEY 
(
	`sell_info_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[sites]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE sites(
	`site_id` int AUTO_INCREMENT NOT NULL,
	`auction_site` nvarchar(255) NULL,
	`auction_url` nvarchar(300) NULL,
	`create_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK__sites__B22FDBCA6B0CCF91` PRIMARY KEY 
(
	`site_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[trade_logs]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE trade_logs(
	`trade_log_id` int AUTO_INCREMENT NOT NULL,
	`sell_user_id` int NOT NULL,
	`buy_user_id` int NOT NULL,
	`final_price` Double NOT NULL,
	`sell_info_id` int NOT NULL,
	`trade_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK_trade_logs` PRIMARY KEY 
(
	`trade_log_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[user_arts]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE user_arts(
	`user_art_id` int AUTO_INCREMENT NOT NULL,
	`user_id` int NULL,
	`artist_id` int NULL,
	`title_kor` nvarchar(200) NULL,
	`title_eng` nvarchar(200) NULL,
	`unit_cd` nchar(10) NULL,
	`size_length` nchar(10) NULL,
	`size_height` nchar(10) NULL,
	`canvas` nchar(10) NULL,
	`edition` nchar(10) NULL,
	`image_name` nchar(10) NULL,
	`create_time` datetime(3) NULL DEFAULT now(3),
 CONSTRAINT `PK_user_arts` PRIMARY KEY 
(
	`user_art_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[user_grades]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE user_grades(
	`user_grade_id` int AUTO_INCREMENT NOT NULL,
	`user_grade` nvarchar(50) NOT NULL,
	`authority` nvarchar(50) NOT NULL,
	`create_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK_user_grade` PRIMARY KEY 
(
	`user_grade_id` ASC
) 
);
/* SQLINES DEMO *** le [dbo].[users]    Script Date: 2021-09-03 오전 9:55:47 ******/
/* SET ANSI_NULLS ON */
 
/* SET QUOTED_IDENTIFIER ON */
 
-- SQLINES LICENSE FOR EVALUATION USE ONLY
CREATE TABLE users(
	`user_id` int AUTO_INCREMENT NOT NULL,
	`user_name_kor` nchar(100) NOT NULL,
	`user_grade_id` int NOT NULL,
	`user_email` nchar(100) NOT NULL,
	`user_cell_num` nchar(100) NULL,
	`create_time` datetime(3) NOT NULL DEFAULT now(3),
 CONSTRAINT `PK_users` PRIMARY KEY 
(
	`user_id` ASC
) 
);
/* Moved to CREATE TABLE
ALTER TABLE art_info_source ADD  CONSTRAINT `DF_art_info_source_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE art_infos ADD  CONSTRAINT `DF_art_infos_creat_time`  DEFAULT (now(3)) FOR `creat_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE artist_search_logs ADD  CONSTRAINT `DF_artist_search_logs_search_date`  DEFAULT (now(3)) FOR `search_date`
GO */
/* Moved to CREATE TABLE
ALTER TABLE artists ADD  CONSTRAINT `DF__artists__create___450A2E92`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE arts ADD  CONSTRAINT `DF__arts__create_tim__4BB72C21`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE auction_arts ADD  CONSTRAINT `DF_auction_arts_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE auctions ADD  CONSTRAINT `DF__auctions__create__47E69B3D`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE chat_messages ADD  CONSTRAINT `DF_chat_messages_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE chat_room_join ADD  CONSTRAINT `DF_chat_room_join_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE chat_rooms ADD  CONSTRAINT `DF_chat_rooms_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE following_artists ADD  CONSTRAINT `DF_following_artists_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE release_images ADD  CONSTRAINT `DF_release_images_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE releases ADD  CONSTRAINT `DF_releases_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE sell_infos ADD  CONSTRAINT `DF_sell_infos_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE sites ADD  CONSTRAINT `DF__sites__create_ti__422DC1E7`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE trade_logs ADD  CONSTRAINT `DF_trade_logs_trade_time`  DEFAULT (now(3)) FOR `trade_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE user_arts ADD  CONSTRAINT `DF_user_arts_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE user_grades ADD  CONSTRAINT `DF_user_grades_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
/* Moved to CREATE TABLE
ALTER TABLE users ADD  CONSTRAINT `DF_users_create_time`  DEFAULT (now(3)) FOR `create_time`
GO */
ALTER TABLE art_infos  ADD  CONSTRAINT `FK_art_info_art_info_source` FOREIGN KEY(`art_info_source_id`)
REFERENCES art_info_source (`art_info_source_id`);
 
ALTER TABLE art_infos CHECK CONSTRAINT [FK_art_info_art_info_source];
 
ALTER TABLE art_infos  ADD  CONSTRAINT `FK_art_info_artists` FOREIGN KEY(`artist_id`)
REFERENCES artists (`artist_id`);
 
ALTER TABLE art_infos CHECK CONSTRAINT [FK_art_info_artists];
 
ALTER TABLE artist_search_logs  ADD  CONSTRAINT `FK_artist_search_logs_artists` FOREIGN KEY(`artist_id`)
REFERENCES artists (`artist_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE artist_search_logs CHECK CONSTRAINT [FK_artist_search_logs_artists];
 
ALTER TABLE artist_search_logs  ADD  CONSTRAINT `FK_artist_search_logs_users` FOREIGN KEY(`user_id`)
REFERENCES users (`user_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE artist_search_logs CHECK CONSTRAINT [FK_artist_search_logs_users];
 
ALTER TABLE auction_arts  ADD  CONSTRAINT `FK_auction_arts_art_info` FOREIGN KEY(`art_info_id`)
REFERENCES art_infos (`art_info_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE auction_arts CHECK CONSTRAINT [FK_auction_arts_art_info];
 
ALTER TABLE auction_arts  ADD  CONSTRAINT `FK_auction_arts_auctions` FOREIGN KEY(`auction_id`)
REFERENCES auctions (`auction_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE auction_arts CHECK CONSTRAINT [FK_auction_arts_auctions];
 
ALTER TABLE auctions  ADD  CONSTRAINT `FK__auctions__site_i__48DABF76` FOREIGN KEY(`site_id`)
REFERENCES sites (`site_id`)
ON UPDATE CASCADE;
 
ALTER TABLE auctions CHECK CONSTRAINT [FK__auctions__site_i__48DABF76];
 
ALTER TABLE chat_messages  ADD  CONSTRAINT `FK_chat_message_chat_rooms` FOREIGN KEY(`chat_room_id`)
REFERENCES chat_rooms (`chat_room_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE chat_messages CHECK CONSTRAINT [FK_chat_message_chat_rooms];
 
ALTER TABLE chat_messages  ADD  CONSTRAINT `FK_chat_message_users` FOREIGN KEY(`user_id`)
REFERENCES users (`user_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE chat_messages CHECK CONSTRAINT [FK_chat_message_users];
 
ALTER TABLE chat_room_join  ADD  CONSTRAINT `FK_chat_room_join_chat_rooms` FOREIGN KEY(`chat_room_id`)
REFERENCES chat_rooms (`chat_room_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE chat_room_join CHECK CONSTRAINT [FK_chat_room_join_chat_rooms];
 
ALTER TABLE chat_room_join  ADD  CONSTRAINT `FK_chat_room_join_users` FOREIGN KEY(`user_id`)
REFERENCES users (`user_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE chat_room_join CHECK CONSTRAINT [FK_chat_room_join_users];
 
ALTER TABLE following_artists  ADD  CONSTRAINT `FK_following_artist_artists` FOREIGN KEY(`artist_id`)
REFERENCES artists (`artist_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE following_artists CHECK CONSTRAINT [FK_following_artist_artists];
 
ALTER TABLE following_artists  ADD  CONSTRAINT `FK_following_artist_users` FOREIGN KEY(`user_id`)
REFERENCES users (`user_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE following_artists CHECK CONSTRAINT [FK_following_artist_users];
 
ALTER TABLE release_images  ADD  CONSTRAINT `FK_release_image_release` FOREIGN KEY(`release_id`)
REFERENCES releases (`release_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE release_images CHECK CONSTRAINT [FK_release_image_release];
 
ALTER TABLE releases  ADD  CONSTRAINT `FK_release_art_info` FOREIGN KEY(`art_info_id`)
REFERENCES art_infos (`art_info_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE releases CHECK CONSTRAINT [FK_release_art_info];
 
ALTER TABLE trade_logs  ADD  CONSTRAINT `FK_trade_logs_sell_info` FOREIGN KEY(`sell_info_id`)
REFERENCES sell_infos (`sell_info_id`);
 
ALTER TABLE trade_logs CHECK CONSTRAINT [FK_trade_logs_sell_info];
 
ALTER TABLE trade_logs  ADD  CONSTRAINT `FK_trade_logs_users` FOREIGN KEY(`sell_user_id`)
REFERENCES users (`user_id`);
 
ALTER TABLE trade_logs CHECK CONSTRAINT [FK_trade_logs_users];
 
ALTER TABLE trade_logs  ADD  CONSTRAINT `FK_trade_logs_users1` FOREIGN KEY(`buy_user_id`)
REFERENCES users (`user_id`);
 
ALTER TABLE trade_logs CHECK CONSTRAINT [FK_trade_logs_users1];
 
ALTER TABLE user_arts  ADD  CONSTRAINT `FK_user_arts_artists` FOREIGN KEY(`artist_id`)
REFERENCES artists (`artist_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE user_arts CHECK CONSTRAINT [FK_user_arts_artists];
 
ALTER TABLE user_arts  ADD  CONSTRAINT `FK_user_arts_users` FOREIGN KEY(`user_id`)
REFERENCES users (`user_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE user_arts CHECK CONSTRAINT [FK_user_arts_users];
 
ALTER TABLE users  ADD  CONSTRAINT `FK_users_user_grade` FOREIGN KEY(`user_grade_id`)
REFERENCES user_grades (`user_grade_id`)
ON UPDATE CASCADE
ON DELETE CASCADE;
 
ALTER TABLE users CHECK CONSTRAINT [FK_users_user_grade];
 