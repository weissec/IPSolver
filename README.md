# ipinfo
OSINT tool which passively retrieves a list of information for a list of IP addresses.

## How to run:
```
python3 ipinfo.py --input ips.txt --output results.csv
```
## Example Results:
IP | Reverse DNS | ASN | Prefix | Country | Registry | ASN Allocated | ASN Name
-- | -- | -- | -- | -- | -- | -- | --
8.8.8.8 | dns.google | 15169 | 8.8.8.0/24 | US | arin | 1992-12-01 | GOOGLE
1.1.1.1 | one.one.one.one | 13335 | 1.1.1.0/24 | US | apnic | 2011-04-11 | CLOUDFLARENET


