from datetime import datetime

from legion_freedom.agents.content.executive_content_director import (
    build_campaign_assets,
)
from legion_freedom.agents.research.research_director import (
    find_affiliate_product,
)
from legion_freedom.core.campaigns.campaign import Campaign


def create_campaign_id() -> str:
    return datetime.now().strftime("LL-%Y%m%d-%H%M%S")


print("=" * 60)
print("LEGION LABS MEDIA ENGINE")
print("=" * 60)

print("\nEmployee #001 — Research Director")
print("Identifying an affiliate product opportunity...")

opportunity = find_affiliate_product()

campaign = Campaign(
    campaign_id=create_campaign_id(),
    product_name=opportunity["product_name"],
    affiliate_program=opportunity["affiliate_program"],
    affiliate_link=opportunity["affiliate_link"],
    commission_rate=opportunity["commission_rate"],
    target_audience=opportunity["target_audience"],
    platforms=opportunity["platforms"],
)

campaign.research_summary = opportunity["opportunity_reason"]
campaign.add_note(
    "Research Director",
    f"Verification required: {opportunity['verification_needed']}",
)

print(f"Selected product: {campaign.product_name}")

campaign.assign_to("Executive Content Director")
campaign.update_status("Content Creation")

print("\nEmployee #002 — Executive Content Director")
print("Creating YouTube and TikTok Shop campaign assets...")

campaign.content_package = build_campaign_assets(campaign)
campaign.add_note(
    "Executive Content Director",
    "Created video scripts, campaign strategy, and production brief.",
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