# AI Agents Glossary for Builders

A practical one-page glossary for shipping agentic products without getting lost in buzzwords.

| Term | Builder-friendly meaning |
|---|---|
| **AI agent** | Software that uses an AI model to pursue a goal, choose next steps, call tools, and act across multiple turns. Caveat: “agent” is fuzzy; many products use it for simple chatbots. |
| **Workflow vs. agent** | A **workflow** follows mostly predefined steps; an **agent** dynamically decides what to do next. Start with workflows when reliability matters. |
| **Autonomy** | How much freedom the system has to plan, act, retry, and make decisions without a human. More autonomy means more need for limits, logs, and review. |
| **Action space / permissions** | The set of actions an agent is allowed to take: read data, send emails, run code, modify records, charge cards, etc. Keep this narrow by default. |
| **Tool / function calling** | Letting the model invoke external capabilities such as APIs, databases, calculators, search, or internal services. Treat tool inputs as untrusted until validated. |
| **Structured outputs** | Forcing model responses into a schema, such as JSON with required fields. Essential when another system will parse or act on the result. |
| **Context window** | The amount of text the model can “see” at once: prompt, conversation, tool results, and retrieved docs. Bigger windows help, but irrelevant context still hurts. |
| **Context engineering** | Designing what information enters the model’s context, in what format, and when. Often more important than clever prompting. |
| **Memory / checkpointing** | Saving useful state across turns or runs: user preferences, task progress, decisions, intermediate outputs. Separate durable facts from temporary scratchpad notes. |
| **RAG / retrieval** | Fetching relevant external information and placing it in context before the model answers or acts. Good retrieval beats dumping entire docs into the prompt. |
| **Embeddings / vector store** | Embeddings turn text into numbers for similarity search; vector stores save and query those embeddings. Useful for semantic retrieval, not magic truth checking. |
| **Planning** | Having the model break a goal into steps before acting. Plans are helpful, but they should be revisable when tools return new information. |
| **ReAct loop** | A common pattern: reason, act with a tool, observe the result, then repeat. Make loops bounded so the agent cannot spin forever. |
| **Orchestration** | The control layer that routes tasks, calls tools, manages state, handles errors, and decides which model or agent runs next. This is where production quality lives. |
| **Router / supervisor** | A router sends requests to the right path; a supervisor oversees agents or steps and decides what happens next. Keep routing rules inspectable where possible. |
| **Multi-agent system** | Multiple specialized agents working together, often with different roles or tools. Useful for separation of concerns, but adds latency, cost, and debugging complexity. |
| **Handoff / subagent / skill** | Ways to delegate part of a job to a narrower component. Prefer small, well-scoped skills before building a swarm of autonomous agents. |
| **Human-in-the-loop (HITL)** | A human reviews, approves, edits, or blocks important actions. Use HITL for high-risk steps like sending messages, spending money, or changing customer data. |
| **Guardrails** | Rules, checks, filters, schemas, and policies that constrain behavior. Guardrails reduce risk but do not replace careful system design and testing. |
| **Sandboxing** | Running tools, code, or file operations in an isolated environment with limited access. Critical when agents can execute code or handle untrusted inputs. |
| **Prompt injection / tool poisoning** | Attacks where external content tries to override instructions or manipulate tool behavior. Never let retrieved text or tool output become trusted instructions. |
| **Observability / tracing** | Capturing prompts, tool calls, model outputs, latency, cost, errors, and decisions. If you cannot trace it, you cannot debug or improve it. |
| **Evals** | Tests that measure whether the agent succeeds, fails safely, and behaves consistently. Include task success, tool accuracy, refusal behavior, cost, and latency. |
| **MCP (Model Context Protocol)** | A standard way to connect models or agent apps to external tools and data sources. Helpful for interoperability, but still requires permissioning and security review. |
| **Latency / cost budget** | The time and money you are willing to spend per task. Agent loops, retrieval, and multi-agent calls can multiply both quickly. |

## Builder rule of thumb

Ship the smallest reliable agentic system: narrow permissions, explicit state, validated tool calls, strong traces, bounded loops, and human approval anywhere the action is expensive, irreversible, or customer-visible.
