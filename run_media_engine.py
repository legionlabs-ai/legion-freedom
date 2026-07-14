from datetime import datetime

from legion_freedom.agents.content.executive_content_director import (
    build_campaign_assets,
)
from legion_freedom.agents.research.research_director import (
    find_ranked_products,
)
from legion_freedom.core.campaigns.campaign import Campaign
from legion_freedom.dashboard.revenue_dashboard import RevenueDashboard


def create_campaign_id() -> str:
    return datetime.now().strftime("LL-%Y%m%d-%H%M%S")


def run_revenue_engine() -> None:
    dashboard = RevenueDashboard()
    dashboard.display()

    print()
    print("=" * 60)
    print("LEGION LABS REVENUE ENGINE")
    print("=" * 60)

    print("\nEmployee #001 — Research Director")
    print("Generating and ranking affiliate product opportunities...")

    products = find_ranked_products()

    for position, product in enumerate(products, start=1):
        product.save_json()

        print(
            f"#{position} — {product.product_name} "
            f"({product.average_score()}/10 — {product.recommendation()})"
        )

    winner = products[0]

    print("\nSelected opportunity:")
    print(f"Product: {winner.product_name}")
    print(f"Score: {winner.average_score()}/10")
    print(f"Recommendation: {winner.recommendation()}")

    campaign = Campaign(
        campaign_id=create_campaign_id(),
        product_name=winner.product_name,
        affiliate_program=winner.affiliate_program,
        affiliate_link=winner.affiliate_link,
        commission_rate=winner.commission_rate,
        target_audience=winner.target_audience,
        platforms=["YouTube", "YouTube Shorts", "TikTok Shop"],
    )

    campaign.research_summary = winner.opportunity_reason
    campaign.add_note(
        "Research Director",
        f"Product score: {winner.average_score()}/10. "
        f"Recommendation: {winner.recommendation()}. "
        f"Verification required: {winner.verification_needed}",
    )

    campaign.assign_to("Executive Content Director")
    campaign.update_status("Content Creation")

    print("\nEmployee #002 — Executive Content Director")
    print("Creating campaign assets...")

    campaign.content_package = build_campaign_assets(campaign)
    campaign.add_note(
        "Executive Content Director",
        "Created YouTube, YouTube Shorts, and TikTok Shop campaign assets.",
    )

    campaign.assign_to("CEO")
    campaign.update_status("Awaiting Human Review")

    saved_path = campaign.save_json()

    print("\n" + "=" * 60)
    print("CAMPAIGN COMPLETE")
    print("=" * 60)
    print(f"Campaign ID: {campaign.campaign_id}")
    print(f"Product: {campaign.product_name}")
    print(f"Status: {campaign.status}")
    print(f"Owner: {campaign.owner}")
    print(f"Saved to: {saved_path}")

    print("\nCONTENT PACKAGE\n")
    print(campaign.content_package)


if __name__ == "__main__":
    run_revenue_engine()