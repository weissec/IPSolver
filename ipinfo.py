import subprocess
import csv
import socket
import time
import argparse
import sys

# Banner
banner = """   _______  _      ___   
  /  _/ _ \\(_)__  / _/__ 
 _/ // ___/ / _ \\/ _/ _ \\
/___/_/  /_/_//_/_/ \\___/
                         
Retrieves: Reverse DNS, ASN, Prefix/CIDR, Country, Registry, ASN Allocated, ASN Name
"""
print(banner)

# Command-line argument parsing
parser = argparse.ArgumentParser(description="Query IP info via Team Cymru WHOIS and reverse DNS")
parser.add_argument("-i", "--input", required=True, help="Path to input file containing IP addresses")
parser.add_argument("-o", "--output", default="ip_info.csv", help="Path to output CSV file")
args = parser.parse_args()

INPUT_FILE = args.input
OUTPUT_FILE = args.output

# Load IPs
try:
    with open(INPUT_FILE) as f:
        ips = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"❌ Input file not found: {INPUT_FILE}")
    sys.exit(1)

if not ips:
    print("❌ No IPs found in input file.")
    sys.exit(1)

results = []

print(f"🔍 Querying {len(ips)} IPs individually...\n")

for ip in ips:
    try:
        cmd = f'whois -h whois.cymru.com " -v {ip}"'
        output = subprocess.check_output(cmd, shell=True, timeout=10).decode()

        lines = output.strip().splitlines()
        if len(lines) < 2:
            print(f"⚠️ No data for {ip}")
            continue
        data_line = lines[1]
        parts = [p.strip() for p in data_line.split("|")]
        if len(parts) < 7:
            print(f"⚠️ Unexpected format for {ip}")
            continue

        asn, ip_out, prefix, cc, registry, allocated, as_name = parts

        try:
            reverse_dns = socket.gethostbyaddr(ip)[0]
        except Exception:
            reverse_dns = "N/A"

        results.append({
            "IP": ip_out,
            "Reverse DNS": reverse_dns,
            "ASN": asn,
            "Prefix": prefix,
            "Country": cc,
            "Registry": registry,
            "ASN Allocated": allocated,
            "ASN Name": as_name
        })

        print(f"✅ {ip_out} → {reverse_dns} | ASN {asn}")
        time.sleep(0.5)

    except subprocess.TimeoutExpired:
        print(f"⏱️ Timeout querying {ip}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error querying {ip}: {e}")
    except Exception as e:
        print(f"❌ Unexpected error with {ip}: {e}")

if not results:
    print("❌ No data collected.")
    sys.exit(1)

# Write to CSV
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print(f"\n📄 Results saved to: {OUTPUT_FILE}")
