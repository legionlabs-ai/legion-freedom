from legion_freedom.core.collectors.base_collector import BaseCollector
from legion_freedom.core.intelligence.product_candidate import ProductCandidate


class AmazonCollector(BaseCollector):
    """
    Amazon marketplace collector.

    Version 1:
    Returns placeholder opportunities.

    Version 2:
    Amazon Product Advertising API.

    Version 3:
    Browser automation fallback.

    Version 4:
    AI-powered opportunity analysis.
    """

    def source_name(self) -> str:
        return "Amazon"

    def collect(self) -> list[ProductCandidate]:
        """
        Version 1 returns placeholder opportunities.

        Future versions will gather real marketplace data.
        """

        return [
            ProductCandidate(
                source="Amazon",
                product_name="Portable Blender",
                category="Kitchen",
                price="TO_BE_VERIFIED",
                rating="TO_BE_VERIFIED",
                review_count="TO_BE_VERIFIED",
                affiliate_program="Amazon Associates",
                product_url="TO_BE_VERIFIED",
                notes="Placeholder product until Amazon integration is implemented.",
            )
        ]