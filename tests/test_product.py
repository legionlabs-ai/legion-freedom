from legion_freedom.core.products.product import Product


product = Product(
    product_id="PR-0001",
    product_name="Portable Blender",
    category="Kitchen",
    affiliate_program="TikTok Shop Affiliate",
    affiliate_link="TO_BE_ADDED",
    commission_rate="TO_BE_VERIFIED",
    target_audience="Busy adults and fitness-focused consumers",
    price="TO_BE_VERIFIED",
    demand_score=9,
    competition_score=7,
    commission_score=8,
    video_potential_score=10,
    evergreen_score=8,
    seasonality_score=7,
    scalability_score=9,
    opportunity_reason=(
        "Easy to demonstrate visually and suitable for short-form product videos."
    ),
    verification_needed=[
        "Confirm current price",
        "Confirm commission rate",
        "Confirm product availability",
    ],
)

print("Product:", product.product_name)
print("Total Score:", product.total_score())
print("Average Score:", product.average_score())
print("Recommendation:", product.recommendation())