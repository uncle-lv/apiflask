from __future__ import annotations

from flask import Blueprint

from .helpers import _sentinel
from .route import route_patch
from .scaffold import APIScaffold


@route_patch
class APIBlueprint(APIScaffold, Blueprint):
    """Flask's `Blueprint` object with some web API support.

    Examples:

    ```python
    from apiflask import APIBlueprint

    bp = APIBlueprint('foo', __name__)
    ```

    *Version changed: 0.5.0*

    - Add `enable_openapi` parameter.

    *Version added: 0.2.0*
    """

    def __init__(
        self,
        name: str,
        import_name: str,
        tag: str | dict | None = None,
        enable_openapi: bool = True,
        static_folder: str | None = None,
        static_url_path: str | None = None,
        template_folder: str | None = None,
        url_prefix: str | None = None,
        subdomain: str | None = None,
        url_defaults: dict | None = None,
        root_path: str | None = None,
        cli_group: str | None = _sentinel,  # type: ignore
    ) -> None:
        """Make a blueprint instance.

        Arguments:
            name: The name of the blueprint. Will be prepended to
                each endpoint name.
            import_name: The name of the blueprint package, usually
                `__name__`. This helps locate the `root_path` for the
                blueprint.
            tag: The tag of this blueprint. If not set, the
                `<blueprint name>.title()` will be used (`'foo'` -> `'Foo'`).
                Accepts a tag name string or an OpenAPI tag dict.
                Example:

                ```python
                bp = APIBlueprint('foo', __name__, tag='Foo')
                ```

                ```python
                bp = APIBlueprint('foo', __name__, tag={'name': 'Foo'})
                ```
            enable_openapi: If `False`, will disable OpenAPI support for the
                current blueprint.

        Other keyword arguments are directly passed to `flask.Blueprint`.
        """
        super().__init__(
            name,
            import_name,
            static_folder=static_folder,
            static_url_path=static_url_path,
            template_folder=template_folder,
            url_prefix=url_prefix,
            subdomain=subdomain,
            url_defaults=url_defaults,
            root_path=root_path,
            cli_group=cli_group,
        )
        self.tag = tag
        self.enable_openapi = enable_openapi
