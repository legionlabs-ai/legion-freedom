import json
from datetime import datetime
from pathlib import Path

from legion_freedom.core.openai.client import ask_ai
from legion_freedom.core.products.product import Product


RESEARCH_DIRECTOR_PROMPT = """
You are Employee #001: Research Director for Legion Labs.

Mission:
Identify affiliate products and consumer opportunities with the highest
probability of generating revenue through YouTube, YouTube Shorts, and
TikTok Shop content.

Important limitation:
You do not currently have live internet access or real-time market data.
Clearly label insights as AI-generated strategic analysis unless research
notes or verified sources are provided.

Rules:
- Be concise.
- Focus on actionable affiliate opportunities.
- Prioritize revenue potential.
- Do not pretend to have live data.
- Do not invent prices, commissions, availability, or sales performance.
- Clearly separate assumptions from verified information.
"""


def load_research_notes() -> str:
    notes_path = Path("data/research_inputs/today_notes.md")

    if not notes_path.exists():
        return "No research notes provided."

    return notes_path.read_text(encoding="utf-8")


def generate_daily_report() -> str:
    research_notes = load_research_notes()

    prompt = f"""
{RESEARCH_DIRECTOR_PROMPT}

Research notes provided by Charles:

{research_notes}

Generate today's executive affiliate intelligence briefing.

Use this format:

# Legion Labs Research Briefing

## Data Status

## Executive Summary

## Insights From Provided Notes

## AI Strategic Analysis

## Top Affiliate Opportunities

## Risks and Warnings

## Recommended Actions Today

## Assumptions
"""

    return ask_ai(prompt)


def find_affiliate_product() -> dict:
    prompt = f"""
{RESEARCH_DIRECTOR_PROMPT}

Identify one product that could be promoted through YouTube videos,
YouTube Shorts, and TikTok Shop affiliate videos.

Return only valid JSON using this exact structure:

{{
  "product_name": "Product category or example product",
  "affiliate_program": "TikTok Shop Affiliate, Amazon Associates, or TO_BE_VERIFIED",
  "affiliate_link": "TO_BE_ADDED",
  "commission_rate": "TO_BE_VERIFIED",
  "target_audience": "Specific customer audience",
  "platforms": ["YouTube", "YouTube Shorts", "TikTok Shop"],
  "opportunity_reason": "Why this product is suitable for video-based affiliate content",
  "verification_needed": [
    "What must be checked before publishing"
  ]
}}
"""

    raw_response = ask_ai(prompt)

    try:
        product_data = json.loads(raw_response)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Research Director returned invalid JSON:\n{raw_response}"
        ) from error

    if not isinstance(product_data, dict):
        raise ValueError(
            "Research Director must return one JSON product object."
        )

    return product_data


def find_ranked_products() -> list[Product]:
    prompt = f"""
{RESEARCH_DIRECTOR_PROMPT}

Identify exactly three affiliate product candidates suitable for YouTube,
YouTube Shorts, and TikTok Shop videos.

Score each product from 1 to 10 for:

- demand_score
- competition_score
- commission_score
- video_potential_score
- evergreen_score
- seasonality_score
- scalability_score

A higher competition_score means a better opportunity with less competition.

Return only valid JSON using this exact structure:

[
  {{
    "product_name": "Product category or example product",
    "category": "Product category",
    "affiliate_program": "TikTok Shop Affiliate, Amazon Associates, or TO_BE_VERIFIED",
    "affiliate_link": "TO_BE_ADDED",
    "commission_rate": "TO_BE_VERIFIED",
    "target_audience": "Specific target audience",
    "price": "TO_BE_VERIFIED",
    "demand_score": 1,
    "competition_score": 1,
    "commission_score": 1,
    "video_potential_score": 1,
    "evergreen_score": 1,
    "seasonality_score": 1,
    "scalability_score": 1,
    "opportunity_reason": "Why this product is suitable for video affiliate content",
    "verification_needed": [
      "Items that must be checked before publishing"
    ]
  }}
]
"""

    raw_response = ask_ai(prompt)

    try:
        product_data = json.loads(raw_response)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Research Director returned invalid JSON:\n{raw_response}"
        ) from error

    if not isinstance(product_data, list) or len(product_data) != 3:
        raise ValueError(
            "Research Director must return exactly three product candidates."
        )

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    products: list[Product] = []

    for index, item in enumerate(product_data, start=1):
        product = Product(
            product_id=f"PR-{timestamp}-{index}",
            product_name=item["product_name"],
            category=item["category"],
            affiliate_program=item["affiliate_program"],
            affiliate_link=item["affiliate_link"],
            commission_rate=item["commission_rate"],
            target_audience=item["target_audience"],
            price=item["price"],
            demand_score=item["demand_score"],
            competition_score=item["competition_score"],
            commission_score=item["commission_score"],
            video_potential_score=item["video_potential_score"],
            evergreen_score=item["evergreen_score"],
            seasonality_score=item["seasonality_score"],
            scalability_score=item["scalability_score"],
            opportunity_reason=item["opportunity_reason"],
            verification_needed=item["verification_needed"],
        )
        products.append(product)

    return sorted(
        products,
        key=lambda product: product.average_score(),
        reverse=True,
    )