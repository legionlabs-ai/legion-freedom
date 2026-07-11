from pathlib import Path
from legion_freedom.core.campaigns.campaign import Campaign
from legion_freedom.core.openai.client import ask_ai


def load_handbook() -> str:
    handbook_path = Path(
        "Knowledge/employees/executive_content_director.md"
    )

    if not handbook_path.exists():
        raise FileNotFoundError(
            f"Employee handbook not found: {handbook_path}"
        )

    return handbook_path.read_text(encoding="utf-8")


def create_content_package(research_report: str) -> str:
    handbook = load_handbook()

    prompt = f"""
You are the Executive Content Director for Legion Labs.

Follow this employee handbook:

{handbook}

The Research Director provided this briefing:

{research_report}

Select the single opportunity most likely to generate revenue quickly.

Create a complete content package using this format:

# Legion Labs Content Package

## Selected Opportunity

## Why This Opportunity Was Selected

## Target Audience

## Affiliate or Revenue Angle

## YouTube Video
### Title
### Hook
### Full Script
### Description
### Call to Action
### Thumbnail Concept
### Thumbnail Image Prompt

## YouTube Short
### Hook
### Script
### Caption

## TikTok Video
### Hook
### Script
### Caption
### Hashtags
### Call to Action

## Verification Needed
List any facts, product claims, prices, commissions, or statistics
that must be verified before publishing.

Do not invent live trends, prices, commissions, or product performance.
Clearly label assumptions.
"""

    return ask_ai(prompt)

def build_campaign_assets(campaign: Campaign) -> str:
    handbook = load_handbook()

    prompt = f"""
You are the Executive Content Director for Legion Labs.

Follow this handbook:

{handbook}

Create an affiliate video campaign for this product:

Product: {campaign.product_name}
Affiliate Program: {campaign.affiliate_program}
Target Audience: {campaign.target_audience}
Platforms: {", ".join(campaign.platforms)}
Research Summary: {campaign.research_summary}

Create this package:

# Campaign Strategy

## Product Positioning

## Target Customer

## Revenue Angle

# YouTube Video

## Title

## Hook

## Full Script

## Description

## Affiliate Disclosure

## Call to Action

## Thumbnail Concept

# YouTube Short

## Hook

## Script

## Caption

## Call to Action

# TikTok Shop Video

## Hook

## Script

## On-Screen Text

## Caption

## Hashtags

## Affiliate Call to Action

# Video Production Brief

## Visual Style

## Scene List

## Voiceover Direction

## B-Roll or Product Shots Needed

## Captions

# Verification Checklist

List every product claim, price, commission, feature, statistic,
or affiliate detail that must be verified before publishing.

Do not invent product facts or claim access to live trends.
"""

    return ask_ai(prompt)