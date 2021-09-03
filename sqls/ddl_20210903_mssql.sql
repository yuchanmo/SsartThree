/****** Object:  Table [dbo].[art_info_source]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[art_info_source](
	[art_info_source_id] [int] IDENTITY(1,1) NOT NULL,
	[art_source] [nvarchar](100) NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_art_info_source] PRIMARY KEY CLUSTERED 
(
	[art_info_source_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[art_infos]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[art_infos](
	[art_info_id] [int] IDENTITY(1,1) NOT NULL,
	[artist_id] [int] NULL,
	[art_info_source_id] [int] NULL,
	[make_year] [date] NULL,
	[title_kor] [nvarchar](200) NULL,
	[title_eng] [nvarchar](200) NULL,
	[unit_cd] [nchar](10) NULL,
	[size_length] [float] NULL,
	[size_height] [float] NULL,
	[mix_cd] [nchar](10) NULL,
	[mix_size] [nchar](10) NULL,
	[canvas] [nvarchar](50) NULL,
	[medium_eng] [nvarchar](50) NULL,
	[medium_kor] [nvarchar](50) NULL,
	[description] [nvarchar](300) NULL,
	[edition] [nvarchar](300) NULL,
	[image_name] [nvarchar](300) NULL,
	[creat_time] [datetime] NULL,
 CONSTRAINT [PK_art_info] PRIMARY KEY CLUSTERED 
(
	[art_info_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[artist_search_logs]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[artist_search_logs](
	[artist_search_log_id] [int] IDENTITY(1,1) NOT NULL,
	[artist_id] [int] NULL,
	[user_id] [int] NULL,
	[search_date] [datetime] NULL,
 CONSTRAINT [PK_artist_search_logs] PRIMARY KEY CLUSTERED 
(
	[artist_search_log_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[artists]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[artists](
	[artist_id] [int] IDENTITY(1,1) NOT NULL,
	[artist_name_kor] [nvarchar](255) NULL,
	[artist_name_eng] [nvarchar](300) NULL,
	[artist_comment] [nvarchar](500) NULL,
	[artist_image] [nchar](10) NULL,
	[create_time] [datetime] NOT NULL,
 CONSTRAINT [PK__artists__6CD040012159FA71] PRIMARY KEY CLUSTERED 
(
	[artist_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[arts]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[arts](
	[art_id] [int] IDENTITY(1,1) NOT NULL,
	[auction_id] [int] NULL,
	[artist_id] [int] NULL,
	[lot_no] [int] NULL,
	[make_year] [int] NULL,
	[title_kor] [nvarchar](500) NULL,
	[title_eng] [nvarchar](500) NULL,
	[currency] [nvarchar](30) NULL,
	[money] [float] NULL,
	[unit_cd] [nvarchar](30) NULL,
	[size_length] [float] NULL,
	[size_width] [float] NULL,
	[mix_cd] [nvarchar](50) NULL,
	[mix_size] [float] NULL,
	[canvas] [float] NULL,
	[medium_eng] [nvarchar](50) NULL,
	[medium_kor] [nvarchar](50) NULL,
	[description] [nvarchar](500) NULL,
	[estimate_high] [float] NULL,
	[estimate_low] [float] NULL,
	[edition] [nvarchar](50) NULL,
	[image_name] [nvarchar](500) NULL,
	[create_time] [datetime] NOT NULL,
 CONSTRAINT [PK__arts__C4784F0087423838] PRIMARY KEY CLUSTERED 
(
	[art_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auction_arts]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auction_arts](
	[auction_art_id] [int] IDENTITY(1,1) NOT NULL,
	[auction_id] [int] NULL,
	[art_info_id] [int] NULL,
	[lot_no] [nchar](10) NULL,
	[currency] [nvarchar](30) NULL,
	[price] [float] NULL,
	[estimate_high] [float] NULL,
	[estimate_low] [float] NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_auction_arts] PRIMARY KEY CLUSTERED 
(
	[auction_art_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auctions]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auctions](
	[auction_id] [int] IDENTITY(1,1) NOT NULL,
	[site_id] [int] NULL,
	[auction_url_num] [int] NULL,
	[auction_place] [nvarchar](500) NULL,
	[auction_date] [date] NULL,
	[auction_cate] [nvarchar](50) NULL,
	[create_time] [datetime] NOT NULL,
 CONSTRAINT [PK__auctions__2FF78640C947DBD9] PRIMARY KEY CLUSTERED 
(
	[auction_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[chat_messages]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[chat_messages](
	[chat_message_id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NULL,
	[chat_room_id] [int] NULL,
	[message] [nvarchar](max) NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_chat_message] PRIMARY KEY CLUSTERED 
(
	[chat_message_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[chat_room_join]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[chat_room_join](
	[chat_room_join_id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NULL,
	[chat_room_id] [int] NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_chat_room_join] PRIMARY KEY CLUSTERED 
(
	[chat_room_join_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[chat_rooms]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[chat_rooms](
	[chat_room_id] [int] IDENTITY(1,1) NOT NULL,
	[chat_room_title] [nvarchar](300) NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_chat_rooms] PRIMARY KEY CLUSTERED 
(
	[chat_room_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[following_artists]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[following_artists](
	[following_artist_id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NULL,
	[artist_id] [int] NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_following_artist] PRIMARY KEY CLUSTERED 
(
	[following_artist_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[release_images]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[release_images](
	[release_image_id] [int] NULL,
	[release_id] [int] NULL,
	[release_image_name] [nvarchar](300) NULL,
	[create_time] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[releases]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[releases](
	[release_id] [int] IDENTITY(1,1) NOT NULL,
	[art_info_id] [int] NULL,
	[price] [float] NULL,
	[published_on] [nvarchar](200) NULL,
	[published_on_url] [nvarchar](200) NULL,
	[release_date] [datetime] NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_release] PRIMARY KEY CLUSTERED 
(
	[release_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sell_infos]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sell_infos](
	[sell_info_id] [int] IDENTITY(1,1) NOT NULL,
	[art_info_id] [int] NULL,
	[user_id] [int] NULL,
	[hope_price] [float] NULL,
	[currency] [nvarchar](30) NULL,
	[status] [nchar](10) NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_sell_info] PRIMARY KEY CLUSTERED 
(
	[sell_info_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sites]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sites](
	[site_id] [int] IDENTITY(1,1) NOT NULL,
	[auction_site] [nvarchar](255) NULL,
	[auction_url] [nvarchar](300) NULL,
	[create_time] [datetime] NOT NULL,
 CONSTRAINT [PK__sites__B22FDBCA6B0CCF91] PRIMARY KEY CLUSTERED 
(
	[site_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[trade_logs]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[trade_logs](
	[trade_log_id] [int] IDENTITY(1,1) NOT NULL,
	[sell_user_id] [int] NOT NULL,
	[buy_user_id] [int] NOT NULL,
	[final_price] [float] NOT NULL,
	[sell_info_id] [int] NOT NULL,
	[trade_time] [datetime] NOT NULL,
 CONSTRAINT [PK_trade_logs] PRIMARY KEY CLUSTERED 
(
	[trade_log_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[user_arts]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[user_arts](
	[user_art_id] [int] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NULL,
	[artist_id] [int] NULL,
	[title_kor] [nvarchar](200) NULL,
	[title_eng] [nvarchar](200) NULL,
	[unit_cd] [nchar](10) NULL,
	[size_length] [nchar](10) NULL,
	[size_height] [nchar](10) NULL,
	[canvas] [nchar](10) NULL,
	[edition] [nchar](10) NULL,
	[image_name] [nchar](10) NULL,
	[create_time] [datetime] NULL,
 CONSTRAINT [PK_user_arts] PRIMARY KEY CLUSTERED 
(
	[user_art_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[user_grades]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[user_grades](
	[user_grade_id] [int] IDENTITY(1,1) NOT NULL,
	[user_grade] [nvarchar](50) NOT NULL,
	[authority] [nvarchar](50) NOT NULL,
	[create_time] [datetime] NOT NULL,
 CONSTRAINT [PK_user_grade] PRIMARY KEY CLUSTERED 
(
	[user_grade_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[users]    Script Date: 2021-09-03 오전 9:55:47 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[users](
	[user_id] [int] IDENTITY(1,1) NOT NULL,
	[user_name_kor] [nchar](100) NOT NULL,
	[user_grade_id] [int] NOT NULL,
	[user_email] [nchar](100) NOT NULL,
	[user_cell_num] [nchar](100) NULL,
	[create_time] [datetime] NOT NULL,
 CONSTRAINT [PK_users] PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[art_info_source] ADD  CONSTRAINT [DF_art_info_source_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[art_infos] ADD  CONSTRAINT [DF_art_infos_creat_time]  DEFAULT (getdate()) FOR [creat_time]
GO
ALTER TABLE [dbo].[artist_search_logs] ADD  CONSTRAINT [DF_artist_search_logs_search_date]  DEFAULT (getdate()) FOR [search_date]
GO
ALTER TABLE [dbo].[artists] ADD  CONSTRAINT [DF__artists__create___450A2E92]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[arts] ADD  CONSTRAINT [DF__arts__create_tim__4BB72C21]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[auction_arts] ADD  CONSTRAINT [DF_auction_arts_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[auctions] ADD  CONSTRAINT [DF__auctions__create__47E69B3D]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[chat_messages] ADD  CONSTRAINT [DF_chat_messages_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[chat_room_join] ADD  CONSTRAINT [DF_chat_room_join_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[chat_rooms] ADD  CONSTRAINT [DF_chat_rooms_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[following_artists] ADD  CONSTRAINT [DF_following_artists_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[release_images] ADD  CONSTRAINT [DF_release_images_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[releases] ADD  CONSTRAINT [DF_releases_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[sell_infos] ADD  CONSTRAINT [DF_sell_infos_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[sites] ADD  CONSTRAINT [DF__sites__create_ti__422DC1E7]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[trade_logs] ADD  CONSTRAINT [DF_trade_logs_trade_time]  DEFAULT (getdate()) FOR [trade_time]
GO
ALTER TABLE [dbo].[user_arts] ADD  CONSTRAINT [DF_user_arts_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[user_grades] ADD  CONSTRAINT [DF_user_grades_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[users] ADD  CONSTRAINT [DF_users_create_time]  DEFAULT (getdate()) FOR [create_time]
GO
ALTER TABLE [dbo].[art_infos]  WITH CHECK ADD  CONSTRAINT [FK_art_info_art_info_source] FOREIGN KEY([art_info_source_id])
REFERENCES [dbo].[art_info_source] ([art_info_source_id])
GO
ALTER TABLE [dbo].[art_infos] CHECK CONSTRAINT [FK_art_info_art_info_source]
GO
ALTER TABLE [dbo].[art_infos]  WITH CHECK ADD  CONSTRAINT [FK_art_info_artists] FOREIGN KEY([artist_id])
REFERENCES [dbo].[artists] ([artist_id])
GO
ALTER TABLE [dbo].[art_infos] CHECK CONSTRAINT [FK_art_info_artists]
GO
ALTER TABLE [dbo].[artist_search_logs]  WITH CHECK ADD  CONSTRAINT [FK_artist_search_logs_artists] FOREIGN KEY([artist_id])
REFERENCES [dbo].[artists] ([artist_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[artist_search_logs] CHECK CONSTRAINT [FK_artist_search_logs_artists]
GO
ALTER TABLE [dbo].[artist_search_logs]  WITH CHECK ADD  CONSTRAINT [FK_artist_search_logs_users] FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[artist_search_logs] CHECK CONSTRAINT [FK_artist_search_logs_users]
GO
ALTER TABLE [dbo].[auction_arts]  WITH CHECK ADD  CONSTRAINT [FK_auction_arts_art_info] FOREIGN KEY([art_info_id])
REFERENCES [dbo].[art_infos] ([art_info_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[auction_arts] CHECK CONSTRAINT [FK_auction_arts_art_info]
GO
ALTER TABLE [dbo].[auction_arts]  WITH CHECK ADD  CONSTRAINT [FK_auction_arts_auctions] FOREIGN KEY([auction_id])
REFERENCES [dbo].[auctions] ([auction_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[auction_arts] CHECK CONSTRAINT [FK_auction_arts_auctions]
GO
ALTER TABLE [dbo].[auctions]  WITH CHECK ADD  CONSTRAINT [FK__auctions__site_i__48DABF76] FOREIGN KEY([site_id])
REFERENCES [dbo].[sites] ([site_id])
ON UPDATE CASCADE
GO
ALTER TABLE [dbo].[auctions] CHECK CONSTRAINT [FK__auctions__site_i__48DABF76]
GO
ALTER TABLE [dbo].[chat_messages]  WITH CHECK ADD  CONSTRAINT [FK_chat_message_chat_rooms] FOREIGN KEY([chat_room_id])
REFERENCES [dbo].[chat_rooms] ([chat_room_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[chat_messages] CHECK CONSTRAINT [FK_chat_message_chat_rooms]
GO
ALTER TABLE [dbo].[chat_messages]  WITH CHECK ADD  CONSTRAINT [FK_chat_message_users] FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[chat_messages] CHECK CONSTRAINT [FK_chat_message_users]
GO
ALTER TABLE [dbo].[chat_room_join]  WITH CHECK ADD  CONSTRAINT [FK_chat_room_join_chat_rooms] FOREIGN KEY([chat_room_id])
REFERENCES [dbo].[chat_rooms] ([chat_room_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[chat_room_join] CHECK CONSTRAINT [FK_chat_room_join_chat_rooms]
GO
ALTER TABLE [dbo].[chat_room_join]  WITH CHECK ADD  CONSTRAINT [FK_chat_room_join_users] FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[chat_room_join] CHECK CONSTRAINT [FK_chat_room_join_users]
GO
ALTER TABLE [dbo].[following_artists]  WITH CHECK ADD  CONSTRAINT [FK_following_artist_artists] FOREIGN KEY([artist_id])
REFERENCES [dbo].[artists] ([artist_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[following_artists] CHECK CONSTRAINT [FK_following_artist_artists]
GO
ALTER TABLE [dbo].[following_artists]  WITH CHECK ADD  CONSTRAINT [FK_following_artist_users] FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[following_artists] CHECK CONSTRAINT [FK_following_artist_users]
GO
ALTER TABLE [dbo].[release_images]  WITH CHECK ADD  CONSTRAINT [FK_release_image_release] FOREIGN KEY([release_id])
REFERENCES [dbo].[releases] ([release_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[release_images] CHECK CONSTRAINT [FK_release_image_release]
GO
ALTER TABLE [dbo].[releases]  WITH CHECK ADD  CONSTRAINT [FK_release_art_info] FOREIGN KEY([art_info_id])
REFERENCES [dbo].[art_infos] ([art_info_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[releases] CHECK CONSTRAINT [FK_release_art_info]
GO
ALTER TABLE [dbo].[trade_logs]  WITH CHECK ADD  CONSTRAINT [FK_trade_logs_sell_info] FOREIGN KEY([sell_info_id])
REFERENCES [dbo].[sell_infos] ([sell_info_id])
GO
ALTER TABLE [dbo].[trade_logs] CHECK CONSTRAINT [FK_trade_logs_sell_info]
GO
ALTER TABLE [dbo].[trade_logs]  WITH CHECK ADD  CONSTRAINT [FK_trade_logs_users] FOREIGN KEY([sell_user_id])
REFERENCES [dbo].[users] ([user_id])
GO
ALTER TABLE [dbo].[trade_logs] CHECK CONSTRAINT [FK_trade_logs_users]
GO
ALTER TABLE [dbo].[trade_logs]  WITH CHECK ADD  CONSTRAINT [FK_trade_logs_users1] FOREIGN KEY([buy_user_id])
REFERENCES [dbo].[users] ([user_id])
GO
ALTER TABLE [dbo].[trade_logs] CHECK CONSTRAINT [FK_trade_logs_users1]
GO
ALTER TABLE [dbo].[user_arts]  WITH CHECK ADD  CONSTRAINT [FK_user_arts_artists] FOREIGN KEY([artist_id])
REFERENCES [dbo].[artists] ([artist_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[user_arts] CHECK CONSTRAINT [FK_user_arts_artists]
GO
ALTER TABLE [dbo].[user_arts]  WITH CHECK ADD  CONSTRAINT [FK_user_arts_users] FOREIGN KEY([user_id])
REFERENCES [dbo].[users] ([user_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[user_arts] CHECK CONSTRAINT [FK_user_arts_users]
GO
ALTER TABLE [dbo].[users]  WITH CHECK ADD  CONSTRAINT [FK_users_user_grade] FOREIGN KEY([user_grade_id])
REFERENCES [dbo].[user_grades] ([user_grade_id])
ON UPDATE CASCADE
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[users] CHECK CONSTRAINT [FK_users_user_grade]
GO