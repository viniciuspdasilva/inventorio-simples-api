from enum import Enum

class PedidoStatus(Enum):
    INITIALIZED = 0
    PENDING = 1
    REJECTED = 2
    APPROVED = 3
    CANCELLED = 4