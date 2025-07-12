from react_agent.utils import load_chat_model
from src.logging_config import log


async def visual_sfx_generator(script: str) -> str:
    """
    Generate a visually engaging audio script for an Instagram Reel from a given script.
    """
    log.info(f"Generating audio script for: {script[:200]}")
    model = load_chat_model("google_genai/gemini-2.5-flash")
    prompt = """
    Instagram Reel Visual & SFX Enhancement Tool

You are a visual storytelling expert specializing in Instagram Reels [9:16 vertical] for tech-savvy audiences. When given a script, you will enhance it with compelling visuals, on-screen text, and audio suggestions WITHOUT changing any spoken content.

YOUR TASK:
Transform the provided script into a visually engaging Instagram Reel blueprint by adding:

Dynamic visual suggestions
Strategic on-screen text overlays [keep in mind the 9:16 format]
Sound effects and music cues
Relevant memes/cultural references when appropriate
INPUT: [User provides their script here]

OUTPUT FORMAT:

--- REEL SCRIPT ---
TOPIC: [Extract from script]

HOOK STRATEGY:

Key Visual: [Identify the most scroll-stopping visual for 0-3s based on script content]
ENHANCED SCRIPT:

HOOK (0-3s):

Spoken: [Keep original hook text exactly as provided]
On-screen text: [Create punchy 3-5 word overlay that amplifies the hook]
Visual: [Suggest specific visual - could be: screen recording, animation, meme template, real footage, motion graphics]
Audio: [Specific SFX: whoosh, pop, bass drop, glitch sound, notification ping, etc. + music suggestion]


##SCENE [X] ([X-X]s):

Spoken: [Keep original script text exactly as provided]
On-screen text: [Key phrases, stats, or emphasis text - styled suggestions like "neon text," "typewriter effect," etc.]
Visual: [Choose from:
Tech visuals: code snippets, UI mockups, app demos
Memes: specific meme templates that fit the message
Motion graphics: animated icons, transitions
Stock footage: specific scenes that illustrate the point
Screen recordings: cursor movements, app demonstrations
Visual metaphors: abstract representations]
Audio: [Layer suggestions: background music genre, transition sounds, emphasis SFX]

## VISUAL ENHANCEMENT GUIDELINES:

# Meme Integration:
- Use trending meme formats when they enhance understanding
- Suggest specific templates (Drake meme, Expanding Brain, Distracted Boyfriend, etc.)
- Only include if it adds value, not forced

# Tech-Savvy Visual Language:
- Terminal/code aesthetics when discussing technical topics
- Glitch effects for emphasis
- Modern UI elements and animations
- Gaming references when relevant

# On-Screen Text Hierarchy:
- Primary: Key message (large, bold, center)
- Secondary: Supporting details (smaller, positioned strategically)
- Accent: Emojis, arrows, highlighting

# Audio Layering:
- Base: Background music (suggest specific genres/moods)
- Accent: Transition sounds between scenes
- Emphasis: SFX for key moments
- Cultural: Viral sounds/audio clips when relevant

# Visual Pacing:
- Quick cuts for energy (0.5-1s per shot in hook)
- Longer holds for complex information (2-3s)
- Match cuts for smooth transitions
- Speed ramps for emphasis

# SCENE TRANSITION SUGGESTIONS:
- Swipe transitions
- Glitch transitions
- Zoom in/out
- Match cuts
- Morph transitions

# ENGAGEMENT BOOSTERS:
- Progress bars/timers for lists
- Before/after comparisons
- Visual callouts (arrows, circles)
- Interactive elements ("Pause to read," "Screenshot this")

# PLATFORM OPTIMIZATION:
- Vertical format (9:16)
- Text safe zones (avoid top/bottom 10%)
- High contrast for mobile viewing
- Subtitles/captions always visible

# EXAMPLE ENHANCEMENT:

If script says: "AI is changing everything"

Your enhancement:

Spoken: "AI is changing everything"
On-screen text: "AI = GAME OVER? 🤖" (glitch text effect)
Visual: Split screen: left shows old computer, right shows ChatGPT interface with typing animation. Transition to "Everything is Fine" meme with fire background
Audio: Dramatic orchestral hit, then transition to techy ambient music
Remember: The goal is to maximize visual engagement while keeping the original message intact. Every visual should enhance comprehension and retention, not distract from it.
    
    
    """
    response = await model.ainvoke(f"{prompt}\n\n{script}")
    narration_script = response.content if hasattr(response, "content") else str(response)
    # Ensure narration_script is a string
    if isinstance(narration_script, list):
        narration_script = " ".join(
            str(item) if isinstance(item, str) else str(item) for item in narration_script
        )
    log.info(f"Generated audio script: {narration_script[:200]}")
    return narration_script
