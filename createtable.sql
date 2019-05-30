
CREATE TABLE arp 
(
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    ip CHAR(50) NOT NULL,
    mac TEXT,
    content TEXT,
    createtime TIMESTAMP,
    PRIMARY KEY(id)
)
