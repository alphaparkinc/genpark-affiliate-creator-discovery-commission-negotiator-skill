from client import AffiliateCreatorDiscoveryCommissionNegotiatorClient

def main():
    client = AffiliateCreatorDiscoveryCommissionNegotiatorClient()
    res = client.negotiate_affiliates("Smart Consumer Robotics", 15.0)
    print(f"Targeted Affiliates: {res['targeted_affiliates_count']}")
    print(f"Projected GMV: ${res['projected_affiliate_gmv_usd']}")
    print("Negotiated Creator Deals:")
    for d in res["negotiated_deals"]:
        print(f"  - {d['creator_handle']} ({d['followers']:,} followers) -> Agreed Rate: {d['agreed_rate_pct']}%")

if __name__ == "__main__":
    main()
