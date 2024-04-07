# Dataset exploration and understanding of fraud detection domain.
Dataset contains two tables: Transaction Table, which contains money transactions information and Identity Table, in which identity information is stored: network connection information and digital signature associated with transactions.

Explanation here is conducted using [information](https://www.kaggle.com/c/ieee-fraud-detection/discussion/101203) from dataset provider and `dataset_explore.py` script which prints unique values from dataset columns.

## Transaction Table 

### TransactionID
Unique ID number of a transaction, integer number ranged from 2987000 to 3577539.

### isFraud
Boolean value showing whether transaction is fraudulent or not.

### TransactionDT
Timedelta from a given reference datetime (not an actual timestamp)

Integer number ranged from 86400 to 15811131. It might be implied that unit of measurement is second because 86400 is a number of seconds in a day (60 sec * 60 min * 24 h = 86400), 15811131 therefore corresponds to day 183, so the data spans 6 months.

### TransactionAMT

Floating point number indicating transaction payment amount in USD.

### ProductCD
Product code for each transaction. Values encountered in a dataset: `['W' 'H' 'C' 'S' 'R']`

### cardX
Payment card information, such as card type, card category, issue bank, country, etc.

card4 is a card issuer: `Discover/MasterCard/Visa/American Express`

card 6 is a card type: `credit/debit/debit or credit/change card`

card1, card2, card3, card5 are some numerical values.

### addrX
Address information, numerical format

Both addresses are for purchaser: addr1 as billing region, addr2 as billing country

### distX
Distance

Distances between (not limited) billing address, mailing address, zip code, IP address, phone area, etc.

### P_emaildomain
Purchaser email domain

Examples: `gmail.com, outlook.com, me.com, embarqmail.com, gmail, servicios-ta.com, protonmail.com`

### R_emaildomain
Recipient email domain, same format as P_emaildomain

Certain transactions don't need recipient, so R_emaildomain might be null

### C1-C14
Counting, such as how many addresses are found to be associated with the payment card, etc. The actual meaning is masked.
Can you please give more examples of counts in the variables C1-15? Would these be like counts of phone numbers, email addresses, names associated with the user? I can't think of 15.
Your guess is good, plus like device, ipaddr, billingaddr, etc. Also these are for both purchaser and recipient, which doubles the number.

### D1-D15
Timedelta, such as days between previous transaction, etc.

### M1-M9
Match, such as names on card and address, etc.

M4 has values 'M0', 'M1' and 'M2', while other have values 'T' and 'F', standing for True and False.

### Vxxx
338 columns of Vesta-engineered rich features, including ranking, counting, and other entity relations.
For example, how many times the payment card associated with a IP and email or address appeared in 24 hours time range, etc.
All Vesta features were derived as numerical. some of them are count of orders within a clustering, a time-period or condition, so the value is finite and has ordering (or ranking).



## Identity Table

### TransactionID

[see above](#transactionid)

### id_XX
id_01-id_11, id_13-id_14, id_17-id_22, id_24-id_26, id_32: Numerical features for identity, which is collected by Vesta and security partners such as device rating, ip_domain rating, proxy rating, etc. Also it recorded behavioral fingerprint like account login times/failed to login times, how long an account stayed on the page, etc. All of these are not able to elaborate due to security partner T&C. I hope you could get basic meaning of these features, and by mentioning them as numerical/categorical, you won't deal with them inappropriately.”

id_12, id_16, id_27, id_29: `['NotFound' 'Found']`

id_15: `['New' 'Found' 'Unknown']`

id_23: IP proxy information`['IP_PROXY:TRANSPARENT' 'IP_PROXY:ANONYMOUS' 'IP_PROXY:HIDDEN']`

id_28: `['New' 'Found']`

id_30: OS info (Windows/Mac OS X/Android/iOS + with or without version number / Linux/func/other without version number)

id_31: browser info (name with or without version number)

id_33: screen resolution (two integer numbers joined by 'x')

id_34: `['match_status:2' 'match_status:1' nan 'match_status:0' 'match_status:-1']`

id_35-id_38: boolean values indicated by 'T' and 'F'

### DeviceType
Type of device: mobile or desktop

### DeviceInfo
Different uncategorized information about device.

Examples: 'SAMSUNG SM-G892A Build/NRD90M', 'iOS Device', 'Windows', 'LDN-LX3 Build/HUAWEILDN-LX3', 'Z955A', 'LG-E975'
