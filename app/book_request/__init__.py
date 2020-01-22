BASE_ROUTE = "request"


def register_routes(api, app, root="api" , version = "v0.1"):
    from .controller import api as request_api

    api.add_namespace(request_api, path=f"/{root}/{version}/{BASE_ROUTE}")
