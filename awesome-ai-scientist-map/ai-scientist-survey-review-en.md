# Awesome AI Scientist: A Survey of AI Systems for Scientific Discovery

## Abstract

AI Scientist systems have moved from isolated literature-search and coding assistants toward agentic workflows that propose hypotheses, execute experiments, generate reports, and expose their own behavior to benchmark evaluation. This survey synthesizes a corpus of 31 verified ecosystem records: 16 systems or products and 15 benchmarks or datasets. Rather than listing artifacts one by one, the survey organizes the field around four questions: what kinds of systems are being built, which stages of the scientific lifecycle they cover, how autonomy is currently bounded, and how the community evaluates their claims. The central finding is that the ecosystem has split into three interacting layers: end-to-end AI Scientist prototypes, domain-specific discovery agents, and evaluation benchmarks that increasingly test long-horizon research behavior. Current systems show credible progress in bounded computational and search-heavy settings, but robust scientific validation still depends on human review, controlled execution environments, and benchmark designs that resist superficial report generation.

**Keywords:** AI Scientist; scientific discovery agents; automated research; research benchmarks; AI for science.

## 1. Introduction

The phrase *AI Scientist* increasingly refers to a family of systems that attempt to automate parts of the scientific lifecycle rather than merely answer research questions. The strongest claims come from end-to-end systems that generate ideas, write code, run experiments, analyze results, and draft papers. Adjacent systems cover narrower but still consequential slices: literature synthesis, hypothesis generation, chemistry planning, autonomous laboratories, algorithm discovery, scientific coding, reproducibility, and deep research reporting.

This survey treats the field as an ecosystem rather than a single benchmark race. The reason is practical: a system such as The AI Scientist is not comparable to Elicit, PaperBench, Coscientist, or AlphaEvolve on one scalar axis. Each artifact occupies a different position in the research stack. A useful review therefore needs a taxonomy, a timeline, an autonomy model, and an evaluation map that connects systems to the benchmarks and real-world settings used to justify them.

## 2. Corpus and Review Method

The review is based on 31 structured records generated from primary or official sources where possible. The corpus includes papers, repositories, product pages, benchmark pages, dataset pages, and exported PDF/Markdown artifacts. Items were included if they automate or substantially augment scientific research workflows, or if they evaluate such systems. General chatbots and unrelated foundation models were excluded unless they appeared as part of a research-agent workflow.

The resulting corpus contains: End-to-end AI Scientist systems: 3, Research workflow agents: 1, Hypothesis and research-planning systems: 1, Domain scientific-discovery agents: 6, Science agent product suites: 2, Deep-research products: 1, Literature-review products: 2, Evaluation benchmarks and datasets: 15. This distribution already reveals the maturity of the field: benchmark work is nearly as numerous as system-building work, suggesting that the community is still negotiating what counts as scientific progress by agents.

| Category | Count | Interpretation |
| --- | --- | --- |
| End-to-end AI Scientist systems | 3 | System or product layer |
| Research workflow agents | 1 | System or product layer |
| Hypothesis and research-planning systems | 1 | System or product layer |
| Domain scientific-discovery agents | 6 | System or product layer |
| Science agent product suites | 2 | System or product layer |
| Deep-research products | 1 | System or product layer |
| Literature-review products | 2 | System or product layer |
| Evaluation benchmarks and datasets | 15 | Evaluation infrastructure |

## 3. Taxonomy of the AI Scientist Ecosystem

The ecosystem is best understood as a layered stack. At the top are end-to-end AI Scientist systems, which attempt to bind ideation, implementation, experimentation, and paper drafting into one loop. The middle layer contains domain discovery agents, such as chemistry, biology, materials, and algorithm-discovery systems. The bottom and cross-cutting layer contains research products and benchmarks: tools that either support human researchers directly or measure whether agents can perform credible research work.

### End-to-end AI Scientist systems

- **DeepScientist** (2025-09-30, L4): Local-first autonomous research studio for long-horizon scientific discovery and paper-oriented workflows.
- **The AI Scientist** (2024-08-12, L4): Autonomous scientist for end-to-end machine learning paper generation.
- **The AI Scientist-v2** (2025-04-07, L4): Autonomous scientist for open-ended machine-learning discovery via agentic tree search.

### Research workflow agents

- **Agent Laboratory** (2025-01-08, L3): Autonomous research assistant

### Hypothesis and research-planning systems

- **AI Co-Scientist / Co-Scientist** (2025-02-19, L3): Collaborative co-scientist for scientist-in-the-loop hypothesis generation and research planning.

### Domain scientific-discovery agents

- **A-Lab / GNoME Materials Discovery Lineage** (2023-11, L4): Autonomous materials discovery stack that combines large-scale learned candidate generation with robotic closed-loop synthesis and characterization.
- **AlphaEvolve** (2025-05-14, L3): A Gemini-powered evolutionary coding agent for algorithm discovery and system optimization.
- **ChemCrow** (2023-04-11, L2): A tool-augmented chemistry assistant that uses GPT-4 plus expert-designed tools to solve reasoning-intensive chemistry tasks.
- **Coscientist** (2023-12-20, L4): A GPT-4-based autonomous chemistry co-scientist for planning, executing, and optimizing laboratory experiments.
- **Robin** (2025-05-19, L3): Semi-autonomous scientific discovery system
- **SciAgents** (2024-09-09, L3): Domain-specific autonomous co-scientist for graph-grounded hypothesis generation in materials science.

### Science agent product suites

- **Asta** (2025-08-26, L2): A science-focused agent ecosystem that combines research assistants, benchmark infrastructure, and developer resources.
- **FutureHouse Platform Agents** (2025-05-01, L2): Scientific agent platform

### Deep-research products

- **OpenAI Deep Research** (2025-02-02, L2): An agentic deep-research product for multi-step web research, source analysis, and citation-grounded report generation.

### Literature-review products

- **Consensus** (2021, L1): AI academic search and evidence-synthesis workspace for scientific research.
- **Elicit** (2021-08-31, L1): An AI research assistant and literature-review platform focused on paper search, evidence extraction, and synthesis.


This taxonomy suggests that autonomy is not a binary property. Literature-review products are often useful at L1, deep-research products and product suites sit near L2, workflow agents approach L3, and the strongest end-to-end or laboratory systems claim L4 behavior in bounded domains. No record in this corpus should be read as demonstrating unconstrained L5 scientific autonomy.

## 4. Historical Development

The modern ecosystem begins with tool-augmented scientific agents and autonomous laboratory work in 2023, expands into broad AI Scientist and benchmark efforts in 2024, and becomes a much denser landscape in 2025-2026. The timeline shows a shift from individual proof-of-concept systems toward benchmark suites and productized scientific assistants.

| Year | Items | Representative records |
| --- | --- | --- |
| 2021 | 2 | Consensus, Elicit |
| 2023 | 4 | ChemCrow, MLAgentBench, A-Lab / GNoME Materials Discovery Lineage, Coscientist |
| 2024 | 7 | DiscoveryBench, SciCode, The AI Scientist, SciAgents, DSBench, CORE-Bench, MLE-bench |
| 2025 | 16 | Agent Laboratory, OpenAI Deep Research, AI Co-Scientist / Co-Scientist, BixBench, ResearchBench, PaperBench, The AI Scientist-v2, Deep Research Bench / RetroSearch, FutureHouse Platform Agents, AlphaEvolve, Robin, DeepResearch Bench, AstaBench, Asta, DeepScientist, AInsteinBench |
| 2026 | 2 | MMDeepResearch-Bench, AIRS-Bench |

## 5. Capability Patterns Across the Scientific Lifecycle

Across the corpus, five recurring capability patterns appear. First, **research synthesis** systems search, screen, summarize, and cite literature. Second, **hypothesis systems** propose candidate explanations, inspirations, or research plans. Third, **computational research agents** write and run code for machine-learning or data-science tasks. Fourth, **domain discovery systems** couple LLM reasoning with domain tools, laboratory automation, or external simulators. Fifth, **evaluation systems** define tasks, rubrics, and environments that convert qualitative research behavior into comparable scores.

The most important design tension is breadth versus validation. Broad agents cover more of the lifecycle but are harder to evaluate rigorously. Domain systems are narrower, but they can sometimes close the loop with real experiments, physical instruments, or task-specific metrics. Benchmarks sit between those extremes: they enable comparison, but they can encourage optimization for benchmark-specific behavior rather than genuine discovery.

## 6. Evaluation Benchmarks and What They Measure

The benchmark layer is the most developed part of the corpus. It covers ML experimentation, paper replication, computational reproducibility, data-driven discovery, scientific coding, bioinformatics, deep research, multimodal report generation, and scientific software maintenance. These benchmarks do not measure the same construct. Some reward code that runs; others reward literature-grounded reports; others test whether an agent can reproduce a paper or maintain a scientific codebase.

| Benchmark | Release | Target autonomy | Evaluates |
| --- | --- | --- | --- |
| AInsteinBench | 2025-12-24 | L2-L3 | scientific repository maintenance, scientific computing code agents, real PR tasks, feature implementation |
| AIRS-Bench | 2026-02-09 | L3-L4 | full ML research lifecycle, idea generation, experiment analysis, iterative refinement |
| AstaBench | 2025-08 | L1-L3 | scientific research agents, paper finding, scholarly question answering, tool use |
| BixBench | 2025-02-28 |  | bioinformatics, biological data analysis, multi-step dataset exploration, open-ended computational biology reasoning |
| CORE-Bench | 2024-09-17 | L2-L3 | computational reproducibility, research artifact execution, code reproducibility |
| Deep Research Bench / RetroSearch | 2025-05 | L2 | web research agents, frozen-web retrieval, tool use, hallucination |
| DeepResearch Bench | 2025-06 | L2 | deep research agents, citation quality, retrieval accuracy, long-form report quality |
| DiscoveryBench | 2024-07-01 | L2-L3 | data-driven discovery, hypothesis generation, multi-step reasoning, data semantics |
| DSBench | 2024-09-12 |  | data science, data analysis, data modeling, spreadsheet and Kaggle-style task solving |
| MLAgentBench | 2023-10-05 |  | ML experimentation, code execution, model improvement, long-term planning |
| MLE-bench | 2024-10-09 | L2-L3 | ML engineering, Kaggle-style competition performance, agent scaffolds, resource scaling behavior |
| MMDeepResearch-Bench | 2026-01 | L2 | multimodal deep research, image-text evidence use, citation grounding, report integrity |
| PaperBench | 2025-04-02 |  | paper-to-code replication, AI research engineering, long-horizon agent execution, autonomous experiment execution |
| ResearchBench | 2025-03-27 | L2-L3 | scientific discovery, inspiration-based reasoning, hypothesis generation, literature-grounded ideation |
| SciCode | 2024-07-18 |  | scientific coding, research problem solving, natural-science computation, code synthesis |

A key conclusion is that benchmark plurality is necessary. PaperBench and MLE-bench stress research engineering; DiscoveryBench and ResearchBench stress hypothesis generation; CORE-Bench and AInsteinBench stress reproducibility and scientific software; DeepResearch Bench and RetroSearch stress source-grounded reporting; BixBench and SciCode add domain-specific scientific reasoning. A single leaderboard cannot represent this ecosystem without hiding major differences in task definition.

## 7. Autonomy, Control, and Human Roles

The records show a consistent pattern: the more a system approaches end-to-end autonomy, the more it needs explicit boundaries. Boundaries include benchmark task definitions, sandboxed execution, human approval, curated datasets, laboratory constraints, citation requirements, or post-hoc expert review. Human scientists remain central as task framers, safety reviewers, domain validators, and judges of novelty.

The practical autonomy ladder in this corpus is therefore relational. L1 systems support human search and synthesis. L2 systems chain tools within a bounded workflow. L3 systems propose and iterate on hypotheses or experiments while relying on human gates. L4 systems execute a full loop in a bounded domain. The evidence base does not yet support treating any of these systems as open-ended autonomous scientists.

## 8. System Relationships and Ecosystem Structure

Several relationships cut across the records. The AI Scientist line motivates end-to-end machine-learning research loops and connects naturally to PaperBench, MLE-bench, MLAgentBench, and AIRS-Bench. Chemistry and materials systems form a second lineage through ChemCrow, Coscientist, A-Lab/GNoME, and related domain agents. Research products such as Elicit, Consensus, OpenAI Deep Research, Asta, and FutureHouse agents form a product layer that is less autonomous than the research prototypes but more likely to be used by working scientists.

This structure matters because progress in one layer does not automatically transfer to another. A benchmark-winning coding agent may not be a reliable literature reviewer. A strong deep-research product may still lack experimental execution. A laboratory agent that succeeds in a narrow chemistry protocol may not generalize to open-ended theory formation.

## 9. Risks, Limitations, and Open Problems

Three risks recur. The first is **scientific integrity risk**: systems can produce plausible but unsupported novelty claims, fabricated or weak citations, and papers that look complete despite fragile evidence. The second is **evaluation risk**: benchmark performance may reflect task-specific adaptation, judge-model bias, or contamination rather than robust research competence. The third is **operational risk**: agents with code execution, web access, chemical planning, or laboratory control require stronger safety and audit mechanisms than ordinary search tools.

The most important open problems are therefore not only model capability problems. They include provenance tracking, benchmark contamination control, reproducible execution logs, human-in-the-loop review design, domain-specific safety policies, and better separation between report quality and discovery quality.

## 10. Future Directions

Future AI Scientist work should move from impressive demonstrations toward controlled evidence. Promising directions include modular evaluation of lifecycle stages, benchmark suites that combine code execution with source-grounded reporting, domain tasks with expert validation, and systems that expose their reasoning, tool calls, failures, and uncertainty. The field also needs negative results: failed hypotheses, invalid experiments, and non-reproducible agent outputs should be preserved rather than filtered away.

## 11. Corpus Census

The full corpus is listed below to preserve the total-count requirement and make the synthesis auditable.

| # | Item | Category | Release | Autonomy | Domains |
| --- | --- | --- | --- | --- | --- |
| 1 | A-Lab / GNoME Materials Discovery Lineage | Domain scientific-discovery agents | 2023-11 | L4 | materials science, inorganic chemistry |
| 2 | Agent Laboratory | Research workflow agents | 2025-01-08 | L3 | machine learning, general computational research |
| 3 | AI Co-Scientist / Co-Scientist | Hypothesis and research-planning systems | 2025-02-19 | L3 | biomedicine, biology, general science |
| 4 | AInsteinBench | Evaluation benchmarks and datasets | 2025-12-24 | L2-L3 | scientific computing, quantum chemistry, quantum computing, molecular dynamics |
| 5 | AIRS-Bench | Evaluation benchmarks and datasets | 2026-02-09 | L3-L4 | machine learning, natural language processing, mathematics, coding |
| 6 | AlphaEvolve | Domain scientific-discovery agents | 2025-05-14 | L3 | algorithms, mathematics, systems optimization, AI infrastructure |
| 7 | Asta | Science agent product suites | 2025-08-26 | L2 | general science |
| 8 | AstaBench | Evaluation benchmarks and datasets | 2025-08 | L1-L3 | scientific research, literature understanding, code execution, data analysis |
| 9 | BixBench | Evaluation benchmarks and datasets | 2025-02-28 |  | bioinformatics, computational biology, genomics, transcriptomics |
| 10 | ChemCrow | Domain scientific-discovery agents | 2023-04-11 | L2 | chemistry |
| 11 | Consensus | Literature-review products | 2021 | L1 | general academic research |
| 12 | CORE-Bench | Evaluation benchmarks and datasets | 2024-09-17 | L2-L3 | computational reproducibility, computer science, social science, medicine |
| 13 | Coscientist | Domain scientific-discovery agents | 2023-12-20 | L4 | chemistry |
| 14 | Deep Research Bench / RetroSearch | Evaluation benchmarks and datasets | 2025-05 | L2 | web research, open-web retrieval, multi-domain factual synthesis, tool-using agents |
| 15 | DeepResearch Bench | Evaluation benchmarks and datasets | 2025-06 | L2 | deep research, web research, citation-rich report generation, science and technology |
| 16 | DeepScientist | End-to-end AI Scientist systems | 2025-09-30 | L4 | machine learning, scientific tasks |
| 17 | DiscoveryBench | Evaluation benchmarks and datasets | 2024-07-01 | L2-L3 | sociology, biology, humanities, economics |
| 18 | DSBench | Evaluation benchmarks and datasets | 2024-09-12 |  | data science, data analysis, data modeling, tabular reasoning |
| 19 | Elicit | Literature-review products | 2021-08-31 | L1 | general academic research, systematic reviews |
| 20 | FutureHouse Platform Agents | Science agent product suites | 2025-05-01 | L2 | biology, chemistry, biomedicine |
| 21 | MLAgentBench | Evaluation benchmarks and datasets | 2023-10-05 |  | machine learning experimentation, ML engineering, agentic code execution, model improvement |
| 22 | MLE-bench | Evaluation benchmarks and datasets | 2024-10-09 | L2-L3 | machine learning engineering, Kaggle-style competitions, applied machine learning |
| 23 | MMDeepResearch-Bench | Evaluation benchmarks and datasets | 2026-01 | L2 | multimodal deep research, image-text evidence synthesis, long-form report generation, general research |
| 24 | OpenAI Deep Research | Deep-research products | 2025-02-02 | L2 | finance, science, policy, engineering |
| 25 | PaperBench | Evaluation benchmarks and datasets | 2025-04-02 |  | AI research engineering, machine learning paper replication, long-horizon agent execution |
| 26 | ResearchBench | Evaluation benchmarks and datasets | 2025-03-27 | L2-L3 | general scientific discovery, natural language processing, hypothesis generation, literature-grounded research |
| 27 | Robin | Domain scientific-discovery agents | 2025-05-19 | L3 | biology, biomedicine |
| 28 | SciAgents | Domain scientific-discovery agents | 2024-09-09 | L3 | materials science, bioinspired materials |
| 29 | SciCode | Evaluation benchmarks and datasets | 2024-07-18 |  | scientific coding, mathematics, physics, chemistry |
| 30 | The AI Scientist | End-to-end AI Scientist systems | 2024-08-12 | L4 | machine learning |
| 31 | The AI Scientist-v2 | End-to-end AI Scientist systems | 2025-04-07 | L4 | machine learning |

## 12. Key Source Links

| Item | Primary or official source |
| --- | --- |
| A-Lab / GNoME Materials Discovery Lineage | https://www.nature.com/articles/s41586-023-06734-w |
| Agent Laboratory | https://arxiv.org/abs/2501.04227 |
| AI Co-Scientist / Co-Scientist | https://www.nature.com/articles/s41586-026-10644-y |
| AInsteinBench | https://arxiv.org/abs/2512.21373 |
| AIRS-Bench | https://arxiv.org/abs/2602.06855 |
| AlphaEvolve | https://arxiv.org/abs/2506.13131 |
| Asta | https://arxiv.org/abs/2510.21652 |
| AstaBench | https://arxiv.org/abs/2510.21652 |
| BixBench | https://arxiv.org/abs/2503.00096 |
| ChemCrow | https://arxiv.org/abs/2304.05376 |
| CORE-Bench | https://arxiv.org/abs/2409.11363 |
| Coscientist | https://www.nature.com/articles/s41586-023-06792-0 |
| Deep Research Bench / RetroSearch | https://arxiv.org/abs/2506.06287 |
| DeepResearch Bench | https://arxiv.org/abs/2506.11763 |
| DeepScientist | https://arxiv.org/abs/2509.26603 |
| DiscoveryBench | https://arxiv.org/abs/2407.01725 |
| DSBench | https://arxiv.org/abs/2409.07703 |
| Elicit | https://elicit.com/ |
| MLAgentBench | https://arxiv.org/abs/2310.03302 |
| MLE-bench | https://arxiv.org/abs/2410.07095 |
| MMDeepResearch-Bench | https://arxiv.org/abs/2601.12346 |
| OpenAI Deep Research | https://openai.com/index/introducing-deep-research/ |
| PaperBench | https://arxiv.org/abs/2504.01848 |
| ResearchBench | https://arxiv.org/abs/2503.21248 |
| Robin | https://arxiv.org/abs/2505.13400 |
| SciAgents | https://arxiv.org/abs/2409.05556 |
| SciCode | https://arxiv.org/abs/2407.13168 |
| The AI Scientist | https://arxiv.org/abs/2408.06292 |
| The AI Scientist-v2 | https://arxiv.org/abs/2504.08066 |
