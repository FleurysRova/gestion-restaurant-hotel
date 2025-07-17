create table users(
    user_id serial primary key,
    user_name varchar(100),
    user_firstname varchar(100),
    user_email varchar(50),
    user_phone int,
    user_adress varchar(50),
    user_password varchar(250)
);

INSERT INTO users (user_name, user_firstname, user_email, user_phone, user_adress, user_password) VALUES
('Rakoto', 'Jean', 'jean.rakoto@example.com', 33012345, 'Antananarivo', 'pass1234'),
('Rasoa', 'Miora', 'miora.rasoa@example.com', 33067890, 'Fianarantsoa', 'password567'),
('Andrianina', 'Hery', 'hery.andrianina@example.com', 33123456, 'Toamasina', 'mypassword89'),
('Razanamasy', 'Lala', 'lala.razanamasy@example.com', 33234567, 'Mahajanga', 'securepass45');
