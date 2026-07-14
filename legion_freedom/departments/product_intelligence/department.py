from legion_freedom.core.intelligence.marketplace import Marketplace


class ProductIntelligenceDepartment:
    """
    Manages all marketplace intelligence for Legion Labs.
    """

    def __init__(self):
        self.marketplace = Marketplace()

    def collect_marketplace_data(self):
        return self.marketplace.collect_all()