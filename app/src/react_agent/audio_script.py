from react_agent.utils import load_chat_model
from src.logging_config import log


async def generate_audio_script(script: str) -> str:
    """
    Processes the script with an LLM to generate a clean audio narration script.
    """
    log.info(f"Generating audio script for: {script[:200]}")
    model = load_chat_model("google_genai/gemini-2.5-flash")
    prompt = "From the provided text, extract only the voiceover script. The voiceover script is the spoken text, often enclosed in quotation marks or following time cues (e.g., '(0-3s)'). Ignore all other details such as visual cues, scene descriptions, strategies, and formatting notes. Present the extracted voiceover as a clean, continuous script."
    response = await model.ainvoke(f"{prompt}\n\n{script}")
    narration_script = response.content if hasattr(response, "content") else str(response)
    # Ensure narration_script is a string
    if isinstance(narration_script, list):
        narration_script = " ".join(
            str(item) if isinstance(item, str) else str(item) for item in narration_script
        )
    log.info(f"Generated audio script: {narration_script[:200]}")
    return narration_script
