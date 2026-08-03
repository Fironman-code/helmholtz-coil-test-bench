import math


MU_0 = 4 * math.pi * 1e-7


def helmholtz_field_at_center(
    current: float,
    radius: float,
    turns: int,
) -> float:
    """
    Calculate the magnetic field at the center of a Helmholtz coil pair.

    Args:
        current: Electric current in amperes.
        radius: Coil radius in metres.
        turns: Number of turns in each coil.

    Returns:
        Magnetic field in teslas.
    """
    if current < 0:
        raise ValueError("Current cannot be negative.")

    if radius <= 0:
        raise ValueError("Radius must be greater than zero.")

    if turns <= 0:
        raise ValueError("Number of turns must be greater than zero.")

    coefficient = (4 / 5) ** (3 / 2)

    return coefficient * MU_0 * turns * current / radius


def main() -> None:
    current = 1.0
    radius = 0.10
    turns = 100

    magnetic_field = helmholtz_field_at_center(
        current=current,
        radius=radius,
        turns=turns,
    )

    print(f"Current: {current} A")
    print(f"Radius: {radius} m")
    print(f"Turns per coil: {turns}")
    print(f"Magnetic field: {magnetic_field:.6e} T")
    print(f"Magnetic field: {magnetic_field * 1e6:.2f} µT")


if __name__ == "__main__":
    main()

