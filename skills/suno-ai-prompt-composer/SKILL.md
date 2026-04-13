---
name: suno-ai-prompt-composer
description: Use when a user has a rough song, instrumental, lyric, or sound-effect idea and wants a short clarification flow that turns it into a clean, copyable Suno AI prompt or Custom Mode field package.
---

# Suno AI Prompt Composer

## Use When

- The user wants a Suno AI prompt for a song, instrumental, lyrics-first track, loop, ambience, sound effect, or sample.
- The user wants the right questions asked before receiving a final Suno-ready prompt.
- The user needs Custom Mode fields such as Style, Lyrics, Exclude, Title, or Sounds settings.
- The user references an artist, celebrity, existing song, or copyrighted lyric and the request must be converted into safe descriptive musical traits.

## Workflow

1. Restate the target in one short sentence and classify the output: Simple song prompt, Custom Mode package, instrumental prompt, lyrics package, or Sounds prompt.
2. If key details are missing, ask one short round of 2-4 questions. Prioritize mode, genre/mood, vocal direction, language, lyric theme, instrumentation, tempo/energy, structure, exclusions, and intended use.
3. If the user asks for speed, provides enough detail, or says not to ask questions, produce the final package immediately.
4. Use Suno-oriented musical vocabulary: genre blend, mood, tempo, rhythm, dynamics, structure, instrumentation, vocal delivery, production texture, effects, and emotional arc.
5. For artist, celebrity, living-person, existing-song, or copyrighted-lyric references, remove the protected reference from the final prompt and replace it with neutral traits such as era, vocal register, arrangement, instrumentation, tempo, production style, and mood.
6. For Simple Mode, provide one compact natural-language song description.
7. For Custom Mode, split the answer into copyable fields:
   - `Style`: genre blend, mood, tempo, instrumentation, vocal style, arrangement, production texture, and structure cues.
   - `Lyrics`: original lyrics only, or a concise lyric brief if the user wants Suno to generate lyrics.
   - `Exclude`: unwanted genres, instruments, vocal traits, profanity, or production artifacts.
   - `Title`: 1-3 title options when useful.
8. For instrumental outputs, state the instrumental intent clearly and avoid vocal or lyric instructions unless the user asks for Add Vocals later.
9. For Sounds outputs, provide a concise sound prompt plus optional `Type`, `BPM`, `Key`, and duration guidance. Prefer direct sound words such as whoosh, rumble, glitch, impact, ambience, chatter, kick, snare, swell, and loop.
10. Add slider or iteration notes only when useful: lower Weirdness for predictable genre fidelity, higher Weirdness for experimental results, stronger Style Influence for strict style adherence, and Audio Influence only when an upload is involved.
11. Keep prompt text copyable and remove filler such as unverifiable quality promises, fake technical guarantees, overlong genre lists, and generic "best ever" language.
12. Do not generate music, call Suno, upload files, download tracks, distribute songs, or guarantee rights. The default output is text-only prompt composition.

## Official Guardrails

- Suno may block well-known artist or person names, copyrighted or trademarked terms, derogatory or defamatory terms, excessive profanity, and inappropriate topics. Avoid placing those in final prompts.
- Use only original lyrics. If the user provides or asks for third-party lyrics, ask for permission context or redirect to a new original lyric direction.
- Rights and commercial use depend on plan, timing, input ownership, and local copyright law. Give only a short policy reminder when relevant; do not present legal certainty.
- Public sharing can expose prompts, lyrics, and other song details to reuse. Mention this only when the user asks about release, sharing, or reuse risk.

## Output Expectations

- If asking questions, keep the first reply short and actionable.
- If producing a final package, use clear labels the user can paste into Suno.
- Default final structure:

```text
Suno Setup
Mode:
Title:
Style:
Lyrics:
Exclude:
Notes:
```

- For Simple Mode, replace the field package with:

```text
Simple Mode Prompt
...
```

- For Sounds, use:

```text
Suno Sounds Setup
Prompt:
Type:
BPM:
Key:
Notes:
```

## References

- See `examples/session-example.md` for a short Custom Mode flow.

## Portability Notes

- This skill's core behavior is provider-specific to Suno prompt writing but runtime-independent.
- Runtime automation, Suno UI instructions, account handling, downloads, or publishing behavior belongs in `adapters/`, not in this core skill.
- When current model availability, pricing, rights, or feature names matter, verify the latest official Suno documentation before answering.
