class OpportunityScorer:
    """
    Calculates the Legion Opportunity Score (LOS).

    This class will evolve as Legion Labs learns from
    real campaign performance.
    """

    WEIGHTS = {
        "demand": 0.20,
        "competition": 0.15,
        "video_potential": 0.20,
        "commission": 0.15,
        "price": 0.10,
        "evergreen": 0.10,
        "trend_velocity": 0.10,
    }

    def score(self, metrics: dict) -> float:
        score = 0.0

        for key, weight in self.WEIGHTS.items():
            score += metrics.get(key, 0) * weight

        return round(score, 2)