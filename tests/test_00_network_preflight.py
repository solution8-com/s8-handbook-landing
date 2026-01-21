import shutil
import socket
import subprocess
import sys
import urllib.error
import urllib.request

import pytest


HOST = "www.thelmbook.com"
HEAD_URL = "https://www.thelmbook.com/wiki/"


def _run_cmd(cmd):
    return subprocess.run(
        cmd, capture_output=True, text=True, timeout=10, check=False
    )


def _dns_check():
    # Prefer getent if available
    if shutil.which("getent"):
        res = _run_cmd(["getent", "hosts", HOST])
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    # Fallback to socket.getaddrinfo
    try:
        infos = socket.getaddrinfo(HOST, None)
        addrs = {info[4][0] for info in infos}
        if addrs:
            return "\n".join(sorted(addrs))
    except socket.gaierror as exc:  # pragma: no cover - network dependent
        raise AssertionError(f"DNS resolution failed: {exc}") from exc

    raise AssertionError("DNS resolution failed: no addresses returned")


def _tcp_check():
    try:
        # Use hostname to allow the resolver to pick the right family
        with socket.create_connection((HOST, 443), timeout=5):
            return "TCP connect to 443 succeeded"
    except OSError as exc:  # pragma: no cover - network dependent
        raise AssertionError(f"TCP connect to 443 failed: {exc}") from exc


def _http_head_check():
    if shutil.which("curl"):
        res = _run_cmd(["curl", "-sS", "-I", HEAD_URL])
        if res.returncode == 0 and res.stdout:
            return res.stdout.splitlines()[:20]
        raise AssertionError(
            f"HTTPS request failed via curl (code {res.returncode}): {res.stderr}"
        )

    req = urllib.request.Request(HEAD_URL, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return [f"HTTP {resp.status}", *(f"{k}: {v}" for k, v in resp.headers.items())]
    except urllib.error.URLError as exc:  # pragma: no cover - network dependent
        raise AssertionError(f"HTTPS request failed: {exc}") from exc


def test_00_network_preflight():
    dns_info = tcp_info = http_info = ""
    try:
        dns_info = _dns_check()
        tcp_info = _tcp_check()
        http_info = _http_head_check()
    except AssertionError as exc:
        details = [
            f"DNS:\n{dns_info or '<no output>'}",
            f"TCP:\n{tcp_info or '<no output>'}",
            f"HTTP:\n{http_info or '<no output>'}",
        ]
        pytest.fail(f"{exc}\n\nPreflight details:\n" + "\n\n".join(details))
