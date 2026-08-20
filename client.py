class AffiliateCreatorDiscoveryCommissionNegotiatorClient:
    def negotiate_affiliates(self, product_category: str, max_commission_rate_pct: float = 15.0) -> dict:
        deals = [
            {"creator_handle": "@tech_gadget_queen", "followers": 850000, "agreed_rate_pct": 12.5, "exclusive_live_agreed": True},
            {"creator_handle": "@future_living_daily", "followers": 420000, "agreed_rate_pct": 10.0, "sample_unit_sent": True}
        ]
        return {
            "targeted_affiliates_count": 35,
            "negotiated_deals": deals,
            "projected_affiliate_gmv_usd": 68000.0
        }
