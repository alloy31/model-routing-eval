"""설정 로더. base.json 위에 환경별 파일을 덮어쓴 뒤 레거시 키와 환경변수를 반영한다."""
import json
import os
import pathlib

CONFIG_DIR = pathlib.Path(__file__).resolve().parent.parent / "config"
ENV_PREFIX = "SHIPLANE__"
ENV_OVERRIDABLE = ("http.retries", "features.bulk_quotes")
# 구버전 배포 스크립트가 쓰던 키. 값이 있으면 새 키를 덮어쓴다.
LEGACY_ALIASES = {"net.request_timeout_s": "http.timeout"}


def _deep_merge(a, b):
    out = dict(a)
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def _get(d, dotted, default=None):
    cur = d
    for part in dotted.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return default
        cur = cur[part]
    return cur


def _set(d, dotted, value):
    parts = dotted.split(".")
    cur = d
    for part in parts[:-1]:
        cur = cur.setdefault(part, {})
    cur[parts[-1]] = value


class Settings:
    def __init__(self, data, env):
        self._d = data
        self.env = env

    def get(self, dotted, default=None):
        return _get(self._d, dotted, default)

    @property
    def http_timeout(self):
        return self.get("http.timeout")

    @property
    def http_retries(self):
        return self.get("http.retries")


def load(env=None):
    env = env or os.environ.get("SHIPLANE_ENV", "dev")
    data = json.loads((CONFIG_DIR / "base.json").read_text())
    overlay = CONFIG_DIR / f"{env}.json"
    if overlay.exists():
        data = _deep_merge(data, json.loads(overlay.read_text()))
    for legacy, modern in LEGACY_ALIASES.items():
        value = _get(data, legacy)
        if value is not None:
            _set(data, modern, value)
    for key in ENV_OVERRIDABLE:
        raw = os.environ.get(ENV_PREFIX + key.replace(".", "__").upper())
        if raw is not None:
            _set(data, key, json.loads(raw))
    return Settings(data, env)
