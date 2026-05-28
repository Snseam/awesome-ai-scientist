#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
ELEGANT = ROOT.parent / "ElegantPaper-0.12"

MD_EN = ROOT / "ai-scientist-survey-review-en.md"
MD_ZH = ROOT / "ai-scientist-survey-review-zh.md"
TEX_EN = ELEGANT / "awesome-ai-scientist-survey-review-en.tex"
TEX_ZH = ELEGANT / "awesome-ai-scientist-survey-review-zh.tex"

CATEGORY_ORDER = [
    "end_to_end_ai_scientist",
    "research_workflow_agent",
    "hypothesis_and_research_planning_system",
    "domain_scientific_discovery_agent",
    "science_product_suite",
    "deep_research_product",
    "literature_review_product",
    "benchmark",
]

CATEGORY_EN = {
    "end_to_end_ai_scientist": "End-to-end AI Scientist systems",
    "research_workflow_agent": "Research workflow agents",
    "hypothesis_and_research_planning_system": "Hypothesis and research-planning systems",
    "domain_scientific_discovery_agent": "Domain scientific-discovery agents",
    "science_product_suite": "Science agent product suites",
    "deep_research_product": "Deep-research products",
    "literature_review_product": "Literature-review products",
    "benchmark": "Evaluation benchmarks and datasets",
}

CATEGORY_ZH = {
    "end_to_end_ai_scientist": "端到端 AI 科学家系统",
    "research_workflow_agent": "科研工作流智能体",
    "hypothesis_and_research_planning_system": "假设生成与研究规划系统",
    "domain_scientific_discovery_agent": "领域科学发现智能体",
    "science_product_suite": "科学智能体产品套件",
    "deep_research_product": "深度研究产品",
    "literature_review_product": "文献综述产品",
    "benchmark": "评测基准与数据集",
}

AUTONOMY_ZH = {
    "L1": "L1：任务辅助",
    "L2": "L2：工作流智能体",
    "L2-L3": "L2-L3：工作流到半自主研究",
    "L3": "L3：半自主研究智能体",
    "L3-L4": "L3-L4：半自主到端到端研究",
    "L4": "L4：端到端自主科学家",
}

DOMAIN_ZH = {
    "machine_learning": "机器学习",
    "general_science": "通用科学",
    "biology": "生物学",
    "biomedicine": "生物医学",
    "chemistry": "化学",
    "materials_science": "材料科学",
    "inorganic_chemistry": "无机化学",
    "algorithms": "算法",
    "mathematics": "数学",
    "AI_infrastructure": "AI 基础设施",
    "data_science": "数据科学",
    "bioinformatics": "生物信息学",
    "general_academic_research": "通用学术研究",
    "systematic_reviews": "系统综述",
    "multimodal deep research": "多模态深度研究",
}


def load_records():
    records = []
    for path in sorted(RESULTS.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["_file"] = path.name
        records.append(data)
    return sorted(records, key=lambda item: str(item.get("first_public_release", "")))


def clean(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return "" if "[uncertain]" in value else value.strip()
    if isinstance(value, list):
        return [item for item in value if not (isinstance(item, str) and "[uncertain]" in item)]
    return value


def release_year(record):
    date = str(record.get("first_public_release", ""))
    match = re.search(r"(20\d{2})", date)
    return match.group(1) if match else "unknown"


def autonomy(record):
    value = record.get("autonomy_level") or record.get("autonomy_level_target") or ""
    if isinstance(value, str) and "[uncertain]" in value:
        return ""
    return value


def domains(record, lang):
    values = clean(record.get("domains", []))
    if not isinstance(values, list):
        return str(values)
    if lang == "zh":
        values = [DOMAIN_ZH.get(v, v.replace("_", " ")) for v in values]
    else:
        values = [v.replace("_", " ") for v in values]
    return ", ".join(values[:4])


def short_role(record):
    text = clean(record.get("positioning")) or clean(record.get("boundary_notes")) or ""
    return text


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(cell).replace("\n", " ") for cell in row) + " |")
    return "\n".join(out)


def category_counts(records):
    counts = Counter(r.get("category") for r in records)
    return [(cat, counts[cat]) for cat in CATEGORY_ORDER if counts[cat]]


def timeline_rows(records, lang):
    by_year = defaultdict(list)
    for record in records:
        by_year[release_year(record)].append(record)
    rows = []
    for year in sorted(by_year):
        names = ", ".join(r["name"] for r in by_year[year])
        if lang == "zh":
            rows.append([year, len(by_year[year]), names])
        else:
            rows.append([year, len(by_year[year]), names])
    return rows


def census_rows(records, lang):
    rows = []
    for idx, record in enumerate(sorted(records, key=lambda r: r["name"].lower()), 1):
        cat = record.get("category", "")
        rows.append([
            idx,
            record["name"],
            (CATEGORY_ZH if lang == "zh" else CATEGORY_EN).get(cat, cat),
            record.get("first_public_release", ""),
            (AUTONOMY_ZH.get(autonomy(record), autonomy(record)) if lang == "zh" else autonomy(record)),
            domains(record, lang),
        ])
    return rows


def benchmark_rows(records, lang):
    rows = []
    for record in sorted([r for r in records if r.get("category") == "benchmark"], key=lambda r: r["name"].lower()):
        evaluates = clean(record.get("evaluates", []))
        if isinstance(evaluates, list):
            evaluates = ", ".join(v.replace("_", " ") for v in evaluates[:4])
        rows.append([
            record["name"],
            record.get("first_public_release", ""),
            AUTONOMY_ZH.get(autonomy(record), autonomy(record)) if lang == "zh" else autonomy(record),
            evaluates,
        ])
    return rows


def systems_by_category(records, lang):
    lines = []
    labels = CATEGORY_ZH if lang == "zh" else CATEGORY_EN
    for category in CATEGORY_ORDER:
        group = [r for r in records if r.get("category") == category]
        if not group or category == "benchmark":
            continue
        title = labels.get(category, category)
        lines.append(f"### {title}")
        lines.append("")
        for record in sorted(group, key=lambda r: r["name"].lower()):
            role = short_role(record)
            if lang == "zh":
                lines.append(
                    f"- **{record['name']}**（{record.get('first_public_release', '')}，"
                    f"{AUTONOMY_ZH.get(autonomy(record), autonomy(record))}）：{role}"
                )
            else:
                lines.append(
                    f"- **{record['name']}** ({record.get('first_public_release', '')}, "
                    f"{autonomy(record)}): {role}"
                )
        lines.append("")
    return "\n".join(lines)


def source_rows(records):
    rows = []
    for record in sorted(records, key=lambda r: r["name"].lower()):
        url = record.get("paper_url") or record.get("product_url") or record.get("code_url") or record.get("dataset_url") or ""
        if isinstance(url, str) and "[uncertain]" not in url:
            rows.append([record["name"], url])
    return rows


def render_md_en(records):
    counts = category_counts(records)
    count_text = ", ".join(f"{CATEGORY_EN[c]}: {n}" for c, n in counts)
    return f"""# Awesome AI Scientist: A Survey of AI Systems for Scientific Discovery

## Abstract

AI Scientist systems have moved from isolated literature-search and coding assistants toward agentic workflows that propose hypotheses, execute experiments, generate reports, and expose their own behavior to benchmark evaluation. This survey synthesizes a corpus of {len(records)} verified ecosystem records: {sum(1 for r in records if r.get('category') != 'benchmark')} systems or products and {sum(1 for r in records if r.get('category') == 'benchmark')} benchmarks or datasets. Rather than listing artifacts one by one, the survey organizes the field around four questions: what kinds of systems are being built, which stages of the scientific lifecycle they cover, how autonomy is currently bounded, and how the community evaluates their claims. The central finding is that the ecosystem has split into three interacting layers: end-to-end AI Scientist prototypes, domain-specific discovery agents, and evaluation benchmarks that increasingly test long-horizon research behavior. Current systems show credible progress in bounded computational and search-heavy settings, but robust scientific validation still depends on human review, controlled execution environments, and benchmark designs that resist superficial report generation.

**Keywords:** AI Scientist; scientific discovery agents; automated research; research benchmarks; AI for science.

## 1. Introduction

The phrase *AI Scientist* increasingly refers to a family of systems that attempt to automate parts of the scientific lifecycle rather than merely answer research questions. The strongest claims come from end-to-end systems that generate ideas, write code, run experiments, analyze results, and draft papers. Adjacent systems cover narrower but still consequential slices: literature synthesis, hypothesis generation, chemistry planning, autonomous laboratories, algorithm discovery, scientific coding, reproducibility, and deep research reporting.

This survey treats the field as an ecosystem rather than a single benchmark race. The reason is practical: a system such as The AI Scientist is not comparable to Elicit, PaperBench, Coscientist, or AlphaEvolve on one scalar axis. Each artifact occupies a different position in the research stack. A useful review therefore needs a taxonomy, a timeline, an autonomy model, and an evaluation map that connects systems to the benchmarks and real-world settings used to justify them.

## 2. Corpus and Review Method

The review is based on {len(records)} structured records generated from primary or official sources where possible. The corpus includes papers, repositories, product pages, benchmark pages, dataset pages, and exported PDF/Markdown artifacts. Items were included if they automate or substantially augment scientific research workflows, or if they evaluate such systems. General chatbots and unrelated foundation models were excluded unless they appeared as part of a research-agent workflow.

The resulting corpus contains: {count_text}. This distribution already reveals the maturity of the field: benchmark work is nearly as numerous as system-building work, suggesting that the community is still negotiating what counts as scientific progress by agents.

{md_table(["Category", "Count", "Interpretation"], [[CATEGORY_EN[c], n, "Evaluation infrastructure" if c == "benchmark" else "System or product layer"] for c, n in counts])}

## 3. Taxonomy of the AI Scientist Ecosystem

The ecosystem is best understood as a layered stack. At the top are end-to-end AI Scientist systems, which attempt to bind ideation, implementation, experimentation, and paper drafting into one loop. The middle layer contains domain discovery agents, such as chemistry, biology, materials, and algorithm-discovery systems. The bottom and cross-cutting layer contains research products and benchmarks: tools that either support human researchers directly or measure whether agents can perform credible research work.

{systems_by_category(records, "en")}

This taxonomy suggests that autonomy is not a binary property. Literature-review products are often useful at L1, deep-research products and product suites sit near L2, workflow agents approach L3, and the strongest end-to-end or laboratory systems claim L4 behavior in bounded domains. No record in this corpus should be read as demonstrating unconstrained L5 scientific autonomy.

## 4. Historical Development

The modern ecosystem begins with tool-augmented scientific agents and autonomous laboratory work in 2023, expands into broad AI Scientist and benchmark efforts in 2024, and becomes a much denser landscape in 2025-2026. The timeline shows a shift from individual proof-of-concept systems toward benchmark suites and productized scientific assistants.

{md_table(["Year", "Items", "Representative records"], timeline_rows(records, "en"))}

## 5. Capability Patterns Across the Scientific Lifecycle

Across the corpus, five recurring capability patterns appear. First, **research synthesis** systems search, screen, summarize, and cite literature. Second, **hypothesis systems** propose candidate explanations, inspirations, or research plans. Third, **computational research agents** write and run code for machine-learning or data-science tasks. Fourth, **domain discovery systems** couple LLM reasoning with domain tools, laboratory automation, or external simulators. Fifth, **evaluation systems** define tasks, rubrics, and environments that convert qualitative research behavior into comparable scores.

The most important design tension is breadth versus validation. Broad agents cover more of the lifecycle but are harder to evaluate rigorously. Domain systems are narrower, but they can sometimes close the loop with real experiments, physical instruments, or task-specific metrics. Benchmarks sit between those extremes: they enable comparison, but they can encourage optimization for benchmark-specific behavior rather than genuine discovery.

## 6. Evaluation Benchmarks and What They Measure

The benchmark layer is the most developed part of the corpus. It covers ML experimentation, paper replication, computational reproducibility, data-driven discovery, scientific coding, bioinformatics, deep research, multimodal report generation, and scientific software maintenance. These benchmarks do not measure the same construct. Some reward code that runs; others reward literature-grounded reports; others test whether an agent can reproduce a paper or maintain a scientific codebase.

{md_table(["Benchmark", "Release", "Target autonomy", "Evaluates"], benchmark_rows(records, "en"))}

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

{md_table(["#", "Item", "Category", "Release", "Autonomy", "Domains"], census_rows(records, "en"))}

## 12. Key Source Links

{md_table(["Item", "Primary or official source"], source_rows(records))}
"""


def render_md_zh(records):
    counts = category_counts(records)
    count_text = "，".join(f"{CATEGORY_ZH[c]} {n} 个" for c, n in counts)
    return f"""# Awesome AI Scientist：AI 科学家系统综述

## 摘要

AI Scientist 系统正在从单点式文献检索、代码辅助和报告生成工具，发展为能够提出假设、调用工具、运行实验、分析结果并输出论文或报告的智能体工作流。本文基于 {len(records)} 个已整理条目进行综述，其中包括 {sum(1 for r in records if r.get('category') != 'benchmark')} 个系统或产品类条目，以及 {sum(1 for r in records if r.get('category') == 'benchmark')} 个评测基准或数据集类条目。与逐条罗列不同，本文围绕四个问题组织材料：AI Scientist 生态中有哪些系统类型，它们覆盖科研生命周期的哪些阶段，其自主性如何被限定，以及当前社区如何评测这些系统的科学能力。综述显示，该领域已经形成三个相互作用的层次：端到端 AI 科学家原型、领域科学发现智能体，以及面向长程科研行为的评测基准。当前系统在边界清晰的计算研究、文献研究和工具调用场景中进展明显，但真正可靠的科学验证仍依赖人工审查、受控执行环境，以及能够区分“报告质量”和“发现质量”的评测设计。

**关键词：** AI 科学家；科研智能体；自动化科学发现；科研评测基准；AI for Science。

## 1. 引言

“AI Scientist”已经不再只是会回答科研问题的聊天机器人，而是指一类试图自动化科研生命周期若干环节的系统。最强的主张来自端到端系统：它们尝试生成研究想法、编写代码、运行实验、分析结果并撰写论文。相邻系统则覆盖更窄但同样重要的环节，例如文献综合、假设生成、化学规划、自动化实验室、算法发现、科学编程、可复现性验证和深度研究报告。

本文将该领域视为一个生态，而不是单一排行榜。原因很直接：The AI Scientist、Elicit、PaperBench、Coscientist 与 AlphaEvolve 并不处在同一条能力轴上。它们分别对应科研栈中的不同位置。因此，一篇有用的综述需要同时给出分类法、时间线、自主等级模型和评测图谱，并说明系统、基准、产品、数据集和现实应用之间的关系。

## 2. 语料与综述方法

本文使用 {len(records)} 个结构化研究记录作为综述语料。记录优先来自论文、官方仓库、产品页面、基准页面和数据集页面。纳入标准是：条目必须自动化或显著增强科学研究工作流，或直接评测这类系统。一般聊天机器人和与科研智能体无直接关系的基础模型不纳入，除非它们作为科研智能体工作流的一部分出现。

语料构成为：{count_text}。这一分布本身说明该领域尚处在定义能力边界的阶段：评测基准数量几乎与系统构建工作相当，说明社区仍在协商什么样的智能体行为才算“科学进展”。

{md_table(["类别", "数量", "解释"], [[CATEGORY_ZH[c], n, "评测基础设施" if c == "benchmark" else "系统或产品层"] for c, n in counts])}

## 3. AI Scientist 生态分类

AI Scientist 生态可以理解为一个分层结构。最上层是端到端 AI 科学家系统，目标是把选题、实现、实验和论文写作整合为闭环。中间层是领域科学发现智能体，覆盖化学、生物、材料和算法发现等方向。底层和横向层是研究产品与评测基准：前者直接支持人类科研工作，后者衡量智能体是否真的具备可信的研究能力。

{systems_by_category(records, "zh")}

这个分类说明，自主性不是一个二元属性。文献综述产品通常处于 L1；深度研究产品和科研产品套件多处于 L2；工作流智能体接近 L3；最强的端到端系统或自动化实验室系统在受限领域内声称达到 L4。本文语料中没有任何条目足以证明开放式 L5 科学自主性。

## 4. 历史演化

现代 AI Scientist 生态从 2023 年的工具增强科学智能体和自动化实验室工作开始，在 2024 年扩展到更广义的 AI Scientist 原型和评测基准，并在 2025-2026 年迅速密集化。时间线显示，领域重心正在从单个概念验证系统转向基准套件和产品化科研助手。

{md_table(["年份", "条目数", "代表性条目"], timeline_rows(records, "zh"))}

## 5. 科研生命周期中的能力模式

语料中反复出现五类能力模式。第一类是**研究综合**，即检索、筛选、总结并引用文献。第二类是**假设系统**，即生成候选解释、研究灵感或研究计划。第三类是**计算研究智能体**，即为机器学习或数据科学任务编写并运行代码。第四类是**领域发现系统**，即将大语言模型推理与领域工具、实验室自动化或外部模拟器结合。第五类是**评测系统**，即通过任务、评分规则和执行环境把定性的研究行为转化为可比较的结果。

这里最重要的设计张力是广度与验证之间的矛盾。覆盖科研生命周期越广的系统，越难被严格评测。领域系统范围较窄，但有时能够通过真实实验、物理仪器或任务特定指标闭环验证。评测基准处在两者之间：它们提供可比较性，但也可能诱导系统优化基准行为，而不是产生真正的科学发现。

## 6. 评测基准综述

评测层是当前语料中最成熟的部分。它覆盖机器学习实验、论文复现、计算可复现性、数据驱动发现、科学编程、生物信息学、深度研究、多模态报告生成和科学软件维护。这些基准并不测量同一种能力：有的奖励能运行的代码，有的奖励文献支撑的报告，有的测试智能体能否复现论文或维护科学代码库。

{md_table(["基准", "发布时间", "目标自主性", "评测内容"], benchmark_rows(records, "zh"))}

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

下表列出全部 {len(records)} 个条目，以满足总数要求并保证综述可审计。

{md_table(["序号", "条目", "类别", "发布时间", "自主性", "领域"], census_rows(records, "zh"))}

## 12. 关键来源链接

{md_table(["条目", "主要或官方来源"], source_rows(records))}
"""


def latex_escape(text):
    text = str(text)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def latex_url(text):
    return r"\url{" + str(text).strip() + "}"


def md_to_tex(md, lang):
    lines = []
    in_table = False
    in_itemize = False
    skip_section = None
    table_rows = []

    def close_itemize():
        nonlocal in_itemize
        if in_itemize:
            lines.append(r"\end{itemize}")
            in_itemize = False

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            title = line[3:].strip()
            if title in {"Abstract", "摘要"}:
                close_itemize()
                skip_section = "abstract"
                continue
            skip_section = None
        elif skip_section == "abstract":
            continue

        if line.startswith("| ") and line.endswith(" |"):
            close_itemize()
            in_table = True
            if re.match(r"^\|(\s*:?-+:?\s*\|)+$", line):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            table_rows.append(cells)
            continue
        if in_table:
            close_itemize()
            lines.extend(render_tex_table(table_rows))
            table_rows = []
            in_table = False

        if not line:
            close_itemize()
            lines.append("")
        elif line.startswith("# "):
            close_itemize()
            continue
        elif line.startswith("## "):
            close_itemize()
            lines.append(r"\section{" + latex_escape(strip_heading_number(line[3:])) + "}")
        elif line.startswith("### "):
            close_itemize()
            lines.append(r"\subsection{" + latex_escape(strip_heading_number(line[4:])) + "}")
        elif line.startswith("- "):
            if not in_itemize:
                lines.append(r"\begin{itemize}[leftmargin=1.4em]")
                in_itemize = True
            lines.append(r"\item " + inline_tex(line[2:]))
        else:
            close_itemize()
            lines.append(inline_tex(line))
    if in_table:
        close_itemize()
        lines.extend(render_tex_table(table_rows))
    close_itemize()
    return "\n".join(lines)


def strip_heading_number(text):
    return re.sub(r"^\s*\d+[\.\uff0e]\s*", "", text.strip())


def inline_tex(text):
    placeholders = {}

    def stash(value):
        key = f"@@LATEX{len(placeholders)}@@"
        placeholders[key] = value
        return key

    def repl_url(match):
        return stash(latex_url(match.group(0)))

    text = re.sub(r"https?://[^\s|)]+", repl_url, text)
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: stash(r"\textbf{" + latex_escape(m.group(1)) + "}"), text)
    text = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", lambda m: stash(r"\emph{" + latex_escape(m.group(1)) + "}"), text)
    text = latex_escape(text)
    for key, value in placeholders.items():
        text = text.replace(latex_escape(key), value)
    return text


def render_tex_table(rows):
    if not rows:
        return []
    cols = len(rows[0])
    width = "0.14\\textwidth" if cols >= 6 else "0.22\\textwidth"
    if cols >= 6:
        spec = "p{0.04\\textwidth}" + "".join([f"p{{{width}}}" for _ in range(cols - 1)])
    else:
        spec = "".join(["p{0.24\\textwidth}" for _ in range(cols)])
    out = [r"\begin{longtable}{" + spec + "}", r"\toprule"]
    out.append(" & ".join(inline_tex(c) for c in rows[0]) + r"\\")
    out.extend([r"\midrule", r"\endhead"])
    for row in rows[1:]:
        out.append(" & ".join(inline_tex(c) for c in row) + r"\\")
    out.extend([r"\bottomrule", r"\end{longtable}", ""])
    return out


def render_tex(md, lang):
    if lang == "zh":
        title = "Awesome AI Scientist：AI 科学家系统综述"
        abstract = "本文将 AI Scientist 生态整理为综述论文格式，综合 31 个系统、产品、基准与数据集条目，分析其分类、能力、自主性、评测方式、风险与未来方向。"
        keywords = "AI 科学家，科研智能体，自动化科学发现，评测基准，综述"
        doc = r"\documentclass[lang=cn,a4paper,11pt]{elegantpaper}"
    else:
        title = "Awesome AI Scientist: A Survey of AI Systems for Scientific Discovery"
        abstract = "This survey synthesizes 31 AI Scientist systems, products, benchmarks, and datasets into a review-style manuscript focused on taxonomy, capabilities, autonomy, evaluation, risks, and future directions."
        keywords = "AI Scientist, scientific discovery agents, automated research, benchmarks, survey"
        doc = r"\documentclass[lang=en,a4paper,11pt]{elegantpaper}"
    body = md_to_tex(md, lang)
    return "\n".join([
        doc,
        r"\title{" + latex_escape(title) + "}",
        r"\author{Generated from awesome-ai-scientist-map}",
        r"\institute{Awesome AI Scientist}",
        r"\version{0.2}",
        r"\date{2026-05-28}",
        r"\usepackage{enumitem}",
        r"\usepackage{longtable}",
        r"\usepackage{booktabs}",
        r"\usepackage{url}",
        r"\addbibresource[location=local]{reference.bib}",
        r"\begin{document}",
        r"\maketitle",
        r"\begin{abstract}",
        latex_escape(abstract),
        r"\keywords{" + latex_escape(keywords) + "}",
        r"\end{abstract}",
        r"\tableofcontents",
        body,
        r"\end{document}",
        "",
    ])


def main():
    records = load_records()
    if len(records) != 31:
        raise SystemExit(f"Expected 31 records, found {len(records)}")
    md_en = render_md_en(records)
    md_zh = render_md_zh(records)
    MD_EN.write_text(md_en, encoding="utf-8")
    MD_ZH.write_text(md_zh, encoding="utf-8")
    TEX_EN.write_text(render_tex(md_en, "en"), encoding="utf-8")
    TEX_ZH.write_text(render_tex(md_zh, "zh"), encoding="utf-8")
    print(f"Wrote {MD_EN}")
    print(f"Wrote {MD_ZH}")
    print(f"Wrote {TEX_EN}")
    print(f"Wrote {TEX_ZH}")


if __name__ == "__main__":
    main()
