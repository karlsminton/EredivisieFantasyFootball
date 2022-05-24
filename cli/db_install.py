from mysql import connector

connection = connector.connect(
    user="eredivisie",
    password="eredivisie",
    host="localhost",
    database="eredivisie"
)
cursor = connection.cursor()

# Football Players
cursor.execute(
    """
    CREATE TABLE `players` (
        `player_id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(40) NOT NULL,
        `position` int(1) NOT NULL,
        `date_of_birth` date NOT NULL,
        `nationality` varchar(100) NOT NULL,
        `shirt_number` int(3) NOT NULL,
        PRIMARY KEY (`player_id`)
    ) ENGINE=InnoDB
    """
)
connection.commit()

# Actual Football clubs
cursor.execute(
    """
    CREATE TABLE `clubs` (
        `club_id` int(11) NOT NULL AUTO_INCREMENT,
        `api_id` int(5) NOT NULL,
        `name` varchar(80) NOT NULL,
        `short_name` varchar(80) NOT NULL,
        `crest_url` varchar(256) NOT NULL,
        `website` varchar(256) NOT NULL,
        `venue` varchar(256) NOT NULL,
        PRIMARY KEY (`club_id`),
        CONSTRAINT club UNIQUE (`api_id`, `name`, `short_name`)
    ) ENGINE=InnoDB
    """
)
connection.commit()

# User Team
cursor.execute(
    """
    CREATE TABLE `user_teams` (
        `user_team_id` int(11) NOT NULL AUTO_INCREMENT,
        `team_name` varchar(80) NOT NULL,
        `score` int(5) NOT NULL,
        `squad` JSON,
        `bench` JSON,
        PRIMARY KEY (`user_team_id`)
    ) ENGINE=InnoDB
    """
)
connection.commit()

# Fantasy Eredivisie Players
cursor.execute(
    """
    CREATE TABLE `users` (
        `user_id` int(11) NOT NULL AUTO_INCREMENT,
        `firstname` varchar(50) NOT NULL,
        `lastname` varchar(50) NOT NULL,
        `email` varchar(128) NOT NULL UNIQUE,
        `password` varchar(512) NOT NULL,
        `date_of_birth` date NOT NULL,
        `user_team_id` int(11) NOT NULL,
        PRIMARY KEY (`user_id`),
        KEY `USERS_USER_TEAM_ID` (`user_team_id`), 
        CONSTRAINT `USERS_USER_TEAM_ID_USER_TEAMS_USER_TEAM_ID` 
        FOREIGN KEY (`user_team_id`) REFERENCES `user_teams` (`user_team_id`)
        ON DELETE CASCADE
    ) ENGINE=InnoDB
    """
)
connection.commit()
