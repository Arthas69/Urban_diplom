from .auth import router as auth_router
from .event import router as event_router
from .user import router as user_router

routers = [auth_router, event_router, user_router]
