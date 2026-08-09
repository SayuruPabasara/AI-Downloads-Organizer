### 🎓 AI-Powered Downloads Organizer for University Materials

#### Workflow

```text
    New completed file 
             │
             ▼
    Extract filename  
             │
             ▼
    Check local rules/mapping
             │
             ▼
          /─────\
         / Match \
        <  found? >
          \─────/
     YES  /     \  NO
         ▼       ▼
       Move       Ask LLM 
     directly        │
                     ▼
                Destination
                 