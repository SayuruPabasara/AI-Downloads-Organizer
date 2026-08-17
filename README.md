### 🎓 AI-Powered Downloads Organizer for University Materials

#### Workflow

```text
             Courseweb page
                   │
                   │ content script
                   ▼
          ┌─────────────────┐
          │ Page information│
          │                 │
          │ course ID       │
          │ section/topic   │
          │ link text       │
          │ download URL    │
          └────────┬────────┘
                   │
                   ▼
             Background.js
                   │
             download event
                   │
                   ▼
                Python
                   │
          ┌────────┴────────┐
          ▼                 ▼
    Local mapping       OpenRouter
             
