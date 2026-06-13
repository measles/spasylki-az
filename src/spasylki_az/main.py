"""
Main application module.

This file is part of spasylki-az.

spasylki-az is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License v3 (LGPLv3) as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

spasylki-az is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License v3 (LGPLv3) for
more details. In file LICENSE which should came with a package, or look at it
in the repo, see <https://github.com/measles/spasylki-az/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3
(LGPLv3) along with Łatynkatar. If not, see <https://www.gnu.org/licenses/>.

:copyright: (c) 2026 Andrej Zacharevicz: https://github.com/measles/spasylki-az
"""

from __future__ import annotations

from typing import TYPE_CHECKING

# pylint: disable-next=import-error
from data.links import SECTIONS  # type: ignore[import-not-found]
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# These are ONLY executed by the type checker
if TYPE_CHECKING:
    from starlette.templating import _TemplateResponse as TemplateResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request) -> TemplateResponse:
    """Read root."""
    return templates.TemplateResponse(
        request=request, name="index.jinja2", context={"links": SECTIONS}
    )
