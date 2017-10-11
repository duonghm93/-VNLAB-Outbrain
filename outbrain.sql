create database if not exists outbrain;

use outbrain;

create table if not exists clicks_train(
	display_id int NOT NULL,
	ad_id int NOT NULL,
	clicked int NOT NULL,
	INDEX(display_id),
	INDEX(ad_id)
) ENGINE = MyISAM;

create table if not exists events(
	display_id int NOT NULL,
	uuid char(255) NOT NULL ,
	document_id int NOT NULL ,
	time_stamp int NOT NULL ,
	platform int NOT NULL ,
	geo_location char(255) NOT NULL,	
	INDEX(display_id)
) ENGINE = MyISAM;

create table if not exists documents_meta(
	document_id int NOT NULL,
	source_id int NOT NULL,
	publisher_id int NOT NULL,
	publish_time DATETIME,
	INDEX(document_id)
) ENGINE = MYISAM;

create table if not exists documents_topics(
	document_id int NOT NULL,
	topic_id int NOT NULL,
	confidence_level float NOT NULL,
	INDEX(document_id, topic_id)
) ENGINE = MYISAM;

create table if not exists documents_entities(
	document_id int NOT NULL,
	entity_id char(255) NOT NULL,
	confidence_level float NOT NULL,
	INDEX(document_id, entity_id)
) ENGINE = MYISAM;

create table if not exists documents_categories(
	document_id int NOT NULL,
	category_id int NOT NULL,
	confidence_level float NOT NULL,
	INDEX(document_id, category_id)
) ENGINE = MYISAM;

create table if not exists promoted_content(
	ad_id int NOT NULL,
	document_id int NOT NULL,
	campaign_id int NOT NULL,
	advertiser_id int NOT NULL,
	INDEX(ad_id)
) ENGINE = MYISAM;

create table if not exists page_view(		
	uuid char(255) NOT NULL ,
	document_id int NOT NULL ,
	time_stamp int NOT NULL ,
	platform int NOT NULL ,
	geo_location char(255) NOT NULL,
	traffic_source int NOT NULL,	
	INDEX(uuid),
	INDEX(document_id)
) ENGINE = MYISAM;

set unique_checks = 0;
set foreign_key_checks = 0;
set sql_log_bin=0;


load data infile 'D:/outbrain/SAMPLE_DATA/clicks_train_sample.csv' into table clicks_train columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/events_sample.csv' into table events columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/documents_meta_sample.csv' into table documents_meta columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/documents_topics_sample.csv' into table documents_topics columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/documents_entities_sample.csv' into table documents_entities columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/documents_categories_sample.csv' into table documents_categories columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/promoted_content_sample.csv' into table promoted_content columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/SAMPLE_DATA/page_views_sample.csv' into table page_view columns terminated by ',' lines terminated by '\n' ignore 1 lines;

--load data infile 'D:/ad_simple_rate.csv' into table ad_rate columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/clicks_train.csv/clicks_train.csv' into table clicks_train columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/events.csv/events.csv' into table events columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/documents_meta.csv/documents_meta.csv' into table documents_meta columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/documents_topics.csv/documents_topics.csv' into table documents_topics columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/documents_entities.csv/documents_entities.csv' into table documents_entities columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/documents_categories.csv/documents_categories.csv' into table documents_categories columns terminated by ',' lines terminated by '\n' ignore 1 lines;
load data infile 'D:/outbrain/promoted_content.csv/promoted_content.csv' into table promoted_content columns terminated by ',' lines terminated by '\n' ignore 1 lines;


select 'clicked', 'display_id', 'ad_id', 'uuid', 'document_id', 'time_stamp', 'platform', 'geo_location', 'source_id', 'publisher_id', 'campaign_id', 'advertiser_id'
union all
select * from merge_data
into outfile 'D:/outbrain/sample_data.csv'
fields terminated by ',' optionally enclosed by '' lines terminated by '\n';