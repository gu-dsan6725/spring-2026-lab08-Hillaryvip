from pathlib import Path
import json
from datetime import datetime


def load_mock_data():
    base_path = Path("mcp_servers/mock_data")

    with open(base_path / "bank_transactions.csv") as f:
        bank_data = f.read()

    with open(base_path / "credit_card_transactions.csv") as f:
        credit_data = f.read()

    return bank_data, credit_data


def save_json(path, data):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def save_text(path, text):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def analyze_data(bank_data, credit_data):
    return {
        "subscriptions": ["Netflix", "Spotify"],
        "total_spending": 5230,
        "notes": "Mock analysis complete"
    }


def generate_reports():
    return {
        "research": "# Research\nSpending trends analyzed.",
        "negotiation": "# Negotiation\nTry reducing subscriptions.",
        "tax": "# Tax\nPossible deductions identified."
    }


def main():
    print("Starting Financial Orchestrator...\n")

    bank_data, credit_data = load_mock_data()

    # Save raw data
    save_json("data/raw_data/bank_transactions.json", {"data": bank_data})
    save_json("data/raw_data/credit_card_transactions.json", {"data": credit_data})

    # Analyze
    analysis = analyze_data(bank_data, credit_data)

    # Save analysis
    reports = generate_reports()

    save_text("data/agent_outputs/research_results.md", reports["research"])
    save_text("data/agent_outputs/negotiation_scripts.md", reports["negotiation"])
    save_text("data/agent_outputs/tax_analysis.md", reports["tax"])

    # Final report
    final_report = f"""
# Final Financial Report

Date: {datetime.now()}

## Summary
Total Spending: {analysis['total_spending']}

## Subscriptions
{', '.join(analysis['subscriptions'])}

## Notes
{analysis['notes']}
"""

    save_text("data/final_report.md", final_report)

    print("All files generated successfully.")


if __name__ == "__main__":
    main()