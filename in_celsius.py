def in_celsius(f: float) -> float:
    # Returns the Celsius equivalent of the Fahrenheit temperature.
    # Formula: (F-32) * 5 / 9 = C
    # Examples:
    # in_celsius(32.0) ~> 0.0
    # in_celsius(212.0) ~> 100.0
    # in_celsius(-40.0) ~> -40.0
    return (f-32) * 5 / 9
