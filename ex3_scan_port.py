from __future__ import annotations

import argparse
from socket import AF_INET, SOCK_STREAM, socket


def main(args=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("host", nargs="?", default="adamj.eu")
    parser.add_argument("port", type=int, nargs="?", default=80)
    parser.add_argument("--timeout", type=float, default=1.0)
    args = parser.parse_args(args)

    is_open = check_port(args.host, args.port, args.timeout)

    if is_open:
        print(f"✅ Port {args.port} is open")
        return 0
    else:
        print(f"❌ Port {args.port} is not open")
        return 1


def check_port(host: str, port: int, timeout: float) -> bool:
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        return result == 0


if __name__ == "__main__":
    exit(main())
