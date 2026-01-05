def validate_data(sales_data, threshold):
    if not sales_data or threshold is None or threshold <= 0:
        return False
    for p in sales_data:
        if p.get("name") is None or p.get("qty") is None or p["qty"] < 0:
            return False
    return True

def classify_products(sales_data, threshold):
    results = []
    for product in sales_data:
        if product["qty"] > threshold:
    label = "Top Product"        
else:
    label = "Standard Product"  

        results.append({"name": product["name"], "qty": product["qty"], "label": label})
    return results

def generate_report(results):
    lines = ["Sales Analysis Report"]
    for r in results:
        lines.append(f"{r['name']}: {r['qty']} → {r['label']}")
    return "\n".join(lines)

def main():
    sales_data = [
        {"name": "Product A", "qty": 120},
        {"name": "Product B", "qty": 80},
    ]
    threshold = 100

    if not validate_data(sales_data, threshold):
        print("Error: Invalid data. Please correct and retry.")
        return

    results = classify_products(sales_data, threshold)
    report = generate_report(results)
    print(report)

if __name__ == "__main__":
    main()
