import csv
import pytest
import os
from wizard_rank import get_wizard_title

def load_test_cases(csv_file="test.csv"):
    """Load test cases from CSV file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, csv_file)
    
    cases = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                mana = int(row["x"])
                attack = int(row["y"])
                expected = row["expected"]
                cases.append((mana, attack, expected))
    except FileNotFoundError:
        print(f"Warning: File {csv_file} not found!")
    
    return cases

@pytest.mark.parametrize("mana,attack,expected", load_test_cases("control_flow.csv"))
def test_control_flow(mana, attack, expected):
    result = get_wizard_title(mana, attack)
    print(f"| result={result}, expected={expected}")
    assert result == expected, f"Failed for mana={mana}, attack={attack}: got {result}, expected {expected}"

