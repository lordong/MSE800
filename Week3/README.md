# These are activities of week 3

## 1. Activity 1

Draw an entity diagram between Student and Course.

Student includes name, age, studentId, address, phone and key ID.

Course includes name, startdate, enddate and key ID.

Related table - EnrolledIn - include the related ID between student's key ID and cource's key ID.

## 2. Activity 1.2

Add Lectuer table, primary key and foreign key.

## 3. Activity 2

ER diagram of a database project for a financial money exchange.

1. Create a customer item for one user in the Customer table. Add a new log to the Logs table, operation type - CreateCustomer.

2. Open NZD and USD accounts for this customer in the Account table; balances are zero. Add two new logs to the Logs table, operation type - OpenAccount.

3. Customer deposits 100 NZD, modifies the balance of the NZD Account to 100 NZD and adds a new record to the Records table, transfer type set to 'deposit' and amount set to 100. Add a new log to the Logs table, operation type - Deposit.

4. Customer exchanges 50 NZD for USD, the currency rate is 0.5902. Withdraws 50 from the NZD account, adds a record and an operation log for this withdrawal, type set to Withdraw. Calculates the USD result is 50 * 0.5902 = 29.51, deposits 29.51 to the USD account, adds a record and operation log for this deposit, type set to Deposit. Add an item to the Transfer table, set the source and destination IDs to the related IDs of the Records table, and set currency_rate to 0.5902.


