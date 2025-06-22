"""Aggregate API routers."""

from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path

from fastapi import APIRouter


router = APIRouter()


def _include_all_routers() -> None:
    package_dir = Path(__file__).resolve().parent
    package_name = __name__
    for module_info in pkgutil.iter_modules([str(package_dir)]):
        name = module_info.name
        if name.startswith("_"):
            continue
        module = importlib.import_module(f"{package_name}.{name}")
        module_router = getattr(module, "router", None)
        if module_router is not None:
            router.include_router(module_router, prefix=f"/{name}")


_include_all_routers()

