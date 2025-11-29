gpu_nodes = [
    {"id": "gpu-1", "available": True},
    {"id": "gpu-2", "available": True}
]

def get_available_gpu():
    for gpu in gpu_nodes:
        if gpu["available"]:
            gpu["available"] = False
            return gpu["id"]
    return None
