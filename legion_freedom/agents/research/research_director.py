from pathlib import Path

from legion_freedom.core.openai.client import ask_ai

import json

RESEARCH_DIRECTOR_PROMPT = """
You are Employee #001: Research Director for Legion Labs.

Mission:
Identify opportunities, risks, trends, and market intelligence that help Legion Labs generate revenue and make better business decisions.

Important limitation:
You do not currently have live internet access or real-time market data inside this version.
Clearly label all insights as AI-generated strategic analysis unless research notes or live sources are provided.

Rules:
- Be concise.
- Focus on action.
- Prioritize revenue opportunities.
- Do not make financial decisions.
- Provide recommendations only.
- Do not pretend to have live data.
- Clearly separate assumptions from provided notes.
"""


def load_research_notes() -> str:
    notes_path = Path("data/research_inputs/today_notes.md")

    if not notes_path.exists():
        return "No research notes provided."

    return notes_path.read_text()


def generate_daily_report() -> str:
    research_notes = load_research_notes()

    prompt = f"""
{RESEARCH_DIRECTOR_PROMPT}

Research notes provided by Charles:
{research_notes}

Generate today's executive intelligence briefing.

Use this format:

# Legion Labs Research Briefing

## Data Status

## Executive Summary

## Insights From Provided Notes

## AI Strategic Analysis

## Top 5 Opportunities

## Risks / Warnings

## Recommended Actions Today

## Assumptions
"""

    return ask_ai(prompt)

def find_affiliate_product() -> dict:
    prompt = """
You are the Research Director for Legion Labs.

Phase 1 objective:
Identify one product that could be promoted through YouTube videos,
YouTube Shorts, and TikTok Shop affiliate videos.

This version does not have live market data. Do not claim that a product
is currently trending or quote unverified prices, commissions, or sales.

Return only valid JSON using this exact structure:

{
  "product_name": "Product category or example product",
  "affiliate_program": "TikTok Shop Affiliate, Amazon Associates, or To Be Confirmed",
  "affiliate_link": "TO_BE_ADDED",
  "commission_rate": "TO_BE_VERIFIED",
  "target_audience": "Specific customer audience",
  "platforms": ["YouTube", "YouTube Shorts", "TikTok Shop"],
  "opportunity_reason": "Why this product is suitable for video-based affiliate content",
  "verification_needed": [
    "What must be checked before publishing"
  ]
}
"""

    raw_response = ask_ai(prompt)

    try:
        return json.loads(raw_response)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Research Director returned invalid JSON:\n{raw_response}"
        ) from error