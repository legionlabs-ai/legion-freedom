from pathlib import Path

from legion_freedom.core.openai.client import ask_ai

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