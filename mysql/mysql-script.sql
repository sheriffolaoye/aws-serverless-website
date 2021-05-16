USE Website;

DROP TABLE IF EXISTS RepositoryData;

CREATE TABLE RepositoryData(
    Id VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(255),
    Description TEXT,
    URL VARCHAR(255),
    Language VARCHAR(255),
    DateCreated DATETIME
);