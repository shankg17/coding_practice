create table reg_txn (
    txnid serial primary key,
    txndate DATE NOT NULL,
    cracc varchar(10),
    dbacc varchar(10),
    amt DECIMAL(10, 1) NOT NULL,
    comment varchar(255)
);
insert into reg_txn(txndate, cracc,dbacc,amt,comment) VALUES
('2022-01-01','ibtfsa','wscq',11000.0,'tfsa contribution'),
('2023-01-01','ibtfsa','wscq',7500.0,'tfsa contribution'),
('2024-01-01','ibtfsa','wscq',7000.0,'tfsa contribution'),
('2024-12-31','wscq','ibtfsa',6500.0,'tfsa withdrawal'),
('2025-01-01','ibtfsa','wscq',1000.0,'tfsa contribution'),
('2025-09-30','wscq','ibtfsa',20200.0,'tfsa withdrawal'),
('2025-01-01','wsfhsa','wscq',16000.0,'fhsa contribution'),
('2025-01-01','ibtfsa','wscq',8000.0,'fhsa contribution');
select * from reg_txn;


insert into reg_txn(txndate,cracc,dbacc,amt,comment) VALUES
('2025-11-10','ut_grc','tdcq',76.34,'wellesley fruit market'),
('2025-11-11','travel','asim',42.24,'uber ride'),
('2025-11-10','ut_grc','asim',90.00,'marche leos'),
('2025-11-10','travel','asim',75.05,'hopp ride'),
('2025-11-10','travel','asim',9.90,'ttc ride'),
('2025-11-10','dine','asim',134.90,'ishq'),
('2025-11-10','dine','tdcq',5.00,'ishq'),
('2025-11-10','dine','asim',59.16,'khao san'),
('2025-11-10','others','asim',9.99,'amex card fee'),
('2025-11-08','others','tdcq',15.00,'haircut'),
('2025-11-06','tdcq','incft',2193.00,'td salary'),
('2025-11-11','ut_grc','twmc',18.76,'panchavati'),
('2025-11-10','dine','twmc',13.55,'butter chicken roti'),
('2025-11-09','others','twmc',16.39,'putting edge');

select * from reg_txn;

select * from reg_txn where cracc = 'travel';


*******************************************************************************************
create table inv_txn (
    txnid serial primary key,
    txndate DATE NOT NULL,
    currency varchar(10),
    acc varchar(10),
    ticker varchar(10),
    assetname varchar(255),
    qty integer,
    price DECIMAL(10, 2) NOT NULL,
    commission varchar(255),
    comment varchar(255)
);

select * from inv_txn;
*****************************************************************************************************
create table balsht (
    currency varchar(10),
    acc varchar(10),
    accname varchar(255),
    oct25 integer
);
select * from balsht;

insert into balsht(currency,acc,accname,oct25) VALUES
('inr','knro','kotak nro','34715'),
('inr','knre','kotak nre','11987');


*******************************************************************************************************
drop table accounts;
create table accounts(
    accid varchar(10),
    accname varchar(40),
    currency varchar(5) check (currency in ('cad','usd','inr','eur')) DEFAULT 'cad',
    acctype varchar(255) check (acctype in ('internal','external')) default 'internal'
);
insert into accounts (accid,accname,currency,acctype) VALUES
('fdnreg','fidelity non-registered','cad','internal');

select * from  accounts;

update accounts set accid = 'agre' where accname = 'amex green';
update accounts set accid = 'agre' where accname = 'amex green';