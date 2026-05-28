# Awesome AI Scientist：AI 科学家系统综述

## 摘要

AI Scientist 系统正在从单点式文献检索、代码辅助和报告生成工具，发展为能够提出假设、调用工具、运行实验、分析结果并输出论文或报告的智能体工作流。本文基于 31 个已整理条目进行综述，其中包括 16 个系统或产品类条目，以及 15 个评测基准或数据集类条目。与逐条罗列不同，本文围绕四个问题组织材料：AI Scientist 生态中有哪些系统类型，它们覆盖科研生命周期的哪些阶段，其自主性如何被限定，以及当前社区如何评测这些系统的科学能力。综述显示，该领域已经形成三个相互作用的层次：端到端 AI 科学家原型、领域科学发现智能体，以及面向长程科研行为的评测基准。当前系统在边界清晰的计算研究、文献研究和工具调用场景中进展明显，但真正可靠的科学验证仍依赖人工审查、受控执行环境，以及能够区分“报告质量”和“发现质量”的评测设计。

**关键词：** AI 科学家；科研智能体；自动化科学发现；科研评测基准；AI for Science。

## 1. 引言

“AI Scientist”已经不再只是会回答科研问题的聊天机器人，而是指一类试图自动化科研生命周期若干环节的系统。最强的主张来自端到端系统：它们尝试生成研究想法、编写代码、运行实验、分析结果并撰写论文。相邻系统则覆盖更窄但同样重要的环节，例如文献综合、假设生成、化学规划、自动化实验室、算法发现、科学编程、可复现性验证和深度研究报告。

本文将该领域视为一个生态，而不是单一排行榜。原因很直接：The AI Scientist、Elicit、PaperBench、Coscientist 与 AlphaEvolve 并不处在同一条能力轴上。它们分别对应科研栈中的不同位置。因此，一篇有用的综述需要同时给出分类法、时间线、自主等级模型和评测图谱，并说明系统、基准、产品、数据集和现实应用之间的关系。

## 2. 语料与综述方法

本文使用 31 个结构化研究记录作为综述语料。记录优先来自论文、官方仓库、产品页面、基准页面和数据集页面。纳入标准是：条目必须自动化或显著增强科学研究工作流，或直接评测这类系统。一般聊天机器人和与科研智能体无直接关系的基础模型不纳入，除非它们作为科研智能体工作流的一部分出现。

语料构成为：端到端 AI 科学家系统 3 个，科研工作流智能体 1 个，假设生成与研究规划系统 1 个，领域科学发现智能体 6 个，科学智能体产品套件 2 个，深度研究产品 1 个，文献综述产品 2 个，评测基准与数据集 15 个。这一分布本身说明该领域尚处在定义能力边界的阶段：评测基准数量几乎与系统构建工作相当，说明社区仍在协商什么样的智能体行为才算“科学进展”。

| 类别 | 数量 | 解释 |
| --- | --- | --- |
| 端到端 AI 科学家系统 | 3 | 系统或产品层 |
| 科研工作流智能体 | 1 | 系统或产品层 |
| 假设生成与研究规划系统 | 1 | 系统或产品层 |
| 领域科学发现智能体 | 6 | 系统或产品层 |
| 科学智能体产品套件 | 2 | 系统或产品层 |
| 深度研究产品 | 1 | 系统或产品层 |
| 文献综述产品 | 2 | 系统或产品层 |
| 评测基准与数据集 | 15 | 评测基础设施 |

## 3. AI Scientist 生态分类

AI Scientist 生态可以理解为一个分层结构。最上层是端到端 AI 科学家系统，目标是把选题、实现、实验和论文写作整合为闭环。中间层是领域科学发现智能体，覆盖化学、生物、材料和算法发现等方向。底层和横向层是研究产品与评测基准：前者直接支持人类科研工作，后者衡量智能体是否真的具备可信的研究能力。

### 端到端 AI 科学家系统

- **DeepScientist**（2025-09-30，L4：端到端自主科学家）：Local-first autonomous research studio for long-horizon scientific discovery and paper-oriented workflows.
- **The AI Scientist**（2024-08-12，L4：端到端自主科学家）：Autonomous scientist for end-to-end machine learning paper generation.
- **The AI Scientist-v2**（2025-04-07，L4：端到端自主科学家）：Autonomous scientist for open-ended machine-learning discovery via agentic tree search.

### 科研工作流智能体

- **Agent Laboratory**（2025-01-08，L3：半自主研究智能体）：Autonomous research assistant

### 假设生成与研究规划系统

- **AI Co-Scientist / Co-Scientist**（2025-02-19，L3：半自主研究智能体）：Collaborative co-scientist for scientist-in-the-loop hypothesis generation and research planning.

### 领域科学发现智能体

- **A-Lab / GNoME Materials Discovery Lineage**（2023-11，L4：端到端自主科学家）：Autonomous materials discovery stack that combines large-scale learned candidate generation with robotic closed-loop synthesis and characterization.
- **AlphaEvolve**（2025-05-14，L3：半自主研究智能体）：A Gemini-powered evolutionary coding agent for algorithm discovery and system optimization.
- **ChemCrow**（2023-04-11，L2：工作流智能体）：A tool-augmented chemistry assistant that uses GPT-4 plus expert-designed tools to solve reasoning-intensive chemistry tasks.
- **Coscientist**（2023-12-20，L4：端到端自主科学家）：A GPT-4-based autonomous chemistry co-scientist for planning, executing, and optimizing laboratory experiments.
- **Robin**（2025-05-19，L3：半自主研究智能体）：Semi-autonomous scientific discovery system
- **SciAgents**（2024-09-09，L3：半自主研究智能体）：Domain-specific autonomous co-scientist for graph-grounded hypothesis generation in materials science.

### 科学智能体产品套件

- **Asta**（2025-08-26，L2：工作流智能体）：A science-focused agent ecosystem that combines research assistants, benchmark infrastructure, and developer resources.
- **FutureHouse Platform Agents**（2025-05-01，L2：工作流智能体）：Scientific agent platform

### 深度研究产品

- **OpenAI Deep Research**（2025-02-02，L2：工作流智能体）：An agentic deep-research product for multi-step web research, source analysis, and citation-grounded report generation.

### 文献综述产品

- **Consensus**（2021，L1：任务辅助）：AI academic search and evidence-synthesis workspace for scientific research.
- **Elicit**（2021-08-31，L1：任务辅助）：An AI research assistant and literature-review platform focused on paper search, evidence extraction, and synthesis.


这个分类说明，自主性不是一个二元属性。文献综述产品通常处于 L1；深度研究产品和科研产品套件多处于 L2；工作流智能体接近 L3；最强的端到端系统或自动化实验室系统在受限领域内声称达到 L4。本文语料中没有任何条目足以证明开放式 L5 科学自主性。

## 4. 历史演化

现代 AI Scientist 生态从 2023 年的工具增强科学智能体和自动化实验室工作开始，在 2024 年扩展到更广义的 AI Scientist 原型和评测基准，并在 2025-2026 年迅速密集化。时间线显示，领域重心正在从单个概念验证系统转向基准套件和产品化科研助手。

| 年份 | 条目数 | 代表性条目 |
| --- | --- | --- |
| 2021 | 2 | Consensus, Elicit |
| 2023 | 4 | ChemCrow, MLAgentBench, A-Lab / GNoME Materials Discovery Lineage, Coscientist |
| 2024 | 7 | DiscoveryBench, SciCode, The AI Scientist, SciAgents, DSBench, CORE-Bench, MLE-bench |
| 2025 | 16 | Agent Laboratory, OpenAI Deep Research, AI Co-Scientist / Co-Scientist, BixBench, ResearchBench, PaperBench, The AI Scientist-v2, Deep Research Bench / RetroSearch, FutureHouse Platform Agents, AlphaEvolve, Robin, DeepResearch Bench, AstaBench, Asta, DeepScientist, AInsteinBench |
| 2026 | 2 | MMDeepResearch-Bench, AIRS-Bench |

## 5. 科研生命周期中的能力模式

语料中反复出现五类能力模式。第一类是**研究综合**，即检索、筛选、总结并引用文献。第二类是**假设系统**，即生成候选解释、研究灵感或研究计划。第三类是**计算研究智能体**，即为机器学习或数据科学任务编写并运行代码。第四类是**领域发现系统**，即将大语言模型推理与领域工具、实验室自动化或外部模拟器结合。第五类是**评测系统**，即通过任务、评分规则和执行环境把定性的研究行为转化为可比较的结果。

这里最重要的设计张力是广度与验证之间的矛盾。覆盖科研生命周期越广的系统，越难被严格评测。领域系统范围较窄，但有时能够通过真实实验、物理仪器或任务特定指标闭环验证。评测基准处在两者之间：它们提供可比较性，但也可能诱导系统优化基准行为，而不是产生真正的科学发现。

## 6. 评测基准综述

评测层是当前语料中最成熟的部分。它覆盖机器学习实验、论文复现、计算可复现性、数据驱动发现、科学编程、生物信息学、深度研究、多模态报告生成和科学软件维护。这些基准并不测量同一种能力：有的奖励能运行的代码，有的奖励文献支撑的报告，有的测试智能体能否复现论文或维护科学代码库。

| 基准 | 发布时间 | 目标自主性 | 评测内容 |
| --- | --- | --- | --- |
| AInsteinBench | 2025-12-24 | L2-L3：工作流到半自主研究 | scientific repository maintenance, scientific computing code agents, real PR tasks, feature implementation |
| AIRS-Bench | 2026-02-09 | L3-L4：半自主到端到端研究 | full ML research lifecycle, idea generation, experiment analysis, iterative refinement |
| AstaBench | 2025-08 | L1-L3 | scientific research agents, paper finding, scholarly question answering, tool use |
| BixBench | 2025-02-28 |  | bioinformatics, biological data analysis, multi-step dataset exploration, open-ended computational biology reasoning |
| CORE-Bench | 2024-09-17 | L2-L3：工作流到半自主研究 | computational reproducibility, research artifact execution, code reproducibility |
| Deep Research Bench / RetroSearch | 2025-05 | L2：工作流智能体 | web research agents, frozen-web retrieval, tool use, hallucination |
| DeepResearch Bench | 2025-06 | L2：工作流智能体 | deep research agents, citation quality, retrieval accuracy, long-form report quality |
| DiscoveryBench | 2024-07-01 | L2-L3：工作流到半自主研究 | data-driven discovery, hypothesis generation, multi-step reasoning, data semantics |
| DSBench | 2024-09-12 |  | data science, data analysis, data modeling, spreadsheet and Kaggle-style task solving |
| MLAgentBench | 2023-10-05 |  | ML experimentation, code execution, model improvement, long-term planning |
| MLE-bench | 2024-10-09 | L2-L3：工作流到半自主研究 | ML engineering, Kaggle-style competition performance, agent scaffolds, resource scaling behavior |
| MMDeepResearch-Bench | 2026-01 | L2：工作流智能体 | multimodal deep research, image-text evidence use, citation grounding, report integrity |
| PaperBench | 2025-04-02 |  | paper-to-code replication, AI research engineering, long-horizon agent execution, autonomous experiment execution |
| ResearchBench | 2025-03-27 | L2-L3：工作流到半自主研究 | scientific discovery, inspiration-based reasoning, hypothesis generation, literature-grounded ideation |
| SciCode | 2024-07-18 |  | scientific coding, research problem solving, natural-science computation, code synthesis |

因此，基准多样性是必要的。PaperBench 和 MLE-bench 更强调科研工程；DiscoveryBench 和 ResearchBench 更强调假设生成；CORE-Bench 和 AInsteinBench 更强调可复现性与科学软件；DeepResearch Bench 和 RetroSearch 更强调来源支撑的报告；BixBench 与 SciCode 则引入领域科学推理。单一排行榜很难代表整个生态，因为它会隐藏任务定义之间的关键差异。

## 7. 自主性、控制与人类角色

这些记录显示出一致模式：系统越接近端到端自主，越需要明确边界。边界包括基准任务定义、沙箱执行、人工审批、策展数据集、实验室约束、引用要求和事后专家审查。人类科学家仍然是任务定义者、安全审查者、领域验证者和新颖性判断者。

因此，本文语料中的自主阶梯是关系性的。L1 系统支持人工检索和综合；L2 系统在有边界的工作流中串联工具；L3 系统能够提出并迭代假设或实验，但依赖人工关卡；L4 系统在受限领域内执行完整闭环。现有证据不足以把任何系统视为开放式自主科学家。

## 8. 系统关系与生态结构

几个关系贯穿整个语料。AI Scientist 系列推动了端到端机器学习研究闭环，并自然连接到 PaperBench、MLE-bench、MLAgentBench 和 AIRS-Bench。化学与材料系统形成第二条谱系，包含 ChemCrow、Coscientist、A-Lab/GNoME 以及相关领域智能体。Elicit、Consensus、OpenAI Deep Research、Asta 和 FutureHouse agents 则构成产品层：这些系统通常不如研究原型自主，但更可能被真实科研工作者使用。

这种结构很重要，因为一个层次的进展不会自动迁移到另一个层次。一个在科学编程基准上表现好的智能体，不一定是可靠的文献综述者。一个强大的深度研究产品，可能仍缺少实验执行能力。一个在窄化学协议中成功的实验室智能体，也不等于具备开放式理论形成能力。

## 9. 风险、局限与开放问题

语料中反复出现三类风险。第一是**科研诚信风险**：系统可能产生看似合理但缺乏支持的新颖性声明、伪造或弱引用，以及形式完整但证据脆弱的论文。第二是**评测风险**：基准表现可能反映任务特定适配、裁判模型偏差或数据污染，而不是稳定的科研能力。第三是**操作风险**：具备代码执行、网页访问、化学规划或实验室控制能力的智能体，需要比普通搜索工具更强的安全与审计机制。

因此，关键开放问题不只是模型能力问题，还包括来源追踪、基准污染控制、可复现实验日志、人机协同审查设计、领域安全政策，以及如何区分“报告写得好”和“真的做出了发现”。

## 10. 未来方向

未来 AI Scientist 研究应从令人印象深刻的演示转向可控证据。值得推进的方向包括：按科研生命周期阶段做模块化评测；把代码执行与来源支撑报告结合的基准套件；具有专家验证的领域任务；以及能够暴露推理、工具调用、失败和不确定性的系统。该领域也需要保留负结果：失败假设、无效实验和不可复现的智能体输出不应被过滤掉。

## 11. 语料总表

下表列出全部 31 个条目，以满足总数要求并保证综述可审计。

| 序号 | 条目 | 类别 | 发布时间 | 自主性 | 领域 |
| --- | --- | --- | --- | --- | --- |
| 1 | A-Lab / GNoME Materials Discovery Lineage | 领域科学发现智能体 | 2023-11 | L4：端到端自主科学家 | 材料科学, 无机化学 |
| 2 | Agent Laboratory | 科研工作流智能体 | 2025-01-08 | L3：半自主研究智能体 | 机器学习, general computational research |
| 3 | AI Co-Scientist / Co-Scientist | 假设生成与研究规划系统 | 2025-02-19 | L3：半自主研究智能体 | 生物医学, 生物学, 通用科学 |
| 4 | AInsteinBench | 评测基准与数据集 | 2025-12-24 | L2-L3：工作流到半自主研究 | scientific computing, quantum chemistry, quantum computing, molecular dynamics |
| 5 | AIRS-Bench | 评测基准与数据集 | 2026-02-09 | L3-L4：半自主到端到端研究 | machine learning, natural language processing, 数学, coding |
| 6 | AlphaEvolve | 领域科学发现智能体 | 2025-05-14 | L3：半自主研究智能体 | 算法, 数学, systems optimization, AI 基础设施 |
| 7 | Asta | 科学智能体产品套件 | 2025-08-26 | L2：工作流智能体 | 通用科学 |
| 8 | AstaBench | 评测基准与数据集 | 2025-08 | L1-L3 | scientific research, literature understanding, code execution, data analysis |
| 9 | BixBench | 评测基准与数据集 | 2025-02-28 |  | 生物信息学, computational biology, genomics, transcriptomics |
| 10 | ChemCrow | 领域科学发现智能体 | 2023-04-11 | L2：工作流智能体 | 化学 |
| 11 | Consensus | 文献综述产品 | 2021 | L1：任务辅助 | 通用学术研究 |
| 12 | CORE-Bench | 评测基准与数据集 | 2024-09-17 | L2-L3：工作流到半自主研究 | computational reproducibility, computer science, social science, medicine |
| 13 | Coscientist | 领域科学发现智能体 | 2023-12-20 | L4：端到端自主科学家 | 化学 |
| 14 | Deep Research Bench / RetroSearch | 评测基准与数据集 | 2025-05 | L2：工作流智能体 | web research, open-web retrieval, multi-domain factual synthesis, tool-using agents |
| 15 | DeepResearch Bench | 评测基准与数据集 | 2025-06 | L2：工作流智能体 | deep research, web research, citation-rich report generation, science and technology |
| 16 | DeepScientist | 端到端 AI 科学家系统 | 2025-09-30 | L4：端到端自主科学家 | 机器学习, scientific tasks |
| 17 | DiscoveryBench | 评测基准与数据集 | 2024-07-01 | L2-L3：工作流到半自主研究 | sociology, 生物学, humanities, economics |
| 18 | DSBench | 评测基准与数据集 | 2024-09-12 |  | data science, data analysis, data modeling, tabular reasoning |
| 19 | Elicit | 文献综述产品 | 2021-08-31 | L1：任务辅助 | 通用学术研究, 系统综述 |
| 20 | FutureHouse Platform Agents | 科学智能体产品套件 | 2025-05-01 | L2：工作流智能体 | 生物学, 化学, 生物医学 |
| 21 | MLAgentBench | 评测基准与数据集 | 2023-10-05 |  | machine learning experimentation, ML engineering, agentic code execution, model improvement |
| 22 | MLE-bench | 评测基准与数据集 | 2024-10-09 | L2-L3：工作流到半自主研究 | machine learning engineering, Kaggle-style competitions, applied machine learning |
| 23 | MMDeepResearch-Bench | 评测基准与数据集 | 2026-01 | L2：工作流智能体 | 多模态深度研究, image-text evidence synthesis, long-form report generation, general research |
| 24 | OpenAI Deep Research | 深度研究产品 | 2025-02-02 | L2：工作流智能体 | finance, science, policy, engineering |
| 25 | PaperBench | 评测基准与数据集 | 2025-04-02 |  | AI research engineering, machine learning paper replication, long-horizon agent execution |
| 26 | ResearchBench | 评测基准与数据集 | 2025-03-27 | L2-L3：工作流到半自主研究 | general scientific discovery, natural language processing, hypothesis generation, literature-grounded research |
| 27 | Robin | 领域科学发现智能体 | 2025-05-19 | L3：半自主研究智能体 | 生物学, 生物医学 |
| 28 | SciAgents | 领域科学发现智能体 | 2024-09-09 | L3：半自主研究智能体 | 材料科学, bioinspired materials |
| 29 | SciCode | 评测基准与数据集 | 2024-07-18 |  | scientific coding, 数学, physics, 化学 |
| 30 | The AI Scientist | 端到端 AI 科学家系统 | 2024-08-12 | L4：端到端自主科学家 | 机器学习 |
| 31 | The AI Scientist-v2 | 端到端 AI 科学家系统 | 2025-04-07 | L4：端到端自主科学家 | 机器学习 |

## 12. 关键来源链接

| 条目 | 主要或官方来源 |
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
