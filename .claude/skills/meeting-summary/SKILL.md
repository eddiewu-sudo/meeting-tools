name: meeting-summary description: Turn a raw meeting transcript, voice逐字稿, or rough notes into a clean, structured meeting record — produced in BOTH English and Traditional Chinese at identical depth, every time, as a single .docx. Works for any meeting type (internal training, internal sync, internal meeting, external/partner meeting, or client meeting) without being told which. Use this skill whenever the user shares a transcript, call notes, recording text, or rough notes and wants it organized, summarized, cleaned up, or written up — even phrasings like "clean this up," "make a meeting file," "summarize this call," "整理會議紀錄," or "organize these notes." Someone who missed the meeting should understand it, and the follow-ups, in under two minutes.
Meeting Summary
Convert messy meeting input into a polished written record. Output is always bilingual and always a Word document.
What this skill ALWAYS does (no need to be told)
Bilingual every run. Produce the complete report in English and in 繁體中文, at identical structure and equal detail — neither language shorter or richer than the other. Never ask which language to use.
One .docx deliverable. Build the final file with the docx skill and present it.
Neutral about identities. Do not assume anyone is a "customer," "client," or "us vs. them." Refer to people by name, or by what they did in the meeting (the host, the presenter, a participant, the other party, attendees). This skill is used for internal training, internal syncs, internal meetings, external meetings, and client meetings alike — so the wording must stay neutral and let the reader infer roles.
Owner left blank. The To-Do table's Owner/負責 column is always left empty for the user to fill in manually (Team A, Team B, or both). Do not auto-assign.
Workflow
Read the whole input first. Identify attendees, topic, and date. Note the meeting type only if it's obvious, and state it neutrally.
Tag substantive moments as: a question, a data point/metric, a discussion point, a decision, or an action item. Drop small talk, scheduling chatter, and filler.
Read /mnt/skills/public/docx/SKILL.md before building the file.
Write the FULL report in English, then the FULL report in 繁體中文 — same sections, same number of points, equal detail — in one document, separated by a page break (English first).
Append the To-Do & Ownership table in each language, with the Owner column blank.
Save the .docx to the outputs folder and present it.
Report structure (use in BOTH languages, identical)
Basic Information / 基本資訊 — Date / 日期, Attendees / 與會人員, Topic / 主題 (and meeting type / 會議性質 only if obvious). Use "待補 / TBD" for anything not stated.
Summary / 摘要 — 3–5 sentences on the purpose, main progress, and conclusion.
Q&A Recap / 問答彙整 — questions raised in the meeting and the responses given. Attribute neutrally (by name or role), not as "customer asked us." Mark open items with status (e.g. "To confirm / 待確認").
Key Data & Metrics / 關鍵數據與指標 — every concrete number mentioned (amounts, %, dates, performance figures, market size). Keep exact; never invent.
Discussion Points / 討論重點 — organized by theme, each with a clear sub-heading. Convert speech to concise written prose; strip filler ("嗯、啊、就是說、那個" and English equivalents).
Decisions / 決議事項 — consensus reached, policy changes, or final calls.
To-Do & Ownership / 待辦事項與分工 — our action items (the table below).
Commitments from Others / 對方承諾事項 — things people outside our own team said they would do or deliver for us later (e.g. "we'll send the sample," "I'll follow up with X"). Attribute by name/role, neutrally — never assume they're a customer. Include the form and any timing/status. Use the table below. Omit the section only if no such commitment was made.
Next Meeting / 下次會議規劃 — time, expected topics, attendees — only if mentioned; otherwise note "未提及 / Not mentioned."
The full bilingual template is in references/format.md; a complete worked example is in references/example.md.
To-Do & Ownership table
Use exactly these four columns, in each language. Leave the Owner column blank.
English:
| Topic / Detail | Action | Format | Owner | |----------------|--------|--------|-------| | [the topic + the key point or detail raised about it] | [the action to take] | [deliverable form: doc / slides / email / data sample…] | [blank — fill in] |
繁體中文:
| 主題／內容 | 你要做的事 | 形式 | 負責 | |-----------|-----------|------|------| | [主題＋當下提出的重點或細節] | [對應要做的事] | [交付形式：文件／簡報／Email／數據樣本…] | [空白，待填] |
Put a one-line note under each table: Owner left blank for manual input (Team A / Team B / Both). / 負責欄留空，請自行填入（Team A／Team B／兩者）。 Do not assign owners yourself.
Commitments from Others table
A separate table for what people outside our own team promised to deliver or follow up on. Attribute by name/role, stay neutral (no "customer/client" labels), and never invent a commitment that wasn't stated.
English:
| Deliverable / Commitment | Promised by | Form | Expected timing / status | |--------------------------|-------------|------|--------------------------| | [what they said they'd provide or do] | [name or role] | [doc / data / intro / email…] | [date, "TBD," or status] |
繁體中文:
| 承諾事項／交付 | 承諾者 | 形式 | 預計時間／狀態 | |---------------|--------|------|----------------| | [對方表示會提供或處理的事項] | [姓名或角色] | [文件／資料／引薦／Email…] | [日期、「待補」或狀態] |
Rules that make it useful
Identical bilingual parity. Every section, row, and point that appears in one language must appear in the other with equal detail.
Preserve specifics exactly. Names, figures, amounts, dates, deadlines, and technical terms (e.g. Ticker-level, Alternative Data) stay in their original wording. If a number wasn't stated, don't supply one.
Mark uncertainty, don't smooth it. Flag ambiguous or likely mis-heard content with [待確認] / [to confirm]. If you fix an obvious transcription error from context, mark it [*].
Stay neutral on identity. Never label anyone a customer/client or frame the meeting as "us vs. them" unless the transcript explicitly says so. Describe people by name or by what they did.
Lead with substance. Cut filler. Every row and bullet should change the reader's understanding.
Quote sparingly — only a memorable or load-bearing line, kept short.
Never fabricate or extend. Organize only what's in the input; do not add topics, conclusions, or numbers that weren't discussed.
Reference files
references/format.md — the unified bilingual report template and processing rules.
references/example.md — a full worked bilingual example (English + 繁體中文) with the To-Do & Ownership table.
