CREATE TABLE PhoneBook (
    id VARCHAR(20) PRIMARY KEY,
    account_name VARCHAR(20) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(50) NOT NULL
)
