def human_readable_format(value):
    suffixes = ['K', 'M', 'B', 'T', 'Q']
    for i, suffix in enumerate(suffixes, 1):
        unit = 1000 ** i
        if value < unit * 1000:
            return f"{value / unit:.1f}{suffix}"
    return f"{value:.0f}"
