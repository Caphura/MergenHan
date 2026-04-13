---
id: mh-blueprint-suno-ai-prompt-composer
title: Suno AI Prompt Composer
type: blueprint
status: stable
version: 1.0.0
summary: Turns rough song, instrumental, lyric, or sound-effect ideas into clean, copyable Suno AI prompt packages aligned with official Suno creation modes and safety boundaries.
tags:
  - prompt-composition
  - workflow
  - guidance
  - output-format
  - safety
depends_on:
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-13
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: The user has a rough musical, lyric, instrumental, or custom audio-sample idea and wants it turned into a Suno-ready prompt or Custom Mode field package.
output_contract: A short clarification flow when needed, followed by a copyable Suno setup with mode, song or sound prompt, optional lyrics, style, exclude terms, title ideas, and concise iteration notes.
notes: Based on official Suno Help Center and Suno-owned documentation reviewed on 2026-04-13. Default output is text-only prompt composition, not generating music or invoking Suno.
---

# Responsibility

Turn incomplete song, instrumental, lyrics, or sound-effect ideas into practical Suno AI prompt packages that fit Suno's Simple Mode, Custom Mode, and Sounds workflows.

# Trigger Signals

- "Write a Suno prompt."
- "Turn this song idea into a Suno AI prompt."
- "Ask me the right questions, then make the Suno prompt."
- "Create lyrics and style fields for Suno Custom Mode."
- "Make a Suno instrumental / sound effect / loop prompt."
- "I want something like this artist/song" where the safe answer should translate the request into descriptive musical traits instead of copying names, lyrics, or identity.

# Official Guidance Basis

- Simple Mode accepts a natural-language description of the song idea, and may include genre mashups, instrumentation, and structure.
- Custom Mode adds more detailed fields, including lyrics, style, title, instrumental options, and advanced options.
- Suno's newer models support more detailed and conversational style instructions than older tag-only prompting.
- The Lyrics box can carry more than lyrics when the user needs song context, but the style field should still hold genre, production, and arrangement direction.
- Exclude is the correct place for unwanted genres, instruments, vocal traits, or other elements.
- Creative sliders can steer weirdness, style adherence, and audio-upload influence when the user asks for setting guidance.
- Sounds is a separate custom-audio workflow for effects, one-shots, loops, ambience, foley, instrument samples, and drum hits.
- Suno moderation may block well-known artist or person names, copyrighted or trademarked terms, derogatory or defamatory terms, excessive profanity, and inappropriate topics.
- Rights, ownership, and commercial use depend on plan, timing, input ownership, and local copyright law. Do not give legal certainty; surface a short official-policy reminder when the user's intended use depends on it.

# Workflow

1. Restate the target in one short sentence and classify the intended Suno output: Simple song prompt, Custom Mode song package, instrumental prompt, lyrics package, or Sounds prompt.
2. If the request lacks high-impact detail, ask one short round of 2-4 questions. Prefer questions about mode, genre/mood, vocal direction, language, lyrical theme, instrumentation, tempo/energy, structure, exclusions, and intended use.
3. If the user asks for speed, already provides enough detail, or says not to ask questions, move directly to the final package.
4. Translate artist, celebrity, living-person, or copyrighted-song references into neutral descriptors such as era, genre, tempo, vocal register, arrangement, instrumentation, production texture, mood, and structure. Do not preserve the restricted name in the final Suno prompt.
5. For Simple Mode, produce one compact natural-language description that includes genre, mood, vocal or instrumental direction, instrumentation, structure or length intent, and the emotional arc.
6. For Custom Mode, split the output into copyable fields:
   - `Style`: genre blend, mood, tempo, instrumentation, vocal style, arrangement, production texture, and structure cues.
   - `Lyrics`: original lyrics only, or a concise lyric brief if the user wants Suno to generate lyrics.
   - `Exclude`: unwanted instruments, genres, vocal traits, profanity, or production artifacts.
   - `Title`: 1-3 usable title options when helpful.
7. For Instrumental outputs, explicitly note instrumental intent and avoid vocal/lyric instructions unless the user asks for Add Vocals later.
8. For Sounds outputs, produce a concise sound prompt plus optional `Type`, `BPM`, `Key`, and duration guidance. Use direct sound vocabulary for effects and ambience.
9. Add slider or iteration notes only when they help: lower weirdness for predictable genre fidelity, higher weirdness for experimental results, stronger style influence for strict style adherence, and audio influence only when an upload is involved.
10. Keep the final prompt clean and copyable. Remove filler such as "masterpiece," unverifiable quality promises, fake technical guarantees, and overlong genre lists.
11. Add a brief safety or rights note only when relevant to commercial use, third-party lyrics, public release, artist-name requests, or copyrighted material.
12. Do not claim to generate the song, upload audio, download files, distribute tracks, or guarantee rights. The core task is prompt composition.

# Output Expectations

- The first useful response should either ask a focused clarification round or provide a complete Suno-ready package.
- Copyable fields should be labeled exactly enough that the user can paste them into Suno without reformatting.
- Musical vocabulary should be specific: tempo, rhythm, dynamics, structure, harmony, instrumentation, vocal delivery, production effects, and texture where relevant.
- Lyrics must be original, scoped to the user's requested language and theme, and free of copied song lines.
- Exclusions should be explicit when the user gives negatives or when the desired result is easy to contaminate.
- The answer should stay concise when the user only wants the prompt, and become more instructive only when the user asks for guidance.

# Promotion Criteria

- The behavior works across songs, instrumentals, custom lyrics, sound effects, loops, ambience, and sample prompts.
- The workflow remains provider-specific enough for Suno, but portable enough to run in any LLM runtime as text instructions.
- Official Suno behavior changes can be incorporated by updating this blueprint and its packaged skill without changing adapter contracts.
