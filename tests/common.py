"""Provide common pytest fixtures."""
import base64
import os


def _make_packet(s: str) -> bytes:
    """Make a packet-bytes from a base64 string."""
    return bytes.fromhex(base64.b64decode(s).decode("utf-8"))


TEST_PACKETS = {
    "discovery1": _make_packet(
        """
    NWQ3NjcyYTI4YTAyMzA2M2ZiNjcyZjA3YmM3MDdkYzY0MjJiYTJmNWQ3MzBhZWVkNTA4ZjA1YTJjMj
    AyOTA5YTViMTI4MWNkNzM2NjA2NjUwZWU4NzA4ZmY0MDU2OTI0NWI3MTQ3N2UzMzYzYzgzMDA5MjQ0
    ZTU4MzZlMWYyOTg1NDI4ZTUxYTRjNTllODYyOGMyMjRjMWYxNjBmMWE5ZTk4YTZhZWQxYjc3ZTk1ZT
    BiNGIzYWVhYzhjYmJjZTdmMzZmMDdjMTc5NzgwYTVlOTAyZDJlNWY5Y2M4MDhhNWQxMmNlZjQ4NDJi
    OThlN2MwYjc5MjQxOTlhNmMyZmQyMGUxZjg4ZjVmYTE1MDJhYWMyMmY3YWMyYjkwMTBhYjE5MjIzMD
    ZmZjA0MGYxN2M3Y2I2NzBiNzA4OTIwNmEy
    """
    ),
    "discovery2": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGZiNjcyZjA3YmM3MDdkYzY0MjJiYTJmNWQ3MzVhZWVkNTA4ZjA1YTJjMj
    AyOTA5YTViMTI4MWNjNzM2NjA2NjUwZWU4NzA4MmUxNDA2OTI2NTk3OTNmNWQxNjNhZjgxZjBmMTQ3
    NjBiNzNlNzgyZDQwM2E3OWNkNmJiZTI2OGFjYmQwYjdjMmUxNzAxNjhjNWMzZWE4ODg0ZWMyMmMwZj
    ZiNmI0YWVhZjljZGM5OTI1Mzg5MTIxNGQ4OTg2OTFkZjMyZTZlYmFkODhhZGQ2NGU2ZmQzOTI4NjNh
    OWJmMWEwZjJiMjc5Yjc5N2MyZmQyZGUxZmQ0ZmY3YTQzZDJlNjk4YWYyNTBkNDZhMTBhZmUwZGRjYm
    FmNTg0N2Y1ODc4M2I2NzA=
    """
    ),
    "hostname": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdlYzc0MjJiYTJmNWQ3MzVhZWVkNTA4ZjUyNTNjMj
    AyOTA5YTViMTI4MWNjNzM2NjA2NjUwZWU4NzA4MmUxNDA2OTI2NTk3OTNmNWQxNjNhZjgxZjBmMTQ3
    NjBiNzNlNzgyZDQwM2E3OWNkNmJiZTI2OGFjYmQwYjdjMmUxNzAxNjhjNWMzZWE4ODg0ZWMyMmMwZj
    ZiNmI0YWVhZjljZGM5OTI1Mzg5MTIxNGQ4OTg2OTFkZjMyZTZlYmFkODhhZGQ2NGU2ZmQzOTI4NjNh
    OWJmMWEwZjJiMjc5Yjc5N2MyZmQyZGUxZmQ0ZmY3YTQzZDJlNjk4YWYyNTBkNDZhMTBhZmUwZGRjYm
    FmNTg0N2Y1ODc4M2I2NzA=
    """
    ),
    "num_ports": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdlMDA0MjJiYTJmNWQ3ODZhZWVkNTA4ZjAwMTljMj
    AyOTA5YTViMTk4MWM3MjJkNWQ0MzY0OQ==
    """
    ),
    "ports": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdjZWU0MjJiYTJmNWQ3ZjRhZWVkNTA4ZjQwMjBjMj
    AyOTA5YTRiMTM4MWMxMjYyYjJiMzc0ZmQ5NDBhN2E0NDA2ZTI2NTg3MTRkMmE3ZjRlOGI3NzM4MTM3
    NTA5NzNlMGY0OWI1NDNlZmRiY2JjZTE2OWIzOGQyNTRjMDAzNzIxMmFiN2FmODdlY2E1ZDgxMmYxM2
    Y3OTgzOWY=
    """
    ),
    "trunk": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdjYjg0MjJiYTJmNWQ3ODJhZWVkNTA4ZjU2ZGVjMj
    AyOTA5YTQ5MTM4MWMzMjYyYTJiMzY0OTI2YmZiN2E0
    """
    ),
    "mtu_vlan": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdkYmM0MjJiYTJmNWQ3ODVhZWVkNTA4ZjA4YWFjMj
    AyOTA5YTdiMTM4MWM0MjcyYmQ0Yzk0OWQ5
    """
    ),
    "vlan": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdlYzY0MjJiYTJmNWQ3ZjFhZWVkNTA4Zjc2YjBjMj
    AyOTA5YTc5MTM4MWM3MjYwODJhMzY1ZWQ5NDFiN2E0NDA3NjI0NTk3MTRjNmUxYTI4ZmEwMjU0NjAy
    OTVlM2ZhMGJjOWI3NjJmZmRhZGJiZDc2OGIzOGMzNDRjMDAyNzIxNmRmMWU3Y2ZhMmUzZGUzMGYyYz
    A4N2EzNjA2NWJjOGU=
    """
    ),
    "pvid": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdmZDk0MjJiYTJmNWQ3ZTNhZWVkNTA4ZjUxYWFjMj
    AyOTA5YTc5MTE4MWM1MjYyYTE5MTQ0YmQ5NDNiNWE0NDE0YjI2NTk3MjRmMmE3ZTZjOTk3NzNiMTA3
    NjA5NTFlM2YyOTg1MTJlZmM5ZWI4ZTU2OTkzNzNkYTRjMDA=
    """
    ),
    # qos1
    # qos2
    # mirror
    # stats
    # loop_prev
    "stats": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdlNWM0MjJiYTJmNWQ3MzhhZWVkNTA4ZjAyYThjMj
    AyOTA5YTFiMTM4MWQ1MjYyYjJkMzZkMDNjYzJiN2E0NDA2OTI0NDk0NGQzMmE3ZjRlOWIzNzM4MTQ2
    NTBhNzJlMWYyOWI1NDJlZmRiY2JiZTU2OGIzOGMyNTRjMDAyNzIxNmFiMGFhOTVlZmE1ZDgxMzkxMj
    RiZDgzOWY5YWJjOGU3ZGNlNmJhMjE5N2JiOWYzOTFkZjI5ZTJlNGY5YzQ4MDg1MDk1ZWUzYTdjMzFh
    YThkZjkwZjJiMjcwYjdkNmMyZmQzYWU0Zjg4OTVmMzE2ZTg3NmM4YWY2YWYyYWU4OWJhM2U2ZGRjZj
    c2MGZiOWYxNzg=
    """
    ),
    "login1": _make_packet(
        """
    NWQ3NjFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdjYmU0MjJiYTJmNWQ3OGJhZWVkNTA4ZjU2ZGVjMj
    AyOTA5YWE0ZWM4MWM2
    """
    ),
    "login2": _make_packet(
        """
    NWQ3MDFhNGIyYTM3ZDFkOGU3NzAwYjI2ODUzMTdjYjk0MjJiYTJmNWQ3OGJhZWVkNTA4ZjU2ZGVjMj
    AyOTA5YWE0ZWM4MWM2
    """
    ),
}


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        return fptr.read()
