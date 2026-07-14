from datetime import datetime


class RevenueDashboard:
    """
    Legion Labs CEO Dashboard.
    Version 1.
    """

    def display(self) -> None:
        print("=" * 60)
        print("LEGION LABS")
        print("CEO MORNING BRIEF")
        print("=" * 60)

        print(f"Date: {datetime.now():%Y-%m-%d}")

        print("\nMission")
        print("Generate the first $100 in affiliate revenue.")

        print("\nToday's Priorities")
        print("- Identify affiliate opportunities")
        print("- Generate Creator Packages")
        print("- Produce videos")
        print("- Publish content")
        print("- Review performance")

        print("\nBusiness Metrics")
        print("Affiliate Revenue: $0.00")
        print("Videos Published: 0")
        print("Creator Packages Ready: 0")
        print("Top Opportunity: Pending")