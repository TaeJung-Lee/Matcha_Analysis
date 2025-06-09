DROP TABLE IF EXISTS uji_matcha;

CREATE TABLE uji_matcha (
    year INTEGER PRIMARY KEY,
    total_field_ha REAL,
    tencha_field_ha REAL,
    cultivated_farmers INTEGER,
    operating_farmers INTEGER,
    total_aracha_tons REAL,
    tencha_tons REAL,
    autumn_tencha_tons REAL,
    total_tencha_tons REAL,
    total_aracha_yen_m REAL,
    tencha_yen_m REAL,
    autumn_tencha_yen_m REAL,
    total_tencha_yen_m REAL
);