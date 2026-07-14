from legion_freedom.agents.research.research_director import (
    find_ranked_products,
)


products = find_ranked_products()

print("=" * 60)
print("LEGION LABS — RANKED PRODUCT OPPORTUNITIES")
print("=" * 60)

for position, product in enumerate(products, start=1):
    saved_path = product.save_json()

    print(f"\n#{position} — {product.product_name}")
    print(f"Category: {product.category}")
    print(f"Affiliate Program: {product.affiliate_program}")
    print(f"Average Score: {product.average_score()}/10")
    print(f"Recommendation: {product.recommendation()}")
    print(f"Reason: {product.opportunity_reason}")
    print(f"Saved to: {saved_path}")

winner = products[0]

print("\n" + "=" * 60)
print("RECOMMENDED WINNER")
print("=" * 60)
print(f"Product: {winner.product_name}")
print(f"Score: {winner.average_score()}/10")
print(f"Recommendation: {winner.recommendation()}")