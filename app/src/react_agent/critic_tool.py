from react_agent.utils import load_chat_model
from react_agent.configuration import Configuration
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



async def critic_content(content: str) -> str:
    """
    Critiques the given content using an LLM and returns comments.

    Args:
        content: The script or content to be critiqued.

    Returns:
        A string containing the critique comments.
    """
    configuration = Configuration.from_context()
    llm = load_chat_model(configuration.model)

    prompt_template = PromptTemplate.from_template(
        """
You are a senior video strategist specializing in viral hooks and the "Max Alignment" framework. Critique the following video hook content for effectiveness and adherence to Max Alignment. For each area below, give specific, actionable feedback and concrete suggestions:

1. **Key Visual:** Is the described visual compelling and curiosity-inducing? Suggest improvements if not.
2. **Hook Format:** Does the content use the best hook format (Fortune Teller, Experimenter, Teacher, Magician, Investigator, Contrarian)? Justify your choice and suggest a better format if needed.
   - *Fortune Teller*: Contrasts present vs. future ("This tech will change marketing forever").
   - *Experimenter*: Peer-to-peer demo ("I tried these glasses, here’s what happened").
   - *Teacher*: Explains a method ("3 things you can learn from this brand").
   - *Magician*: Visual/auditory stun ("Check this out!").
   - *Investigator*: Reveals a secret ("This is a secret city no one knows about").
   - *Contrarian*: Challenges convention ("Everyone loves this, but it’s overhyped").
3. **Spoken Hook:** Are the 2-4 spoken lines effective (context-lean-in, contrast/snapback)? Suggest line-by-line improvements.
4. **Visual & Text Hooks:**
   - *Visual*: Is the first 3-5 seconds clear, engaging, and supportive? Suggest alternatives.
   - *Text*: Is the overlay (3-5 words) concise and supportive? Suggest alternatives.
5. **Alignment:** Do spoken, visual, and text hooks work together for Max Alignment and a curiosity loop? Point out misalignments and suggest improvements.

**Reference Example:**
- *Authority*: "I'm one of the first engineers at a stealth healthcare AI startup."
- *Proof*: "We've already boosted response rates by 40%."
- *Value*: "How to scale AI apps, use LLMs, and what skills matter."
- *Visual Fix*: Replace unrelated visuals (e.g., Minecraft) with code, diagrams, or data.
- *Hook Fix*: Move proof/stat to the front, use Contrarian/Investigator format.

**Workflow:**
- Start with the most compelling visual.
- Find the biggest contrast and select the best hook format.
- Write 2-4 spoken lines (context + contrast).
- Add concise on-screen text.
- Ensure all elements are aligned for clarity and impact.

**Example of an ideal critique reply:**
Does this reel have potential?  
Yes, absolutely. It has massive potential. You have the most important and hardest-to-get ingredient for a successful piece of content: genuine authority and a valuable secret.

Here’s what’s working very well:

Strong Authority: You immediately establish credibility. "I'm one of the first engineers at a stealth healthcare AI startup" is an incredibly powerful statement. It tells the viewer you're on the inside and have knowledge they can't get elsewhere.

Specific Proof Point: "we've already boosted response rates by 40%" is a fantastic piece of data. It's not a vague claim; it's a concrete result that proves your methods work.

Clear Value Proposition: You clearly state what the viewer will learn: how to scale AI apps, use LLMs, and what skills actually matter. This is exactly what your target audience wants to know.

You have the core substance of a viral video. The current issue isn't the message, but the delivery mechanism that wraps it.

What can I fix? How to Unlock its Full Potential  
The primary area for improvement is the alignment between your visual, spoken, and text hooks. Right now, there's a significant disconnect that weakens the hook's impact.

Let's use the "Max Alignment" framework we discussed.

1. The Visual Hook: The Minecraft Problem  
The Issue: The Minecraft parkour footage is what's called a "visual pacifier." It's visually interesting enough to keep someone watching passively, but it has zero connection to the topic of building an AI product. This creates confusion and comprehension loss. A viewer thinks, "Am I watching a gaming video or a tech video?" This confusion happens in the critical first 2-3 seconds and can cause them to scroll away.

The Fix: Your Key Visual should directly relate to your topic. The visual must support the spoken words.

Option A (Best): A screen recording of you navigating a complex piece of code, a system architecture diagram on a whiteboard, or a mind-map of your AI platform.

Option B: A simple shot of you talking directly to the camera with passion and authority.

Option C: A compelling data visualization showing the "40% boost" in response rates.

2. The Spoken Hook & Hook Format  
Current Format: You're using a mix of The Investigator ("What it really takes...") and The Teacher. This is a good starting point.

The Issue: The hook is a little slow and takes too long to get to the proof point (the 40% stat). The most powerful information arrives after the 15-second mark. We need to front-load that value.

The Fix: Let's make it more direct and faster, using a more aggressive hook format like The Contrarian. This creates immediate contrast and leverages your authority.

Let's Re-architect the Hook (A Practical Example)  
Imagine you have a key visual of a complex code structure on your screen. Here is how you could apply the frameworks to create a much more powerful hook:

(The screen shows a fast-moving screen recording of complex code or an architecture diagram)

1. Select the Best Hook Format:  
Chosen Format: The Contrarian combined with The Investigator. We'll challenge a common belief and promise a secret.

Justification: This immediately frames you as an expert with non-obvious knowledge, creating a powerful curiosity loop.

2. Design the Visual & Text Hooks:  
Visual Hook: A screen recording of an impressive-looking code editor, a complex systems diagram being drawn, or a data dashboard.

Text Hook: "You're learning AI all wrong." (This is bold, direct, and supports the contrarian angle).

3. Write the Spoken Hook:  
(0-3 seconds): "Stop trying to learn every new AI library. It's not what the pros do."

(3-7 seconds): "I'm a founding engineer at a stealth AI startup, and we boosted our response rates by 40% by focusing on one thing."

4. Justify the Alignment:  
This new hook achieves Max Alignment: The visual (complex code) matches the spoken words ("AI library," "pros") and the text ("learning AI") to create a single, powerful, and instantly understandable message of expert insight.

The rest of the video script is great!  
The lines "Now I'm pulling back the curtain..." and the promise to share how you scale apps and what skills matter are perfect. The only change is moving the core value proposition and proof point right to the front to stop the scroll instantly.

In summary: You have A+ content. By swapping the unrelated visual for something relevant and reframing your hook to be more direct and contrarian, you will create a much stronger video that has a real chance of performing exceptionally well.

---
Content to critique:
---
{content}
---

Critique:
"""
    )

    chain = prompt_template | llm | StrOutputParser()
    critique = await chain.ainvoke({"content": content})
    return critique


