def register_routes(api, app, root="api", version):
    from app.book_request import register_routes as register_routes

    # Add routes
    register_routes(api, app, version)

