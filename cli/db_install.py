from mysql import connector

connection = connector.connect(
    user="eredivisie",
    password="eredivisie",
    host="localhost",
    database="eredivisie"
)

cursor = connection.cursor()

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
