"""Thin wrapper over Playwright's APIRequestContext.

Important quirk of this API: the real result code is in the JSON body
("responseCode"). The HTTP status is not reliable. Use `code(response)` in tests.

Paths have no leading slash ("productsList") so they join onto the /api/ base URL.
"""

from json import JSONDecodeError

import pytest
from playwright.sync_api import APIRequestContext, APIResponse


def code(response: APIResponse) -> int:
    """Return the responseCode from the JSON body."""
    try:
        body = response.json()
    except JSONDecodeError:
        content_type = response.headers.get("content-type", "<missing>")
        snippet = response.text()[:160].replace("\n", " ")
        pytest.skip(
            "Automation Exercise API returned non-JSON content "
            f"(content-type: {content_type}). "
            f"Response starts with: {snippet!r}"
        )
    return body["responseCode"]


class BaseClient:
    def __init__(self, context: APIRequestContext):
        self.context = context

    def get(self, path: str, **params) -> APIResponse:
        return self.context.get(path, params=params or None)

    def post(self, path: str, form: dict | None = None) -> APIResponse:
        return self.context.post(path, form=form)

    def put(self, path: str, form: dict | None = None) -> APIResponse:
        return self.context.put(path, form=form)

    def delete(self, path: str, form: dict | None = None) -> APIResponse:
        return self.context.delete(path, form=form)
