import sys

def run_adaptive_sentinel():
    print("--- ORACLE-TRADE: ENTERPRISE ADAPTIVE ENGINE ---", flush=True)

    # 1. USER INVENTORY (This is what the client 'plugs in')
    # SKU: [Product Name, HTS Code, Annual Import Volume in USD]
    user_inventory = {
        "SKU-772": ["Steel Fasteners", "7318.15.00", 12000000], # $12M volume
        "SKU-105": ["Aluminum Housing", "7606.12.30", 5000000],   # $5M volume
        "SKU-009": ["Lithium Cells", "8507.60.00", 25000000]    # $25M volume
    }

    # 2. LIVE LAW FEED (Simulating the 2026 USITC JSON update)
    # In a real scenario, this is pulled from the API we discussed
    latest_legal_updates = [
        {"hts_code": "7318.15.00", "new_rate": 0.25, "reason": "Section 232 Steel Action"},
        {"hts_code": "8507.60.00", "new_rate": 0.07, "reason": "New Green Battery Surcharge"}
    ]

    total_risk_exposure = 0

    print(f"Scanning {len(user_inventory)} SKUs against live HTS revisions...", flush=True)

    for update in latest_legal_updates:
        target_code = update["hts_code"]
        
        # Check every SKU in the user's inventory
        for sku, details in user_inventory.items():
            name, hts, volume = details
            
            if hts == target_code:
                impact = volume * update["new_rate"]
                total_risk_exposure += impact
                print(f"\n[!] CRITICAL ALERT: {sku} ({name})", flush=True)
                print(f"    - Tariff Spike: {int(update['new_rate']*100)}% ({update['reason']})", flush=True)
                print(f"    - ANNUAL FINANCIAL IMPACT: ${impact:,.2f}", flush=True)

    print("\n--- FINAL RISK SUMMARY ---", flush=True)
    if total_risk_exposure > 0:
        print(f"TOTAL EXPOSURE IDENTIFIED: ${total_risk_exposure:,.2f}", flush=True)
        print("ACTION: Reroute logistics or update pricing immediately.", flush=True)
    else:
        print("No immediate financial exposure found for your SKU list.", flush=True)

if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    run_adaptive_sentinel()
