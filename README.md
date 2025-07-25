# IPSolver
OSINT tool which passively retrieves a list of information for a list of IP addresses.

## How to run:
```
python3 ipsolver.py --input ips.txt --output results.csv
```
### Example Input File
```
8.8.8.8
1.1.1.1
```

## Example Results:
IP | Reverse DNS | ASN | Prefix | Country | Registry | ASN Allocated | ASN Name
-- | -- | -- | -- | -- | -- | -- | --
8.8.8.8 | dns.google | 15169 | 8.8.8.0/24 | US | arin | 1992-12-01 | GOOGLE
1.1.1.1 | one.one.one.one | 13335 | 1.1.1.0/24 | US | apnic | 2011-04-11 | CLOUDFLARENET

## Notes:
The tool currently queries Team Cymru’s WHOIS-based IP-to-ASN service.  
TODO: An optional/fallback service will be added for the next release: ipinfo.io

# IPSolver Fallback Script
A second script has been added to the repository (ipsolver-fallback.py). This script uses the "ipwhois" python library instead of the Team Cymru service and can therefore be used in case of issues with the main script.

## Usage:
```
python3 ipsolver-fallback.py ips.txt output.csv
```

## Example Result:
IP | Organization | ASN | NetName | CIDR
-- | -- | -- | -- | -- |
1.1.1.1	| CLOUDFLARENET	| US13335	| APNIC-LABS | 1.1.1.0/24
