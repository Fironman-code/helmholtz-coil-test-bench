import pytest

from helmholtz_test_bench.analysis import load_measurements


def test_load_measurements_reads_csv():
    rows = load_measurements("data/raw/sample_measurements.csv")

    assert len(rows) == 5
    assert rows[0]["turns"] == 200
    assert rows[1]["current_a"] == 0.25


@pytest.mark.parametrize(
    ("missing_column", "header"),
    [
        ("turns", "coil_radius_m,current_a,measured_field_mt\n"),
        ("coil_radius_m", "turns,current_a,measured_field_mt\n"),
        ("current_a", "turns,coil_radius_m,measured_field_mt\n"),
        ("measured_field_mt", "turns,coil_radius_m,current_a\n"),
    ],
)
def test_load_measurements_rejects_missing_required_column(
    tmp_path, missing_column, header
):
    csv_path = tmp_path / f"missing_{missing_column}.csv"
    csv_path.write_text(header, encoding="utf-8")

    with pytest.raises(ValueError, match=missing_column):
        load_measurements(csv_path)
