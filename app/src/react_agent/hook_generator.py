from react_agent.utils import load_chat_model
from react_agent.configuration import Configuration

async def generate_hook_with_word_count(script: str) -> str:
    configuration = Configuration.from_context()
    model = load_chat_model(configuration.model)
    hook_ideas = """A. Bold Statements
    “This will change your life!”
    “You won’t believe what happened next…”
    “The secret to success is simpler than you think!”
    “Stop wasting your time with this mistake!”
    “Here’s why most people fail at this.”
    “This is the ultimate hack for [topic]!”
    “This one tip will save you hours!”
    “I was shocked when I learned this!”
    “You’re doing it wrong if you want to succeed!”
    “Here’s the truth about [common myth]!”
    “This is the most underrated trick ever!”
    “You’ve been lied to about [topic]!”
    “Watch me transform in just [time frame]!”
    “The biggest mistake you’re making right now!”
    “This is the key to unlocking your potential!”
    B. Question-Based Hooks
    “Ever wondered why [specific situation]?”
    “What if I told you [surprising fact]?”
    “Can you relate to this common struggle?”
    “Have you tried this simple trick?”
    “Do you want to know how to [achieve something]?”
    “What���s stopping you from [goal]?”
    “Did you know [interesting statistic]?”
    “Why is no one talking about this?”
    “Are you making this crucial error?”
    “Do you want to learn how to [skill] fast?”
    “What would you do in this situation?”
    “Have you ever felt [specific emotion]?”
    “What’s the craziest thing you’ve done for [topic]?”
    “Why does this always happen?”
    “What if you could change one thing about [topic]?”
    C. Controversial or Intriguing Statements
    “I don’t think [popular opinion] is true.”
    “Here’s why I stopped [common practice].”
    “This is why you should never [action].”
    “You might be surprised by this!”
    “Most people don’t know this about [topic].”
    “Forget everything you’ve heard about [topic]!”
    “Here’s the hidden truth about [situation].”
    “I used to believe [common belief], but now…”
    “This is why [popular trend] is overrated.”
    “The real reason behind [event] might shock you.”
    “You’re missing out on this simple change!”
    “This one thing could change everything for you!”
    “If you want to be successful, do this!”
    “Here’s what no one tells you about [topic].”
    “You’ll never guess what happened when I tried this!”
    D. Visual or Action-Based Hooks
    “Watch me turn [item] into [result]!”
    “Here’s a quick transformation you need to see!”
    “Let’s see if this actually works!”
    “Check out this epic before-and-after!”
    “Here’s how I did [impressive feat] in just [time].”
    “Follow along as I show you [process]!”
    “This is what happens when you [action].”
    “Let’s break this down step by step.”
    “I tried [trend/challenge], and here’s what happened!”
    “Watch till the end for a surprise!”
    “I can’t believe I did this!”
    “Here’s a sneak peek of my process!”
    “Let me show you my secret weapon!”
    “Can you spot the difference in [items]?”
    “You’ll want to see this!”
    E. Story-Based Hooks
    “Let me tell you a quick story about [event].”
    “I learned the hard way when I [experience].”
    “Once upon a time, I faced [challenge]…”
    “This is how I overcame my biggest obstacle.”
    “Here’s a story about the time I [memorable moment].”
    “You won’t believe what happened when I [action].”
    “I used to struggle with [issue], and here’s how I fixed it.”
    “This experience changed my life forever.”
    “Here’s what happened when I tried [action].”
    “I’ll never forget the day I [event].”
    “This moment taught me a valuable lesson.”
    “Here’s a funny story about [situation].”
    “This is what I wish I knew when I started [journey].”
    “Let me share my biggest regret with you.”
    “Here’s how I turned my failure into success.”
    F. Urgency and Encouragement Hooks
    “You need to act fast to see results!”
    “Don’t miss out on this limited-time offer!”
    “This will only be available for a short time!”
    “If you want to improve, start today!”
    “Your chance to change your life is now!”
    “Why wait? Start your journey today!”
    “You deserve to know this—don’t wait!”
    “The time to make a change is now!”
    “This could be your turning point—don’t ignore it!”
    “Take the first step toward [goal] today!”
    """

    prompt = f"""Your task is to generate a compelling video hook for the given script. Instead of just writing a generic hook, you must use the "3-Step Hook Formula" and incorporate other key strategies for creating viral hooks.

Here is the framework to follow:

**The 3-Step Hook Formula:**

1.  **Step 1: The Context Lean-in:** Start by establishing the video's topic for clarity. Then, get the viewer to "lean in" by:
    *   Establishing common ground.
    *   Referencing a benefit or a pain point.
    *   Using a metaphor.
    *   Presenting a mind-blowing fact.

2.  **Step 2: The Scroll-Stop Interjection:** Add a single, short line that acts as a "stun gun" to stop the viewer from scrolling. Often this uses a contrasting word like "but," "however," or "yet." This builds anticipation.

3.  **Step 3: The Contrarian Snapback:** Deliver a "haymaker" sentence that takes the topic in a surprising and opposite direction from the initial lean-in. This creates a strong curiosity loop.

**Additional Key Strategies to Incorporate:**

*   **Visual Hooks:** Suggest on-screen text (3-5 bold words) to accompany the hook.
*   **Focus on Audience Interest:** Frame the hook around a benefit or pain point the target audience already cares about.
*   **Cult Hopping:** If applicable, use well-known brands, celebrities, or cultural references as metaphors to make the topic more relatable.
*   **Staccato Sentences:** Use short, punchy sentences for maximum clarity and impact.
*   **Compress Speed to Value:** Deliver a quick "hit of value" within the hook itself.

**Here are some hook ideas to inspire you:**

{hook_ideas}

**Now, analyze the following script and generate a hook using this entire framework.**

**Script:**
---
{script}
---

**Generated Hook (following the 3-step formula and strategies):**
"""

    # For now, just return the script as a placeholder.
    # You can add real processing logic here.
    # Assuming the model has a simple invoke method for synchronous calls
    # For async, you would need to adjust the viral_hook_generator in tools.py to be async
    response = await model.ainvoke(prompt)
    hook = response.content if hasattr(response, 'content') else str(response)

    word_count = len(script.split())
    return f"{hook}\nWord count: {word_count}"

