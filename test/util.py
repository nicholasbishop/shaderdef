"""Unit test utilities."""

def deindent(text):
    """Remove newlines and de-indent the input."""
    lines = text.splitlines()
    out_lines = []
    for line in lines:
        out_lines.append(line.lstrip())
    return ''.join(out_lines)
