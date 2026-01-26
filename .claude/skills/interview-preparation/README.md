# Interview Preparation Skills Directory

This directory contains Claude agent skills for technical interview preparation, organized by problem category and difficulty level.

## 📚 Directory Overview

```
.claude/skills/interview-preparation/
├── SKILL.md                    (Core skill - template for header notes)
├── README.md                   (This file - directory index)
├── merge-sorted-arrays.md      (Solution guide example)
└── [additional-skills]/
```

---

## 🎯 Core Skill: Adding Interview-Ready Header Notes

### **[SKILL.md](./SKILL.md)** — Template & Guide for Header Notes

This is the foundational skill that defines how to add comprehensive header notes to all Python implementation files.

**What it covers:**
- Standardized header structure
- Step-by-step implementation guide
- Key concepts explanation patterns
- Interview talking points (30s, rapid-fire, one-liner)
- Quality checklist
- Common pitfalls to avoid

**When to use:**
- Creating new interview preparation solution files
- Updating existing Python scripts with proper documentation
- Ensuring consistent interview preparation across the project

**Quick reference:**
```python
"""
## Problem Statement
[Clear objective and context]

## Whiteboard Coding Challenge Notes

* For this problem, I'm using [approach]:
[Why this approach]

* Key Concepts:
  - [Concept 1: Why/How?]
  - [Concept 2: Why/How?]

* Logic:
1. [Step 1]
2. [Step 2]
...

* **30-Second Pitch**: [Verbal explanation]
* **Rapid-Fire Version**: [Bullet points]
* **Ultra-Minimal One-Liner**: [Single sentence]
"""
```

---

## 📋 Available Solution Guides

### Array & String Algorithms

#### **[merge-sorted-arrays.md](./merge-sorted-arrays.md)** — Merge Two Sorted Arrays In-Place
- **Category:** Array Manipulation
- **Difficulty:** Medium
- **Algorithm:** GAP Method (Shell Sort inspired)
- **Time Complexity:** O((n+m) × log(n+m))
- **Space Complexity:** O(1)
- **Key Concepts:**
  - Gap initialization and reduction formula
  - Helper functions for abstraction
  - In-place algorithm design
- **Interview Focus:** Space optimization, algorithm design, code clarity

---

## 🚀 How to Use These Skills

### For Interview Practice
1. Start with **[SKILL.md](./SKILL.md)** to understand the header structure
2. Review a specific solution guide (e.g., **merge-sorted-arrays.md**)
3. Read the **Problem Statement** section first
4. Study the **Key Concepts** deeply
5. Practice the **30-Second Pitch**, **Rapid-Fire Version**, and **Ultra-Minimal One-Liner**
6. Work through **Test Cases** to validate understanding
7. Review **Common Interview Questions** for anticipated follow-ups

### For Adding New Solutions
1. Reference **[SKILL.md](./SKILL.md)** template
2. Follow the standardized structure
3. Ensure all checklist items are completed
4. Update this README.md with new solution entry

### For Agent Interaction
Reference skills using Claude's @ mention feature:
```
@SKILL explain the header structure I should use
@merge-sorted-arrays explain the gap reduction formula
```

### For Continuous Learning
- Review one skill per day
- Practice articulating answers in different timeframes (30s, 1m, 5m)
- Test implementations against provided test cases
- Study variations and follow-up discussions

---

## 📖 Solution Guide Structure

Each solution guide (e.g., merge-sorted-arrays.md) includes:

| Section | Purpose |
|---------|---------|
| **Overview** | Quick context and importance |
| **Problem Statement** | Clear objective, constraints, and context |
| **Solution Approach** | Algorithm overview and key insight |
| **Complexity Analysis** | Time and space complexity breakdown |
| **Key Concepts** | Design decisions and their rationale |
| **Implementation Logic** | Step-by-step algorithm description |
| **Interview Talking Points** | Multiple explanation formats |
| **Common Questions** | Anticipated follow-ups with answers |
| **Variations** | Alternative approaches and trade-offs |
| **Test Cases** | Validation scenarios |
| **Follow-up Discussion** | Advanced topics for deeper exploration |

---

## 🔗 Skill Relationships

### Prerequisite Skills
- Two-Pointer Technique
- Array Manipulation Basics
- Sorting Algorithms fundamentals
- Space-Time Trade-offs

### Similar Problem Patterns
- Merge Intervals
- Merge k Sorted Lists
- Sort Colors (Dutch National Flag)
- In-Place Array Rotation

---

## ✅ Quality Assurance

All skills in this directory follow these standards:

- ✅ Consistent markdown formatting
- ✅ Clear section hierarchy
- ✅ Multiple explanation formats
- ✅ Real implementation examples
- ✅ Comprehensive test cases
- ✅ Interview-contextualized content
- ✅ Complexity analysis included
- ✅ Design decisions explained

---

## 🏷️ Tags & Keywords

### Skill Tags
`#interview-prep` `#algorithm` `#interview-coaching` `#documentation`

### By Difficulty
`#beginner` `#intermediate` `#advanced`

### By Category
`#array` `#string` `#graph` `#tree` `#dynamic-programming` `#sorting` `#searching`

### By Algorithm Type
`#gap-method` `#two-pointer` `#sliding-window` `#dfs` `#bfs` `#dp`

---

## 📝 File Naming Convention

Solutions follow this naming pattern:
```
{problem-name-with-hyphens}.md
```

Examples:
- `merge-sorted-arrays.md`
- `longest-substring-without-repeating.md`
- `merge-k-sorted-lists.md`

---

## 🔄 Skill Development Guidelines

### When Creating New Skills
1. Start with the **[SKILL.md](./SKILL.md)** template
2. Maintain consistent formatting across all skills
3. Include both theoretical understanding and practical implementation
4. Provide multiple time-based pitch variations
5. Include test cases and edge cases
6. Add follow-up discussion points
7. Reference related problems and patterns
8. Update this README.md with new entry

### Review & Maintenance
- Skills should be reviewed and updated quarterly
- Include feedback from recent interviews
- Add new patterns as encountered in practice
- Keep solution links functional and current

---

## 🎓 Learning Path Suggestion

### Week 1: Foundations
- [ ] Read [SKILL.md](./SKILL.md) thoroughly
- [ ] Study [merge-sorted-arrays.md](./merge-sorted-arrays.md)
- [ ] Implement the merge-sorted-arrays solution locally

### Week 2: Practice & Articulation
- [ ] Practice 30-second pitch for merge-sorted-arrays
- [ ] Study common interview questions
- [ ] Explore variations and alternative approaches

### Week 3: Extension
- [ ] Work through follow-up discussion points
- [ ] Add one new solution guide following [SKILL.md](./SKILL.md) template
- [ ] Cross-reference related problem patterns

---

## 📞 Integration Points

### With Main Project
- Link solution Python files in `/drills/` or `/leetcode/` to solution guides
- Update file headers using [SKILL.md](./SKILL.md) template
- Reference during code reviews and learning sessions

### With Interview Preparation
- Use as preparation material before coding interviews
- Reference specific solutions during mock interviews
- Adapt talking points for different interview scenarios

---

## 📊 Statistics

| Metric | Count |
|--------|-------|
| Total Solutions | 1 |
| Categories | 1 (Array & String) |
| Difficulty Levels | Medium |
| Average Complexity | O((n+m) × log(n+m)) |

---

## 📅 Maintenance Log

| Date | Change | Author |
|------|--------|--------|
| 2026-01-26 | Created SKILL.md and README.md structure | Copilot |
| 2026-01-26 | Added merge-sorted-arrays.md solution guide | Copilot |

---

## 🔗 Quick Links

- **[SKILL.md](./SKILL.md)** — Core skill template
- **[merge-sorted-arrays.md](./merge-sorted-arrays.md)** — First solution guide
- **[Project Root README](../../README.md)** — Main project documentation

---

## 💡 Tips for Best Results

1. **Read actively:** Don't just skim; engage with each concept
2. **Practice articulation:** Say the explanations out loud
3. **Time yourself:** Use the 30-second and rapid-fire versions as actual exercises
4. **Test implementations:** Run code against provided test cases
5. **Explain to others:** Teaching reinforces understanding
6. **Review periodically:** Revisit skills weekly for retention

---

**Last Updated:** January 26, 2026  
**Review Cycle:** Quarterly or when significant project structure changes occur  
**Maintainer Notes:** Add feedback from recent interviews and new patterns discovered
