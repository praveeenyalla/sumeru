import os
import uvicorn

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))

    print("=" * 60)
    print(" Sumeru Technologies Enterprise Platform")
    print(f" -> Main Website:      http://localhost:{port}")
    print(f" -> Loopback Address:  http://127.0.0.1:{port}")
    print(f" -> API Documentation: http://localhost:{port}/docs")
    print("=" * 60)

    uvicorn.run("app.main:app", host=host, port=port, reload=True)

