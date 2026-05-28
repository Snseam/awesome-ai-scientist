# Awesome AI Scientist

Verified ecosystem map of AI Scientist systems, papers, benchmarks, products, and open-source implementations

- Generated from: `C:\Users\25705\Desktop\awesome-ai-scientist\awesome-ai-scientist-map\results`
- Items: 31
- Last verified in source records: 2026-05-28

## Table of Contents

1. [A-Lab / GNoME Materials Discovery Lineage](#a-lab-gnome-materials-discovery-lineage) - Category: domain_scientific_discovery_agent | First Public Release: 2023-11 | Autonomy Level: L4
2. [Agent Laboratory](#agent-laboratory) - Category: research_workflow_agent | First Public Release: 2025-01-08 | Autonomy Level: L3
3. [AI Co-Scientist / Co-Scientist](#ai-co-scientist-co-scientist) - Category: hypothesis_and_research_planning_system | First Public Release: 2025-02-19 | Autonomy Level: L3
4. [AInsteinBench](#ainsteinbench) - Category: benchmark | First Public Release: 2025-12-24 | Autonomy Level: L2-L3
5. [AIRS-Bench](#airs-bench) - Category: benchmark | First Public Release: 2026-02-09 | Autonomy Level: L3-L4
6. [AlphaEvolve](#alphaevolve) - Category: domain_scientific_discovery_agent | First Public Release: 2025-05-14 | Autonomy Level: L3
7. [Asta](#asta) - Category: science_product_suite | First Public Release: 2025-08-26 | Autonomy Level: L2
8. [AstaBench](#astabench) - Category: benchmark | First Public Release: 2025-08 | Autonomy Level: L1-L3
9. [BixBench](#bixbench) - Category: benchmark | First Public Release: 2025-02-28
10. [ChemCrow](#chemcrow) - Category: domain_scientific_discovery_agent | First Public Release: 2023-04-11 | Autonomy Level: L2
11. [Consensus](#consensus) - Category: literature_review_product | First Public Release: 2021 | Autonomy Level: L1
12. [CORE-Bench](#core-bench) - Category: benchmark | First Public Release: 2024-09-17 | Autonomy Level: L2-L3
13. [Coscientist](#coscientist) - Category: domain_scientific_discovery_agent | First Public Release: 2023-12-20 | Autonomy Level: L4
14. [Deep Research Bench / RetroSearch](#deep-research-bench-retrosearch) - Category: benchmark | First Public Release: 2025-05 | Autonomy Level: L2
15. [DeepResearch Bench](#deepresearch-bench) - Category: benchmark | First Public Release: 2025-06 | Autonomy Level: L2
16. [DeepScientist](#deepscientist) - Category: end_to_end_ai_scientist | First Public Release: 2025-09-30 | Autonomy Level: L4
17. [DiscoveryBench](#discoverybench) - Category: benchmark | First Public Release: 2024-07-01 | Autonomy Level: L2-L3
18. [DSBench](#dsbench) - Category: benchmark | First Public Release: 2024-09-12
19. [Elicit](#elicit) - Category: literature_review_product | First Public Release: 2021-08-31 | Autonomy Level: L1
20. [FutureHouse Platform Agents](#futurehouse-platform-agents) - Category: science_product_suite | First Public Release: 2025-05-01 | Autonomy Level: L2
21. [MLAgentBench](#mlagentbench) - Category: benchmark | First Public Release: 2023-10-05
22. [MLE-bench](#mle-bench) - Category: benchmark | First Public Release: 2024-10-09 | Autonomy Level: L2-L3
23. [MMDeepResearch-Bench](#mmdeepresearch-bench) - Category: benchmark | First Public Release: 2026-01 | Autonomy Level: L2
24. [OpenAI Deep Research](#openai-deep-research) - Category: deep_research_product | First Public Release: 2025-02-02 | Autonomy Level: L2
25. [PaperBench](#paperbench) - Category: benchmark | First Public Release: 2025-04-02
26. [ResearchBench](#researchbench) - Category: benchmark | First Public Release: 2025-03-27 | Autonomy Level: L2-L3
27. [Robin](#robin) - Category: domain_scientific_discovery_agent | First Public Release: 2025-05-19 | Autonomy Level: L3
28. [SciAgents](#sciagents) - Category: domain_scientific_discovery_agent | First Public Release: 2024-09-09 | Autonomy Level: L3
29. [SciCode](#scicode) - Category: benchmark | First Public Release: 2024-07-18
30. [The AI Scientist](#the-ai-scientist) - Category: end_to_end_ai_scientist | First Public Release: 2024-08-12 | Autonomy Level: L4
31. [The AI Scientist-v2](#the-ai-scientist-v2) - Category: end_to_end_ai_scientist | First Public Release: 2025-04-07 | Autonomy Level: L4

## Detailed Content

### A-Lab / GNoME Materials Discovery Lineage

#### Identity

**Id:** alab_gnome_materials_lineage


**Name:** A-Lab / GNoME Materials Discovery Lineage


**Aliases:**

- A-Lab
- GNoME
- An autonomous laboratory for the accelerated synthesis of inorganic materials
- Scaling deep learning for materials discovery
- Materials Discovery: GNoME


**Organization:**

> Lawrence Berkeley National Laboratory, University of California Berkeley, Google DeepMind, and collaborators


**First Public Release:** 2023-11


**Current Status:**

> Active research lineage with public Nature papers, a public GNoME dataset and code repository, and ongoing follow-up evaluation and replication activity.


#### Taxonomy

**Category:** domain_scientific_discovery_agent


**Type:** paper, dataset, infrastructure


**Domains:** materials_science, inorganic_chemistry


**Positioning:**

> Autonomous materials discovery stack that combines large-scale learned candidate generation with robotic closed-loop synthesis and characterization.


**Boundary Notes:**

> Included because the lineage spans both computational discovery and real-world autonomous execution in a scientific domain. It is broader than a single paper but narrower than a general AI scientist platform because it is centered on inorganic materials discovery.


#### Capabilities

**Lifecycle Coverage:**

- materials_candidate_generation
- stability_screening
- synthesis_planning
- robotic_synthesis
- characterization
- active_learning
- autonomous_decision_making


**Tool Access:**

- large-scale DFT workflows
- Materials Project data
- OQMD data
- natural-language synthesis models
- ARROWS active learning
- robotic powder handling
- box furnaces
- XRD characterization
- laboratory API
- GNoME dataset and models


**Execution Environment:**

> Hybrid environment: large-scale computational materials discovery on DeepMind and database infrastructure, plus robotic closed-loop execution in the Berkeley Lab A-Lab.


**Artifact Outputs:**

- predicted stable crystal structures
- updated convex-hull materials dataset
- synthesis recipes
- experimental XRD analyses
- validated inorganic compounds
- follow-up active-learning decisions


**Human Roles:**

> Humans defined the initial target set, can submit jobs through the lab API, and manually refined diffraction patterns after the autonomous runs to confirm outcomes. Researchers also decide follow-up scientific use of predicted or synthesized materials.


#### Autonomy

**Autonomy Level:** L4


**Autonomy Rationale:**

> The lineage moves beyond recommendation into constrained real-world autonomous action: GNoME generates candidates at scale and A-Lab plans, executes, characterizes, and iterates on experiments through robotics and active learning. Humans still frame targets, maintain the platform, and validate broader scientific conclusions.


**Iteration Loop:**

> Yes. GNoME performs iterative active-learning discovery with DFT feedback, and A-Lab closes the loop by proposing new synthesis recipes when yields are poor and feeding characterization results back into decision making.


**Stopping And Guardrails:**

> The A-Lab operates on air-stable targets, within a bounded robotic workflow, and through a lab API. Manual post-hoc confirmation of diffraction results and constrained materials domains limit risk. GNoME predictions remain bounded by stability heuristics and database snapshots.


**Known Failure Modes:**

> Reported failure modes include slow reaction kinetics, precursor volatility, amorphization, computational inaccuracy, false positives near convex-hull boundaries, and materials that appear stable computationally but are not synthesizable in practice.


#### Evaluation

**Benchmarks Used:**

- 36 of 57 target compounds synthesized over 17 days in A-Lab
- 381,000 new stable convex-hull entries from GNoME
- ICSD and Materials Project snapshot matching
- r2SCAN validation for discovered materials
- later crystal-stability evaluation frameworks


**Metrics:**

- A-Lab: 36 of 57 targets synthesized over 17 days with 63% target success.
- A-Lab: 353 experiments performed.
- GNoME: 2.2 million structures below the previous convex hull.
- GNoME: 381,000 newly discovered stable convex-hull entries.
- GNoME: more than 45,500 novel prototypes.
- GNoME: 84% of discovered binary and ternary materials remain stable under r2SCAN validation.
- GNoME: 86.8% of tested quaternaries remain stable on the r2SCAN convex hull.


**Baselines:**

- Materials Project and OQMD stable-material catalogs
- literature-inspired synthesis recipes without active-learning follow-up
- previous human and heuristic materials discovery workflows


**Validation Strength:**

> Peer-reviewed primary papers, open dataset and code, real robotic lab execution, manual post-hoc confirmation of synthesis outcomes, and later third-party evaluation work make this one of the stronger validation profiles in AI-for-science.


**Evaluation Limitations:**

> Predicted stability is not identical to synthesizability, convex-hull status can change as new materials are discovered, lab success depends on precursor and kinetics constraints, and later public scrutiny led to correction and reproduction questions that temper headline claims.


#### Links And Provenance

**Paper Url:** https://www.nature.com/articles/s41586-023-06734-w


**Code Url:** https://github.com/google-deepmind/materials_discovery


**Dataset Url:** https://github.com/google-deepmind/materials_discovery


**Product Url:** https://deepmind.google/blog/millions-of-new-materials-discovered-with-deep-learning/


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:**

- Materials Project
- OQMD
- text-mined synthesis-planning models
- ARROWS active-learning synthesis optimization
- prior high-throughput ab initio materials screening


**Successors:**

- google-deepmind/materials_discovery public release and August 2024 dataset expansion
- later external evaluations such as crystal-stability benchmark frameworks
- independent experimental follow-up on specific GNoME-discovered materials


**Components:**

- GNoME message-passing models
- A-Lab robotic synthesis platform
- Materials Project
- OQMD
- ARROWS
- SynthesisSimilarity
- s4 temperature model
- XRD-AutoAnalyzer
- robotic arms
- powder preparation station
- furnace station
- XRD characterization station
- laboratory API


**Evaluated By:**

- manual post-hoc diffraction refinement
- ICSD experimental matches
- Materials Project snapshot matching
- r2SCAN stability checks
- later external benchmark-style evaluation papers


**Evaluates:**

> Not a benchmark; it evaluates materials candidates and synthesis routes rather than ranking general AI systems.


**Competes With Or Complements:** SciAgents, Google Co-Scientist, other autonomous laboratory systems and materials discovery stacks


#### Timeline

**Version History:**

> The main public evolution is from the 2023 papers to the public materials_discovery repository and the August 2024 dataset expansion. A-Lab itself appears as a research platform rather than a semantically versioned product.


**Adoption Signals:**

> The lineage has high visibility through Nature publications, an official DeepMind blog, a public GitHub repository, and independent experimental matches for 736 structures reported by DeepMind. Downstream studies are already using the GNoME dataset.


**Supersession Notes:**

> Not superseded. Later evaluation papers and corrections refine how the original claims should be interpreted, especially around stability metrics and autonomous synthesis reporting.


#### Applications

**Real World Applications:**

- inorganic crystal discovery
- battery and ion-conductor screening
- layered-material discovery
- robotic solid-state synthesis
- autonomous materials validation pipelines


**Users:**

- materials scientists
- autonomous-lab researchers
- computational chemistry and physics teams
- industrial R&D groups interested in inorganic materials discovery


**Deployment Constraints:**

> Requires major computational infrastructure, high-quality materials databases, specialized ML tooling, robotic lab hardware, XRD characterization, controlled precursor handling, and strong safety and maintenance processes.


#### Governance And Risk

**Scientific Integrity Risks:**

> The biggest risks are overstating computational stability as practical discovery, reporting optimistic autonomous-synthesis counts without enough nuance, and underestimating how much manual validation is still required.


**Security And Safety Risks:**

> Robotic synthesis introduces equipment, heat, chemical, and lab-protocol risks. At the computational layer, false positives can waste scarce lab time and materials.


**Mitigations:**

> Air-stable target selection, bounded robotic workflows, API-mediated control, manual post-hoc verification, multiple validation layers for predicted materials, and later external evaluation all help contain risk.


**Policy Relevance:**

> This lineage is a concrete reference point for governance of autonomous laboratories, claims standards for AI-assisted discovery, and the distinction between predictive novelty, experimental realization, and reproducible scientific validation.


#### Uncertain Fields

- cost_and_runtime
- leaderboard_url
- milestones

### Agent Laboratory

#### Identity

**Id:** agent_laboratory


**Name:** Agent Laboratory


**Aliases:** Agent Laboratory: Using LLM Agents as Research Assistants


**Organization:** Academic open-source project


**First Public Release:** 2025-01-08


**Current Status:** Active open-source research workflow


#### Taxonomy

**Category:** research_workflow_agent


**Type:** paper, open_source_system


**Domains:** machine_learning, general_computational_research


**Positioning:** Autonomous research assistant


**Boundary Notes:**

> Included because it covers literature review, experimentation, and report writing as a unified research workflow. It is narrower than wet-lab discovery platforms and broader than single-stage literature tools.


#### Capabilities

**Lifecycle Coverage:** literature_review, experiment_planning, code_execution, paper_drafting


**Tool Access:** arXiv, Hugging Face, Python, LaTeX, LLM APIs


**Execution Environment:**

> Local or user-managed compute environment with Python 3.12, optional pdflatex, and user-supplied model/API access


**Artifact Outputs:** research report, code repository, experiment plans, notes, generated machine learning experiments


**Human Roles:**

> A human provides the research idea, task notes, available compute details, and optional feedback at each phase. The system is framed as an assistant rather than a replacement for researcher creativity.


#### Autonomy

**Autonomy Level:** L3


**Autonomy Rationale:**

> Agent Laboratory autonomously executes a multi-stage workflow across literature review, experimentation, and report writing, but still depends on human goal setting, optional stage feedback, and user-managed execution resources.


**Iteration Loop:**

> Yes. The workflow progresses through staged agent collaboration, can resume from checkpoints, and supports human feedback between stages.


**Stopping And Guardrails:**

> Guardrails include human-provided task notes, optional copilot mode, checkpoint saves, optional disabling of LaTeX compilation, and dependence on user-managed compute and API configuration.


**Known Failure Modes:**

- hallucinated literature synthesis
- invalid or weak experiment design
- code generation errors
- model-quality dependence
- overclaiming novelty without strong human review


#### Evaluation

**Metrics:**

- human evaluation of final paper quality
- best outcomes reported with o1-preview
- state-of-the-art performance against existing methods in generated machine learning code
- 84% lower research expense than previous autonomous research methods


**Validation Strength:** Benchmarked and human-reviewed


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2501.04227


**Code Url:** https://github.com/SamuelSchmidgall/AgentLaboratory


**Product Url:** https://agentlaboratory.github.io/


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** AgentRxiv


**Components:** Literature Review phase, Experimentation phase, Report Writing phase, specialized LLM-driven agents


**Evaluated By:** human researcher survey, human feedback during staged execution, task-specific machine learning outcome comparisons


**Evaluates:** Not a benchmark; it does not primarily evaluate other systems.


#### Timeline

**Milestones:** 2025-01-08: arXiv v1 submitted, 2025-03-24: README announced AgentRxiv integration, 2025-06-17: arXiv v2 posted


**Version History:**

- arXiv v1 on 2025-01-08
- arXiv v2 on 2025-06-17
- README lists support for OpenAI and DeepSeek model backends as of verification date


**Adoption Signals:** GitHub repository showed 5.6k stars and 783 forks on 2026-05-28, Public multilingual README and project website


**Supersession Notes:**

> Not superseded in the reviewed sources. AgentRxiv appears to extend collaborative accumulation rather than replace Agent Laboratory.


#### Applications

**Real World Applications:**

- machine learning literature review
- experiment planning
- automated code-based empirical research
- drafting research reports


**Users:** academic researchers, machine learning engineers, students, independent research practitioners


**Deployment Constraints:**

- Python 3.12 recommended
- LLM API or supported model backend access
- optional pdflatex installation for compilation
- user-managed compute, datasets, and hardware configuration


#### Governance And Risk

**Scientific Integrity Risks:**

- fabricated or weak citations
- invalid benchmark conclusions
- false novelty claims
- overreliance on generated reports without expert review


**Security And Safety Risks:**

- unsafe generated code execution in user environments
- uncontrolled API spending
- external-tool misuse if agents are given broad access


**Mitigations:**

- human goal setting and optional feedback at each stage
- user control over compute and configuration
- checkpointing for auditability and recovery
- assistant framing rather than fully unsupervised deployment


**Policy Relevance:**

> Relevant to responsible AI in science because it automates manuscript and experiment generation, raising questions about provenance, reproducibility, authorship, and review burden.


#### Uncertain Fields

- baselines
- benchmarks_used
- competes_with_or_complements
- cost_and_runtime
- dataset_url
- evaluation_limitations
- leaderboard_url
- predecessors

### AI Co-Scientist / Co-Scientist

#### Identity

**Id:** google_ai_co_scientist


**Name:** AI Co-Scientist / Co-Scientist


**Aliases:** AI co-scientist, Co-Scientist, Towards an AI co-scientist


**Organization:** Google Research, Google DeepMind


**First Public Release:** 2025-02-19


**Current Status:** Research system with Trusted Tester early access; not publicly self-serve as of 2026-05-28.


#### Taxonomy

**Category:** hypothesis_and_research_planning_system


**Type:** paper, product


**Domains:** biomedicine, biology, general_science


**Positioning:** Collaborative co-scientist for scientist-in-the-loop hypothesis generation and research planning.


**Boundary Notes:**

> Included because it produces novel, literature-grounded hypotheses and research plans with real-world validation, but it is not framed as a fully autonomous end-to-end lab or publication agent. Its scope is collaborative discovery support rather than independent scientific authorship.


#### Capabilities

**Lifecycle Coverage:** literature_reasoning, hypothesis_generation, research_plan_generation, self_evaluation, scientist_collaboration


**Tool Access:**

- Web search
- Literature reasoning over papers and large context inputs
- Specialized AI models through APIs
- Persistent context memory
- Natural-language scientist interface


**Execution Environment:**

> Product-hosted multi-agent Gemini 2.0 environment with asynchronous task execution, persistent memory, and a scientist-facing natural-language interface.


**Artifact Outputs:** Novel hypotheses, Research overviews, Experimental protocols, Cited literature summaries, Ranked and refined proposals


**Human Roles:**

- Scientists specify goals, constraints, and preferences
- Scientists provide natural-language feedback and seed ideas
- Domain experts evaluate output quality
- Human research teams perform the downstream wet-lab or in vitro validation


#### Autonomy

**Autonomy Level:** L3


**Autonomy Rationale:**

> It autonomously searches, reasons, debates, ranks, and refines hypotheses and research plans, but it is explicitly framed as a collaborative scientist-in-the-loop system rather than a fully autonomous research executor.


**Iteration Loop:**

> Specialized agents continuously generate, critique, rank, evolve, and meta-review hypotheses within an asynchronous tournament loop backed by persistent context memory.


**Stopping And Guardrails:**

- Scientists remain in the loop and can steer goals or constraints in natural language
- The system is explicitly not meant to automate the full scientific process
- Safety is one of the default evaluation criteria for generated outputs
- Access was gated through a Trusted Tester Program at launch


**Known Failure Modes:**

- Auto-Elo scores are not independent ground truth
- Incorrect or weakly grounded biological hypotheses still require expert validation
- Novelty and impact judgments may be biased by the available literature or model limitations
- General-purpose claims are stronger than the currently disclosed validation breadth


#### Evaluation

**Benchmarks Used:**

- 15 expert-curated open research goals with best-guess solutions
- GPQA diamond concordance analysis for Elo auto-ratings
- Expert assessment on a subset of 11 research goals
- > Real-world validation in acute myeloid leukemia drug repurposing, liver fibrosis target discovery, and antimicrobial-resistance mechanism explanation


**Metrics:**

- Elo auto-ratings from tournament comparisons
- Higher Elo correlated with higher GPQA diamond accuracy
- > Experts preferred the system's outputs for novelty and impact over relevant baselines on a smaller subset
- In vitro validation for AML repurposing candidates at clinically relevant concentrations
- Human hepatic organoid validation for anti-fibrotic target suggestions


**Baselines:**

- Reference Gemini 2.0 responses
- Other state-of-the-art agentic and reasoning models
- Unassisted human experts on expert-curated goals


**Validation Strength:** Peer-reviewed and real-world validated.


**Evaluation Limitations:**

- Most disclosed validation is in biomedicine even though the framing is general-purpose
- Elo is an auto-evaluation rather than independent ground truth
- The expert-preference subset was small
- Some validation details are deferred to co-timed or upcoming reports


#### Links And Provenance

**Paper Url:** https://www.nature.com/articles/s41586-026-10644-y


**Code Url:** None publicly released as of 2026-05-28.


**Dataset Url:** None.


**Product Url:** https://blog.google/feed/google-research-ai-co-scientist/


**Leaderboard Url:** None.


**Source Quality:** Primary journal article and official Google launch and research posts.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- Supervisor agent
- Generation agent
- Reflection agent
- Ranking agent
- Evolution agent
- Proximity agent
- Meta-review agent
- Context memory
- Gemini 2.0


**Evaluated By:** Nature peer review, Expert-curated goal evaluations, Expert preference studies, Wet-lab and in vitro validations


**Competes With Or Complements:** The AI Scientist family, Deep research tools, Domain-specific biomedical discovery systems


#### Timeline

**Milestones:**

- 2025-02-19: Google announced AI co-scientist and Trusted Tester access
- 2025-02: 'Towards an AI co-scientist' preprint circulated publicly
- 2026-05-19: Nature published 'Accelerating scientific discovery with Co-Scientist'


**Version History:** 2025-02 launch on top of Gemini 2.0, 2026-05 Nature publication with broader validation evidence


**Adoption Signals:**

- Trusted Tester early-access program was announced at launch
- When checked on 2026-05-28, the Nature page showed about 125k accesses and 345 Altmetric
- The system received prominent Google Research and Google blog coverage


**Supersession Notes:** No public successor was verified as of 2026-05-28.


#### Applications

**Real World Applications:**

- Drug repurposing for acute myeloid leukemia
- Novel treatment-target discovery for liver fibrosis
- Mechanistic hypothesis generation for antimicrobial resistance
- Collaborative scientific research planning


**Users:**

- Biomedical scientists
- Research teams
- Translational medicine groups
- General scientists needing collaborative hypothesis support


**Deployment Constraints:**

- Trusted Tester or internal access rather than public self-serve availability
- Scientist input and validation remain necessary
- Wet-lab or clinical validation capacity is needed for high-stakes claims
- Frontier-model infrastructure and literature access are required


#### Governance And Risk

**Scientific Integrity Risks:**

- Weakly grounded or fabricated hypotheses if expert review is skipped
- Overclaiming novelty relative to the underlying literature
- Authorship and credit ambiguity around AI-generated proposals
- Misinterpretation of preliminary model suggestions as validated science


**Mitigations:**

- Scientist-in-the-loop collaboration
- Safety as a default evaluation criterion
- Natural-language constraints and feedback from experts
- Wet-lab or in vitro validation before strong claims
- Access gating through a Trusted Tester Program


**Policy Relevance:**

> Highly relevant to responsible release of AI discovery systems, cyberbiosecurity, human oversight in scientific automation, and governance of AI-generated hypotheses in biomedicine.


#### Uncertain Fields

- cost_and_runtime
- security_and_safety_risks

### AInsteinBench

#### Identity

**Id:** ainsteinbench


**Name:** AInsteinBench


**Aliases:** AInsteinBench: Benchmarking Coding Agents on Scientific Repositories


**Organization:** ByteDance Seed and Princeton University


**First Public Release:** 2025-12-24


**Current Status:**

> Active public benchmark with an arXiv paper, a public GitHub project page, and a public Hugging Face dataset.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset, codebase


**Domains:**

- scientific computing
- quantum chemistry
- quantum computing
- molecular dynamics
- numerical relativity
- fluid dynamics
- cheminformatics


**Positioning:**

> Benchmark for scientific computing code agents operating on real scientific repositories and executable development tasks.


**Boundary Notes:**

> Included because it evaluates repository-scale scientific software maintenance, bug fixing, and feature implementation in executable environments rather than only closed-form science QA or generic programming tasks. It sits at the intersection of scientific reasoning and real pull-request-style coding work.


#### Capabilities

**Lifecycle Coverage:**

- repository navigation
- issue understanding
- feature implementation
- bug fixing
- code writing
- test execution
- evaluation


**Tool Access:**

- containerized shell access
- file inspection
- code editing
- package installation
- repository test execution
- Docker images


**Execution Environment:**

> Each benchmark instance runs in an isolated Docker container with the appropriate repository snapshot, dependencies, and a restricted command-line interface. The public repository provides a unified evaluator and scripts for preparing benchmark images and running tests.


**Artifact Outputs:**

- patches
- implemented source files
- evaluation_results.json outputs
- question files
- difficulty annotations
- pass/fail benchmark scores


**Human Roles:**

> Benchmark creators select repositories, curate tasks, reconstruct environments, and recruit domain experts to verify scientific meaning, test quality, and difficulty. Users run agents against the benchmark and interpret the resulting scores and trajectories.


#### Autonomy

**Autonomy Level:** L2-L3


**Autonomy Rationale:**

> AInsteinBench targets agents that can independently inspect repositories, edit code, run tests, install dependencies, and iterate on failures inside a sandboxed environment, but still operate within benchmark-provided infrastructure, task definitions, and evaluation harnesses.


**Iteration Loop:**

> The evaluated CodeAct-based agent follows a plan-act loop: it searches the codebase, inspects failures, proposes edits, reruns reproduction scripts and tests, and iteratively refines patches. The paper reports that virtually all problems take at least 20 iterations and that many successful trajectories accumulate within 20-60 steps.


**Stopping And Guardrails:**

> Guardrails include isolated Docker containers, fixed repository snapshots, curated fail-to-pass instances, maintainer-linked pull requests, expert review, and test-driven acceptance. Evaluation stops when the agent reaches a terminal success or failure outcome under the benchmark harness.


**Known Failure Modes:**

- scientifically invalid but locally plausible fixes
- mathematical precision errors
- violated physical or conservation invariants
- cross-file reasoning failures
- spatial reasoning failures on cheminformatics tasks
- false positives from under-covered tests
- false negatives from over-prescriptive tests


#### Evaluation

**Benchmarks Used:**

> AInsteinBench itself is the primary benchmark. Its construction and positioning are explicitly compared against SWE-Bench, SWE-Bench Verified, SWE-Gym, and Multi-SWE-Bench.


**Metrics:**

- problem resolution rate
- difficulty-stratified pass rate
- domain-specific pass rate
- issue-localization score
- efficiency measured by iteration count


**Baselines:**

- CodeAct agent with Claude 4.5 Opus
- CodeAct agent with Gemini 3 Pro
- CodeAct agent with DeepSeek V3.2
- CodeAct agent with Doubao Seed 1.8
- CodeAct agent with GPT-5-high
- CodeAct agent with Claude 4.5 Sonnet
- CodeAct agent with GPT-5.1
- CodeAct agent with Kimi K2
- CodeAct agent with GLM 4.6
- CodeAct agent with Gemini 2.5 Pro
- CodeAct agent with GPT-4o
- CodeAct agent with Grok-4


**Validation Strength:**

> Benchmarked in executable environments with test-driven verification, multi-stage filtering, reconstructed historical environments, and domain-expert human review. The benchmark is publicly documented in an arXiv paper and released with code and dataset artifacts.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2512.21373


**Code Url:** https://github.com/ByteDance-Seed/AInsteinBench


**Dataset Url:** https://huggingface.co/datasets/ByteDance-Seed/AInsteinBench


**Product Url:** https://github.com/ByteDance-Seed/AInsteinBench


**Source Quality:**

> Primary sources: official arXiv paper, official GitHub repository, and official Hugging Face dataset page.


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** SWE-Bench, SWE-Bench Verified, SWE-Gym, Multi-SWE-Bench


**Components:**

- 244 maintainer-validated benchmark problems in the paper evaluation
- repo-crawled questions
- synthesized Einstein Toolkit questions
- isolated Docker execution environments
- fail-to-pass filtering
- expert verification pipeline
- difficulty annotations
- CodeAct-based evaluation harness
- Hugging Face dataset subsets for msb_type, difficulty_tag, and et_type


**Evaluates:**

- scientific_repository_maintenance
- scientific_computing_code_agents
- real_PR_tasks
- feature implementation
- bug fixing
- issue localization


**Competes With Or Complements:**

- SciCode
- PaperBench
- SWE-Bench
- SWE-Bench Verified
- SWE-Gym
- Multi-SWE-Bench


#### Timeline

**Milestones:**

- 2025-12-24: arXiv v1 submitted.
- 2025-12-29: Paper dated December 29, 2025 and linked to the public GitHub project page.
- > 2026-05-28: Public GitHub repository available with evaluator, scripts, tests, and Docker-based setup instructions.
- > 2026-05-28: Public Hugging Face dataset available under CC0-1.0 with msb_type, difficulty_tag, and et_type subsets.


**Version History:**

- arXiv v1 released on 2025-12-24
- > public GitHub repository exposes unified question formats for Einstein Toolkit and Multi-SWE-Bench-style tasks
- public dataset page exposes benchmark artifacts through Hugging Face datasets


**Adoption Signals:**

- Public arXiv paper
- Public GitHub repository
- Public Hugging Face dataset
- GitHub repository showed 8 stars on 2026-05-28
- Hugging Face dataset page showed 4 likes on 2026-05-28


**Supersession Notes:** No supersession was identified in the consulted primary sources.


#### Applications

**Real World Applications:**

- benchmarking autonomous scientific coding agents
- measuring ability to maintain scientific repositories
- evaluating real pull-request-style issue resolution in scientific software
- studying feature implementation and bug fixing in computational research codebases


**Users:**

- AI agent researchers
- scientific software maintainers
- benchmark designers
- LLM evaluation teams
- computational science researchers


**Deployment Constraints:**

> Full evaluation requires Python 3.8+, Docker, prebuilt benchmark images, and significant disk space. The repository notes that pulling all images may take minutes or hours and requires more than 50GB of free storage. Some question types additionally require Multi-SWE-Bench installation or Einstein Toolkit setup.


**Cost And Runtime:**

> Runtime depends on image downloads, repository setup, and agent iteration count. The repository warns that pulling all images can take minutes or hours and needs more than 50GB free storage, while the paper reports that virtually all tasks take at least 20 iterations and that many successful trajectories accumulate within 20-60 steps.


#### Governance And Risk

**Scientific Integrity Risks:**

- benchmark overfitting to a fixed set of scientific repositories
- false positives from under-covered tests
- false negatives from over-prescriptive tests
- mistaking test success for full scientific validity
- limited repository coverage relative to the broader scientific software ecosystem


**Security And Safety Risks:**

- agents execute code and install packages inside Docker containers
- historical repository snapshots and Docker images expand the attack surface if isolation is weak
- large scientific dependencies and build steps increase operational risk during evaluation


**Mitigations:**

- isolated Docker containers
- fixed repository snapshots and reconstructed dependencies
- fail-to-pass verification
- maintainer-authored pull-request linkage for repo-crawled tasks
- domain-expert human verification
- test revisions to reduce false positives and false negatives


**Policy Relevance:**

> Relevant to governance of increasingly autonomous coding agents for research software, especially around reproducibility, benchmark validity, and safe deployment of agents that can modify scientific codebases.


#### Uncertain Fields

- evaluated_by
- evaluation_limitations
- leaderboard_url
- successors

### AIRS-Bench

#### Identity

**Id:** airs_bench


**Name:** AIRS-Bench


**Aliases:** AIRS-Bench, AI Research Science Benchmark, AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents


**Organization:** Meta FAIR and collaborators


**First Public Release:** 2026-02-09


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark_suite


**Domains:**

- machine learning
- natural language processing
- mathematics
- coding
- biochemical modeling
- time series prediction


**Positioning:** Benchmark suite for evaluating AI agents across the full machine-learning research lifecycle.


**Boundary Notes:**

> Included because it directly targets autonomous AI research-science agents and asks agents to improve on recent ML research tasks without baseline code.


#### Capabilities

**Lifecycle Coverage:**

- idea generation
- problem understanding
- resource discovery
- implementation
- debugging
- experiment execution
- experiment analysis
- iterative refinement
- final result comparison


**Execution Environment:**

> Benchmark suite of 20 machine-learning research tasks sourced from recent papers; agents are evaluated without being given baseline code.


**Artifact Outputs:** research code, experiment logs, model outputs, analysis artifacts, final task scores


**Human Roles:**

- Humans curate recent research tasks.
- Humans define expected evaluation protocols.
- Human SOTA results act as reference targets.
- Humans interpret agent failures and benchmark limitations.


#### Autonomy

**Autonomy Level:** L3-L4


**Autonomy Rationale:**

> AIRS-Bench is designed for agents that must conduct long-horizon ML research workflows from underspecified goals through implementation and iteration. It remains a benchmark with human-curated tasks, so it evaluates bounded autonomy rather than open-ended science.


**Iteration Loop:**

> Yes. The benchmark emphasizes iterative refinement, debugging, experiment analysis, and improving results over multiple attempts.


**Stopping And Guardrails:**

- Tasks are bounded to benchmark-provided research problems.
- No baseline code is supplied, increasing realism but keeping evaluation constrained.
- Agents are compared against task-specific reference outcomes.


**Known Failure Modes:**

- Failure to understand vague research requirements.
- Selecting weak experimental strategies.
- Implementation bugs in ML code.
- Compute budget exhaustion.
- Poor analysis of failed or noisy experiments.
- Overfitting to benchmark tasks once public.


#### Evaluation

**Benchmarks Used:** AIRS-Bench suite of 20 research tasks


**Validation Strength:** Primary arXiv paper; independent reproduction and public leaderboard were not verified.


**Evaluation Limitations:**

- Only 20 tasks, so coverage is deep but not exhaustive.
- High compute requirements may limit reproducibility.
- Task-specific grading can be hard to normalize across research domains.
- Public release may introduce contamination over time.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2602.06855


**Source Quality:** Primary arXiv paper plus Hugging Face paper metadata and secondary summaries.


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** MLAgentBench, MLE-bench, PaperBench, The AI Scientist-v2


**Components:**

- 20 recent ML-paper-derived tasks
- no-baseline-code task setting
- research lifecycle evaluation protocol
- task-specific scoring


**Evaluates:**

- full ML research lifecycle
- idea generation
- experiment analysis
- iterative refinement
- autonomous implementation
- debugging


**Competes With Or Complements:** MLAgentBench, MLE-bench, PaperBench, AI Scientist-v2


#### Timeline

**Milestones:**

- 2026-02-09: arXiv preprint posted.
- 2026: Hugging Face paper page summarizes the 20-task suite.
- 2026-05-28: paper source verified.


**Supersession Notes:** No official successor or replacement was identified.


#### Applications

**Real World Applications:**

- Evaluating AI agents for ML research automation.
- Stress-testing research workflows beyond coding-only tasks.
- Comparing agent scaffolds on long-horizon research problems.


**Users:** Frontier AI labs, agent benchmark researchers, ML research automation teams, safety and evaluation teams


#### Governance And Risk

**Scientific Integrity Risks:**

- Conflating benchmark performance with real scientific discovery.
- Benchmark contamination once tasks are public.
- Overstating agent contributions relative to human task curation.


**Security And Safety Risks:**

- Generated code execution in ML environments.
- Potential misuse of increasingly capable autonomous research workflows.
- Resource exhaustion from unbounded experiment loops.


**Mitigations:**

- Use sandboxed compute environments.
- Track exact task versions and model/tool access.
- Separate benchmark success from publication-quality scientific validation.
- Use budget limits and execution logs.


**Policy Relevance:**

> Relevant to frontier-agent evaluations, autonomous R&D governance, benchmark contamination, and claims about AI systems performing research work.


#### Uncertain Fields

- adoption_signals
- baselines
- code_url
- cost_and_runtime
- current_status
- dataset_url
- deployment_constraints
- evaluated_by
- leaderboard_url
- metrics
- product_url
- successors
- tool_access
- version_history

### AlphaEvolve

#### Identity

**Id:** alphaevolve


**Name:** AlphaEvolve


**Aliases:** AlphaEvolve: A coding agent for scientific and algorithmic discovery


**Organization:** Google DeepMind / Google Cloud


**First Public Release:** 2025-05-14


**Current Status:**

> Research preview with an official white paper, launch blog, and companion problem repository; early-access interest was announced, but the core runtime is not publicly released.


#### Taxonomy

**Category:** domain_scientific_discovery_agent


**Type:** paper, product, infrastructure


**Domains:** algorithms, mathematics, systems_optimization, AI_infrastructure


**Positioning:** A Gemini-powered evolutionary coding agent for algorithm discovery and system optimization.


**Boundary Notes:**

> Included because it autonomously searches over code variants to discover new algorithms and production heuristics, not merely act as an IDE assistant. Excludes generic coding copilots without automated evaluation and evolutionary search loops.


#### Capabilities

**Lifecycle Coverage:** code_generation, evolutionary_search, program_evaluation, algorithm_optimization


**Tool Access:**

- Gemini Flash and Gemini Pro models
- Prompt sampler
- Program database
- Automated evaluators
- Code execution
- Distributed controller loop
- User-provided evaluation code and initial programs
- Companion Colab notebooks and problem repository


**Execution Environment:**

> A product-hosted and research-hosted distributed evaluation loop that queries Gemini models, runs generated code, scores programs automatically, and stores promising candidates in an evolutionary database.


**Artifact Outputs:**

- Improved code diffs
- Optimized heuristics and kernels
- Mathematical constructions
- Search algorithms
- Hardware design rewrites
- Problem-specific notebooks and results


**Human Roles:**

- Humans define the task, evaluation criteria, initial solution, and optional background knowledge.
- Humans choose which code blocks are evolvable and review high-value outputs before deployment.
- Engineers validate or integrate production-facing improvements into Google systems.


#### Autonomy

**Autonomy Level:** L3


**Autonomy Rationale:**

> Once the task, evaluation function, and initial program are supplied, AlphaEvolve runs an autonomous improvement loop over code and scores candidates without step-by-step human steering. It stays below L4 and L5 because it is limited to machine-gradeable tasks, depends on human-specified evaluators and seed code, and is not a general end-to-end scientist across physical experimentation.


**Iteration Loop:**

> Yes. AlphaEvolve repeatedly samples prompts from past programs, asks an LLM ensemble for diffs, executes evaluators, and feeds scored programs back into the database.


**Stopping And Guardrails:**

> The system is constrained by user-defined evaluation functions, EVOLVE-BLOCK markers, automated verification, and the requirement that tasks be machine-gradeable. Hardware and infrastructure proposals pass robust verification before integration, and public access was limited to a planned early-access program.


**Known Failure Modes:**

- Over-optimizing to imperfect evaluator metrics
- Missing good solutions when the search space or prompt distribution is poorly chosen
- Generating invalid code diffs that fail evaluation
- False novelty claims if verification is incomplete
- Limited applicability to tasks that cannot be automatically scored


#### Evaluation

**Benchmarks Used:**

- More than 50 open problems in mathematical analysis, geometry, combinatorics, and number theory
- Matrix multiplication algorithm discovery tasks
- Google Borg data-center scheduling
- TPU arithmetic-circuit optimization
- Gemini training kernel optimization
- FlashAttention kernel optimization


**Metrics:**

- Automated scalar evaluation metrics supplied by the user
- Recovered compute percentage in data-center scheduling
- Kernel speedups and training-time reduction
- Number of scalar multiplications for matrix multiplication algorithms
- Rate of rediscovering state-of-the-art solutions and rate of improving them


**Baselines:**

- Human-written initial programs
- Prior state-of-the-art solutions on each problem
- FunSearch
- AlphaTensor
- Existing production heuristics and kernels


**Validation Strength:** Benchmarked plus real-world internal production validation; not peer-reviewed as of 2026-05-28.


**Evaluation Limitations:**

> AlphaEvolve only applies where progress can be reduced to automatic evaluation metrics. The strongest production claims depend on internal Google environments, and the public companion repository does not release the full agent runtime.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2506.13131


**Code Url:** https://github.com/google-deepmind/alphaevolve_repository_of_problems


**Dataset Url:** https://google-deepmind.github.io/alphaevolve_repository_of_problems/


**Product Url:**

> https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/


**Leaderboard Url:** Not applicable; no official public leaderboard.


**Source Quality:**

> Primary sources: official Google DeepMind blog, AlphaEvolve white paper, and official Google DeepMind companion repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:**

- > The public companion repository for mathematical problems extends the AlphaEvolve release footprint but is not a successor system.
- > OpenEvolve and similar open-source implementations are community follow-ons rather than official successors.


**Components:**

- Prompt sampler
- LLM ensemble
- Program database
- Evaluators pool
- Distributed controller loop
- EVOLVE-BLOCK API
- Evaluation function interface


**Evaluated By:**

- Internal and white-paper evaluations across math, algorithms, and systems tasks
- Automatic evaluators on each problem
- Production verification on selected Google infrastructure improvements


**Evaluates:** Not a benchmark item; it evaluates and improves algorithms supplied as code under automated metrics.


**Competes With Or Complements:** FunSearch, AlphaTensor, AlphaDev, OpenEvolve implementations, Other coding agents with automated evaluation loops


#### Timeline

**Milestones:**

- 2025-05-14: DeepMind blog announcement
- 2025-06-16: AlphaEvolve white paper released on arXiv
- 2025: Official mathematical problem repository and Colab artifacts published
- 2025: Reported deployments across Google's compute ecosystem and math-discovery studies


**Version History:**

- Initial public release began with the May 14, 2025 product preview blog post.
- The white paper was posted to arXiv on 2025-06-16.
- > A later official companion repository released problem pages and notebooks but explicitly did not release the AlphaEvolve runtime.


**Adoption Signals:**

- > DeepMind reported that a scheduling heuristic found by AlphaEvolve had been in production for over a year and recovered about 0.7% of Google's worldwide compute resources on average.
- > DeepMind reported a 23% speedup for a Gemini training kernel, yielding roughly a 1% training-time reduction, and up to 32.5% speedup on a FlashAttention kernel.
- The official companion repository showed about 224 GitHub stars and 10 forks on 2026-05-28.


**Supersession Notes:** No official successor or general public product release was announced as of 2026-05-28.


#### Applications

**Real World Applications:**

- Algorithm discovery in mathematics
- Data-center scheduling optimization
- TPU arithmetic-circuit simplification
- Kernel optimization for AI training and inference
- Search over machine-gradeable scientific and engineering problems


**Users:**

- Algorithm researchers
- Systems and infrastructure engineers
- Chip designers
- Mathematicians
- Selected academic users in the announced early-access program


**Deployment Constraints:**

- Requires a machine-gradeable evaluation function
- Requires an initial program or code skeleton with evolvable blocks
- Can require substantial parallel compute and accelerators for slow evaluators
- > Core system availability was limited; the public repo releases problems and notebooks, not the full runtime


#### Governance And Risk

**Scientific Integrity Risks:**

- Overfitting to evaluation functions rather than true scientific value
- Mistaking evaluator-approved improvements for broader novelty or usefulness
- Limited external reproducibility when the strongest results depend on internal infrastructure
- Selection bias toward problems that are easy to auto-grade


**Security And Safety Risks:**

- > Autonomous code changes against critical infrastructure or kernels could cause regressions if verification is incomplete
- Hardware-design modifications need strong correctness checks before deployment
- Large-scale automated search can consume substantial compute and privileges


**Mitigations:**

- Automated evaluators verify correctness and quality before programs are retained
- Users explicitly define the evaluation code and evolvable regions
- Production-facing hardware proposals pass robust verification
- > Release scope was limited to a preview, white paper, and companion artifacts rather than unrestricted runtime access


**Policy Relevance:**

> Relevant to governance of powerful coding agents, verification standards for AI-generated infrastructure changes, and access controls for agentic systems that can optimize critical compute stacks.


#### Uncertain Fields

- cost_and_runtime
- predecessors

### Asta

#### Identity

**Id:** asta


**Name:** Asta


**Aliases:** Ai2 Asta, Asta ecosystem


**Organization:** Allen Institute for AI


**First Public Release:** 2025-08-26


**Current Status:**

> Active; public scientific AI ecosystem with open-source benchmark/resources and some preview or beta product features.


#### Taxonomy

**Category:** science_product_suite


**Type:** product, benchmark, codebase, infrastructure


**Domains:** general_science


**Positioning:**

> A science-focused agent ecosystem that combines research assistants, benchmark infrastructure, and developer resources.


**Boundary Notes:**

> Included because Ai2 presents Asta as an integrated ecosystem for scientific research assistance, benchmarking, and scientific tool infrastructure rather than a generic consumer web agent.


#### Capabilities

**Lifecycle Coverage:**

- paper_finding
- scholarly_qa
- literature_synthesis
- scientific_tool_use
- data_analysis
- benchmarking


**Tool Access:**

- Scientific paper search and retrieval
- Citation following
- Full-text literature access
- Structured dataset upload and analysis
- Model Context Protocol tools
- Benchmark evaluation tools
- Open-source agent baselines


**Execution Environment:**

> Hosted Asta web product for researchers, plus open-source benchmark and tool environments for local or private deployment.


**Artifact Outputs:**

- Ranked paper sets with rationales
- Citation-grounded literature summaries
- Research answers with source traces
- Reproducible data analyses
- Benchmark scores and leaderboards
- Agent baselines and evaluation logs


**Human Roles:**

- Researchers define the question or dataset and review cited outputs
- Users validate claims and decide whether to trust or reuse results
- Developers fork or modify open-source agents and benchmark setups
- Institutions must choose self-hosting for regulated datasets


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> Asta autonomously performs multi-step literature search, question answering, synthesis, and some data-analysis workflows, but humans still set goals, review evidence, and remain responsible for sensitive-data handling and downstream scientific decisions.


**Iteration Loop:**

> Yes. Asta reformulates queries, follows citations, clusters evidence, and in analysis mode explores datasets with follow-up analyses inside a bounded research workflow.


**Stopping And Guardrails:**

> Ai2 emphasizes user control, transparency, and clear boundaries. Hosted analysis warns against regulated data, deletes uploaded datasets after 7 days, keeps explorations active for 24 hours before read-only mode, and requires self-hosting for HIPAA, GDPR, or similar regulated data.


**Known Failure Modes:**

> Scientific-agent errors can include hallucinated synthesis, incomplete evidence retrieval, weak cross-domain performance, benchmark overfitting, and cost blowups or loops in general-agent baselines. Ai2 also notes that scientific AI remains far from solved on end-to-end tasks.


#### Evaluation

**Benchmarks Used:**

- AstaBench
- PaperFindingBench
- ScholarQA-CS2
- LitQA2-FullText-Search
- Data analysis benchmarks in AstaBench
- End-to-end discovery benchmarks in AstaBench


**Metrics:**

- Task accuracy
- Leaderboard rank
- Reasoning quality
- Runtime cost per problem
- Transparency of logs and tool usage
- Pareto frontier over accuracy and computational cost


**Baselines:**

- 57 evaluated agents across 22 agent classes in the AstaBench report
- ReAct agents with multiple frontier models
- Open-source baseline agents in agent-baselines
- Commercial literature tools such as Elicit and SciSpace Deep Review on literature tasks


**Validation Strength:**

> Benchmarked, open-source, and backed by an ICLR 2026 conference paper for AstaBench plus real-world product usage feedback.


**Evaluation Limitations:**

> AstaBench is evolving, some task instructions changed after release, and even strong agents still score modestly overall. Controlled tools improve comparability but may not capture every live-production workflow or every scientific domain equally well.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2510.21652


**Code Url:** https://github.com/allenai/agent-baselines


**Product Url:** https://allenai.org/asta


**Leaderboard Url:** https://allenai.org/asta/bench


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** Ai2 Paper Finder, Ai2 Scholar QA


**Components:**

- Asta agents
- AstaBench
- Asta resources
- Ai2 Paper Finder
- Ai2 Scholar QA
- Analyze data / DataVoyager
- Asta Scientific Corpus Tool
- agent-baselines


**Competes With Or Complements:** OpenAI Deep Research, Google AI co-scientist, FutureHouse platforms, Elicit, Perplexity


#### Timeline

**Milestones:**

- 2025-08-26: Ai2 publicly announced Asta, AstaBench, and Asta resources.
- 2025-08-26: Asta launch included paper finding, literature summarization, and beta data analysis.
- 2025-10-24: AstaBench technical report first submitted to arXiv.
- 2026-04-21: AstaBench arXiv paper updated to v2 and published as an ICLR 2026 conference paper.
- 2026-05: Asta Scientific Corpus Tool documentation and MCP endpoint were publicly available.


**Version History:**

- Initial Asta ecosystem release in August 2025.
- AstaBench received a 0.3.1 update that adjusted paper-search task instructions after launch.
- Asta continues to fold previously standalone tools into a unified product experience.


**Adoption Signals:**

- Ai2 runs a public Asta Preview program for researchers and research-adjacent professionals.
- Ai2 published user testimonials from organizations such as DeepFlux and NewLimit.
- AstaBench ships public leaderboards and open-source baseline agents for community reuse.


**Supersession Notes:**

> Not superseded. Asta is presented as an evolving ecosystem, with new features being folded into the platform over time.


#### Applications

**Real World Applications:**

- Finding relevant papers for hard scientific queries
- Answering scholarly questions from scientific documents
- Summarizing evidence across papers with citations
- Analyzing uploaded research datasets
- Benchmarking scientific AI agents under controlled conditions


**Users:**

- Academic researchers
- Industry scientists
- Research engineers
- AI agent developers
- Graduate students
- Research-adjacent analysts


**Deployment Constraints:**

- Hosted deployment should not be used for sensitive or regulated data
- Self-hosting is required for HIPAA, GDPR, or similarly regulated datasets
- Dataset uploads are retained for 7 days unless deleted sooner
- Explorations become read-only after 24 hours
- Some capabilities are beta or preview-only
- Developer workflows may require API keys such as an Asta tool key


#### Governance And Risk

**Scientific Integrity Risks:**

- Hallucinated or weakly supported literature synthesis
- False confidence in incomplete scientific coverage
- Benchmark overfitting or benchmark-specific optimization
- Misinterpretation of statistical analyses
- Over-trust in agent outputs without source checking


**Security And Safety Risks:**

- Exposure of sensitive research data if used in the hosted environment
- Improper use with regulated datasets
- Unsafe downstream decisions based on incorrect analyses
- Potential leakage or misuse of API-backed scientific tools


**Mitigations:**

- Citation-grounded and traceable outputs
- Open-source benchmark and baseline agents for inspection
- Controlled, reproducible evaluation tools
- Self-hosting option for regulated data
- Automatic file retention limits and deletion controls
- User-control framing instead of full researcher replacement


**Policy Relevance:**

> Relevant to scientific integrity, reproducibility, benchmark governance, data-governance choices for research organizations, and the broader policy question of how to evaluate science-focused AI agents transparently.


#### Uncertain Fields

- cost_and_runtime

### AstaBench

#### Identity

**Id:** astabench


**Name:** AstaBench


**Aliases:** Asta Bench


**Organization:** Allen Institute for AI (Ai2)


**First Public Release:** 2025-08


**Current Status:** Active benchmark suite with open-source code, a gated dataset, and a public leaderboard.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark_suite, leaderboard, codebase


**Domains:**

- scientific research
- literature understanding
- code execution
- data analysis
- scientific discovery
- multi-domain science


**Positioning:** Scientific research benchmark suite and leaderboard for AI agents.


**Boundary Notes:**

> Included because it is a benchmark suite explicitly designed to measure agentic scientific research ability across literature, coding, data analysis, and end-to-end discovery, rather than a general chatbot benchmark.


#### Capabilities

**Lifecycle Coverage:**

- literature search
- scientific question answering
- code writing
- code execution
- data analysis
- structured summarization
- end-to-end discovery


**Tool Access:**

- date-restricted scientific literature search tools
- Asta Scientific Corpus tool
- sandboxed code execution
- stateful python notebook tools
- InspectAI-compatible tool interfaces
- MCP-accessible research tools


**Execution Environment:**

> InspectAI-based local or Dockerized benchmark runner with standardized tools, gated dataset access through Hugging Face, and sandboxed environments for coding and data tasks.


**Artifact Outputs:**

- benchmark scores
- cost reports
- leaderboard submissions
- execution logs
- traceable evaluation artifacts
- agent compatibility metadata


**Human Roles:**

- Researchers define tasks and rubrics, maintain the benchmark, and review methodology.
- Agent developers run evaluations and submit results.
- Humans still interpret leaderboard tradeoffs and scientific usefulness.


#### Autonomy

**Autonomy Level:** L1-L3


**Autonomy Rationale:**

> AstaBench evaluates agents that use tools and multi-step workflows for bounded scientific tasks, from focused assistants up to partially autonomous end-to-end research agents, rather than fully self-directing L4-L5 systems.


**Iteration Loop:**

> Yes. Agents can be run repeatedly across validation and test splits, with leaderboard submissions and cost-scored re-evaluation loops, but the benchmark itself is an evaluation loop rather than a self-improving agent.


**Stopping And Guardrails:**

- Standardized tool interfaces and date-restricted literature access improve reproducibility.
- Cost logging and time-invariant pricing reduce confounding from repeated-agent strategies.
- Sandboxed execution constrains code and notebook tasks.
- Leaderboard metadata records openness, tool usage, logs, and reproducibility warnings.


**Known Failure Modes:**

- Agents may hallucinate citations or analyses.
- Agents may exploit tool differences rather than core reasoning gains.
- LLM-as-a-judge grading can miss subtle scientific quality issues.
- High-memory tasks can fail operationally before measuring true capability.
- Benchmark-specific optimization can overfit to suite interfaces.


#### Evaluation

**Benchmarks Used:**

- PaperFindingBench
- ScholarQABench2
- LitQA2-FT
- LitQA2-FT-Search
- ArxivDIGESTables-Clean
- CORE-Bench-Hard
- DS-1000
- SUPER-Expert
- DiscoveryBench
- E2E-Bench
- E2E-Bench-Hard


**Metrics:**

- task-level rubric scores
- cross-category overall score
- cost per problem
- Pareto frontier of score vs cost
- benchmark-specific scoring outputs from InspectAI and AstaBench scorers


**Baselines:**

- 57 agents across 22 agent classes in the paper
- Asta science-specific agents
- ReAct-style general agents
- open- and closed-weight model backends
- wrappers around external commercial research tools


**Validation Strength:**

> Benchmarked with standardized tooling, public leaderboard reporting, open-source code, and an arXiv technical report; not yet a peer-reviewed archival publication in the checked sources.


**Evaluation Limitations:**

- Scores depend partly on LLM-as-a-judge rubrics.
- > Some benchmark areas, especially data analysis and discovery, remain difficult and may be noisy to score.
- The dataset is gated, which can limit immediate reproducibility.
- Large compute and memory requirements can bias who can run the full suite.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2510.21652


**Code Url:** https://github.com/allenai/asta-bench


**Dataset Url:** https://huggingface.co/datasets/allenai/asta-bench


**Product Url:** https://allenai.org/asta/bench


**Leaderboard Url:** https://huggingface.co/spaces/allenai/asta-bench-leaderboard


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:**

- PaperFindingBench
- ScholarQABench2
- LitQA2
- CORE-Bench-Hard
- DS-1000
- SUPER
- DiscoveryBench
- E2E-Bench


**Components:**

- AstaBench suite
- Asta Scientific Corpus tool
- Computational Notebook and python_session environment
- agent-eval leaderboard framework
- agent-baselines repository
- 2400+ problems across 11 benchmarks


**Evaluated By:**

- A public leaderboard backed by agent-eval and InspectAI.
- An arXiv technical report describing methodology and baselines.
- Community and internal reruns through validation and test splits.


**Evaluates:**

- scientific research agents
- paper finding
- scholarly question answering
- tool use
- code execution
- data analysis
- end-to-end scientific discovery
- multi-domain science


**Competes With Or Complements:**

- Part of the broader Asta ecosystem alongside Asta agents and Asta resources.
- > Complements general deep-research benchmarks by focusing specifically on scientific research workflows.


#### Timeline

**Milestones:**

- 2025-08-26: Ai2 published the launch blog for AstaBench and its initial public leaderboard.
- 2025-10-24: arXiv v1 of the AstaBench paper was released.
- 2026-04-21: arXiv v2 of the paper was released.
- 2026-05-28: Public code repository and leaderboard remained available.


**Version History:**

- AstaBench paper v1 released on 2025-10-24 and v2 on 2026-04-21.
- AstaBench 0.3.1 adjusted paper-search task instructions to better match scoring criteria.
- > The benchmark is described by Ai2 as an evolving evaluation with refreshed problems and leaderboard updates.


**Adoption Signals:**

- Ai2 hosts a dedicated benchmark page and public leaderboard.
- The public GitHub repository showed 105 stars on 2026-05-28.
- The suite is positioned as one of the three core pillars of the Asta ecosystem.


**Supersession Notes:** Not superseded in the checked sources; it is presented as the current benchmarking pillar of Asta.


#### Applications

**Real World Applications:**

- > Comparing scientific research agents for literature understanding, code execution, data analysis, and discovery workflows.
- Evaluating whether general or specialized agents are better suited for research assistance.
- Providing a reproducible benchmark for teams building science-focused agent products.


**Users:**

- AI agent researchers
- scientific AI developers
- benchmark maintainers
- research-product teams
- labs evaluating scholarly assistants


**Deployment Constraints:**

- Requires Hugging Face access to the gated dataset.
- Requires API keys for supported model providers and Asta tools.
- Docker is recommended, and some tasks require sandboxed execution.
- Full-suite runs may require high RAM and multicore CPU resources.


**Cost And Runtime:**

> AstaBench explicitly tracks score and cost together. The repo notes roughly 10 GB internal framework memory for full-suite runs, with some SUPER and E2E instances using 20-30 GB more; Ai2 reports using a 128 GB RAM, 8-core machine for many internal runs.


#### Governance And Risk

**Scientific Integrity Risks:**

- LLM-judged scientific tasks can reward polished but weak reasoning.
- Agents may fabricate citations or overstate findings.
- Benchmark optimization may not transfer cleanly to real scientific work.


**Security And Safety Risks:**

- Sandboxed code tasks still involve executing agent-generated code.
- Scientific search and execution tools could be misused if guardrails are weakened.
- Closed-source submissions can reduce transparency about unsafe behaviors.


**Mitigations:**

- Date-restricted literature tools for reproducibility.
- Sandboxed notebooks and constrained task tools.
- Cost logging, traceable logs, and source-code collection for leaderboard submissions.
- Submission metadata that flags openness, tool categories, and missing reproducibility evidence.


**Policy Relevance:**

> Relevant to trustworthy evaluation of scientific AI agents, reproducibility standards, and responsible disclosure of benchmarked agent capabilities.


#### Uncertain Fields

- successors

### BixBench

#### Identity

**Id:** bixbench


**Name:** BixBench


**Aliases:** BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology, Bioinformatics Benchmark


**Organization:** FutureHouse and ScienceMachine


**First Public Release:** 2025-02-28


**Current Status:**

> Active public benchmark with a public arXiv preprint, public GitHub evaluation harness, and a public Hugging Face dataset. The current dataset main branch reflects a v1.5 update beyond the original preprint's question set.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset, codebase


**Domains:** bioinformatics, computational biology, genomics, transcriptomics, phylogenetics and evolutionary analysis


**Positioning:**

> Benchmark for AI agents performing real-world biological data analysis and multi-step notebook-based exploration.


**Boundary Notes:**

> Included because BixBench evaluates open-ended scientific dataset exploration, code execution, and interpretation in biology-focused analysis tasks. It is more realistic than recall-style biology benchmarks and more domain-specific than generic data-science agent benchmarks.


#### Capabilities

**Lifecycle Coverage:**

- research-question understanding
- dataset exploration
- multi-step computational analysis
- code writing and execution
- result interpretation
- open-answer submission and grading


**Tool Access:**

- Jupyter notebook environment
- Python
- R
- Bash
- Aviary agent framework
- Dockerized bioinformatics environment
- Hugging Face dataset access


**Execution Environment:**

> A controlled Jupyter-notebook-based agent environment built on Aviary, with containerized bioinformatics packages and evaluation harness scripts for zero-shot and agentic runs.


**Artifact Outputs:**

- analysis trajectories
- Jupyter notebooks
- open-answer submissions
- multiple-choice predictions
- accuracy scores
- graded evaluation results


**Human Roles:**

> Bioinformatics experts contributed the source analytical scenarios and reviewed generated questions. Users configure models and APIs, run the harness, and interpret the resulting notebooks and scores.


#### Autonomy

**Autonomy Rationale:**

> BixBench evaluates code-executing agents that can plan and iterate through multi-step biological analyses in a notebook environment, but they remain bounded by fixed benchmark capsules, tools, and scoring rather than acting as unconstrained autonomous scientists.


**Iteration Loop:**

> The benchmark explicitly supports iterative notebook-based agent execution: agents inspect files, edit cells, rerun analyses, and submit answers after multi-step exploration.


**Stopping And Guardrails:**

> Evaluation is bounded by benchmark capsules, fixed tools, an Aviary-controlled environment, Dockerized dependencies, and automatic grading. The dataset also includes explicit warnings that benchmark data should not appear in training corpora.


**Known Failure Modes:**

- poor open-answer accuracy on complex biological analyses
- multiple-choice performance near or below random
- plot or notebook-output misinterpretation
- reliance on recall rather than grounded analysis
- coverage gaps across bioinformatics workflows not represented in the benchmark


#### Evaluation

**Benchmarks Used:**

> BixBench itself in open-answer and multiple-choice evaluation regimes, including majority-vote experiments across repeated trajectories.


**Metrics:**

- open-answer accuracy
- multiple-choice accuracy
- comparison against random guessing
- majority-vote evaluation across repeated trajectories
- benchmark runtime comparisons


**Evaluation Limitations:**

> The original paper reports 53 scenarios and 296 questions, while the current public repository and dataset main branch describe a v1.5 benchmark with 60 notebooks and 205 questions, so version comparisons require care. The paper evaluates only two frontier models and explicitly notes that many bioinformatics workflows remain outside current benchmark coverage.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2503.00096


**Code Url:** https://github.com/Future-House/BixBench


**Dataset Url:** https://huggingface.co/datasets/futurehouse/BixBench


**Product Url:** https://www.futurehouse.org/research-announcements/bixbench


**Source Quality:**

> Primary sources: official arXiv preprint, official GitHub repository, official Hugging Face dataset, and official FutureHouse announcement.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- 53 scenarios and 296 questions in the original preprint
- 60 notebooks and 205 questions in the current public v1.5 dataset
- Aviary-based evaluation harness
- data-analysis-crow agent framework
- Dockerized notebook environment
- open-answer grading pipeline
- multiple-choice evaluation mode
- benchmark canary strings in the public dataset


**Evaluates:**

- bioinformatics
- biological data analysis
- multi-step dataset exploration
- open-ended computational biology reasoning
- notebook-based scientific code execution


#### Timeline

**Milestones:**

- 2025-02-28: arXiv v1 released.
- 2025-03-04: FutureHouse and ScienceMachine publicly announced BixBench.
- 2025-03-08: arXiv v2 released.
- 2025-10-08: arXiv v3 released.
- 2025: public dataset updated to a v1.5 question set while retaining the original v1.0 tag.


**Version History:**

- arXiv v1 on 2025-02-28
- arXiv v2 on 2025-03-08
- arXiv v3 on 2025-10-08
- current public dataset main branch and v1.5 tag contain 205 rows
- original question set remains accessible under the v1.0 tag


**Adoption Signals:**

- 109 GitHub stars at verification time
- 36 Hugging Face dataset likes at verification time
- official FutureHouse announcement
- public open dataset and evaluation harness


**Supersession Notes:**

> The current main and v1.5 dataset state supersede the original v1.0 question set for ongoing public use, while the original set remains available for reproducibility.


#### Applications

**Real World Applications:**

- benchmarking autonomous bioinformatics agents
- testing notebook-based biological data analysis systems
- measuring multi-step dataset exploration ability in biology
- guiding development of FutureHouse-style scientific agents


**Users:**

- AI-for-biology researchers
- bioinformatics agent developers
- computational biologists evaluating assistants
- benchmark designers


**Deployment Constraints:**

> Running the harness requires dataset access through Hugging Face, Docker, a containerized notebook environment, bioinformatics packages, and API keys for supported LLMs. The repository notes that agentic evaluations can require significant API credits and 24-48 hours.


#### Governance And Risk

**Scientific Integrity Risks:**

- public benchmark contamination or training-data leakage
- benchmark overfitting to a limited slice of bioinformatics workflows
- models answering from recall rather than grounded analysis
- version mismatch between the original preprint and the current public dataset


**Security And Safety Risks:**

- agents execute Python, R, and Bash code in notebook environments
- misinterpretation of biological analyses could mislead downstream scientific decisions
- bioinformatics package execution and external data handling create operational risk


**Mitigations:**

- controlled Aviary environment
- Dockerized dependency isolation
- open evaluation harness
- calibration experiments for data leakage and model choice
- dataset canary warnings against inclusion in training corpora


**Policy Relevance:**

> BixBench is relevant to scientific-AI governance because it measures how close current models are to autonomous biological data analysis, while also surfacing risks around benchmark contamination, code execution, and overclaiming progress from narrow scientific domains.


#### Uncertain Fields

- autonomy_level
- baselines
- competes_with_or_complements
- cost_and_runtime
- evaluated_by
- leaderboard_url
- predecessors
- successors
- validation_strength

### ChemCrow

#### Identity

**Id:** chemcrow


**Name:** ChemCrow


**Aliases:** ChemCrow: Augmenting large-language models with chemistry tools


**Organization:** University of Rochester White Lab and collaborators


**First Public Release:** 2023-04-11


**Current Status:**

> Peer-reviewed open-source research system; the public package omits some paper-era tools because of API restrictions.


#### Taxonomy

**Category:** domain_scientific_discovery_agent


**Type:** paper, codebase


**Domains:** chemistry


**Positioning:**

> A tool-augmented chemistry assistant that uses GPT-4 plus expert-designed tools to solve reasoning-intensive chemistry tasks.


**Boundary Notes:**

> Included because it combines LLM reasoning, chemistry-specific tools, safety controls, and limited physical-lab linkage. Excludes generic chat assistants that answer chemistry questions without specialized tools or action loops.


#### Capabilities

**Lifecycle Coverage:**

- chemistry_question_answering
- synthesis_planning
- tool_use
- safety_checks
- cloud_lab_execution
- molecular_design


**Tool Access:**

- LangChain agent framework
- Web search via SerpAPI
- Literature search via paper-qa and FAISS
- Python REPL
- Human input tool
- RDKit
- PubChem
- chem-space
- RXN4Chem API
- IBM Research RoboRXN platform
- Optional self-hosted reaction-prediction and retrosynthesis Docker services


**Execution Environment:**

> GPT-4 running inside a LangChain tool-using loop with external chemistry APIs, optional self-hosted services, and paper-era experiments connected to IBM Research's RoboRXN platform.


**Artifact Outputs:**

- Chemistry answers grounded in tools
- Synthesis plans
- Safety guidance
- Experiment scripts
- Chromophore candidates
- Reasoning traces


**Human Roles:**

- Users specify the chemistry task and can answer follow-up questions through the Human tool.
- Human operators and chemist experts retain control over automated chemical platforms.
- Expert chemists reviewed model outputs during evaluation.


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> ChemCrow autonomously selects and chains tools within a reasoning loop and can drive bounded chemistry workflows, including cloud-connected synthesis in the paper. It remains assistant-level because users initiate tasks, human oversight remains central for laboratory execution, and the public system is a partial release rather than a fully autonomous end-to-end scientist.


**Iteration Loop:**

> Yes. ChemCrow follows repeated Thought, Action, Action Input, and Observation cycles until it reaches a final answer.


**Stopping And Guardrails:**

> Safety controls combine hard-coded and prompted rules, including checks for dangerous or controlled chemicals. The agent can stop execution when a task is unsafe, ask humans for permission, and remains bounded by the external tools and APIs available to it.


**Known Failure Modes:**

- Hallucinated conclusions if tool outputs are weak or misused
- Invalid or non-executable synthesis procedures
- Reasoning errors despite access to tools
- Unreliable LLM-based evaluation that rewards fluent but incorrect answers
- Performance regressions when required APIs or tools are unavailable


#### Evaluation

**Benchmarks Used:**

- Fourteen chemistry use cases spanning synthesis, molecular design, and chemical logic
- Expert chemist comparisons between ChemCrow and tool-less GPT-4
- EvaluatorGPT scoring of task responses
- Physical synthesis validation on IBM Research's RoboRXN platform


**Metrics:**

- Degree of task completion
- Chemical correctness and factuality
- Quality of reasoning
- Expert preference between ChemCrow and GPT-4
- EvaluatorGPT scores
- Successful execution of robotic syntheses and chromophore discovery workflow


**Baselines:** GPT-4 without external tools, Individual chemistry tools used outside the agent loop


**Validation Strength:** Peer-reviewed and real-world validated.


**Evaluation Limitations:**

> The evaluation suite is bespoke rather than standardized, the strongest results depend on a closed GPT-4 API, and the paper shows that LLM-based evaluation can be misleading when factual chemistry matters. The public repository also does not reproduce the full paper system because some tools are missing.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2304.05376


**Code Url:** https://github.com/ur-whitelab/chemcrow-public


**Dataset Url:** https://github.com/ur-whitelab/chemcrow-runs


**Product Url:** Not applicable; this is a research system rather than a commercial product.


**Leaderboard Url:** Not applicable; no official public leaderboard.


**Source Quality:**

> Primary sources: Nature Machine Intelligence article, arXiv paper, and official ChemCrow repositories.


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** ReAct, MRKL, RXN for Chemistry, AIZynthFinder


**Components:**

- Reaction tools
- Molecule tools
- Safety tools
- Search tools
- Standard tools
- WebSearch
- LitSearch
- Python REPL
- Human tool
- RoboRXN integration


**Evaluated By:**

- Expert chemist review across fourteen use cases
- EvaluatorGPT scoring
- Physical synthesis validation on IBM Research's RoboRXN platform


**Evaluates:**

> Not a benchmark item; it evaluates a chemistry tool-using agent across synthesis, design, and reasoning tasks.


**Competes With Or Complements:** Coscientist, RXN for Chemistry, AIZynthFinder, Other tool-augmented chemistry copilots


#### Timeline

**Milestones:**

- 2023-04-11: arXiv preprint submitted
- 2024: Nature Machine Intelligence article published
- 2024-03-27: ChemCrow-runs public release noted in repository metadata
- 2024: Open-source package and experiment repositories publicly available


**Version History:**

- ArXiv versions progressed from v1 on 2023-04-11 to v5 on 2023-10-02.
- > The public package is a partial open-source release and does not include all tools used in the paper because of API restrictions.
- The peer-reviewed Nature Machine Intelligence version appeared in 2024.


**Adoption Signals:**

- Nature Machine Intelligence reported 138k accesses at verification time.
- The official package repository showed about 913 GitHub stars and 143 forks on 2026-05-28.
- ChemCrow-runs showed about 96 GitHub stars on 2026-05-28.


**Supersession Notes:**

> No official direct successor was announced as of 2026-05-28, although later chemistry agents reuse the same tool-augmented design pattern.


#### Applications

**Real World Applications:**

- Chemistry question answering grounded in external tools
- Retrosynthesis and synthesis planning
- Safety screening for proposed reactions or controlled substances
- Cloud-connected robotic synthesis execution on RoboRXN
- Chromophore discovery and simple chemistry machine-learning workflows


**Users:**

- Academic chemists
- Medicinal and materials researchers
- Students and non-experts needing a chemistry assistant
- Robotic chemistry platform users


**Deployment Constraints:**

- Requires GPT-4 or a comparable OpenAI model API
- Optionally uses SerpAPI for web search
- Relies on external chemistry APIs such as RXN4Chem unless users self-host replacements
- Physical execution in the paper used IBM Research's proprietary RoboRXN platform
- The public repository does not reproduce the full paper system because some tools are missing


#### Governance And Risk

**Scientific Integrity Risks:**

- Hallucinated conclusions when tool outputs are weak or misused
- Closed-model reproducibility issues
- LLM-based evaluation preferring fluent but wrong answers
- Over-reliance by non-expert users on imperfect chemistry reasoning


**Security And Safety Risks:**

- Unsafe laboratory actions if synthesized procedures are wrong
- Dual-use misuse for controlled or hazardous chemicals
- Risk from autonomous tool chaining into cloud-connected lab hardware
- Exposure of API credentials or misuse of external services


**Mitigations:**

- Hard-coded and prompted safety guidelines
- Execution stops when the target is flagged as dangerous or related to controlled chemicals
- Human review and control remain heavy on automated chemical platforms
- Tool grounding reduces hallucinations versus a tool-less GPT-4 baseline
- The Human tool can require explicit user permission before certain actions


**Policy Relevance:**

> Relevant to chemical safety policy, dual-use governance for open-source chemistry agents, and responsible release practices for LLM systems that can steer physical lab workflows.


#### Uncertain Fields

- cost_and_runtime
- successors

### Consensus

#### Identity

**Id:** consensus


**Name:** Consensus


**Aliases:** Consensus AI, ResearchGPT


**Organization:** Consensus


**First Public Release:** 2021


**Current Status:** Active commercial product with free, paid, team, enterprise, API, and ChatGPT app offerings.


#### Taxonomy

**Category:** literature_review_product


**Type:** product


**Domains:** general_academic_research


**Positioning:** AI academic search and evidence-synthesis workspace for scientific research.


**Boundary Notes:**

> Included because it is purpose-built for scientific literature search, paper summarization, and evidence synthesis. It is distinct from general-purpose chatbots because it grounds outputs in retrieved academic papers and citations.


#### Capabilities

**Lifecycle Coverage:**

- literature search
- paper summarization
- evidence synthesis
- citation export
- research question exploration
- literature review support


**Tool Access:**

- semantic search
- keyword search
- citation-grounded summarization
- study metadata extraction
- reference manager export
- ChatGPT app integration
- API access by application


**Execution Environment:** Product-hosted web application with official integrations in ChatGPT and a separate API offering.


**Artifact Outputs:**

- paper lists
- cited summaries
- study snapshots
- consensus meter views
- research briefs
- citation exports
- literature reviews


**Human Roles:**

> Users choose research questions, inspect cited papers, manage saved libraries, decide whether summaries are trustworthy, and use the outputs in their own research or writing workflows.


#### Autonomy

**Autonomy Level:** L1


**Autonomy Rationale:**

> Consensus automates retrieval and synthesis of scientific literature, but the user still frames the task, reviews evidence, and decides how to use the result.


**Iteration Loop:**

> Supports iterative follow-up through Threads, and the 2026 Research Agent feature can plan searches, chain tools, and return citation-backed answers for multi-step research questions.


**Stopping And Guardrails:**

> Every AI-generated response starts with literature search; summaries are constrained to retrieved papers, relevance thresholds and checker models are used before synthesis, and cited papers remain directly inspectable by the user.


**Known Failure Modes:**

- misread-source summarization errors
- limited corpus coverage
- consensus meter misclassification when evidence is sparse or mixed
- over-reliance on summaries without reading the underlying papers


#### Evaluation

**Evaluation Limitations:**

> Consensus documentation states that the corpus does not include every scientific paper and that AI summaries can still misinterpret papers, even when sources are real and cited.


#### Links And Provenance

**Product Url:** https://consensus.app/


**Source Quality:**

> Primary sources: official product pages, help-center documentation, official changelog, and official about page.


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** Consensus 2.0, Consensus GPT / ChatGPT App integration, Research Agent


**Components:**

- semantic and keyword search pipeline
- Pro Analysis
- Consensus Meter
- Study Snapshot
- Ask Paper
- Advanced Search Filters
- Threads
- My Library
- Search History
- Consensus API
- Research Agent


**Competes With Or Complements:** Elicit, Google Scholar, PubMed, ChatGPT with the Consensus app


#### Timeline

**Milestones:**

- 2021: Consensus founded by Christian Salem and Eric Olson.
- 2022-02-08: Public introduction of Consensus.
- 2023-11-01: Consensus 2.0 launched with hybrid search across 200 million papers.
- 2024-01-15: Consensus Meter launched.
- 2024-01-10: Consensus GPT launched in ChatGPT.
- 2025-05-01: Threads launched.
- 2025-03-24: Research Hub for uploaded PDFs launched.
- 2026-05-06: Consensus became available as a ChatGPT App.
- 2026-05-12: Research Agent launched.
- 2026-05-13: Consensus expanded integration across ChatGPT, Claude, Codex, Claude Code, and the API.


**Version History:**

- Consensus 2.0 improved hybrid search and answer extraction in November 2023.
- > The product added ChatGPT integration, Consensus Meter, advanced filters, search history, Teams, Ask Paper, and Threads during 2024-2025.
- > In May 2026, the product added the ChatGPT App, Research Agent, improved external integrations, and broader API positioning.


**Adoption Signals:**

- 10+ million researchers, students, and clinicians choose Consensus.
- 12,500+ universities are represented among users.
- 20+ million papers from Consensus have been shared with others.
- 150+ million research questions have been handled to date.
- The product offers Free, Pro, Deep, Teams, and Enterprise plans.


**Supersession Notes:**

> The core product remains active. Older surfaces such as Consensus GPT / plugin-style usage have been superseded by newer app-style integrations, but the main product is not superseded.


#### Applications

**Real World Applications:**

- literature review
- finding supporting citations for papers
- comparing evidence across studies
- identifying gaps in the literature
- building research briefs
- faster academic search for researchers, students, and clinicians


**Users:**

- academic researchers
- students
- clinicians
- research organizations
- universities
- knowledge workers needing evidence-backed answers


**Deployment Constraints:**

> Requires internet access and a Consensus account. Deeper usage depends on subscription tier, full-text availability, and for API usage, application-based access and pricing.


**Cost And Runtime:**

> As of 2026-05-28, the Free tier is $0, Pro is $15 per month or $120 per year, Deep is $65 per month or $540 per year, Teams is custom priced, Enterprise is quote-based, and API pricing starts at $0.10 per call plus a platform fee.


#### Governance And Risk

**Scientific Integrity Risks:**

- misinterpreting retrieved papers
- over-trusting synthesized summaries
- missing relevant evidence outside the indexed corpus
- using quick summaries in place of full critical reading


**Mitigations:**

- search before synthesis
- citations to real papers in every response
- relevance thresholds before summary features can run
- checker models for relevance verification
- direct links back to underlying papers
- user feedback and support channels for corrections


**Policy Relevance:**

> Relevant to evidence-grounded AI, citation integrity, responsible AI for research workflows, and institutional deployment of AI-assisted academic search tools.


#### Uncertain Fields

- baselines
- benchmarks_used
- code_url
- dataset_url
- evaluated_by
- evaluates
- leaderboard_url
- metrics
- paper_url
- predecessors
- security_and_safety_risks
- validation_strength

### CORE-Bench

#### Identity

**Id:** core_bench


**Name:** CORE-Bench


**Aliases:**

- CORE-Bench
- Computational Reproducibility Agent Benchmark
- > CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark


**Organization:** Princeton-affiliated academic authorship group


**First Public Release:** 2024-09-17


**Current Status:**

> Open-source benchmark, dataset, and harness; the original repository says its current harness is no longer actively maintained and recommends the Holistic Agent Leaderboard harness.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset, codebase


**Domains:** computational reproducibility, computer science, social science, medicine


**Positioning:**

> Benchmark for evaluating whether AI agents can computationally reproduce published scientific papers.


**Boundary Notes:**

> Included because it evaluates agents on running real research artifacts, installing dependencies, and extracting published results. It targets research reproducibility rather than novel hypothesis generation or wet-lab science.


#### Capabilities

**Lifecycle Coverage:**

- dependency installation
- code execution
- environment configuration
- result extraction
- report writing
- figure and table interpretation


**Tool Access:**

- shell
- Docker
- virtual machines
- vision-language model queries
- Python environments
- R environments
- downloaded research code capsules


**Execution Environment:**

> Agents are evaluated in isolated Docker containers or virtual machines that download paper capsules and write a report.json output.


**Artifact Outputs:** report.json answers, agent traces, benchmark result files, leaderboard submission JSON


**Human Roles:**

- Humans define the benchmark tasks and difficulty levels.
- Humans provide API keys and infrastructure setup.
- Humans inspect reproducibility results and submit leaderboard artifacts.


#### Autonomy

**Autonomy Level:** L2-L3


**Autonomy Rationale:**

> Tasks require multi-step autonomous environment setup, code execution, debugging, and output interpretation, but goals, datasets, and infrastructure are predefined by humans. The agent is autonomous within a bounded reproducibility task rather than fully self-directed research.


**Iteration Loop:**

> Yes. Agents can iteratively inspect failures, install dependencies, rerun code, and repair their reporting until the task completes or the budget is exhausted.


**Stopping And Guardrails:**

- Three difficulty levels constrain what information is available to the agent.
- Original evaluation uses isolated virtual machines; local runs can use Docker.
- The paper uses a per-task time limit of 2 hours.
- Programmatic checking ensures report.json uses the correct keys.


**Known Failure Modes:**

- Dependency installation failures.
- Incorrect run commands or environment assumptions.
- Failure to inspect figures, HTML, or PDF outputs correctly.
- Writing an invalid or incomplete report.json.
- Benchmark saturation if agents overfit known capsules.


#### Evaluation

**Benchmarks Used:**

- 270 tasks from 90 papers across three disciplines.
- CORE-Bench-Easy, CORE-Bench-Medium, and CORE-Bench-Hard.
- Holistic Agent Leaderboard for ongoing external comparison.


**Metrics:**

- Accuracy or pass@1 by difficulty level.
- Per-task cost and runtime analyses in the paper.
- Paper headline: best agent scored 58.52% on Easy, 55.56% on Medium, and 19.26% on Hard.


**Baselines:** AutoGPT with GPT-4o., AutoGPT with GPT-4o-mini., CORE-Agent with GPT-4o., CORE-Agent with GPT-4o-mini.


**Validation Strength:**

> Benchmarked with open-source code and dataset, plus a paper published in Transactions on Machine Learning Research in January 2025.


**Evaluation Limitations:**

- Benchmark focuses on code reproducibility rather than full result reproducibility.
- Tasks were selected from CodeOcean under screening criteria, so scope is not all research papers.
- Running untrusted research code requires heavy isolation and infrastructure.
- The original GitHub harness is no longer actively maintained.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2409.11363


**Code Url:** https://github.com/siegelz/core-bench


**Dataset Url:** https://huggingface.co/datasets/siegelz/core-bench


**Leaderboard Url:** https://agent-evals-leaderboard.hf.space/


**Source Quality:**

> Primary sources: arXiv paper, TMLR/OpenReview PDF, official GitHub repository, and official Hugging Face dataset card.


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** Holistic Agent Leaderboard harness integration


**Components:**

- 270 benchmark tasks
- 90 source papers
- three difficulty levels
- isolated VM or Docker harness
- Hugging Face dataset files
- HAL submission conversion scripts


**Evaluated By:** Holistic Agent Leaderboard


**Competes With Or Complements:** PaperBench, MLE-bench, DiscoveryBench


#### Timeline

**Milestones:**

- 2024-09-17: arXiv preprint posted.
- 2025-01: published in Transactions on Machine Learning Research.
- > 2026-05-28: repository states the original harness is no longer actively maintained and recommends HAL.


**Version History:**

- Initial benchmark and harness released in 2024.
- > Later workflow shifted toward the Holistic Agent Leaderboard harness rather than the original repository harness.


**Adoption Signals:**

- GitHub repository shows about 75 stars as of 2026-05-28.
- Hugging Face dataset card shows about 291 downloads in the last month.
- Public leaderboard integration exists through the Holistic Agent Leaderboard.


**Supersession Notes:**

> The dataset and benchmark remain usable, but the repository says the original harness is superseded operationally by the Holistic Agent Leaderboard harness.


#### Applications

**Real World Applications:**

- Testing whether agents can reproduce published computational results.
- Screening research artifacts before publication or review.
- Measuring agent reliability on scientific code execution tasks.


**Users:** Reproducibility researchers, conference organizers, journal editors, research engineers, agent evaluation teams


**Deployment Constraints:**

- Python 3.9 environment for the original harness.
- Docker or Azure VM infrastructure.
- Privileged Docker is required for some medium tasks.
- Benchmark downloads external capsules and may require GPU quotas for some tasks.


**Cost And Runtime:**

> The paper used a 2-hour per-task limit. Sequential evaluation of all 270 tasks would take over 20 days, while the VM-based harness reduced a full run to a little over two hours by parallelizing across many machines.


#### Governance And Risk

**Scientific Integrity Risks:**

- Mistaking code reproducibility for full scientific validity.
- Benchmark overfitting to fixed capsules.
- Incorrectly claiming paper results are validated when only execution was reproduced.


**Security And Safety Risks:**

- Running arbitrary third-party research code.
- Using privileged Docker or remote virtual machines.
- Handling API keys and downloaded external artifacts.


**Mitigations:**

- Isolated VM or Docker execution.
- Programmatic validation of report.json keys.
- Clear benchmark difficulty structure and task prompts.
- Leaderboard workflow requiring logged traces and structured outputs.


**Policy Relevance:**

> Relevant to reproducibility norms, benchmark governance, and the credibility of claims about AI agents performing research-adjacent work.


#### Uncertain Fields

- evaluates
- predecessors
- product_url

### Coscientist

#### Identity

**Id:** coscientist


**Name:** Coscientist


**Aliases:** Autonomous chemical research with large language models


**Organization:** Carnegie Mellon University / Gomes Group


**First Public Release:** 2023-12-20


**Current Status:**

> Peer-reviewed research system with an official supporting-information repository; not released as a turnkey product.


#### Taxonomy

**Category:** domain_scientific_discovery_agent


**Type:** paper, codebase, research demo


**Domains:** chemistry


**Positioning:**

> A GPT-4-based autonomous chemistry co-scientist for planning, executing, and optimizing laboratory experiments.


**Boundary Notes:**

> Included because it closes the loop from planning to wet-lab/cloud-lab execution in chemistry. Excludes generic coding agents and lab robots without LLM-driven scientific planning.


#### Capabilities

**Lifecycle Coverage:** synthesis_planning, hardware_documentation_search, cloud_lab_execution, liquid_handler_control, experiment_optimization


**Tool Access:**

- Internet search via a dedicated web-search module
- Documentation retrieval over API manuals
- Isolated Python code execution in Docker
- Opentrons Python API
- Emerald Cloud Lab Symbolic Lab Language (SLL)
- Laboratory automation APIs
- UV-Vis plate-reader integration


**Execution Environment:**

> GPT-4 planner plus helper modules running with web access, documentation retrieval, Docker-based code execution, and robotic/cloud-lab hardware interfaces.


**Artifact Outputs:**

- Synthesis plans
- Experimental protocols
- Executable automation code
- Cloud-lab instructions
- Optimization decisions
- Analytical reasoning traces


**Human Roles:**

- Humans provide the natural-language task and prepare the hardware context.
- Humans manually moved plates in the integrated cross-coupling setup.
- Humans inspect outcomes and can intervene if the physical workflow or safety constraints require it.


#### Autonomy

**Autonomy Level:** L4


**Autonomy Rationale:**

> Coscientist autonomously planned, wrote code for, and executed chemistry tasks across six experimental categories, including cloud-lab and liquid-handler actions. It remains below L5 because the reported setup still relied on human-provided goals, partial manual handling, and bounded tool interfaces.


**Iteration Loop:**

> Yes. The planner repeatedly calls GOOGLE, DOCUMENTATION, PYTHON, and EXPERIMENT actions, incorporates returned observations, fixes failing code, and revises experimental plans.


**Stopping And Guardrails:**

> Guardrails include tool-bounded actions, Docker-isolated code execution, documentation grounding, and task-specific hardware and API constraints. In some experiments internet access was disabled, and the integrated wet-lab workflow still required manual plate transfer.


**Known Failure Modes:**

- Hallucinated or incomplete synthesis plans without grounding
- Incorrect API or hardware instructions when documentation retrieval is insufficient
- Suboptimal reaction parameter choices
- Physical experiment failures from imperfect automation assumptions
- Subjective grading noise in chemistry-planning evaluation


#### Evaluation

**Benchmarks Used:**

- A seven-compound synthesis-planning test set scored on a 1-5 chemistry rubric
- Documentation-search tasks for Opentrons and Emerald Cloud Lab APIs
- Cloud-lab HPLC execution tasks
- Low-level liquid-handler control tasks
- Cross-coupling reaction design and optimization experiments


**Metrics:**

- Chemistry-planning rubric scores from 1 to 5
- Task success or failure for documentation lookup and command execution
- Successful physical execution of robotic and cloud-lab procedures
- Successful optimization of palladium-catalysed cross-couplings


**Baselines:** GPT-3.5, GPT-4, Claude 1.3, Falcon-40B-Instruct, A GPT-3.5-based Web Searcher variant


**Validation Strength:** Peer-reviewed and real-world lab validated.


**Evaluation Limitations:**

> The synthesis-planning rubric is partly subjective, the task suite is small, and different modules were validated on bespoke tasks rather than a standardized benchmark. The integrated wet-lab setup was not fully automated because plate movement remained manual.


#### Links And Provenance

**Paper Url:** https://www.nature.com/articles/s41586-023-06792-0


**Code Url:** https://github.com/gomesgroup/coscientist


**Dataset Url:** https://github.com/gomesgroup/coscientist


**Product Url:** Not applicable; this is a research system rather than a commercial product.


**Leaderboard Url:** Not applicable; no official public leaderboard.


**Source Quality:** Primary sources: peer-reviewed Nature article and official Gomes Group GitHub repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** Self-driving lab and autonomous experimentation systems, Tool-augmented chemistry agents such as ChemCrow


**Components:**

- Planner (GPT-4 chat completion instance)
- Web Searcher module
- Documentation module
- Code execution module
- Automation / EXPERIMENT module
- Opentrons OT-2 integration
- Emerald Cloud Lab SLL integration
- UVVIS command


**Evaluated By:** The six-task experimental suite reported in the Nature paper, Chemistry-planning comparisons against model baselines


**Evaluates:** Not a benchmark item; it demonstrates and evaluates an autonomous chemistry agent.


**Competes With Or Complements:** ChemCrow, Self-driving lab platforms, Cloud-lab automation systems, Robotic chemistry workflow tools


#### Timeline

**Milestones:**

- 2023-12-20: Nature paper published
- 2023-12: Official supporting-information repository released publicly
- > 2023-12: Demonstrated six chemistry and lab task classes, including cloud-lab execution and reaction optimization


**Version History:**

- Initial public release centered on the 2023 Nature paper and supporting repository.
- > No major public software version series or packaged releases were documented in the official repository as of 2026-05-28.


**Adoption Signals:**

- Nature reported 254k accesses and 948 citations at verification time.
- The official repository showed about 202 to 203 GitHub stars and 29 forks on 2026-05-28.


**Supersession Notes:** No official superseding version was announced as of 2026-05-28.


#### Applications

**Real World Applications:**

- Autonomous synthesis planning for known compounds
- Hardware documentation retrieval for robotic APIs
- Cloud-lab experiment execution
- Liquid-handler protocol generation
- Reaction optimization for palladium-catalysed cross-couplings


**Users:** Academic chemists, Self-driving lab researchers, Laboratory automation engineers, Cloud-lab users


**Deployment Constraints:**

- Requires access to GPT-4-class models and associated APIs
- Requires the relevant documentation corpus and tool wrappers
- Requires robotic hardware or cloud-lab endpoints such as Opentrons OT-2 or Emerald Cloud Lab
- Requires wet-lab safety oversight and compatible instrumentation


#### Governance And Risk

**Scientific Integrity Risks:**

- Hallucinated procedures or unsupported justifications if grounding fails
- Overstating autonomy despite remaining manual steps
- Weak reproducibility across changing closed-model APIs
- Small bespoke evaluation tasks that may not generalize


**Security And Safety Risks:**

- Unsafe chemical or robotic actions if instructions are wrong
- Risky code or hardware calls from an autonomous planner
- Dual-use concerns around automating synthesis workflows
- Cloud-lab misuse if execution permissions are not tightly scoped


**Mitigations:**

- Documentation grounding and web grounding before action
- Docker isolation for Python execution
- Tool-bounded action space via GOOGLE, DOCUMENTATION, PYTHON, and EXPERIMENT commands
- Human setup and residual manual handling in the physical workflow
- Existing laboratory controls on instruments and cloud-lab APIs


**Policy Relevance:**

> Relevant to responsible AI in laboratories, dual-use governance for chemistry automation, and policies for human oversight of autonomous experimental systems.


#### Uncertain Fields

- cost_and_runtime
- successors

### Deep Research Bench / RetroSearch

#### Identity

**Id:** futuresearch_deep_research_bench


**Name:** Deep Research Bench / RetroSearch


**Aliases:** Deep Research Bench, DRB, RetroSearch


**Organization:** FutureSearch


**First Public Release:** 2025-05


**Current Status:** Active public benchmark and leaderboard hosted by FutureSearch.


#### Taxonomy

**Category:** benchmark


**Type:** paper, leaderboard, benchmark_environment


**Domains:** web research, open-web retrieval, multi-domain factual synthesis, tool-using agents


**Positioning:**

> Open-web deep research benchmark with a frozen-web retrieval environment for reproducible agent evaluation.


**Boundary Notes:**

> Included because it directly benchmarks web research agents and introduces RetroSearch, a frozen-web environment intended to make open-web agent evaluation reproducible over time.


#### Capabilities

**Lifecycle Coverage:**

- multistep web search
- retrieval over archived webpages
- evidence synthesis
- long-form answer generation
- agent-trace evaluation


**Tool Access:**

- RetroSearch frozen-web search environment
- archived webpage corpus
- public leaderboard infrastructure
- trace-based evaluation tooling
- retro and live evaluation modes


**Execution Environment:**

> FutureSearch-hosted benchmark and leaderboard environment where agents operate against RetroSearch, a frozen approximation of web search backed by archived pages.


**Artifact Outputs:**

- leaderboard scores
- cost estimates
- runtime estimates
- task-category scores
- trace-level evaluations for hallucination, tool use, and forgetting


**Human Roles:**

- Skilled humans worked out benchmark answers and curated task instances.
- > Benchmark maintainers scrape and freeze web content, maintain RetroSearch, and update the leaderboard.
- Developers or product teams submit models and agents for evaluation.


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> The benchmark targets bounded, tool-using web research agents that autonomously search, read, and synthesize information for a user task, but not open-ended self-directed scientific systems or physical-world agents.


**Iteration Loop:**

> Yes. FutureSearch continuously evaluates newly released models and agents, and the benchmark supports repeatable retro runs as the live web changes.


**Stopping And Guardrails:**

- RetroSearch freezes page candidates to improve reproducibility over time.
- Carefully curated answers ground objective scoring.
- The benchmark tracks cost and runtime alongside quality.
- Automated trace analysis explicitly monitors hallucination, tool use, and forgetting.


**Known Failure Modes:**

- Agents may hallucinate unsupported claims.
- Agents may forget earlier evidence in long traces.
- Tool misuse can degrade performance even with good base models.
- Benchmark-specific strategies may overfit to RetroSearch behavior instead of the live web.
- Frozen corpora can omit pages that a real-time agent would have found.


#### Evaluation

**Benchmarks Used:**

- 89 multi-step web research task instances in the paper
- 8 diverse task categories
- RetroSearch frozen-web retrieval environment
- retro versus live-agent comparison protocols


**Metrics:**

- task success on curated-answer research tasks
- category-level scores
- hallucination progress over traces
- tool-use progress over traces
- forgetting progress over traces
- cost
- runtime


**Baselines:**

- major LLMs released around the paper period, including thinking models such as o3 and Gemini 2.5 Pro
- commercial deep-research products such as OpenAI Deep Research and Perplexity
- retro versus live versions of web research agents


**Validation Strength:**

> Benchmarked with human-worked-out answers, a public leaderboard, an explicit reproducibility environment, and an arXiv paper; still a preprint rather than a peer-reviewed archival publication in the checked sources.


**Evaluation Limitations:**

- RetroSearch approximates live search rather than reproducing it perfectly.
- > The public website and paper refer to slightly different task counts, indicating a moving benchmark target.
- Public leaderboard rankings can change as new models are added.
- No public self-hostable code repository was identified in the primary sources checked.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2506.06287


**Product Url:** https://futuresearch.ai/deep-research-bench/index.html


**Leaderboard Url:** https://drb.futuresearch.ai/


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- Deep Research Bench task set
- RetroSearch frozen-web search system
- archived webpage corpus with 10-100k pages per task on the public site description
- public leaderboard
- trace-evaluation pipeline for hallucination, tool use, and forgetting


**Evaluated By:**

- A public FutureSearch leaderboard.
- Community scrutiny through a public benchmark website and paper.
- Comparisons between retro and live evaluation modes described by FutureSearch.


**Evaluates:**

- web research agents
- frozen-web retrieval
- tool use
- hallucination
- forgetting
- commercial deep-research products


**Competes With Or Complements:**

- > Complements DeepResearch Bench by emphasizing reproducible frozen-web evaluation and leaderboard tracking for web research agents.
- > Directly compares branded commercial research products and research-agent configurations on the same benchmark.


#### Timeline

**Milestones:**

- 2025-05-06: arXiv paper for Deep Research Bench was released.
- 2025-05: Public DRB leaderboard and RetroSearch framing were launched by FutureSearch.
- > 2025-05: The benchmark evaluated several live commercial research products on the May 2025 DRB version.
- 2026-05-28: FutureSearch continued to host the benchmark and leaderboard publicly.


**Adoption Signals:**

- FutureSearch maintains a public leaderboard for DRB.
- The benchmark page says DRB is featured on Epoch's Benchmark Hub.
- FutureSearch continues to publish benchmark-related analyses and cost tradeoff posts using DRB.


**Supersession Notes:**

> Not superseded in the checked sources; FutureSearch presents DRB as an actively maintained benchmark within its benchmark portfolio.


#### Applications

**Real World Applications:**

- Evaluating commercial and research-grade web research agents under stable retrieval conditions.
- > Tracking whether progress comes from better reasoning, better tool use, or reduced hallucination and forgetting.
- Comparing live-web and frozen-web performance for open-web agent products.


**Users:**

- web research agent developers
- frontier model evaluators
- benchmark researchers
- teams comparing commercial deep-research products


**Deployment Constraints:**

- > Benchmark access is centered on FutureSearch-hosted infrastructure rather than a public self-hosted code release in the checked sources.
- RetroSearch depends on frozen archived pages and search emulation infrastructure.
- Leaderboard participation appears to require contacting FutureSearch.


**Cost And Runtime:**

> FutureSearch tracks both cost and runtime on DRB. The public leaderboard notes that runtime is estimated from ReAct steps rather than wall-clock time, and FutureSearch also publishes Pareto analyses of accuracy versus dollar cost.


#### Governance And Risk

**Scientific Integrity Risks:**

- A frozen web snapshot can diverge from what users experience on the live web.
- Carefully curated answers still reflect benchmark-author assumptions about correctness.
- Model providers may optimize for the benchmark without improving general research reliability.


**Security And Safety Risks:**

- Open-web research agents can ingest misleading, malicious, or unsafe content.
- Benchmarking archived web content still exposes systems to untrusted text and links.
- Public comparison pressure can incentivize opaque product-specific tuning.


**Mitigations:**

- RetroSearch freezes the candidate web corpus to reduce drift.
- Human-worked-out answers anchor evaluation targets.
- Trace-level analysis surfaces hallucination, tool-use, and forgetting behaviors.
- Cost and runtime reporting help contextualize leaderboard scores.


**Policy Relevance:**

> Relevant to reproducibility standards for open-web agent evaluation and to responsible claims about commercial deep-research system performance.


#### Uncertain Fields

- code_url
- dataset_url
- predecessors
- successors
- version_history

### DeepResearch Bench

#### Identity

**Id:** deepresearch_bench_comprehensive


**Name:** DeepResearch Bench


**Aliases:** Deep Research Bench, DRB


**Organization:** University of Science and Technology of China and Metastone Technology


**First Public Release:** 2025-06


**Current Status:** Active open benchmark with public code, dataset, leaderboard, and ongoing benchmark updates.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark_code, leaderboard, dataset


**Domains:**

- deep research
- web research
- citation-rich report generation
- science and technology
- business and finance
- software
- multi-domain long-form research


**Positioning:** Comprehensive benchmark for evaluating deep research agents on long-form, PhD-level research tasks.


**Boundary Notes:**

> Included because it directly benchmarks deep research agents on multi-step retrieval, synthesis, and citation quality across 22 fields, rather than evaluating only short-form search or single-answer QA.


#### Capabilities

**Lifecycle Coverage:**

- problem framing from user prompts
- multistep web exploration
- information retrieval
- citation collection
- long-form report writing
- report evaluation


**Tool Access:**

- benchmark prompt set
- RACE evaluator
- FACT evaluator
- OpenAI or OpenRouter judge-model backends
- Jina web-scraping support for FACT
- public leaderboard and submission workflow


**Execution Environment:**

> Local Python benchmark code that evaluates outputs generated by external deep research agents, with API-based judge models and optional web-scraping support for citation checking.


**Artifact Outputs:**

- overall benchmark scores
- dimension-wise report-quality scores
- citation accuracy metrics
- effective citation counts
- leaderboard entries
- raw generated research reports


**Human Roles:**

- 100+ domain experts created tasks across 22 fields.
- Human annotators with relevant expertise rated report quality for the human-consistency study.
- Developers run their own deep research agents on the prompts and submit outputs for scoring.


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> The benchmark targets agents that autonomously perform multistep web research and synthesis within a bounded user prompt, but it does not evaluate open-ended self-directed scientific programs or physical-world execution.


**Iteration Loop:**

> Yes. Developers repeatedly run their agents on the fixed prompt set, score outputs with RACE and FACT, and resubmit to the leaderboard as evaluators and model backends evolve.


**Stopping And Guardrails:**

- A fixed 100-task benchmark scope bounds evaluation cost and runtime.
- RACE and FACT separate report quality from citation and retrieval quality.
- Leaderboard submissions require reproducibility materials such as raw reports and model metadata.
- Human-consistency studies were used to calibrate automated evaluation methods.


**Known Failure Modes:**

- Judge-model bias can distort report-quality rankings.
- Citation-heavy systems may still miss deeper analytical quality.
- Agents can produce fluent but weakly grounded reports.
- Benchmark optimization may overfit to the evaluation prompts and scoring frameworks.
- API or scraping failures can affect FACT evaluation reliability.


#### Evaluation

**Benchmarks Used:**

- 100 PhD-level research tasks across 22 fields
- RACE (Reference-based Adaptive Criteria-driven Evaluation)
- FACT (Framework for Factual Abundance and Citation Trustworthiness)
- human-consistency evaluation on expert-rated subsets


**Metrics:**

- RACE overall score
- comprehensiveness
- depth
- instruction-following
- readability
- citation accuracy
- effective citation count
- PAR
- OPC
- FAP
- FAS


**Baselines:**

- OpenAI Deep Research
- Gemini 2.5 Pro Deep Research
- Perplexity Deep Research
- Grok Deeper Search
- LLMs with built-in search tools such as Claude, Gemini, GPT-4.1, and Perplexity Sonar variants


**Validation Strength:**

> Benchmarked with public code, project site, dataset, leaderboard, and a human-consistency study reported in an arXiv paper; still a preprint rather than a peer-reviewed archival publication in the checked sources.


**Evaluation Limitations:**

- The benchmark covers 100 tasks, so breadth is substantial but still finite.
- Automated scoring depends on proprietary judge models.
- > The benchmark mixes English and Chinese tasks, which may confound direct language-agnostic comparisons.
- FACT evaluation depends on citation extraction and web-scraping pipelines that can fail or drift.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2506.11763


**Code Url:** https://github.com/Ayanami0730/deep_research_bench


**Dataset Url:** https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset


**Product Url:** https://deepresearch-bench.github.io/


**Leaderboard Url:** https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard


**Source Quality:** Primary with official secondary hosting


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** DeepResearch Bench II


**Components:**

- 100 benchmark tasks
- 22 research fields
- RACE evaluator
- FACT evaluator
- reference reports and adaptive criteria
- public leaderboard
- official dataset and raw report releases


**Evaluated By:**

- Human-consistency studies comparing automated scores to expert judgments.
- A public leaderboard hosted on Hugging Face.
- Availability on AGI-Eval for broader community testing.


**Evaluates:**

- deep research agents
- citation quality
- retrieval accuracy
- long-form report quality
- instruction following
- research depth
- cross-domain synthesis


**Competes With Or Complements:**

- > Complements FutureSearch's Deep Research Bench by focusing more heavily on long-form report quality and citation evaluation for 100 PhD-level tasks.
- > Directly evaluates commercial deep-research products such as OpenAI Deep Research, Gemini Deep Research, Perplexity Deep Research, and Grok Deeper Search.


#### Timeline

**Milestones:**

- 2025-06-13: arXiv paper for DeepResearch Bench was released.
- 2025-06: Project website, code repository, and leaderboard were publicly available.
- > 2025-07-15: The repository announced a major leaderboard and evaluator update with more systems and public raw outputs.
- 2025-07-18: DeepResearch Bench became available on AGI-Eval.
- 2026-02-06: The authors announced DeepResearch Bench II as a follow-up benchmark.


**Version History:**

- Initial 2025 release centered on a 100-task benchmark with RACE and FACT.
- A July 2025 update added additional deep-research systems and public raw results on the leaderboard.
- > The repository later announced continued evaluator and leaderboard maintenance beyond the original paper.


**Adoption Signals:**

- The public GitHub repository showed 733 stars and 77 forks on 2026-05-28.
- The benchmark has a public Hugging Face leaderboard.
- The project announced AGI-Eval integration for easier community evaluation.


**Supersession Notes:**

> Not superseded in the checked sources. DeepResearch Bench II is presented as a follow-up with a different evaluation focus, while the original benchmark continues to be maintained.


#### Applications

**Real World Applications:**

- Comparing deep research products and agents on complex analyst-style research tasks.
- Studying tradeoffs between retrieval quality, citation reliability, and long-form synthesis.
- Benchmarking agent architectures intended for enterprise, academic, or market research workflows.


**Users:**

- deep research agent developers
- benchmark researchers
- product teams building long-form research assistants
- academic researchers studying agent evaluation


**Deployment Constraints:**

- Requires Python 3.9+.
- Requires OpenAI or OpenRouter API access for judge-model evaluation.
- Requires a Jina API key for FACT web-scraping workflows.
- Users must run their own deep research agents and format outputs as required JSONL files.


**Cost And Runtime:**

> Evaluation depends on external API usage and the cost of the chosen judge models. The project originally highlighted Gemini 2.5 Pro Preview as a strong cost-performance judge at about $0.13 per query in its website comparison table, while benchmark runtime also depends on running the evaluated agent itself.


#### Governance And Risk

**Scientific Integrity Risks:**

- Automated judges can prefer style over substance in long reports.
- Citation-count incentives can encourage superficial source accumulation.
- Benchmarked agents may optimize for evaluator quirks instead of genuine research quality.


**Security And Safety Risks:**

- > Benchmarking requires processing web-derived content that may contain malicious or misleading material.
- Closed-source agent submissions reduce transparency into unsafe browsing or data-handling behavior.
- API-based evaluation adds operational and privacy dependencies on third-party services.


**Mitigations:**

- Expert-authored tasks and manual screening improve task quality.
- Reference-based scoring reduces reliance on purely free-form judging.
- FACT explicitly measures citation trustworthiness rather than only report fluency.
- Human-consistency studies were used to validate the automated evaluation design.


**Policy Relevance:**

> Relevant to evaluation standards for deep research systems, especially around citation reliability, automated judging, and claims about agentic research quality.


#### Uncertain Fields

- predecessors

### DeepScientist

#### Identity

**Id:** deep_scientist


**Name:** DeepScientist


**Aliases:** DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively, ResearAI DeepScientist


**Organization:** ResearAI


**First Public Release:** 2025-09-30


**Current Status:**

> Active local-first open-source AI scientist system with public repository, website, documentation, and install path.


#### Taxonomy

**Category:** end_to_end_ai_scientist


**Type:** paper, codebase, product


**Domains:** machine_learning, scientific_tasks


**Positioning:**

> Local-first autonomous research studio for long-horizon scientific discovery and paper-oriented workflows.


**Boundary Notes:**

> Included because it explicitly claims end-to-end autonomous scientific discovery over month-long timelines, not just literature assistance or code generation. It remains mainly focused on computational research tasks rather than wet-lab automation.


#### Capabilities

**Lifecycle Coverage:**

- challenge_framing
- literature_survey
- baseline_setup
- hypothesis_generation
- experiment_design
- experimentation
- analysis
- writing
- review
- frontier_progression


**Tool Access:**

- local web UI
- TUI
- connector entry points
- repository and paper inputs
- built-in runners for Codex
- built-in runners for Claude Code
- built-in runners for Kimi Code
- built-in runners for OpenCode


**Execution Environment:**

> Local-first workstation or server environment with browser access, optional local auth, and long-running project state preserved inside a per-quest repository.


**Artifact Outputs:**

- papers
- experiment traces
- notes
- figures
- reviews
- export-ready research deliverables


**Human Roles:**

> Humans provide the research goal and source materials, can take over at any time, choose deployment settings, and remain responsible for final scientific judgments, claims, and experimental results.


#### Autonomy

**Autonomy Level:** L4


**Autonomy Rationale:**

> DeepScientist claims fully autonomous, goal-oriented scientific discovery over month-long timelines with persistent memory, automated validation loops, and thousands of experiment checks, yet still keeps humans in control of initiation, oversight, and final responsibility.


**Iteration Loop:**

> Yes. The core loop combines Findings Memory, Bayesian optimization, hierarchical evaluation, baseline comparison, and repeated experiment validation to turn each result into the next search step.


**Stopping And Guardrails:**

> The project emphasizes local-first execution, human takeover at any time, optional local auth, non-root deployment guidance, and a roadmap toward stronger permission controls, reduced fabrication, and better auditability.


#### Evaluation

**Metrics:**

- about 20,000 GPU hours consumed
- about 5,000 unique scientific ideas generated
- approximately 1,100 ideas experimentally validated
- reported gains over human-designed SOTA of 183.7%, 1.9%, and 7.9% on three frontier AI tasks


**Baselines:** human-designed state-of-the-art methods, one-shot AI Scientist systems, autoresearch-style systems


**Validation Strength:**

> Public paper, repository, website, docs, and install path provide strong artifact transparency for an emerging system, but the central scientific-performance claims still need broader independent reproduction.


**Evaluation Limitations:**

> The system is emerging, benchmark/task details were only partially verified in retrieved snippets, and the high compute budget may make external replication difficult. Public claims should therefore be treated as promising but not yet fully settled.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2509.26603


**Code Url:** https://github.com/ResearAI/DeepScientist/


**Product Url:** https://deepscientist.cc/


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:**

- AI Scientist system family
- autoresearch-style systems
- Bayesian optimization for research search
- long-horizon agent memory systems


**Components:**

- Findings Memory
- Research Map
- hierarchical evaluation process
- Bayesian optimization loop
- local web interface
- TUI
- connector entry points
- Codex runner
- Claude Code runner
- Kimi Code runner
- OpenCode runner


**Evaluated By:** paper experiments on three frontier AI tasks, OpenReview / ICLR 2026 paper process


**Evaluates:**

> Not a benchmark; it aims to generate and validate scientific findings rather than score third-party systems.


**Competes With Or Complements:** The AI Scientist family, SciAgents, Google Co-Scientist, local-first autonomous research tools


#### Timeline

**Milestones:**

- 2025-09-30: arXiv preprint submitted.
- 2026-02-01: paper went live on OpenReview for ICLR 2026.
- 2026-03-24: DeepScientist officially released v1.5.
- > 2026-05-28: public repository, website, docs, npm install path, and connector references were all still visible.


**Supersession Notes:**

> No superseding replacement was verified as of 2026-05-28. The system appears active and still under development.


#### Applications

**Real World Applications:**

- ML paper reproduction
- long-horizon experiment loops
- baseline improvement for frontier AI tasks
- paper drafting and review workflows
- research project management inside a local-first workspace


**Users:** graduate students, research engineers, ML labs, teams running long computational experiment cycles


**Deployment Constraints:**

> Requires Python 3.11+, local or server compute, supported model providers or runners, careful handling of credentials and unpublished ideas, and enough compute budget for serious long-horizon experimentation.


**Cost And Runtime:**

> The paper abstract reports month-long timelines and more than 20,000 GPU hours, while the product materials advertise roughly 10-minute software setup. Practical research cost therefore ranges from light local setup to very heavy compute depending on the workload.


#### Governance And Risk

**Scientific Integrity Risks:**

> Key risks include fabricated novelty, inflated frontier claims, irreproducible large-scale experiments, and confusion between autonomous assistance and human-authored scientific accountability.


**Security And Safety Risks:**

> Long-running autonomous research agents can expose local credentials, leak unpublished ideas, or take unsafe actions through connected tools if deployment controls are weak.


**Mitigations:**

> Local-first execution, optional auth, takeover power for humans, explicit citation and disclosure guidance, non-root setup advice, and a roadmap for stronger verification and permission controls are the main public mitigations.


**Policy Relevance:**

> DeepScientist is relevant to AI-scientist governance because it operationalizes long-horizon autonomous research with explicit claims of frontier progress, raising issues around attribution, disclosure, reproducibility, and safe local deployment.


#### Uncertain Fields

- adoption_signals
- benchmarks_used
- dataset_url
- known_failure_modes
- leaderboard_url
- successors
- version_history

### DiscoveryBench

#### Identity

**Id:** discoverybench


**Name:** DiscoveryBench


**Aliases:** DiscoveryBench, DISCOVERYBENCH, DiscoveryBench: Towards Data-Driven Discovery with Large Language Models


**Organization:** Allen Institute for AI (Ai2) with OpenLocus and University of Massachusetts Amherst authors


**First Public Release:** 2024-07-01


**Current Status:**

> Active open-source benchmark, dataset, and codebase; the paper was later published at ICLR 2025, and the GitHub repository shows no packaged releases.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset, codebase


**Domains:**

- sociology
- biology
- humanities
- economics
- engineering
- meta-science


**Positioning:** Benchmark for data-driven discovery and hypothesis generation from datasets.


**Boundary Notes:**

> Included because it measures whether agents can derive dataset-supported scientific hypotheses through multistep analysis. It does not cover wet-lab execution or real-world validation of new discoveries.


#### Capabilities

**Lifecycle Coverage:**

- goal interpretation
- data loading
- data cleaning
- data integration
- feature engineering
- statistical analysis
- hypothesis generation
- workflow summarization
- evaluation


**Execution Environment:**

> Python benchmark code and datasets distributed through GitHub and Hugging Face, where agents receive dataset paths, metadata, and a natural-language discovery goal.


**Artifact Outputs:** natural-language hypotheses, workflow summaries, evaluation reports, generated analysis code


**Human Roles:**

- Humans curate DB-REAL tasks from published papers.
- Humans can optionally supply domain knowledge hints.
- Humans interpret benchmark results and compare agent outputs.


#### Autonomy

**Autonomy Level:** L2-L3


**Autonomy Rationale:**

> Tasks require multi-step autonomous workflow design, code generation, statistical analysis, and semantic reasoning over provided datasets, but humans still choose the benchmark tasks and provide the datasets. This fits bounded research-workflow autonomy rather than fully autonomous science.


**Iteration Loop:**

> Yes. Agents can iteratively propose code, inspect outputs, refine workflows, and revise hypotheses before producing a final answer.


**Stopping And Guardrails:**

- Tasks are bounded to provided datasets and metadata.
- Evaluation uses a structured hypothesis-matching metric with facet-level checks.
- Benchmark does not claim novel scientific validation beyond known published discoveries.


**Known Failure Modes:**

- Wrong or underspecified hypotheses.
- Failure to map goal terms to dataset variables.
- Skipping necessary multistep statistical analysis.
- Poor performance on long or domain-specific workflows.
- Reliance on shallow heuristics instead of full verification.


#### Evaluation

**Benchmarks Used:**

- DB-REAL with 264 tasks across 6 domains.
- DB-SYNTH with 903 synthetic tasks across 48 domains.
- Train and test split of 25 and 239 tasks for the public Hugging Face DB-REAL dataset card.


**Metrics:**

- Hypothesis Match Score (HMS) scaled from 0 to 100.
- Facet-based submetrics for context alignment, variable F1, and relationship accuracy.
- Human alignment check: HMS ranking matched annotator preference 95% of the time in the paper.
- Best reported non-oracle performance peaks at about 25%.


**Baselines:**

- CodeGen
- ReAct
- DataVoyager
- Reflexion (Oracle)
- NoDataGuess
- GPT-4o
- GPT-4-0125-preview
- Llama-3-70B


**Validation Strength:** Peer-reviewed benchmark paper at ICLR 2025, open-source code, and a public dataset card.


**Evaluation Limitations:**

- > Benchmark covers data-driven discovery from provided datasets, not wet-lab or novel experimental validation.
- Real tasks are manually derived from published papers, so coverage is broad but not exhaustive.
- Performance drops sharply with workflow length and domain-specific methods.
- > Some domain knowledge gains were measured with added hints, so pure zero-shot performance can understate assisted use cases.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2407.01725


**Code Url:** https://github.com/allenai/discoverybench


**Dataset Url:** https://huggingface.co/datasets/allenai/discoverybench


**Source Quality:**

> Primary sources: arXiv paper, ICLR/OpenReview PDF, official GitHub repository, and official Hugging Face dataset card.


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** QRData, DSBench, BLADE


**Components:**

- DB-REAL task set
- DB-SYNTH task set
- discovery agents
- evaluation scripts
- Hugging Face dataset card
- workflow metadata and answer keys


**Evaluates:** data-driven discovery, hypothesis generation, multi-step reasoning, data semantics, workflow design


#### Timeline

**Milestones:**

- 2024-07-01: arXiv preprint posted.
- 2024-07: GitHub code and benchmark release publicly referenced from the paper.
- 2025: published at ICLR 2025.
- > 2026-05-28: Hugging Face dataset card shows about 2,508 downloads in the last month and 264 rows in the public viewer.


**Version History:**

- Initial arXiv and GitHub release in 2024.
- ICLR 2025 camera-ready publication followed the initial release.
- GitHub repository reports no formal packaged releases as of 2026-05-28.


**Adoption Signals:**

- GitHub repository shows about 145 stars and 18 forks as of 2026-05-28.
- Hugging Face dataset card shows about 2,508 downloads in the last month.


**Supersession Notes:** No official replacement or v2 benchmark was identified in the primary sources.


#### Applications

**Real World Applications:**

- Evaluating agents that search for dataset-supported hypotheses.
- Studying multistep scientific data analysis behavior.
- Benchmarking open-ended discovery workflows across domains.


**Users:**

- AI research groups
- scientific discovery agent developers
- benchmark designers
- data-centric machine learning researchers


**Deployment Constraints:**

- Requires dataset access and Python-based analysis tooling.
- Some tasks need multiple datasets and domain-specific statistical methods.
- Open-ended evaluation depends on an LLM-based evaluator and benchmark metadata.


#### Governance And Risk

**Scientific Integrity Risks:**

- Overclaiming novel discovery from a benchmark based on already published findings.
- Benchmark gaming against the HMS evaluator.
- Using shallow correlations instead of domain-valid analysis workflows.


**Security And Safety Risks:**

- Executing generated analysis code over diverse datasets.
- Overreliance on LLM evaluator judgments.
- Potential misuse of open-ended data workflows without domain review.


**Mitigations:**

- Facet-based evaluation decomposes context, variables, and relationships.
- The paper reports human agreement checks for HMS.
- Tasks are grounded in published papers and provided datasets rather than unconstrained web search.


**Policy Relevance:**

> Relevant to claims about autonomous scientific discovery, benchmark validity, and safe evaluation of research agents.


#### Uncertain Fields

- competes_with_or_complements
- cost_and_runtime
- evaluated_by
- leaderboard_url
- product_url
- successors
- tool_access

### DSBench

#### Identity

**Id:** dsbench


**Name:** DSBench


**Aliases:** DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?


**Organization:** Tencent AI Lab, Seattle with University of Texas at Dallas and University of Southern California


**First Public Release:** 2024-09-12


**Current Status:**

> Active public benchmark with an arXiv paper, public repository, and ICLR 2025 acceptance; the repository also notes later reuse in OpenAI's ChatGPT agent evaluation.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, codebase


**Domains:** data science, data analysis, data modeling, tabular reasoning, competition-style spreadsheet and Kaggle workflows


**Positioning:**

> Benchmark for realistic data science agents that must analyze files, reason over multimodal context, and solve end-to-end modeling tasks.


**Boundary Notes:**

> Included because DSBench evaluates realistic data science workflows rather than narrow code completion. It covers long contexts, tables, images, data files, and full modeling pipelines with executable evaluation.


#### Capabilities

**Lifecycle Coverage:**

- task understanding
- data inspection
- multimodal context interpretation
- data analysis
- feature engineering and modeling
- code execution
- submission generation
- performance evaluation


**Tool Access:**

- local data files
- Python packages
- local shell or code execution through agent frameworks
- OpenAI Assistant Code Interpreter for one baseline
- images and tables embedded in tasks


**Execution Environment:**

> Local benchmark evaluation over repository-provided data analysis and data modeling tasks, with support for model-only baselines, AutoGen agents, and Code Interpreter-style baselines.


**Artifact Outputs:**

- question answers
- submission files
- task-level accuracy scores
- competition-level accuracy scores
- relative performance gap scores
- cost and inference-time measurements


**Human Roles:**

> Benchmark authors curate tasks and evaluation scripts. Users install dependencies, configure APIs or model frameworks, run the benchmark, and interpret the reported scores.


#### Autonomy

**Autonomy Rationale:**

> DSBench evaluates both plain models and tool-using agents, but all systems stay within fixed benchmark tasks, fixed data files, and executable evaluation scripts rather than acting autonomously in the open world.


**Iteration Loop:**

> Agent baselines such as AutoGen revise code over multiple turns and rerun analyses, while model-only baselines operate in more limited bounded interactions.


**Stopping And Guardrails:**

> The benchmark constrains work through predefined tasks, executable evaluation, local file-based inputs, explicit environment setup, and a non-commercial-use disclaimer for the released dataset.


**Known Failure Modes:**

- misunderstanding long or multimodal task context
- failing to identify the right tables or files
- producing invalid submission files for modeling tasks
- high cost or long runtime for stronger agent baselines
- weak performance on harder or newer competition tasks


#### Evaluation

**Benchmarks Used:** DSBench itself across 466 data-analysis tasks and 74 data-modeling tasks.


**Metrics:**

- task-level accuracy for data analysis
- competition-level accuracy for data analysis
- task success rate for data modeling
- Relative Performance Gap (RPG) for data modeling
- cost
- inference time


**Baselines:**

- > model-only baselines including LLaVA, Llama 3, GPT-3.5, GPT-4, GPT-4o, GPT-4o mini, Claude, and Gemini
- AutoGen-based agents
- OpenAI Code Interpreter baselines
- human baseline


**Validation Strength:**

> Peer-reviewed benchmark with public code, executable evaluation, quantitative baselines, and human comparison.


**Evaluation Limitations:**

> Data-modeling tasks use an internal 8:2 train-test split because original Kaggle test labels are inaccessible. Data-analysis correctness relies on semantic comparison with an LLM-based judge, and the benchmark is limited to tasks sourced from ModelOff and Kaggle-style competitions.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2409.07703


**Code Url:** https://github.com/LiqiangJing/DSBench


**Dataset Url:** https://github.com/LiqiangJing/DSBench


**Product Url:** https://liqiangjing.github.io/dsbench.github.io/


**Source Quality:** Primary sources: official arXiv paper and official GitHub repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- 466 data-analysis tasks
- 74 data-modeling tasks
- ModelOff-derived analysis set
- Kaggle-derived modeling set
- executable evaluation scripts
- Relative Performance Gap metric
- AutoGen baseline setup
- Code Interpreter baseline setup
- data_analysis and data_modeling task directories


**Evaluates:** data science, data analysis, data modeling, spreadsheet and Kaggle-style task solving, multimodal file-based reasoning


**Competes With Or Complements:** DiscoveryBench, MLE-bench, MLAgentBench, DS-1000, DSEval


#### Timeline

**Milestones:**

- 2024-09-12: arXiv v1 released.
- 2025-01-22: repository announced ICLR 2025 acceptance.
- 2025-02-22: arXiv v2 released.
- 2025-04-11: arXiv v3 released.
- 2025-07-17: repository noted use in OpenAI's ChatGPT agent evaluation.


**Version History:**

- arXiv v1 on 2024-09-12
- arXiv v2 on 2025-02-22
- arXiv v3 on 2025-04-11
- public repository continues to host benchmark code, task data, and evaluation instructions


**Adoption Signals:**

- 117 GitHub stars at verification time
- ICLR 2025 acceptance
- public repository
- later reuse in OpenAI's ChatGPT agent evaluation as noted by the repository


**Supersession Notes:** No supersession was identified in the consulted primary sources.


#### Applications

**Real World Applications:**

- benchmarking autonomous data science agents
- testing multimodal spreadsheet and table reasoning
- evaluating end-to-end model-building assistants
- comparing agent frameworks for Kaggle-like workflows


**Users:** data-science agent researchers, benchmark designers, AI systems researchers, developers of notebook and analytics agents


**Deployment Constraints:**

> Requires local benchmark setup, Python dependencies, access to task files, and possibly API-based model frameworks such as AutoGen or Code Interpreter-style baselines. The dataset is released for research and educational use only.


#### Governance And Risk

**Scientific Integrity Risks:**

- benchmark overfitting to public competition tasks
- data leakage from well-known Kaggle or ModelOff tasks
- judge errors in semantic evaluation for data-analysis answers
- overgeneralizing benchmark performance to all real-world data science


**Security And Safety Risks:**

- agent frameworks may execute generated code locally
- uploaded data to hosted code-interpreter tools may raise privacy concerns
- competition data licensing or compliance issues if reused outside the benchmark rules


**Mitigations:**

- executable evaluation scripts
- explicit benchmark task definitions
- held-out split creation for modeling tasks
- public baseline reporting
- non-commercial-use and compliance disclaimers in the repository


**Policy Relevance:**

> DSBench is relevant to governance of code-executing agents because it measures realistic data-centric work with files, tables, and modeling loops rather than toy code tasks, helping clarify current limits of practical data science automation.


#### Uncertain Fields

- autonomy_level
- cost_and_runtime
- evaluated_by
- leaderboard_url
- predecessors
- successors

### Elicit

#### Identity

**Id:** elicit


**Name:** Elicit


**Aliases:** Elicit AI, Elicit Systematic Review


**Organization:** Elicit


**First Public Release:** 2021-08-31


**Current Status:**

> Active commercial research product with web app, enterprise systematic-review workflows, and a public API.


#### Taxonomy

**Category:** literature_review_product


**Type:** product, infrastructure


**Domains:** general_academic_research, systematic_reviews


**Positioning:**

> An AI research assistant and literature-review platform focused on paper search, evidence extraction, and synthesis.


**Boundary Notes:**

> Included because Elicit directly supports literature review and systematic review workflows that are central to AI-assisted scientific research, even though it is not a full end-to-end autonomous scientist.


#### Capabilities

**Lifecycle Coverage:**

- paper_search
- screening
- data_extraction
- literature_synthesis
- report_generation
- monitoring_new_literature


**Tool Access:**

- Search over Elicit corpus
- PubMed search
- ClinicalTrials search
- PDF and full-text screening
- Structured extraction tables
- Report generation
- API for reports and systematic reviews


**Execution Environment:** Hosted Elicit product and API-backed long-running report or systematic-review jobs.


**Artifact Outputs:**

- Paper lists
- Screening recommendations
- Extraction tables
- Sentence-level citations and quotes
- Systematic review reports
- Saved libraries and alerts


**Human Roles:**

- Researchers define the research question and review scope
- Users inspect and override screening decisions
- Users verify extracted data against source quotes, tables, or figures
- Teams can use Elicit as one reviewer or a second reviewer in dual-review workflows


#### Autonomy

**Autonomy Level:** L1


**Autonomy Rationale:**

> Elicit automates bounded parts of literature and systematic-review workflows, but the user still defines the protocol, reviews or overrides key screening and extraction outputs, and owns the final research judgment.


**Iteration Loop:**

> Limited and workflow-bounded. Elicit can search, screen, extract, and synthesize within a configured review pipeline, but it is not presented as an open-ended autonomous agent that independently broadens its mission.


**Stopping And Guardrails:**

> Systematic-review workflows are structured around explicit criteria, extraction questions, citation-backed verification, plan-specific limits, and user review of outputs. Enterprise gating and plan limits constrain the most advanced workflow stages.


**Known Failure Modes:**

> Official evaluations note that misses can arise from poorly generated screening criteria, search recall limits, extraction errors, and the difficulty of exactly reproducing heterogeneous published systematic reviews.


#### Evaluation

**Benchmarks Used:**

- Internal and external systematic-review evaluations reported by Elicit
- Cochrane-review replication-style evaluations
- AstaBench literature understanding tasks such as ScholarQA-CS2


**Metrics:**

- Search recall
- Abstract-screening sensitivity and specificity
- Full-text-screening sensitivity and specificity
- Extraction accuracy
- Time savings
- Hallucination rate in extraction and report workflows


**Baselines:**

- Published systematic reviews
- Manual human extraction gold standards
- Independent external evaluation teams
- Consensus search engine as an irrelevant-paper source in one evaluation
- Other literature tools evaluated in AstaBench


**Validation Strength:**

> Benchmarked and externally case-studied, with product-specific evaluations reported by the company and evidence of use by research organizations.


**Evaluation Limitations:**

> Elicit notes that published reviews are heterogeneous and not always reproducible from the paper alone, so exact replication is difficult. Some evaluation claims come from company-run studies or partner case studies rather than peer-reviewed product papers.


#### Links And Provenance

**Product Url:** https://elicit.com/


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- Paper Search
- Systematic Review
- Screening
- Data Extraction
- Reports
- Library
- Alerts
- API
- Research Agents


**Evaluated By:** AstaBench literature tasks


**Competes With Or Complements:** Consensus, Asta Scholar QA, SciSpace Deep Review, OpenAI Deep Research, Perplexity


#### Timeline

**Milestones:**

- 2021-08-31: Elicit first launched its literature-review workflow.
- 2024-02-28: Elicit reported it had been launching user-facing features weekly since September 2021.
- 2025-02: Elicit introduced Systematic Review workflows.
- 2025-03-18: Elicit published an evaluation of its Systematic Review workflow.
- 2026-03-03: Elicit introduced the public API.
- > 2026-05-06: Elicit announced PRISMA 2020 support and published larger-scale systematic-review evaluation results.


**Version History:**

- Started as a literature-review workflow in 2021.
- Expanded into structured reports and systematic-review workflows in 2024-2025.
- Added keyword search, clinical-trials coverage, research agents, and API access in 2025-2026.
- Current systematic-review workflow supports PRISMA 2020-oriented documentation and dual review.


**Adoption Signals:**

- Elicit says it is trusted by top research institutions.
- The company reported over 200,000 monthly users by early 2024.
- Public case studies include Formation Bio, VDI/VDE, and Oxford PharmaGenesis.
- The API exposes reports and systematic-review workflows for programmatic use.


**Supersession Notes:**

> Not superseded. The product is expanding from literature review into systematic-review, API, and broader research-agent workflows.


#### Applications

**Real World Applications:**

- Academic literature review
- Systematic reviews
- Evidence synthesis for policy briefs
- Clinical and pharma landscape reviews
- Structured extraction from many papers
- Monitoring new literature with alerts


**Users:**

- Academic researchers
- Systematic-review specialists
- Policy researchers
- Pharma and medtech teams
- Research operations teams
- Students


**Deployment Constraints:**

- Advanced systematic-review workflow availability depends on plan tier
- The systematic-review API requires Enterprise
- Plan limits cap columns and search results
- Figure extraction is not available on all plans
- Long-running jobs require polling or watching progress in the product


**Cost And Runtime:**

> API reports are asynchronous jobs that typically take 5 to 15 minutes. Systematic reviews are long-running and plan-limited, with higher tiers supporting up to 40,000 titles, abstracts, and full texts per review.


#### Governance And Risk

**Scientific Integrity Risks:**

- Missed relevant studies due to imperfect recall
- Improperly generated screening criteria
- Extraction errors or hallucinated synthesis
- Over-reliance on AI recommendations without human verification
- Difficulty reproducing published reviews exactly


**Security And Safety Risks:**

- Exposure of sensitive unpublished materials if uploaded carelessly
- Misuse of automated evidence synthesis in high-stakes decisions without review
- Incorrect extraction propagating into downstream policy or clinical work


**Mitigations:**

- Sentence-level citations and supporting quotes
- Traceable and auditable extraction workflow
- Editable screening and extraction criteria
- Dual-review support
- Explicit plan limits and staged workflow structure


**Policy Relevance:**

> Relevant to evidence-synthesis governance, reproducibility standards such as PRISMA 2020, responsible use of AI in policy and health research, and human-verification expectations for literature-review automation.


### FutureHouse Platform Agents

#### Identity

**Id:** futurehouse_platform_agents


**Name:** FutureHouse Platform Agents


**Aliases:** FutureHouse Platform, FutureHouse Platform: Superintelligent AI Agents for Scientific Discovery


**Organization:** FutureHouse


**First Public Release:** 2025-05-01


**Current Status:** Active public science product suite with web interface and API


#### Taxonomy

**Category:** science_product_suite


**Type:** product, agent_suite


**Domains:** biology, chemistry, biomedicine


**Positioning:** Scientific agent platform


**Boundary Notes:**

> Included because it offers a suite of specialized agents for literature search, synthesis, chemistry planning, and data analysis through a product platform. It is broader than a single research assistant and narrower than a fully autonomous end-to-end scientist.


#### Capabilities

**Lifecycle Coverage:** literature_search, literature_synthesis, research_gap_analysis, chemistry_planning, data_analysis


**Tool Access:**

- web interface
- API
- open-access paper corpus
- specialized scientific databases including OpenTargets
- specialized chemistry tools


**Execution Environment:** Product-hosted environment accessible through a web interface and API


**Artifact Outputs:** scholarly answers, deep literature reviews, prior-art checks, chemistry experiment plans, data-analysis outputs


**Human Roles:**

> Researchers choose the agent, provide the scientific question, interpret results, and decide whether to act on outputs. Downstream experiments and scientific decisions remain human responsibilities.


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> The platform automates specialized research subtasks with strong retrieval and synthesis capabilities, but it does not independently run a full closed-loop discovery process without user orchestration or later composition into a system such as Robin.


**Iteration Loop:**

> Limited. Individual agents support iterative querying and source review, and the platform can be chained by users, but the launch announcement does not present a fully autonomous end-to-end research loop.


**Stopping And Guardrails:**

> Guardrails described in the launch materials include transparent reasoning, source-quality evaluation, human-facing delivery through a web interface and API, and an explicit warning that Phoenix is experimental and may make more mistakes.


**Known Failure Modes:**

- literature retrieval mistakes
- incorrect synthesis or gap analysis
- unsafe or weak chemistry planning
- overreliance on platform outputs without experimental review


#### Evaluation

**Benchmarks Used:**

- LitQA precision and accuracy comparisons
- head-to-head literature search tasks against PhD-level researchers
- retrieval precision and accuracy comparisons against frontier search models


**Metrics:** retrieval precision, accuracy, head-to-head literature search precision versus PhD-level researchers


**Baselines:** major frontier search models with a search tool, PhD-level researchers in literature search tasks


**Validation Strength:** Benchmarked and experimentally validated


**Evaluation Limitations:**

> The launch post states that Phoenix is less deeply benchmarked than the other agents, and the reviewed sources do not provide a single unified benchmark covering every agent in the suite.


#### Links And Provenance

**Product Url:** https://www.futurehouse.org/research-announcements/launching-futurehouse-platform-ai-agents


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** Robin


**Components:** Crow, Falcon, Owl, Phoenix, Finch


**Evaluated By:** LitQA-style evaluation, retrieval precision and accuracy comparisons, head-to-head literature search tasks


**Evaluates:** Not a benchmark; it does not primarily evaluate other systems.


#### Timeline

**Milestones:**

- 2025-05-01: FutureHouse platform launch announcement published
- 2025-05-01: public web interface and API announced
- > 2025-05-20: Robin announcement described Crow, Falcon, Owl, Phoenix, and Finch as specialized agents feeding a unified workflow


**Adoption Signals:**

- Public launch with free access via web interface at announcement time
- API availability announced for researcher workflows
- FutureHouse positioned the suite as publicly available to scientists everywhere


**Supersession Notes:**

> Not superseded in the reviewed primary sources. Robin is presented as a downstream orchestration of specialized platform agents rather than a replacement for the suite.


#### Applications

**Real World Applications:**

- scientific literature search
- deep literature review and synthesis
- prior-art checking
- chemistry experiment planning
- scientific data analysis


**Users:** academic researchers, biomedical scientists, chemists, R&D teams


**Deployment Constraints:**

- platform account access
- API integration for programmatic use
- dependence on FutureHouse-hosted infrastructure
- human review for chemistry and downstream experimental decisions


#### Governance And Risk

**Scientific Integrity Risks:**

- incorrect literature synthesis at scale
- source-quality errors that shape scientific conclusions
- benchmark overclaiming from narrow task coverage


**Security And Safety Risks:**

- chemistry-planning misuse
- unsafe downstream action on unverified agent advice
- platform concentration risk if users overtrust hosted agents


**Mitigations:**

- transparent reasoning visible to users
- source-quality evaluation methods
- benchmarking against frontier models and human experts
- explicit warning that Phoenix is experimental


**Policy Relevance:**

> The platform is relevant to governance because it operationalizes high-capability scientific agents behind a hosted interface and API, raising issues around access control, evidence standards, chemical dual use, and responsible deployment.


#### Uncertain Fields

- code_url
- competes_with_or_complements
- cost_and_runtime
- dataset_url
- leaderboard_url
- paper_url
- predecessors
- version_history

### MLAgentBench

#### Identity

**Id:** mlagentbench


**Name:** MLAgentBench


**Aliases:** MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation


**Organization:** Stanford SNAP


**First Public Release:** 2023-10-05


**Current Status:** Active public benchmark with an arXiv paper and open-source repository.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, codebase


**Domains:** machine learning experimentation, ML engineering, agentic code execution, model improvement


**Positioning:** Benchmark for end-to-end machine learning experimentation by language agents.


**Boundary Notes:**

> Included because it evaluates autonomous ML experimentation across data, modeling, training, and analysis loops. It is broader than a generic coding benchmark because the goal is to improve ML models through iterative experimentation.


#### Capabilities

**Lifecycle Coverage:**

- experiment design
- code writing
- code execution
- result analysis
- model improvement
- long-term planning evaluation


**Tool Access:**

- file read and write
- code execution
- output inspection
- interactive task environments
- Docker
- Kaggle API for some tasks
- LLM API keys


**Execution Environment:**

> Interactive task environments that resemble human research workflows. The repository supports local execution and Docker, and tasks may require dataset preparation and repeated experiment runs.


**Artifact Outputs:**

- improved model submissions
- experiment logs
- success-rate metrics
- improvement-over-baseline metrics
- agent plans and traces


**Human Roles:**

> Benchmark creators define tasks and starter code. Users configure dependencies, provide API keys, accept competition rules where required, run agents, and review experimental outputs.


#### Autonomy

**Autonomy Rationale:**

> MLAgentBench targets agents that autonomously run ML experiments and improve models, but within bounded tasks, starter code, user-provided infrastructure, and explicit evaluation scripts.


**Iteration Loop:**

> Iterative ML experimentation is central to the benchmark: agents read and write files, run experiments, inspect outputs, and revise approaches over multiple steps.


**Stopping And Guardrails:**

> The repository recommends Docker because agents modify and execute files. Tasks require explicit environment setup, API credentials, and Kaggle authentication for some datasets.


**Known Failure Modes:**

- weak long-term planning
- hallucination during experimentation
- poor transfer to recent Kaggle challenges
- environment and setup failures
- uneven success across tasks


#### Evaluation

**Benchmarks Used:** MLAgentBench itself across 13 ML engineering tasks.


**Metrics:** success rate, improvement over the starter-code baseline, valid submission rate


**Baselines:**

- Claude v1.0 agent
- Claude v2.1 agent
- Claude v3 Opus agent
- GPT-4 agent
- GPT-4-turbo agent
- Gemini-Pro agent
- Mixtral agent
- starter-code baseline


**Validation Strength:** Benchmarked with public tasks, a public paper, and repository-reported quantitative results.


**Evaluation Limitations:**

> Performance varies widely across tasks, from strong results on older datasets to 0% on some recent Kaggle challenges, so benchmark scores depend heavily on task recency and environment setup.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2310.03302


**Code Url:** https://github.com/snap-stanford/MLAgentBench


**Product Url:** https://github.com/snap-stanford/MLAgentBench


**Source Quality:** Primary sources: official arXiv paper and official Stanford SNAP repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** MLE-bench


**Components:**

- 13 ML engineering tasks
- starter code
- interactive task environments
- ReAct-based reference agent
- Docker image
- task preparation scripts
- evaluation scripts


**Evaluates:** ML experimentation, code execution, model improvement, long-term planning


**Competes With Or Complements:** AIRS-Bench, MLE-bench


#### Timeline

**Milestones:**

- 2023-10-05: arXiv v1 released.
- 2024-04-14: arXiv v2 released.
- Public repository released with setup instructions, Docker guidance, and benchmark scripts.


**Version History:**

- arXiv v1 on 2023-10-05
- arXiv v2 on 2024-04-14
- the public repository continues to host setup, task preparation, and evaluation workflows


**Adoption Signals:** Public arXiv paper, Public GitHub repository, Public log repository is linked from the official repository


#### Applications

**Real World Applications:**

- benchmarking agentic ML research assistants
- testing autonomous model-improvement workflows
- studying iterative experiment planning and execution
- comparing language models on ML engineering tasks


**Users:** ML agent researchers, benchmark designers, AI systems researchers, autonomous experimentation developers


**Deployment Constraints:**

> Requires Python 3.10, benchmark dependencies, code-execution permissions, possible Docker usage, Kaggle authentication for some tasks, and API keys for supported models.


#### Governance And Risk

**Scientific Integrity Risks:**

- benchmark overfitting
- training-data leakage on public tasks
- misleading comparisons when environment setup differs
- overgeneralizing from 13 tasks to all ML research


**Security And Safety Risks:**

- agents modify and execute code
- external data downloads and Kaggle access increase operational risk
- API-key handling and container isolation must be managed carefully


**Mitigations:**

- Docker and sandbox recommendation
- explicit setup instructions
- starter-code baselines
- public logs and scripts for inspection


**Policy Relevance:**

> Relevant to evaluation of autonomous experimentation systems, reproducibility of agent benchmarks, and governance of code-executing research agents.


#### Uncertain Fields

- autonomy_level
- cost_and_runtime
- dataset_url
- evaluated_by
- leaderboard_url
- predecessors
- supersession_notes

### MLE-bench

#### Identity

**Id:** mle_bench


**Name:** MLE-bench


**Aliases:** MLE-bench, MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering


**Organization:** OpenAI


**First Public Release:** 2024-10-09


**Current Status:**

> Active open-source benchmark and codebase; the public leaderboard remains visible, but new leaderboard submissions were paused on 2026-04-24 while the maintainers work on a fairer comparison process.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, codebase


**Domains:** machine learning engineering, Kaggle-style competitions, applied machine learning


**Positioning:** Benchmark for evaluating AI agents on end-to-end machine learning engineering competition tasks.


**Boundary Notes:**

> Included because it evaluates autonomous ML engineering work such as data preparation, model training, experiment execution, and benchmark grading. It is not a general research assistant or wet-lab scientist system.


#### Capabilities

**Tool Access:** shell, Python execution, Docker environment, benchmark grading server, Kaggle-style datasets


**Execution Environment:**

> Benchmark-hosted ML engineering environment executed through the MLE-bench codebase, typically in a Linux Docker setup with benchmark-provided datasets and grading tools.


**Artifact Outputs:** competition submissions, grading reports, agent run logs, leaderboard scores


**Human Roles:**

- Humans choose the agent, model, and resource settings.
- Humans review leaderboard submissions and grading reports.
- Humans interpret benchmark results and fairness caveats.


#### Autonomy

**Autonomy Level:** L2-L3


**Autonomy Rationale:**

> Tasks require multi-step autonomous coding, data preparation, model training, and experiment iteration over long runtimes, but humans still choose goals, resources, and submission settings. The benchmark measures substantial bounded autonomy rather than fully self-directed research.


**Iteration Loop:**

> Yes. Agents can iteratively train models, inspect results, revise code, and resubmit within the allowed runtime.


**Stopping And Guardrails:**

- Canonical benchmark settings use a 24-hour runtime, 36 vCPUs, 440 GB RAM, and one 24 GB A10 GPU.
- Benchmark code provides a grading server and structured submission workflow.
- Agents run inside a provided Docker-based environment.
- Competition rules must be accepted before some local tests run.


**Known Failure Modes:**

- Benchmark contamination from pre-training on public Kaggle material.
- Benchmark overfitting to specific competitions or leaderboard quirks.
- Rule violations or plagiarism in generated submissions.
- High variance across seeds and resource settings.
- Known issues in some benchmark competitions pending a future v2 release.


#### Evaluation

**Benchmarks Used:**

- 75 Kaggle competitions in the full benchmark.
- Low, Medium, High, and All splits in the official evaluation setup.
- Human baselines derived from public Kaggle leaderboards.


**Metrics:**

- Any Medal (%) reported across Low, Medium, High, and All splits.
- Mean plus standard error across repeated runs.
- > Paper headline result: bronze-medal-or-better performance in 16.9% of competitions for the best reported setup.


**Baselines:**

- AIDE with o1-preview.
- AIDE with gpt-4o-2024-08-06.
- AIDE with claude-3-5-sonnet-20240620.
- OpenHands with gpt-4o-2024-08-06.
- MLAB with gpt-4o-2024-08-06.
- Human comparison via public Kaggle leaderboards.


**Evaluation Limitations:**

- Full evaluation is expensive and data-heavy: about 3.3 TB across 75 competitions.
- Performance is sensitive to runtime and compute budgets.
- The authors explicitly study contamination risk from pre-training.
- The repository documents known competition issues and plans a batched v2 fix release.
- As of 2026-04-24, leaderboard submissions are paused while fairness and comparability are revised.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2410.07095


**Code Url:** https://github.com/openai/mle-bench/


**Product Url:** https://openai.com/index/mle-bench/


**Leaderboard Url:** https://github.com/openai/mle-bench/#leaderboard


**Source Quality:** Primary sources: arXiv paper, official OpenAI page, and official GitHub repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** Planned MLE-bench v2 release on openai/frontier-evals.


**Components:**

- 75-competition benchmark dataset
- Low-complexity Lite split of 22 competitions
- Docker base environment
- grading server
- leaderboard aggregation scripts
- rule-violation detector
- plagiarism detector
- evaluated agent implementations


**Evaluated By:** Community leaderboard submissions in the official repository.


**Evaluates:**

- ML engineering
- Kaggle-style competition performance
- agent scaffolds
- resource scaling behavior
- pre-training contamination sensitivity


**Competes With Or Complements:** PaperBench, CORE-Bench, DiscoveryBench


#### Timeline

**Milestones:**

- 2024-10-09: arXiv preprint submitted.
- 2024-10-10: official OpenAI research page published.
- 2025-02-26: arXiv v6 released.
- 2026-04-24: leaderboard paused for new submissions pending a fairer comparison process.


**Version History:**

- v1 benchmark released with the paper and GitHub repository in October 2024.
- Repository notes a planned v2 release on openai/frontier-evals with versioned leaderboard results.


**Adoption Signals:**

- GitHub repository shows about 1.5k stars and 249 forks as of 2026-05-28.
- Multiple external agent submissions appear on the public leaderboard.


**Supersession Notes:**

> The benchmark is still active, but the repository signals a future v2 with batched competition fixes and explicit leaderboard versioning.


#### Applications

**Real World Applications:**

- Evaluating autonomous ML engineering agents.
- Comparing scaffold and model choices for Kaggle-style workflows.
- Stress-testing long-horizon coding agents on realistic ML tasks.


**Users:** Agent researchers, ML engineers, benchmark designers, foundation model evaluation teams


**Deployment Constraints:**

- Full benchmark evaluation is storage- and compute-intensive.
- Canonical setup assumes Linux amd64 Docker support.
- Some runs require GPU access.
- Fair comparison depends on reporting runtime, hardware, seeds, and grading reports.


**Cost And Runtime:**

> The canonical benchmark uses 24 hours per run. The Low split reduces total dataset size to about 158 GB, while the full 75-competition benchmark is about 3.3 TB and is explicitly described as expensive.


#### Governance And Risk

**Scientific Integrity Risks:**

- Benchmark gaming against public leaderboards.
- Plagiarism or leakage from public competition artifacts.
- Contamination from model pre-training on benchmark-relevant materials.
- Overinterpreting leaderboard gains as general scientific autonomy.


**Security And Safety Risks:**

- Executing agent-written code in a heavy ML environment.
- Potential misuse of external compute or data resources.
- Unsafe shell or package installation behavior inside benchmark runs.


**Mitigations:**

- Docker-based execution environment.
- Leaderboard submission review and grading report requirements.
- Included rule-violation and plagiarism detectors.
- Explicit reporting of hardware, runtime, seeds, and split-specific scores.


**Policy Relevance:**

> Relevant to frontier-model evaluation, benchmark governance, contamination auditing, and claims about autonomous ML engineering capability.


#### Uncertain Fields

- dataset_url
- lifecycle_coverage
- predecessors
- validation_strength

### MMDeepResearch-Bench

#### Identity

**Id:** mmdeepresearch_bench


**Name:** MMDeepResearch-Bench


**Aliases:** MMDeepResearch-Bench, MMDR-Bench, MMDeepResearch-Bench: A Benchmark for Multimodal Deep Research Agents


**First Public Release:** 2026-01


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark


**Domains:** multimodal deep research, image-text evidence synthesis, long-form report generation, general research


**Positioning:**

> Benchmark for evaluating deep research agents that must retrieve, reason over, and cite multimodal evidence in long-form reports.


**Boundary Notes:**

> Included because it extends text-oriented deep-research evaluation to multimodal evidence, which is central for scientific and technical research reports using figures, charts, images, and documents.


#### Capabilities

**Lifecycle Coverage:**

- research question analysis
- multimodal retrieval
- image and document evidence use
- citation grounding
- long-form report synthesis
- report integrity evaluation


**Execution Environment:**

> Benchmark of multimodal deep-research tasks described in arXiv and mirrored on Hugging Face paper pages.


**Artifact Outputs:** long-form research reports, citations, multimodal evidence references, evaluation scores


**Human Roles:**

- Humans define research tasks and expected multimodal evidence criteria.
- Humans inspect report quality and benchmark failures.
- Judge-model outputs require human sanity checks for high-stakes use.


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> The benchmark evaluates agents that perform multi-step retrieval and synthesis, but tasks remain predefined and validation is benchmark-based rather than real-world scientific validation.


**Stopping And Guardrails:**

- Tasks are bounded to benchmark prompts.
- Reports are evaluated with multimodal evidence and citation-quality metrics.
- Judge-model grading should be audited for critical claims.


**Known Failure Modes:**

- Citing sources that do not support the visual claim.
- Ignoring images, figures, or charts despite their relevance.
- Hallucinating evidence in long-form reports.
- Weak cross-modal reasoning.
- Overreliance on text snippets when visual evidence is decisive.


#### Evaluation

**Benchmarks Used:** MMDeepResearch-Bench / MMDR-Bench


**Validation Strength:**

> Primary arXiv paper and Hugging Face paper metadata; code, data release, and leaderboard were not verified.


**Evaluation Limitations:**

- Recent benchmark with limited independent replication.
- Judge-model evaluation can inherit model biases.
- Exact code/data availability was not verified.
- Multimodal evidence grading is difficult to audit at scale.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2601.12346


**Source Quality:**

> Primary arXiv paper plus Hugging Face paper metadata; some metric details cross-checked from secondary benchmark summaries.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:** multimodal research tasks, long-form report evaluation, citation grounding checks, visual evidence scoring


**Evaluates:** multimodal deep research, image-text evidence use, citation grounding, report integrity, retrieval effectiveness


**Competes With Or Complements:** DeepResearch Bench, Deep Research Bench / RetroSearch, AstaBench, MMMU


#### Timeline

**Milestones:**

- 2026-01: arXiv preprint posted.
- 2026: Hugging Face paper page indexed the benchmark.
- 2026-05-28: paper source verified.


**Supersession Notes:** No official successor or replacement was identified.


#### Applications

**Real World Applications:**

- Evaluating research agents that need to analyze figures, charts, screenshots, and documents.
- Testing citation-grounded multimodal report generation.
- Studying failure modes in visual evidence use.


**Users:**

- deep research agent developers
- multimodal model evaluation teams
- scientific and technical report automation teams
- AI safety and hallucination evaluation researchers


**Deployment Constraints:**

- Requires multimodal model access.
- Requires retrieval over image-rich sources and citation tracking.
- Needs careful judge-model calibration and human review for high-stakes settings.


#### Governance And Risk

**Scientific Integrity Risks:**

- False visual evidence claims.
- Citations that support text but not image-derived conclusions.
- Long-form reports masking unsupported claims.
- Benchmark scores overstating reliability in real scientific workflows.


**Security And Safety Risks:**

- Automated browsing and retrieval over untrusted media.
- Misinterpretation of scientific images or charts.
- Use in high-stakes research without expert review.


**Mitigations:**

- Require source-level provenance for each visual claim.
- Audit judge-model scores with human reviewers.
- Separate retrieval, visual interpretation, and synthesis scores.
- Retain screenshots or source snapshots for reproducibility.


**Policy Relevance:**

> Relevant to responsible deployment of deep research agents, citation integrity, and evaluation of multimodal evidence claims.


#### Uncertain Fields

- adoption_signals
- baselines
- code_url
- cost_and_runtime
- current_status
- dataset_url
- evaluated_by
- iteration_loop
- leaderboard_url
- metrics
- organization
- predecessors
- product_url
- successors
- tool_access
- version_history

### OpenAI Deep Research

#### Identity

**Id:** openai_deep_research


**Name:** OpenAI Deep Research


**Aliases:** Deep research, ChatGPT deep research, o3-deep-research


**Organization:** OpenAI


**First Public Release:** 2025-02-02


**Current Status:**

> Active; available in ChatGPT on select plans and countries, available via API, and partially extended through ChatGPT agent capabilities.


#### Taxonomy

**Category:** deep_research_product


**Type:** product, infrastructure


**Domains:** finance, science, policy, engineering, general_research


**Positioning:**

> An agentic deep-research product for multi-step web research, source analysis, and citation-grounded report generation.


**Boundary Notes:**

> Included because OpenAI positions deep research as a research-focused agent that plans and executes multi-step evidence gathering, rather than as a generic chat feature.


#### Capabilities

**Lifecycle Coverage:** web_search, source_analysis, citation_grounded_report_generation, data_analysis, file_analysis


**Tool Access:**

- Public web search
- Specific-site restriction or prioritization
- Uploaded file analysis
- Connected ChatGPT apps
- MCP data sources
- Python data analysis in a sandbox
- API background mode and webhooks


**Execution Environment:**

> ChatGPT-hosted deep research workflow and OpenAI API deep-research models using long-running background execution.


**Artifact Outputs:**

- Structured cited reports
- Source lists and links
- Activity history
- Downloaded Markdown, Word, or PDF reports
- Graphs or images embedded in reports


**Human Roles:**

- Users define the research task and desired outcome
- Users choose or constrain sources before execution
- Users can review and modify the proposed research plan
- Users can interrupt and redirect the run
- Admins control access in Enterprise and Edu workspaces


#### Autonomy

**Autonomy Level:** L2


**Autonomy Rationale:**

> Deep research autonomously plans and executes multi-step browsing and analysis, but the human still chooses goals, controls sources, can edit the plan, and must verify or act on the output.


**Iteration Loop:**

> Yes. The product proposes a plan, refines searches across sources, and iterates during long-running research tasks; follow-up prompts can extend or redirect the analysis.


**Stopping And Guardrails:**

> Users stay in control through source selection, plan review, live progress, and interruption. OpenAI also applies safety training, blocklists, privacy protections, sandboxed Python execution, enterprise controls, and API limits such as max tool calls.


**Known Failure Modes:**

> OpenAI documents risks around hallucinated capabilities, privacy-sensitive aggregation of public information, prompt injection from browsed content, unsafe or regulated advice, bias, and residual hallucination despite source grounding.


#### Evaluation

**Benchmarks Used:**

- Humanity's Last Exam
- GAIA
- OpenAI deep research safety evaluations
- StrongReject jailbreak evaluation
- PersonQA hallucination evaluation
- Preparedness evaluations


**Metrics:**

- Accuracy on public benchmarks
- Citation quality and source grounding
- Task completion quality
- Safety refusal performance
- Hallucination rate
- Preparedness risk level


**Baselines:**

- GPT-4o
- OpenAI o1
- o3-mini
- Claude 3.5 Sonnet
- Gemini Thinking
- DeepSeek-R1
- Previous GAIA SOTA systems


**Validation Strength:**

> Benchmarked on public evaluations, accompanied by an official system card and safety testing, but not presented as a peer-reviewed scientific product paper.


**Evaluation Limitations:**

> OpenAI notes that preparedness evaluations are a lower bound on capability, performance can vary with system prompts and scaffolding, and live-web behavior creates contamination and prompt-injection challenges that are hard to exhaustively measure.


#### Links And Provenance

**Product Url:** https://openai.com/index/introducing-deep-research/


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** ChatGPT agent deep research mode


**Components:**

- ChatGPT deep research
- o3-deep-research API model
- Web search
- Connected apps
- MCP support
- Sandboxed Python analysis
- Background mode
- Webhooks


**Evaluated By:** Humanity's Last Exam, GAIA, OpenAI system card safety and preparedness evaluations


**Competes With Or Complements:** Asta, Elicit, Perplexity, Google Deep Research-style products, ChatGPT search


#### Timeline

**Milestones:**

- 2025-02-02: OpenAI launched deep research in ChatGPT.
- 2025-02-25: availability expanded to Plus users.
- 2025-04-24: higher usage limits and a lightweight version powered by o4-mini were announced.
- > 2025-07-17: visual-browser access was added as part of ChatGPT agent while the original deep research mode remained available.
- > 2026-02-10: MCP and app connectivity, trusted-site restriction, and real-time progress refinements were announced.


**Version History:**

- Initial ChatGPT-only deep research launch in February 2025.
- Later rollout to more plans and countries.
- Lightweight deep research variant added in April 2025.
- Capabilities broadened through ChatGPT agent integration in July 2025.
- API guidance now recommends background mode for long-running requests.


**Adoption Signals:**

- Rolled out across Pro, Plus, Team, Enterprise, Edu, and a lightweight Free-tier mode over time.
- Official API productization via the o3-deep-research model.
- OpenAI Academy and Help Center position it as a standard workflow for research-heavy users.


**Supersession Notes:**

> Not fully superseded. OpenAI states that deeper and broader capabilities are available via ChatGPT agent, while the original deep research tool remains available in the tools menu.


#### Applications

**Real World Applications:**

- Competitive and market research
- Scientific landscape analysis
- Policy briefs
- Engineering technology surveys
- Source-backed due diligence
- Multi-source analysis of uploaded documents


**Users:**

- Knowledge workers
- Analysts
- Researchers
- Policy teams
- Engineers
- Enterprise users


**Deployment Constraints:**

- Availability depends on plan and country or territory
- Long-running tasks may take minutes to tens of minutes
- Sensitive workflows may require disabling web search when paired with private MCP data
- Connected-app access depends on workspace configuration
- API users should manage tool-call budgets and background execution


#### Governance And Risk

**Scientific Integrity Risks:**

- Hallucinated synthesis or incorrect claims despite citations
- Overconfident reports on ambiguous evidence
- Hidden source-quality variation across the open web
- Prompt injection from browsed content
- Outdated or low-quality sources affecting conclusions


**Security And Safety Risks:**

- Aggregation of personal information from public sources
- Unsafe or regulated advice at higher scale than plain chat
- Prompt-injection attacks in browsed pages
- Potential misuse of long-horizon browsing for harmful tasks


**Mitigations:**

- User-controlled source selection and site restriction
- Plan review before execution
- Interruptibility and live progress visibility
- Sandboxed Python environment without direct internet access
- Safety training, blocklists, and post-deployment monitoring
- Admin controls for enterprise access


**Policy Relevance:**

> Directly relevant to web-agent governance, privacy and personal-data aggregation, safety of autonomous research tools, enterprise source-control policies, and the evaluation of frontier-agent capabilities.


#### Uncertain Fields

- cost_and_runtime

### PaperBench

#### Identity

**Id:** paperbench


**Name:** PaperBench


**Aliases:** PaperBench: Evaluating AI's Ability to Replicate AI Research


**Organization:** OpenAI


**First Public Release:** 2025-04-02


**Current Status:** Active public benchmark with an official paper, OpenAI release page, and open repository.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset, codebase


**Domains:** AI research engineering, machine learning paper replication, long-horizon agent execution


**Positioning:** Benchmark for end-to-end AI research replication from paper to code.


**Boundary Notes:**

> Included because it evaluates long-horizon AI research engineering rather than narrow coding or question answering. Each task requires understanding a paper, building a codebase, executing experiments, and being graded against a rubric.


#### Capabilities

**Lifecycle Coverage:** paper understanding, code writing, experiment execution, result reproduction, rubric-based evaluation


**Tool Access:**

- Ubuntu containers
- GPU execution for reproduction
- API access for agents and judge
- Git-LFS data hydration
- LLM-based grading


**Execution Environment:**

> Three-stage containerized evaluation: agent rollout in an Ubuntu container, reproduction in a fresh GPU container, and grading in a third container.


**Artifact Outputs:** replication codebases, executed submissions, rubric grades, leaderboard scores, judge-evaluation artifacts


**Human Roles:**

> Benchmark designers select the papers and co-develop rubrics with the original paper authors. Users configure the benchmark, provide API keys and compute, run agents, and interpret the scores.


#### Autonomy

**Autonomy Rationale:**

> PaperBench targets agents that must independently read papers, build codebases, run experiments, and iterate over failures, but still operate inside benchmark-provided infrastructure and evaluation scaffolding.


**Iteration Loop:**

> Evaluated agents are expected to iterate over implementation and experiments; the benchmark itself runs rollout, reproduction, and grading as separate stages.


**Stopping And Guardrails:**

> Container isolation, explicit rubrics, separate grading infrastructure, required API-key configuration, and judge-based scoring constrain execution and evaluation.


#### Evaluation

**Benchmarks Used:** PaperBench itself, plus a separate benchmark for evaluating the LLM judge.


**Metrics:**

- average replication score
- rubric-level task completion
- judge quality on a separate judge benchmark
- comparison against a human baseline


**Baselines:**

- BasicAgent and IterativeAgent variants on frontier models
- Claude 3.5 Sonnet (New) with open-source scaffolding
- top ML PhD human baseline on a subset


**Validation Strength:**

> Benchmarked with hierarchical rubrics co-developed with the original paper authors and compared against a human baseline.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2504.01848


**Code Url:** https://github.com/openai/preparedness/tree/main/project/paperbench


**Dataset Url:** https://github.com/openai/preparedness/tree/main/project/paperbench


**Product Url:** https://openai.com/index/paperbench/


**Leaderboard Url:** https://github.com/openai/preparedness/tree/main/project/paperbench


**Source Quality:** Primary sources: official OpenAI benchmark page, official arXiv paper, and official repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- 20 ICML 2024 Spotlight and Oral papers
- 8,316 individually gradable tasks
- hierarchical rubrics
- LLM-based judge
- agent rollout container
- reproduction container
- grading container
- Git-LFS-hosted benchmark data


**Evaluates:** paper-to-code replication, AI research engineering, long-horizon agent execution, autonomous experiment execution


**Competes With Or Complements:** MLE-bench, Core-Bench


#### Timeline

**Milestones:**

- 2025-04-02: Official OpenAI release page published.
- 2025-04-02: arXiv v1 released.
- 2025-04-04: arXiv v2 released.
- 2025-04-07: arXiv v3 released.
- > 2025: Public repository released with benchmark data, code, setup instructions, and leaderboard section.


**Version History:**

- arXiv v1 on 2025-04-02
- arXiv v2 on 2025-04-04
- arXiv v3 on 2025-04-07
- > public repository documentation includes setup, data hydration, leaderboard, and judge-evaluation instructions


**Adoption Signals:** Public OpenAI release page, Public arXiv paper, Public official repository with a leaderboard section


**Supersession Notes:** No supersession was noted in the consulted primary sources.


#### Applications

**Real World Applications:**

- evaluating autonomous agents for research engineering
- comparing paper-replication agents
- studying long-horizon coding and experiment workflows
- preparedness-style capability measurement


**Users:** AI evaluation researchers, agent developers, preparedness teams, ML systems researchers


**Deployment Constraints:**

> Requires containerized execution, GPU access for reproduction, hydrated Git-LFS data, and API keys for the agents and judge. Some papers also require access to the OpenAI API and Hugging Face.


#### Governance And Risk

**Mitigations:**

- three-stage isolated container workflow
- co-developed rubrics with original paper authors
- separate judge evaluation
- explicit environment and API-key setup instructions


**Policy Relevance:**

> Relevant to frontier-model preparedness, measurement of long-horizon autonomous AI research capabilities, and the design of evaluations for increasingly capable coding and research agents.


#### Uncertain Fields

- autonomy_level
- cost_and_runtime
- evaluated_by
- evaluation_limitations
- known_failure_modes
- predecessors
- scientific_integrity_risks
- security_and_safety_risks
- successors

### ResearchBench

#### Identity

**Id:** researchbench


**Name:** ResearchBench


**Aliases:** ResearchBench, ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition


**Organization:** Academic research team; dataset page maintained by ankilok on Hugging Face


**First Public Release:** 2025-03-27


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset


**Domains:** general scientific discovery, natural language processing, hypothesis generation, literature-grounded research


**Positioning:**

> Benchmark for evaluating whether LLMs can produce scientific hypotheses through inspiration-based task decomposition.


**Boundary Notes:**

> Included because it explicitly targets scientific discovery capabilities, especially inspiration retrieval and hypothesis generation. It is not an end-to-end experiment execution benchmark.


#### Capabilities

**Lifecycle Coverage:** inspiration retrieval, inspiration reconstruction, hypothesis proposal, hypothesis evaluation, scientific reasoning


**Execution Environment:** Benchmark dataset and evaluation setting described in the arXiv paper and Hugging Face dataset page.


**Artifact Outputs:** retrieved inspirations, reconstructed inspiration explanations, generated research hypotheses, benchmark scores


**Human Roles:**

- Humans curate benchmark tasks and ground-truth inspirations.
- Humans interpret whether generated hypotheses are novel, feasible, and relevant.
- Researchers run and compare LLM baselines.


#### Autonomy

**Autonomy Level:** L2-L3


**Autonomy Rationale:**

> The benchmark targets bounded scientific-discovery subtasks rather than autonomous experiment execution. Strong agents can retrieve inspirations and propose hypotheses, but task setup and validation remain human-defined.


**Stopping And Guardrails:**

- Tasks are constrained to benchmark-provided scientific contexts.
- Outputs are scored against benchmark criteria rather than accepted as discoveries.
- Human interpretation remains necessary for scientific novelty and feasibility.


**Known Failure Modes:**

- Retrieving irrelevant or weak inspirations.
- Producing hypotheses that are plausible but not genuinely novel.
- Overfitting to benchmark phrasing.
- Missing domain constraints needed for feasible experiments.


#### Evaluation

**Benchmarks Used:**

- ResearchBench benchmark tasks
- Inspiration retrieval subtask
- Inspiration reconstruction subtask
- Hypothesis generation subtask


**Validation Strength:**

> Primary arXiv paper plus public Hugging Face dataset page; independent reproduction or official leaderboard was not verified.


**Evaluation Limitations:**

- Focuses on inspiration and hypothesis generation, not wet-lab validation or code execution.
- Scientific quality judgments can be subjective.
- Public code and official leaderboard availability were not verified.
- Dataset contamination risk should be assessed before using frontier model results.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2503.21248


**Dataset Url:** https://huggingface.co/datasets/ankilok/Researchbench


**Source Quality:** Primary arXiv paper and public Hugging Face dataset card.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:** inspiration retrieval task, inspiration reconstruction task, hypothesis generation task, ResearchBench dataset


**Evaluates:** scientific discovery, inspiration-based reasoning, hypothesis generation, literature-grounded ideation


**Competes With Or Complements:** DiscoveryBench, AI Co-Scientist, DeepResearch Bench, PaperBench


#### Timeline

**Milestones:**

- 2025-03-27: arXiv preprint posted.
- 2025: Hugging Face dataset page references the paper and benchmark decomposition.
- 2026-05-28: verified paper and dataset landing pages.


**Supersession Notes:** No official replacement or v2 was identified.


#### Applications

**Real World Applications:**

- Evaluating AI systems that assist research ideation.
- Studying how LLMs connect papers to new hypotheses.
- Benchmarking co-scientist and discovery-agent workflows.


**Users:**

- AI research-agent developers
- scientific-discovery benchmark designers
- NLP researchers
- research organizations evaluating hypothesis-generation tools


#### Governance And Risk

**Scientific Integrity Risks:**

- Overclaiming generated hypotheses as validated discoveries.
- Subjective scoring of novelty and feasibility.
- Possible benchmark contamination in future model training data.


**Security And Safety Risks:**

- Low direct operational risk because tasks are benchmarked ideation tasks.
- Potential dual-use concerns if used for sensitive scientific domains without review.
- Risk of unsupported research claims being propagated.


**Mitigations:**

- Treat outputs as hypotheses, not discoveries.
- Use expert review for high-stakes domains.
- Record provenance for inspirations and generated claims.


**Policy Relevance:**

> Relevant to publication norms, disclosure of AI-generated hypotheses, benchmark governance, and responsible scientific ideation.


#### Uncertain Fields

- adoption_signals
- baselines
- code_url
- cost_and_runtime
- current_status
- deployment_constraints
- evaluated_by
- iteration_loop
- leaderboard_url
- metrics
- predecessors
- product_url
- successors
- tool_access
- version_history

### Robin

#### Identity

**Id:** futurehouse_robin


**Name:** Robin


**Aliases:** Robin: A multi-agent system for automating scientific discovery


**Organization:** FutureHouse


**First Public Release:** 2025-05-19


**Current Status:** Active open-source research demo and paper-backed discovery workflow


#### Taxonomy

**Category:** domain_scientific_discovery_agent


**Type:** paper, open_source_system, research_demo


**Domains:** biology, biomedicine


**Positioning:** Semi-autonomous scientific discovery system


**Boundary Notes:**

> Included because Robin orchestrates background research, hypothesis generation, experiment proposal, data analysis, and hypothesis updating in one discovery loop. It is more integrated than standalone literature or chemistry agents, but still depends on humans for wet-lab execution.


#### Capabilities

**Lifecycle Coverage:** background_research, hypothesis_generation, experiment_proposal, data_analysis, hypothesis_update


**Tool Access:**

- Edison platform agents
- literature search agents
- data analysis agents
- LiteLLM-compatible LLM APIs
- Jupyter notebooks
- Docker


**Execution Environment:**

> User-run Python or Docker environment with Jupyter notebooks, Edison platform access for literature and data analysis, and external wet-lab execution for biological experiments


**Artifact Outputs:**

- hypotheses
- experiment proposals
- data analyses
- figures
- agent trajectories
- manuscript text


**Human Roles:**

> Humans provide the disease target, configure API keys and notebooks, and execute physical experiments. Robin handles the intellectual workflow, while human researchers remain responsible for wet-lab validation and downstream scientific judgment.


#### Autonomy

**Autonomy Level:** L3


**Autonomy Rationale:**

> Robin automates the key intellectual steps of scientific discovery across multiple iterations, but it is not fully closed-loop because human researchers perform the physical experiments and supply the runtime environment and platform access.


**Iteration Loop:**

> Yes. Robin iterates from literature review to candidate selection, experiment proposal, data analysis, and updated hypotheses in a lab-in-the-loop cycle.


**Stopping And Guardrails:**

> Operational limits include dependence on Edison platform access, user-supplied LLM credentials, notebook-based execution, and a hard boundary where humans execute and validate physical experiments.


**Known Failure Modes:**

- hallucinated biological mechanisms
- weak candidate prioritization
- overfitting to available literature
- errors in notebook-driven analysis
- false positives that fail wet-lab validation


#### Evaluation

**Benchmarks Used:**

- Real-world iterative dry age-related macular degeneration discovery workflow
- preclinical validation of proposed candidates
- follow-up RNA-seq analysis


**Metrics:**

- > identification of ripasudil as a novel therapeutic candidate for dry age-related macular degeneration
- successful generation of experiment plans and updated mechanistic hypotheses
- analysis identifying ABCA1 upregulation in the follow-up RNA-seq experiment


**Validation Strength:** Real-world validated


**Evaluation Limitations:**

> Public sources emphasize a single flagship case study in one biomedical problem. Generalization across diseases, broader benchmark comparisons, and fully independent reproductions are not yet demonstrated in the reviewed primary sources.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2505.13400


**Code Url:** https://github.com/Future-House/robin


**Product Url:**

> https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** FutureHouse Platform Agents, Crow, Falcon, Finch


**Components:**

- Crow
- Falcon
- Finch
- hypothesis generation workflow
- experiment proposal workflow
- data analysis workflow


**Evaluated By:** preclinical wet-lab validation, RNA-seq follow-up analysis, paper case study


**Evaluates:** Not a benchmark; it does not primarily evaluate other systems.


#### Timeline

**Milestones:**

- 2025-05-19: arXiv paper submitted
- 2025-05-20: FutureHouse announcement published
- 2025-05-27: code, data, and trajectories announced for release


**Adoption Signals:**

- GitHub repository showed 432 stars and 64 forks on 2026-05-28
- Open-source repository, public preprint, and published FutureHouse announcement


**Supersession Notes:** Not superseded in the reviewed primary sources.


#### Applications

**Real World Applications:**

- biomedical hypothesis generation
- therapeutic candidate identification
- experiment proposal for disease research
- analysis of follow-up biological data


**Users:** biomedical researchers, computational biologists, scientific AI teams, translational research groups


**Deployment Constraints:**

- Python 3.12 or higher
- Edison platform API access
- LLM provider API access
- Jupyter or Docker environment
- wet-lab capability for real-world validation


**Cost And Runtime:**

> FutureHouse states the full process from conceptualizing Robin to paper submission took about 2.5 months. Running the open-source workflow also requires platform access, LLM API costs, and potentially wet-lab spending for validation.


#### Governance And Risk

**Scientific Integrity Risks:**

- overclaiming novelty from limited literature evidence
- single-case discovery overgeneralization
- mechanistic misinterpretation
- authorship and provenance ambiguity in AI-generated scientific outputs


**Security And Safety Risks:**

- unsafe biomedical recommendations if used without expert oversight
- misuse of automated disease-target discovery workflows
- external API and notebook execution risks


**Mitigations:**

- human-performed wet-lab experiments
- interpretable multi-agent workflow
- public code and example trajectories
- requirement for platform and notebook configuration rather than hidden autonomous deployment


**Policy Relevance:**

> Robin is relevant to AI governance in science because it combines autonomous hypothesis generation with real biological validation, creating questions about dual use, authorship, evidence standards, and lab oversight.


#### Uncertain Fields

- baselines
- competes_with_or_complements
- dataset_url
- leaderboard_url
- successors
- version_history

### SciAgents

#### Identity

**Id:** sciagents


**Name:** SciAgents


**Aliases:**

- SciAgentsDiscovery
- SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning
- > SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoning


**Organization:** Massachusetts Institute of Technology (MIT)


**First Public Release:** 2024-09-09


**Current Status:** Active open-source research prototype with a public paper and public GitHub repository.


#### Taxonomy

**Category:** domain_scientific_discovery_agent


**Type:** paper, codebase, research demo


**Domains:** materials_science, bioinspired_materials


**Positioning:**

> Domain-specific autonomous co-scientist for graph-grounded hypothesis generation in materials science.


**Boundary Notes:**

> Included because it couples literature retrieval, ontological knowledge graphs, and multi-agent critique to generate scientific hypotheses in a real scientific domain. It is not a general-purpose product suite, and it does not autonomously execute wet-lab experiments.


#### Capabilities

**Lifecycle Coverage:** literature_retrieval, knowledge_graph_reasoning, hypothesis_generation, multi_agent_critique, proposal_refinement


**Tool Access:**

- large language models
- data retrieval tools
- OpenAI API
- Semantic Scholar API
- ontological knowledge graph files
- Hugging Face graph and embedding downloads


**Execution Environment:**

> Local Python and notebook workflow using GraphReasoning, AG2, downloaded graph artifacts, and external APIs.


**Artifact Outputs:** research hypotheses, research proposals, critiques, structured JSON summaries, draft documents


**Human Roles:**

> Humans choose the domain and prompts, provide API keys and graph resources, inspect outputs, and decide whether any generated hypothesis is scientifically valid or worth experimental follow-up.


#### Autonomy

**Autonomy Level:** L3


**Autonomy Rationale:**

> SciAgents can autonomously retrieve context, traverse a knowledge graph, generate hypotheses, and critique/refine them through multiple specialized agents, but it still depends on humans for setup, API access, and downstream validation.


**Iteration Loop:**

> Yes. The system samples graph context, generates proposals, critiques them with specialized agents, refines them, and expands the output into a more detailed research draft.


**Stopping And Guardrails:**

> The workflow is constrained by local execution, external API availability, graph coverage, and human review. It does not include autonomous lab actuation or irreversible real-world actions.


**Known Failure Modes:**

> Possible failure modes include hallucinated novelty claims, weak or noisy graph links, retrieval gaps, overconfident hypothesis ranking, and generated ideas that are scientifically interesting but not experimentally feasible.


#### Evaluation

**Validation Strength:**

> Peer-reviewed publication lineage and public code support the claims, but the central validation is still case-study based rather than independent large-scale external reproduction.


**Evaluation Limitations:**

> Evaluation is domain-specific, largely qualitative, and focused on ideation quality rather than downstream experimental success. External replication evidence for the generated discoveries was not verified in the retrieved sources.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2409.05556


**Code Url:** https://github.com/lamm-mit/SciAgentsDiscovery


**Dataset Url:** https://huggingface.co/lamm-mit/bio-graph-1K


**Source Quality:** Primary


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:**

- GraphReasoning and generative knowledge extraction work from the same MIT group
- ontological knowledge graph methods for scientific discovery
- multi-agent LLM research planning frameworks


**Components:**

- Ontologist agent
- Scientist 1 agent
- Scientist 2 agent
- Critic agent
- Planner agent
- Assistant agent
- global knowledge graph
- GraphReasoning package
- AG2 automation framework
- OpenAI API
- Semantic Scholar API


**Evaluated By:** paper case studies in biologically inspired materials


**Evaluates:**

> Not a benchmark; it generates and critiques scientific hypotheses rather than scoring external systems.


#### Timeline

**Milestones:**

- 2024-09-09: arXiv preprint submitted.
- 2024: repository released with automated and non-automated notebooks.
- 2024: repository citation points to publication in Advanced Materials.


#### Applications

**Real World Applications:**

- bioinspired materials ideation
- mechanism discovery from literature
- early-stage hypothesis generation for materials R&D
- graph-grounded literature synthesis


**Users:**

- academic materials scientists
- computational materials researchers
- AI-for-science researchers
- R&D teams exploring bioinspired materials


**Deployment Constraints:**

> Requires Python setup, GraphReasoning installation, downloaded graph artifacts, OpenAI access, Semantic Scholar access, and enough local resources to run notebook-driven multi-agent workflows.


#### Governance And Risk

**Scientific Integrity Risks:**

> The main integrity risks are fabricated novelty, overstated interdisciplinary links, and weak evidence chains from graph connections to scientific claims.


**Security And Safety Risks:**

> The system has relatively low direct physical risk because it is a reasoning workflow, but unsafe downstream use could misdirect lab resources or produce misleading scientific narratives.


**Mitigations:**

> Graph-grounded context, specialized critique agents, human review, local execution, and explicit downstream validation by scientists act as the main safeguards.


**Policy Relevance:**

> Relevant to AI-for-science governance because it shows how autonomous ideation systems can influence research direction without directly executing experiments, raising questions about provenance, attribution, and validation standards.


#### Uncertain Fields

- adoption_signals
- baselines
- benchmarks_used
- competes_with_or_complements
- cost_and_runtime
- leaderboard_url
- metrics
- product_url
- successors
- supersession_notes
- version_history

### SciCode

#### Identity

**Id:** scicode


**Name:** SciCode


**Aliases:** SciCode: A Research Coding Benchmark Curated by Scientists


**Organization:**

> Multi-institution academic collaboration led by University of Illinois Urbana-Champaign, Argonne National Laboratory, and Carnegie Mellon University


**First Public Release:** 2024-07-18


**Current Status:**

> Active public benchmark with an arXiv paper, GitHub evaluation code, a public Hugging Face dataset, and a public leaderboard.


#### Taxonomy

**Category:** benchmark


**Type:** paper, benchmark, dataset, codebase


**Domains:**

- scientific coding
- mathematics
- physics
- chemistry
- biology
- materials science


**Positioning:** Scientist-curated benchmark for realistic research coding in the natural sciences.


**Boundary Notes:**

> Included because SciCode evaluates realistic scientific problem solving through code synthesis, decomposition into subproblems, and automatic execution-based checking. It is broader than a narrow code-generation benchmark but narrower than a full end-to-end autonomous scientist system.


#### Capabilities

**Lifecycle Coverage:**

- scientific problem understanding
- subproblem decomposition
- code writing
- scientific reasoning
- execution-based verification


**Tool Access:**

- Python evaluation package
- automatic test cases
- inspect_ai integration
- OpenCompass integration
- model API access for benchmark runs


**Execution Environment:**

> Benchmark-hosted evaluation code run by users locally against the SciCode package, optional inspect_ai workflows, and benchmark test assets.


**Artifact Outputs:** generated code solutions, subproblem predictions, main-problem predictions, pass@1 scores, leaderboard submissions


**Human Roles:**

> Scientists curated the problems, background descriptions, gold solutions, and tests. Users configure models, run evaluations, and interpret benchmark scores.


#### Autonomy

**Autonomy Rationale:**

> SciCode can evaluate anything from direct model code generation to bounded tool-using coding agents, but all systems operate inside a fixed benchmark with predefined problems, tests, and scoring.


**Iteration Loop:**

> The benchmark supports iterative agent-style evaluation, but each run remains bounded by predefined scientific coding tasks, optional background text, and automatic tests.


**Stopping And Guardrails:**

> Execution is bounded by predefined benchmark tasks, gold-standard tests, dev/test splits, optional background settings, and user-controlled evaluation infrastructure such as inspect_ai.


#### Evaluation

**Benchmarks Used:**

> SciCode itself across subproblem and main-problem evaluation, with standard and background-assisted settings.


**Metrics:**

- subproblem pass@1 rate
- main-problem pass@1 rate
- main problem resolve rate on the public leaderboard
- comparison between standard and background-assisted settings


**Baselines:**

- Claude 3.5 Sonnet
- GPT-4o
- GPT-4-Turbo
- Gemini 1.5 Pro
- Claude 3 Opus
- DeepSeek-Coder-v2
- DeepSeek-R1
- Qwen2-72B-Instruct
- OpenAI o1-preview
- OpenAI o3-mini variants


**Validation Strength:**

> Benchmarked with scientist-curated tasks, gold-standard solutions, automatic test cases, a public leaderboard, and a public dataset release.


**Evaluation Limitations:**

> SciCode covers 80 main problems across five natural-science domains rather than the full space of scientific coding. It focuses on computation and simulation code, and benchmark scores may not capture broader scientific judgment or downstream wet-lab usefulness.


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2407.13168


**Code Url:** https://github.com/scicode-bench/SciCode


**Dataset Url:** https://huggingface.co/datasets/SciCode1/SciCode


**Product Url:** https://scicode-bench.github.io/


**Leaderboard Url:** https://scicode-bench.github.io/leaderboard/


**Source Quality:**

> Primary sources: official arXiv paper, official GitHub repository, official benchmark website, and the official Hugging Face dataset linked from the repository.


**Last Verified At:** 2026-05-28


#### Relationships

**Components:**

- 80 main problems
- 338 subproblems
- 15-problem development split
- 65-problem test split
- scientist-authored background descriptions
- gold-standard solutions
- automatic test cases
- inspect_ai integration
- OpenCompass integration
- public leaderboard


**Evaluates:**

- scientific coding
- research problem solving
- natural-science computation
- code synthesis
- scientific reasoning under realistic task structure


#### Timeline

**Milestones:**

- 2024-07-18: arXiv paper released.
- 2024-07-24: scientist-annotated background support added for background-assisted evaluation.
- 2024-08-22: benchmark integrated into OpenCompass.
- 2024-09-26: benchmark accepted at the NeurIPS 2024 Datasets and Benchmarks Track.
- 2024-11-04: public leaderboard launched.
- 2025-01-24: inspect_ai integration announced.
- 2025-02-17: Hugging Face dataset release announced.


**Version History:**

- Initial arXiv release on 2024-07-18
- background-assisted evaluation support added on 2024-07-24
- OpenCompass integration announced on 2024-08-22
- leaderboard launched on 2024-11-04
- inspect_ai became the recommended evaluation path on 2025-01-24
- public Hugging Face dataset announced on 2025-02-17


**Adoption Signals:**

- 199 GitHub stars at verification time
- public leaderboard
- OpenCompass integration
- public Hugging Face dataset
- NeurIPS 2024 Datasets and Benchmarks Track acceptance


**Supersession Notes:** No supersession was identified in the consulted primary sources.


#### Applications

**Real World Applications:**

- benchmarking scientific coding assistants
- comparing models for computational research support
- measuring progress on multi-step natural-science coding tasks
- testing whether coding agents can translate scientific concepts into executable computation


**Users:** AI-for-science researchers, benchmark designers, scientific coding agent developers, language-model evaluators


**Deployment Constraints:**

> Running new evaluations requires the SciCode package, benchmark test assets including numeric test data, compatible model APIs, and local execution permissions for the evaluation workflow.


#### Governance And Risk

**Mitigations:**

- scientist curation of tasks
- gold-standard solutions and automatic tests
- development and test split separation
- bounded benchmark tasks
- inspect_ai and public evaluation tooling


**Policy Relevance:**

> SciCode is relevant to governance of scientific AI because it measures realistic scientific coding ability in a bounded, transparent benchmark and helps track progress toward more capable research agents.


#### Uncertain Fields

- autonomy_level
- competes_with_or_complements
- cost_and_runtime
- evaluated_by
- known_failure_modes
- predecessors
- scientific_integrity_risks
- security_and_safety_risks
- successors

### The AI Scientist

#### Identity

**Id:** sakana_ai_scientist_v1


**Name:** The AI Scientist


**Aliases:** AI Scientist, The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery


**Organization:** Sakana AI, University of British Columbia, University of Oxford, Vector Institute


**First Public Release:** 2024-08-12


**Current Status:** Open-source research system; still public, but the broader successor is The AI Scientist-v2.


#### Taxonomy

**Category:** end_to_end_ai_scientist


**Type:** paper, codebase, product


**Domains:** machine_learning


**Positioning:** Autonomous scientist for end-to-end machine learning paper generation.


**Boundary Notes:**

> Included because it closes the machine-learning research loop from idea generation through coding, experiments, figures, manuscript drafting, and simulated review. It excludes general coding agents that do not produce and evaluate full research artifacts.


#### Capabilities

**Lifecycle Coverage:**

- idea_generation
- code_writing
- experiment_execution
- visualization
- paper_writing
- automated_review


**Tool Access:**

- Semantic Scholar search
- LLM-based code editing
- Shell and process execution
- Experiment execution on GPU-backed ML code
- Plot generation
- LaTeX and PDF generation
- Automated paper review


**Execution Environment:**

> Local or server-side Linux environment with NVIDIA GPUs, CUDA, PyTorch, API-accessed frontier models, and LaTeX tooling.


**Artifact Outputs:**

- Research ideas
- Modified code
- Experiment runs
- Plots and figures
- LaTeX manuscripts and PDFs
- Automated reviews


**Human Roles:**

- Humans provide the starting template or codebase and choose the research area
- Humans supply API keys, compute, and infrastructure
- Humans are expected to sandbox runs and inspect outputs before external dissemination


#### Autonomy

**Autonomy Level:** L4


**Autonomy Rationale:**

> It autonomously covers idea generation, coding, experiment execution, plotting, manuscript drafting, and simulated reviewing inside a bounded machine-learning workflow, but humans still choose scope, provide infrastructure, and control publication or submission.


**Iteration Loop:**

> Open-ended loop over idea generation, novelty checking, experiment iteration, automated review, and archive growth.


**Stopping And Guardrails:**

- User-provided templates and topics bound the search space
- Authors recommend containerization and restricted web access
- Timeouts and reproducible saved artifacts act as operational checks
- Human review is still needed before publication or submission


**Known Failure Modes:**

- Unreadable plots or broken paper layout because the first version lacks vision capabilities
- Incorrect implementations or unfair baseline comparisons
- Numerical reasoning mistakes when interpreting results
- Self-modifying behavior such as relaunching or extending its own execution path
- Reviewer-workload inflation if used to mass-produce submissions


#### Evaluation

**Benchmarks Used:**

- Internal template-based machine-learning research tasks: NanoGPT, 2D Diffusion, and Grokking
- Automated reviewer aligned to top-tier machine-learning conference review standards


**Metrics:**

- Automated reviewer described as near-human for generated-paper evaluation
- Under strong models, generated papers can reach automated 'Weak Accept' judgments
- Approximate generation cost: about 15 USD per paper


**Validation Strength:**

> Benchmarked and internally reviewed; later official follow-up work added stronger human-review evidence.


**Evaluation Limitations:**

- Evaluation is concentrated in machine-learning templates rather than broad science
- Automated review is not a substitute for human peer review
- The early version lacks multimodal figure understanding
- Success depends heavily on the underlying foundation model


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2408.06292


**Code Url:** https://github.com/SakanaAI/AI-Scientist


**Dataset Url:** None.


**Product Url:** https://sakana.ai/ai-scientist


**Leaderboard Url:** None.


**Source Quality:** Primary paper, official repository, and official Sakana AI post.


**Last Verified At:** 2026-05-28


#### Relationships

**Successors:** sakana_ai_scientist_v2


**Components:**

- Idea generation
- Novelty checking via Semantic Scholar
- Experimental iteration
- Paper write-up
- Automated reviewer
- Template codebases for NanoGPT, 2D Diffusion, and Grokking


**Competes With Or Complements:** The AI Scientist-v2, AI Co-Scientist / Co-Scientist


#### Timeline

**Milestones:**

- 2024-08-12: arXiv v1 submitted
- 2024-08-13: Sakana AI launch post and repository release
- 2024-09-01: arXiv v3 revision posted
- 2025-03-12: Sakana AI announced the peer-review milestone achieved by the improved v2 system
- 2026-03-26: Sakana AI reported the broader AI Scientist line in Nature


**Version History:**

- v1 arXiv release on 2024-08-12
- arXiv v2 on 2024-08-15
- arXiv v3 on 2024-09-01
- Later superseded in breadth by the template-free v2 line


**Adoption Signals:**

- GitHub repository had about 13.8k stars and about 2k forks when checked on 2026-05-28
- Community-contributed templates are listed in the repository
- Generated example papers and run artifacts were publicly released


**Supersession Notes:**

> Not obsolete, but v2 is the more general successor because it removes reliance on human-authored templates and adds agentic tree search.


#### Applications

**Real World Applications:**

- Machine-learning method ideation and ablation generation
- Automated experimentation on existing ML codebases
- Drafting research papers and reviewer-style feedback


**Users:** Machine-learning researchers, AI research engineers, Autonomous-science researchers


**Deployment Constraints:**

- Linux plus NVIDIA GPU and CUDA stack
- Frontier-model API access
- Template preparation and baseline runs
- LaTeX and PDF tooling
- Safe sandboxing because the system executes LLM-written code


**Cost And Runtime:**

> Official sources describe roughly 15 USD per paper in the first release; runtime depends on the template and hardware, and CPU-only use is described as likely infeasible.


#### Governance And Risk

**Scientific Integrity Risks:**

- Fabricated or misattributed citations
- Misleading claims from flawed implementations or unfair baselines
- Automated review being mistaken for real peer review
- Submission spam that burdens reviewers


**Security And Safety Risks:**

- Execution of LLM-written code
- Potential use of dangerous packages
- Unrestricted web access
- Unexpected process spawning and self-modification


**Mitigations:**

- Containerize the environment
- Restrict web access
- Store reproducible artifacts for executed experiments
- Require human inspection before publication or submission


**Policy Relevance:**

> Relevant to responsible publication of AI-generated science, disclosure norms, benchmark governance for automated reviewers, and safe sandboxing of autonomous research agents.


#### Uncertain Fields

- baselines
- evaluated_by

### The AI Scientist-v2

#### Identity

**Id:** sakana_ai_scientist_v2


**Name:** The AI Scientist-v2


**Aliases:** AI Scientist-v2, The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search


**Organization:** Sakana AI, University of British Columbia, Vector Institute, University of Oxford


**First Public Release:** 2025-04-07


**Current Status:** Active open-source research system.


#### Taxonomy

**Category:** end_to_end_ai_scientist


**Type:** paper, codebase


**Domains:** machine_learning


**Positioning:** Autonomous scientist for open-ended machine-learning discovery via agentic tree search.


**Boundary Notes:**

> Included because it performs end-to-end machine-learning research without human-authored experimental templates, from hypothesis generation through peer-review-submitted manuscripts. It is broader than pure literature or planning tools but still scoped to compute-based ML research.


#### Capabilities

**Lifecycle Coverage:**

- hypothesis_generation
- experiment_design
- experiment_execution
- data_analysis
- figure_refinement
- paper_writing
- peer_review_submission


**Tool Access:**

- Semantic Scholar literature search
- LLM-written code generation and debugging
- GPU experiment execution
- Agentic tree search orchestration
- LaTeX and PDF generation
- AI reviewer with a VLM figure-refinement loop


**Execution Environment:**

> Local or server-side Linux environment with NVIDIA GPUs, CUDA, PyTorch, LaTeX and PDF tooling, API-accessed foundation models, and optional Semantic Scholar API access.


**Artifact Outputs:**

- Structured research ideas
- Code changes and experiment branches
- Experiment logs
- Tree-search visualizations
- Figures
- Scientific manuscripts
- AI reviews


**Human Roles:**

- Humans provide a broad topic and infrastructure
- Humans sandbox execution and supply model or API credentials
- Humans selected which generated papers to submit in the workshop experiment
- Humans retained final authority over publication and release


#### Autonomy

**Autonomy Level:** L4


**Autonomy Rationale:**

> It autonomously generates hypotheses, conducts experiments, analyzes results, refines figures, and writes full manuscripts in an open-ended ML setting without topic-specific code templates, but humans still provide the topic, compute, and publication decisions.


**Iteration Loop:**

> Progressive agentic tree search over experimental branches, plus iterative review and figure-refinement feedback loops.


**Stopping And Guardrails:**

- Authors require use inside a controlled sandbox such as Docker
- Resource use is bounded by tree-search parameters, worker counts, and step limits
- Novelty and citation grounding can use Semantic Scholar
- The repository license mandates clear disclosure of AI use in resulting manuscripts


**Known Failure Modes:**

- Lower success rates than v1 on template-friendly tasks
- Potentially unsafe code execution, uncontrolled web access, or unintended process spawning
- CUDA out-of-memory failures or model-capacity mismatches
- Citation or figure-quality issues that require reviewer feedback
- Workshop-level acceptance does not guarantee conference-track quality


#### Evaluation

**Benchmarks Used:**

- Three fully autonomous submissions to the ICLR 2025 I Can't Believe It's Not Better workshop
- Peer-review scores against human workshop acceptance thresholds
- Internal human review and reproducibility checks on the submitted papers


**Metrics:**

- One manuscript received reviewer scores 6, 7, and 6, for an average of 6.33
- One of three fully autonomous submissions exceeded the average human acceptance threshold
- > Typical experimentation cost is about 15 to 20 USD per run, with about 5 USD more for writing under the example defaults
- > Example runs typically finish within several hours, with writing taking about 20 to 30 minutes once experiments are complete


**Baselines:**

- The AI Scientist-v1
- Average human workshop acceptance threshold
- The template-based v1 workflow as the stronger option for tasks with a clear starting template


**Validation Strength:** Human-reviewed and peer-reviewed, with official submission evidence.


**Evaluation Limitations:**

- Only three workshop submissions were tested
- The workshop bar is lower than a top conference main track
- > The accepted-threshold paper was withdrawn before publication and did not receive a public meta-review
- Authors state that v2 can have lower success rates than v1 when strong templates are available


#### Links And Provenance

**Paper Url:** https://arxiv.org/abs/2504.08066


**Code Url:** https://github.com/SakanaAI/AI-Scientist-v2


**Dataset Url:** None.


**Product Url:** https://sakana.ai/ai-scientist-first-publication/


**Leaderboard Url:** None.


**Source Quality:** Primary paper, official repository, and official Sakana AI post.


**Last Verified At:** 2026-05-28


#### Relationships

**Predecessors:** sakana_ai_scientist_v1


**Components:**

- Agentic tree search
- Experiment manager agent
- Template-free ideation pipeline
- Semantic Scholar novelty search
- AI reviewer with VLM figure-refinement loop
- Best-first search configuration and worker-based branching


**Evaluated By:**

- ICLR 2025 I Can't Believe It's Not Better workshop peer review
- Internal human review
- Internal code and reproducibility review


**Competes With Or Complements:** The AI Scientist, AI Co-Scientist / Co-Scientist


#### Timeline

**Milestones:**

- > 2025-03-12: Sakana AI announced that a fully AI-generated paper from the improved system crossed a workshop acceptance threshold
- 2025-04-07: Sakana AI published the technical report and open-sourced v2
- 2025-04-10: arXiv submission of paper 2504.08066
- 2026-03-26: Sakana AI reported the broader AI Scientist line in Nature


**Version History:**

- 2025-03 workshop-result announcement
- 2025-04 technical report and repository release
- No formal GitHub release tags were published as of 2026-05-28


**Adoption Signals:**

- GitHub repository had about 6.4k stars and 857 forks when checked on 2026-05-28
- The peer-review result drew official Sakana AI coverage and public discussion
- Generated papers and analysis were released publicly


**Supersession Notes:** This is the documented successor of v1; no later public successor was verified as of 2026-05-28.


#### Applications

**Real World Applications:**

- Open-ended machine-learning hypothesis generation
- Autonomous workshop-paper drafting and submission experiments
- Automated exploratory experimentation across multiple ML domains


**Users:** Autonomous-science researchers, Machine-learning researchers, AI research labs studying end-to-end research automation


**Deployment Constraints:**

- Linux plus NVIDIA GPU and CUDA stack
- OpenAI, Gemini, or Claude model access
- Optional Semantic Scholar API access
- LaTeX, Poppler, and chktex tooling
- Controlled sandboxing because the system executes LLM-written code
- License-based disclosure obligations for downstream papers


**Cost And Runtime:**

> The official repository estimates a few dollars for ideation, about 15 to 20 USD for the main experimentation run with Claude 3.5 Sonnet, about 5 USD more for writing under the example defaults, and several hours of wall-clock time for a full run.


#### Governance And Risk

**Scientific Integrity Risks:**

- AI-generated manuscripts may overstate novelty or rigor
- Peer-review gaming or reviewer-overload concerns
- Citation, formatting, or statistical mistakes in generated papers
- Ambiguity around authorship and disclosure without explicit policy


**Security And Safety Risks:** Execution of LLM-written code, Uncontrolled web access, Dangerous package use, Unintended spawned processes


**Mitigations:**

- Run only inside a controlled sandbox
- Use bounded worker and search-step settings
- Perform human review and reproducibility checks before release
- Disclose AI use clearly in any resulting manuscript


**Policy Relevance:**

> Strongly relevant to AI-authorship disclosure, peer-review integrity, IRB-governed experiments with AI-generated papers, and the safe release of autonomous research systems.
