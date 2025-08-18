![Prompt Engineering](docs/assets/prompt-engineering.png)

## 🧠️ What it is prompt engineering?
Prompt engineering is the practice of designing and iterating instructions, context, and constraints to reliably guide language models to desired outputs.

## 🎯 Goals
- Reliability and control, format adherence, safety/guardrails, and cost/latency efficiency.

## 🛠️ Core techniques
- State the task and success criteria explicitly.
- Provide necessary context or data; avoid ambiguity and hidden assumptions.
- Specify the output format (e.g., JSON schema, headings, bullets) and any constraints.
- Use a few targeted examples (few-shot) to demonstrate style/structure.
- Decompose complex tasks into steps; ask the model to think then act.
- Assign a role/tone when helpful (e.g., "You are a support agent…").
- Add self-checks or rubrics (e.g., "Verify all required fields are present; if missing, say UNKNOWN").

## 🧪 Evaluation and iteration
- Create small test sets; measure accuracy, completeness, and format adherence.
- Compare prompt variants with A/B evaluation; keep the best and document changes.
- Capture failure cases and iterate with minimal, focused edits.

## 🚫 Anti-patterns
- Vague asks, unnecessary verbosity, or relying on hidden context/memory.
- Overfitting to examples; leaking sensitive data in prompts.
- Depending on free-form chain-of-thought; prefer structured intermediate steps or checklists.

## 🎛️ When to fine-tune
- Use fine-tuning or retrieval-augmented context when prompt-only tweaks cannot meet consistency, scale, or domain specificity requirements.

## ✅ Quick checklist
- Define task, inputs, outputs, and success criteria.
- Provide context; specify format and constraints.
- Include 1–3 targeted examples.
- Add verification steps; test on a small set.
- Measure and iterate with A/B comparisons.
