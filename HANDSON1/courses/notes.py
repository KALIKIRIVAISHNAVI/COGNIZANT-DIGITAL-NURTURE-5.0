"""
REQUEST-RESPONSE CYCLE: GET /api/courses/
1. Browser sends GET /api/courses/
2. urls.py (URL router) matches path to a view
3. Middleware runs before the view (Security, Session, Auth, etc.)
4. View talks to Model (ORM) -> gets data from DB
5. View sends data to Template/Serializer
6. Response object is built
7. Middleware runs again in reverse on the way out
8. Response sent back to browser

MIDDLEWARE:
- SecurityMiddleware: adds security headers to every response
- SessionMiddleware: enables request.session for per-user data

WSGI vs ASGI:
- WSGI: synchronous, Django's default (wsgi.py)
- ASGI: async, needed for WebSockets/real-time features (asgi.py)

MVC -> MVT:
- Model -> Model (same role)
- Controller -> View (business logic)
- View (UI) -> Template (renders output)
"""