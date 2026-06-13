def get_prompt(content_type, topic, tone):

    tone_guide = {
        "Professional": "Use formal language, avoid slang, be authoritative and credible.",
        "Casual": "Use conversational language, contractions are fine, keep it relaxed.",
        "Friendly": "Be warm, approachable, and encouraging. Use inclusive language.",
        "Persuasive": "Use compelling arguments, strong calls-to-action, and emotional appeal.",
        "Humorous": "Be witty and light-hearted, use wordplay where appropriate.",
        "Inspirational": "Be motivational and uplifting. Use powerful, energizing language that moves people to action.",
        "Formal": "Use academic and official language. Be precise, structured, and authoritative.",
        "Storytelling": "Use narrative style. Paint vivid scenes, build tension, and engage emotionally like a story.",
        "Minimalist": "Be extremely concise and punchy. No fluff, no filler. Every word must earn its place.",
        "Empathetic": "Be warm, understanding, and emotionally sensitive. Acknowledge feelings and connect deeply.",
        "Bold & Edgy": "Be provocative, daring, and attention-grabbing. Challenge norms and push boundaries.",
        "Poetic": "Use lyrical, expressive, and creative language. Use metaphors, imagery, and rhythm."
    }

    tone_instruction = tone_guide.get(tone, "")

    if content_type == "Blog Post":
        return f"""You are an expert blog writer.
Write a well-structured blog post about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Catchy title
- Introduction that hooks the reader
- 3-4 body paragraphs with subheadings
- Conclusion with a takeaway
- Length: 300-400 words

Write only the blog post, no extra commentary."""

    elif content_type == "Social Media Caption":
        return f"""You are a social media expert.
Write an engaging Instagram/Twitter caption about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Attention-grabbing first line
- 3-5 relevant hashtags at the end
- Include an emoji or two
- Length: 50-80 words

Write only the caption, no extra commentary."""

    elif content_type == "LinkedIn Post":
        return f"""You are a LinkedIn content strategist.
Write a professional LinkedIn post about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Strong opening line (no "I am excited to share" clichés)
- Personal insight or lesson
- End with a thought-provoking question to drive engagement
- 3 relevant hashtags
- Length: 150-200 words

Write only the post, no extra commentary."""

    elif content_type == "Email Subject Line":
        return f"""You are an email marketing expert.
Generate 5 compelling email subject lines for the topic: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Each subject line under 60 characters
- Varied styles: curiosity, urgency, benefit-driven, question, personalized
- Number each one (1. 2. 3. 4. 5.)

Write only the subject lines, no extra commentary."""

    elif content_type == "Text Summary":
        return f"""You are a professional content summarizer.
Write a concise summary about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Cover the key points clearly
- Easy to read and understand
- Length: 100-150 words

Write only the summary, no extra commentary."""

    elif content_type == "YouTube Video Description":
        return f"""You are a YouTube SEO and content expert.
Write a compelling YouTube video description for a video about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Hook in the first 2 lines (shown before "Show more")
- Brief overview of what the video covers (3-4 bullet points)
- Call-to-action (like, subscribe, comment)
- 5-7 relevant SEO hashtags at the end
- Length: 150-200 words

Write only the description, no extra commentary."""

    elif content_type == "Product Description":
        return f"""You are a professional copywriter specializing in e-commerce.
Write a persuasive product description for: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Catchy product headline
- 2-3 sentences highlighting key benefits (not just features)
- Bullet points for 4-5 key features
- Closing line with a call-to-action
- Length: 100-150 words

Write only the product description, no extra commentary."""

    elif content_type == "Tweet Thread":
        return f"""You are a Twitter/X content strategist.
Write an engaging tweet thread about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- 5-7 tweets in the thread
- First tweet must hook the reader and end with (🧵 Thread)
- Each tweet numbered (1/, 2/, etc.)
- Each tweet under 280 characters
- Last tweet with a call-to-action or key takeaway

Write only the tweet thread, no extra commentary."""

    elif content_type == "Newsletter Intro":
        return f"""You are an expert newsletter writer.
Write a compelling newsletter introduction about: "{topic}"
Tone: {tone}. {tone_instruction}

Requirements:
- Warm, personal greeting to the reader
- Hook that makes them want to keep reading
- Brief preview of what's inside the newsletter
- Smooth transition sentence into the main content
- Length: 80-120 words

Write only the newsletter intro, no extra commentary."""
