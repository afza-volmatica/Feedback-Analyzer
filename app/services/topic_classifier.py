def classify_topic(review: str):

    review = review.lower()

    # Delivery
    if any(word in review for word in [
        "delivery",
        "delivered",
        "shipping",
        "shipment",
        "package",
        "courier",
        "arrived late",
        "late delivery"
    ]):
        return "Delivery Issues"

    # Payment
    if any(word in review for word in [
        "payment",
        "card",
        "charged",
        "charge",
        "billing",
        "refund",
        "money",
        "debit",
        "credit card"
    ]):
        return "Payment Issues"

    # Login
    if any(word in review for word in [
        "login",
        "password",
        "account",
        "sign in",
        "authentication",
        "otp"
    ]):
        return "Account Issues"

    # Customer Support
    if any(word in review for word in [
        "customer service",
        "support",
        "representative",
        "agent",
        "help desk"
    ]):
        return "Customer Support"

    # Website/App
    if any(word in review for word in [
        "website",
        "app",
        "bug",
        "crash",
        "slow",
        "loading",
        "dashboard"
    ]):
        return "Website/App Issues"

    # Product Quality
    if any(word in review for word in [
        "broken",
        "defective",
        "damaged",
        "quality",
        "faulty"
    ]):
        return "Product Quality"

    return "Other"