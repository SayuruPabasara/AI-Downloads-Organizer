# 🎓 AI-Powered Downloads Organizer for University Materials

## Workflow Architecture

```text
   ┌────────────────────┐
   │ New completed file │
   └─────────┬──────────┘
             │
             ▼
   ┌────────────────────┐
   │  Extract filename  │
   └─────────┬──────────┘
             │
             ▼
   ┌───────────────────────────┐
   │ Check local rules/mapping │
   └─────────┬─────────────────┘
             │
             ▼
          /─────\
         / Match \
        <  found? >
         \       /
          \─────/
           /   \
     YES  /     \  NO
         ▼       ▼
┌───────────────┐   ┌───────────┐
│ Move directly │   │  Ask LLM  │
└───────────────┘   └─────┬─────┘
                          │
                          ▼
                    ┌───────────┐
                    │Destination│
                    └───────────┘