import os

import threading
from app.udaconnect.grpc_server import serve_grpc
from app import create_app

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":

    print("Flask server initiated")

    grpc_thread = threading.Thread(target=serve_grpc, daemon=True)
    grpc_thread.start()

    app.run(debug=True)
    grpc_thread.join()
