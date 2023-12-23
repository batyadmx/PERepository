from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from main import generate_audio

app = FastAPI()

@app.post("/text-to-speech")
async def text_to_speech(text: str):
    path = "output.wav"
    try:
        generate_audio(text, path)
        return FileResponse(path, media_type="audio/wav", headers={'Content-Disposition': f'attachment; filename="{path}"'})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)