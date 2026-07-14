from legion_freedom.core.collectors.amazon_collector import AmazonCollector


class Marketplace:
    """
    Coordinates all marketplace collectors.
    """

    def __init__(self):
        self.collectors = [
            AmazonCollector(),
        ]

    def collect_all(self):
        candidates = []

        for collector in self.collectors:
            candidates.extend(collector.collect())

        return candidates