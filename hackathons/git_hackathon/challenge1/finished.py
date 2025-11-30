import sys
def safe_float(value):
    """convert string to float
        returns float value if it's valid, None if not valid
        """
    try:
        num = float(value)
        if num != num or num in (float("inf"), float("-inf")):
            return None
        return num
    except (ValueError, TypeError):
        return None

def read_numbers_from_csv(path):
    """Read numeric values from a CSV file (one value per line).

    BUGS: this function does not correctly handle invalid values or empty lines.
    """
    numbers = []
    with open(path, "r") as f:
        for line in f:
            value = line.strip()
            num = safe_float(value)
            if num is not None:
                numbers.append(value)
    return numbers


def compute_mean(values):
    """Return the mean of a list of numbers.

    BUGS: implementation is incomplete / incorrect.
    """
    total = 0
    for v in values:
        total += v
    return total / len(values) if values else None

def compute_median(values):
    """Return the median of a list of numbers.

    BUGS: does not handle even-length lists or empty lists correctly.
    """
    if not values:
        return None
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 1:
        return sorted_values[mid]
    else:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python starter.py <data.csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    nums = read_numbers_from_csv(csv_path)
    print("Read values:", nums)

    mean_val = compute_mean(nums)
    median_val = compute_median(nums)

    print("Mean:", mean_val)
    print("Median:", median_val)

if __name__ == "__main__":
    main()


