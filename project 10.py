def fare_reconciliation_system():
    # 1. Base fares for different transit routes
    route_base_fares = {
        "Route A (Downtown)": 10.0,
        "Route B (Airport)": 25.0,
        "Route C (Suburban)": 15.0
    }

    # 2. Discount multipliers for passenger categories
    category_multipliers = {
        "Adult": 1.0,  # Full fare (100%)
        "Student": 0.5,  # 50% discount
        "Senior": 0.6  # 40% discount
    }

    # 3. Simulated ticketing & revenue data per route
    # Contains passenger counts per category and the actual revenue collected in the cash/digital box
    route_data = {
        "Route A (Downtown)": {
            "counts": {"Adult": 100, "Student": 50, "Senior": 30},
            "collected": 1200.0  # Actual collected amount
        },
        "Route B (Airport)": {
            "counts": {"Adult": 80, "Student": 10, "Senior": 20},
            "collected": 2425.0  # Matches expected exactly
        },
        "Route C (Suburban)": {
            "counts": {"Adult": 60, "Student": 40, "Senior": 10},
            "collected": 1150.0  # Actual collected amount (contains shortfall)
        }
    }

    # Header for report
    print("=" * 70)
    print("PUBLIC TRANSPORT FARE RECONCILIATION REPORT")
    print("=" * 70)
    print(f"{'Route Name':<22} | {'Expected ($)':<12} | {'Collected ($)':<13} | {'Discrepancy Status'}")
    print("-" * 70)

    total_expected = 0
    total_collected = 0

    # 4. Process each route
    for route, data in route_data.items():
        base_fare = route_base_fares[route]
        counts = data["counts"]
        collected_revenue = data["collected"]

        # Calculate expected revenue for this route
        expected_revenue = 0
        for category, count in counts.items():
            fare_per_person = base_fare * category_multipliers[category]
            expected_revenue += fare_per_person * count

        # Add to grand totals
        total_expected += expected_revenue
        total_collected += collected_revenue

        # Identify discrepancies (difference between collected and expected)
        difference = collected_revenue - expected_revenue

        if difference == 0:
            status = "Balanced"
        elif difference > 0:
            status = f"Surplus: +${difference:.2f}"
        else:
            status = f"Shortfall: -${abs(difference):.2f}"

        print(f"{route:<22} | ${expected_revenue:<11.2f} | ${collected_revenue:<12.2f} | {status}")

    print("-" * 70)

    # Grand Total summary
    total_diff = total_collected - total_expected
    print(f"{'TOTAL SYSTEM':<22} | ${total_expected:<11.2f} | ${total_collected:<12.2f} | Net Diff: ${total_diff:.2f}")


# Run the program
if __name__ == "__main__":
    fare_reconciliation_system()