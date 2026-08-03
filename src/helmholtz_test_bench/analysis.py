import csv
def load_measurements(csv_path):
    measurements = []

    with open(csv_path, encoding="utf-8", newline="") as data_file:
        reader = csv.DictReader(data_file)
        required_columns = {
            "turns",
            "coil_radius_m",
            "current_a",
            "measured_field_mt",
        }
        actual_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - actual_columns

        if missing_columns:
            missing_columns_text = ", ".join(sorted(missing_columns))
            raise ValueError(
                f"Missing required CSV columns: {missing_columns_text}"
            )

        for row in reader:
            measurement = {
                "turns": int(row["turns"]),
                "coil_radius_m": float(row["coil_radius_m"]),
                "current_a": float(row["current_a"]),
                "measured_field_mt": float(row["measured_field_mt"]),
            }
            measurements.append(measurement)

    return measurements
