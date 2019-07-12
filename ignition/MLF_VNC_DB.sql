------------
-- tables --
------------
CREATE TABLE HMI_DATA
	(
		id int IDENTITY(1,1) PRIMARY KEY,
		HMI varchar(50) not null,
		URL varchar(250) not null,
		CMD varchar(100) not null,
	)

CREATE TABLE USR
	(
		id int IDENTITY(1,1) PRIMARY KEY,
		name varchar(30) not null,
	)
CREATE UNIQUE INDEX ui_USR__name
ON USR (name)

CREATE TABLE USR_HMI_DATA_LINK
	(
		id int IDENTITY(1,1) PRIMARY KEY,
		USR_id int not null,
		HMI_DATA_id int not null,
	)
CREATE UNIQUE INDEX ui_USR_HMI_DATA_LINK_USR_id_HMI_DATA_id
ON USR_HMI_DATA_LINK (USR_id,HMI_DATA_id,page)

ALTER TABLE USR_HMI_DATA_LINK
ADD xpos int not null 
ALTER TABLE USR_HMI_DATA_LINK
ADD ypos int not null 
ALTER TABLE USR_HMI_DATA_LINK
ADD width int not null 
ALTER TABLE USR_HMI_DATA_LINK
ADD height int not null 
ALTER TABLE USR_HMI_DATA_LINK
ADD page varchar(30) not null 

CREATE TABLE page
	(
		id int IDENTITY(1,1) PRIMARY KEY,
		title varchar(30) not null,
	)
CREATE UNIQUE INDEX ui_page_title
ON page (title)
-----------------
--Foreign Keys--
-----------------
ALTER TABLE USR_HMI_DATA_LINK
ADD CONSTRAINT fk_HMI_DATA_id__USR_HMI_DATA_LINK__HMI_DATA_id
FOREIGN KEY (HMI_DATA_id) REFERENCES HMI_DATA(id) ON DELETE CASCADE

ALTER TABLE USR_HMI_DATA_LINK
ADD CONSTRAINT fk_USR_id__USR_HMI_DATA_LINK__USR_id
FOREIGN KEY (USR_id) REFERENCES USR(id) ON DELETE CASCADE

ALTER TABLE USR_HMI_DATA_LINK
ADD CONSTRAINT fk_page__USR_HMI_DATA_LINK__title
FOREIGN KEY (page) REFERENCES page(title) ON DELETE CASCADE


------------
-- Insert --
------------

INSERT INTO HMI_DATA(HMI,URL,CMD)
VALUES('Bowlchopper','http://ra-ignition:6080/vnc.html?host=RA-IGNITION&port=6080&autoconnect=true&reconnect=true&show_dot=true',' -h 10.10.0.72:5900 -p 6080');

INSERT INTO HMI_DATA(HMI,URL,CMD)
VALUES('Grinding01','http://ra-ignition:6081/vnc.html?host=RA-IGNITION&port=6081&autoconnect=true&password=Maple@123&reconnect=true&show_dot=true',' -h 10.10.0.142:5900 -p 6081');

INSERT INTO HMI_DATA(HMI,URL,CMD)
VALUES('Injection01','http://ra-ignition:6082/vnc.html?host=RA-IGNITION&port=6082&autoconnect=true&password=RTAI.444&reconnect=true&show_dot=true',' -h 10.10.0.51:5900 -p 6082');
