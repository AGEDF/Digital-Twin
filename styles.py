"""Styling constants for the digital twin Gradio app."""

GOLD = "#ecad0a"
BLUE = "#209dd7"
PURPLE = "#753991"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
  --twin-gold: #ecad0a;
  --twin-blue: #209dd7;
  --twin-purple: #753991;

  --twin-bg: #0a0a0f;
  --twin-surface: #12121a;
  --twin-surface-2: #1a1a24;
  --twin-border: #262633;
  --twin-border-strong: #3a3a4a;
  --twin-text: #ededf2;
  --twin-muted: #8e8e9c;
  --twin-shadow: 0 8px 32px rgba(0, 0, 0, 0.45);

  --twin-radius-lg: 20px;
  --twin-radius-md: 14px;
  --twin-radius-sm: 10px;
}

/* Light mode: Gradio adds `.dark` to <body> when dark; absence = light.
   Only the neutrals flip. Gold/blue/purple accents stay identical. */
body:not(.dark) {
  --twin-bg: #f5f5f8;
  --twin-surface: #ffffff;
  --twin-surface-2: #f0f0f5;
  --twin-border: #e2e2ea;
  --twin-border-strong: #c4c4d0;
  --twin-text: #17171f;
  --twin-muted: #6b6b7a;
  --twin-shadow: 0 8px 32px rgba(30, 30, 60, 0.08);
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, body, gradio-app { background: var(--twin-bg) !important; }

/* Soft ambient glow behind the page. Purely atmospheric, sits behind content. */
body::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background:
    radial-gradient(60% 40% at 15% 0%, rgba(117, 57, 145, 0.18), transparent 70%),
    radial-gradient(50% 35% at 90% 5%, rgba(32, 157, 215, 0.14), transparent 70%);
}
body:not(.dark)::before {
  background:
    radial-gradient(60% 40% at 15% 0%, rgba(117, 57, 145, 0.07), transparent 70%),
    radial-gradient(50% 35% at 90% 5%, rgba(32, 157, 215, 0.07), transparent 70%);
}

/* ---------- Stable layout ---------- */
.gradio-container {
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 820px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 48px 24px 56px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 30px !important;
  font-weight: 700 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.15 !important;
  margin: 0 0 6px !important;
  padding: 0 !important;
  text-align: left !important;
}
/* The one signature detail: a short three-colour rule under the title. */
.gradio-container h1::after {
  content: "";
  display: block;
  width: 56px;
  height: 4px;
  margin-top: 12px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--twin-gold), var(--twin-purple) 55%, var(--twin-blue));
}
.gradio-container p, .gradio-container .prose {
  color: var(--twin-muted) !important;
}

/* ---------- Block surfaces ---------- */
.block, .form { background: transparent !important; box-shadow: none !important; }

/* ---------- Hide the Chatbot label / header strip ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame ---------- */
.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-lg) !important;
  min-height: 520px !important;
  box-shadow: var(--twin-shadow) !important;
  overflow: hidden;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

/* ---------- Bubble base (covers every Gradio variant) ---------- */
.message-row :is(.message, .message-bubble, .bubble) {
  border: 1px solid transparent !important;
  box-shadow: none !important;
  padding: 10px 14px !important;
  font-size: 14.5px !important;
  line-height: 1.6 !important;
  max-width: 100%;
}

/* ---------- User bubble: brand blue, tail on bottom right ---------- */
.message-row:is(.user-row, [data-role="user"]) :is(.message, .message-bubble, .bubble) {
  background: linear-gradient(135deg, var(--twin-blue), #1a85b8) !important;
  color: #ffffff !important;
  border-radius: 18px 18px 4px 18px !important;
}

/* ---------- Assistant bubble: quiet surface, tail on bottom left ---------- */
.message-row:is(.bot-row, [data-role="assistant"]) :is(.message, .message-bubble, .bubble) {
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  border-color: var(--twin-border) !important;
  border-radius: 18px 18px 18px 4px !important;
}

/* ---------- Nested bubble elements: flatten so only the outermost draws ---------- */
.message-row:is(.bot-row, .user-row, [data-role]) :is(.message, .message-bubble, .bubble) :is(.message, .message-bubble, .bubble) {
  background: transparent !important;
  border: 0 !important;
  border-radius: 0 !important;
  padding: 0 !important;
}

/* ---------- Text inside bubbles ---------- */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14.5px !important;
  line-height: 1.6 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

.message-row .message a,
.message-row .message-bubble a {
  color: var(--twin-gold) !important;
  text-decoration: underline;
  text-underline-offset: 3px;
}
.message-row:is(.user-row, [data-role="user"]) .message a { color: #ffffff !important; }

/* Lists inside answers */
.message-row .message :is(ul, ol),
.message-row .message-bubble :is(ul, ol) {
  margin: 4px 0 8px !important;
  padding-left: 20px !important;
}

/* Code: re-enable a surface after the blanket reset above */
.message-row .message pre,
.message-row .message-bubble pre {
  background: rgba(0, 0, 0, 0.28) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-sm) !important;
  padding: 12px 14px !important;
  overflow-x: auto;
}
.message-row .message code,
.message-row .message-bubble code {
  font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace !important;
  font-size: 13px !important;
}
.message-row .message :not(pre) > code,
.message-row .message-bubble :not(pre) > code {
  background: rgba(127, 127, 150, 0.2) !important;
  border-radius: 6px !important;
  padding: 1px 6px !important;
}

/* A single, quick fade for new messages. It responds to the user sending something. */
@media (prefers-reduced-motion: no-preference) {
  .message-row { animation: twin-in 0.18s ease-out; }
  @keyframes twin-in {
    from { opacity: 0; transform: translateY(4px); }
    to   { opacity: 1; transform: none; }
  }
}

/* ---------- Input ---------- */
textarea, input[type="text"] {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-md) !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14.5px !important;
  padding: 13px 16px !important;
  line-height: 1.45 !important;
  min-height: 50px !important;
  box-shadow: none !important;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
textarea:focus, input[type="text"]:focus {
  border-color: var(--twin-gold) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(236, 173, 10, 0.18) !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] { align-items: stretch !important; gap: 10px !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: var(--twin-radius-md) !important;
  background: var(--twin-surface) !important;
  color: var(--twin-text) !important;
  padding: 0 18px !important;
  min-height: 50px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease, transform 0.1s ease;
}
button:hover { border-color: var(--twin-gold) !important; color: var(--twin-gold) !important; }
button:active { transform: scale(0.98); }
button:focus-visible {
  outline: 2px solid var(--twin-gold) !important;
  outline-offset: 2px !important;
}

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-gold) !important;
  border: 1px solid var(--twin-gold) !important;
  color: #15110a !important;
  min-height: 50px !important;
  min-width: 50px !important;
  padding: 0 16px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: #ffc320 !important;
  border-color: #ffc320 !important;
  color: #15110a !important;
}

/* Submit-button icon: centred and sized */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #15110a !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Example prompts as chips ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 18px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 999px !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 400 !important;
  padding: 9px 16px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;
  color: var(--twin-blue) !important;
  background: var(--twin-surface) !important;
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 8px !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 6px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color: var(--twin-gold) !important;
  background: var(--twin-surface-2) !important;
}

/* ---------- Scrollbar ---------- */
* { scrollbar-width: thin; scrollbar-color: var(--twin-border-strong) transparent; }
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-purple); }

/* ---------- Selection ---------- */
::selection { background: var(--twin-gold); color: #15110a; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 28px 14px 36px !important; }
  .gradio-container h1 { font-size: 24px !important; }
  .chatbot, .chatbot.block { min-height: 420px !important; border-radius: var(--twin-radius-md) !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""