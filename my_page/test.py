match x:
    case host, port:
        mode = "http"
    case host, port, mode:
        pass