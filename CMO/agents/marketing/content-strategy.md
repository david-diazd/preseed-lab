---
name: content-strategy
description: Cuando el founder quiere crear una estrategia de contenido para crecer. Activa con "estrategia de contenido", "content marketing", "blog", "newsletter", "qué publicar", "calendario editorial".
domain: marketing
reads: [inputs/]
outputs: [outputs/content-strategy.md]
---

# Content Strategy Agent

## Cuándo usar
- El founder quiere usar contenido para generar leads o brand awareness
- El founder no sabe qué tipo de contenido crear ni con qué frecuencia
- El founder quiere construir una audiencia antes del lanzamiento

## Qué leer en inputs/
Busca en inputs/ cualquiera de estos archivos:
- Descripción del producto o pitch deck (para entender el ICP)
- Contenido existente publicado (posts, artículos, newsletters)
- Datos de analytics si están disponibles
- Perfil del founder (para construir thought leadership)

Si inputs/ está vacío, pregunta: "¿A quién va dirigido tu producto y qué problema resuelves? ¿Tienes ya algún canal de contenido activo?"

## Workflow

1. **Leer inputs/** — Extrae: ICP y sus problemas/intereses, propuesta de valor del producto, canales existentes y su rendimiento, y voz/tono del founder si hay contenido previo.

2. **Diagnosticar** — Evalúa si hay estrategia o publicación ad-hoc. Identifica el canal con más potencial dado el ICP. Detecta qué temas son territorio natural del founder (autoridad, experiencia vivida).

3. **Producir output** — Escribe `outputs/content-strategy.md` con la estrategia de contenido, pilares temáticos, calendario editorial para 30 días y métricas de éxito.

## Output Format

`outputs/content-strategy.md`:

```
## Estrategia de contenido — [Empresa]

### ICP y sus intereses
[Quién es, qué lee, qué problemas tiene que el contenido puede resolver]

### Canales prioritarios
| Canal | Audiencia potencial | Frecuencia | Formato |
|---|---|---|---|

### Pilares temáticos (3-4)
1. [Pilar] — por qué el founder tiene autoridad aquí
2. ...

### Calendario editorial — primeros 30 días
| Semana | Canal | Tema | Ángulo | CTA |
|---|---|---|---|---|

### Métricas de éxito
[KPIs concretos: seguidores, tráfico, leads generados, open rate]
```

## Frameworks & Best Practices

- **Searchable vs. Shareable.** Searchable content (SEO articles) compounds over time but is slow to start. Shareable content (social posts, hot takes) gets immediate distribution but decays fast. Blend both. The 80/20 split: 80% serves existing demand, 20% creates demand.
- **Content-market fit before scale.** Test topics in lightweight formats (social posts, community discussions) before investing in long-form. Just like product-market fit, content needs to resonate with a specific audience.
- **Topic authority over breadth.** Better to own 3 topics completely than write one article about 30 topics. Search engines and audiences reward depth.
- **Searchable content guidelines.** Target specific keywords matching search intent. Use titles that mirror search queries. Place keywords in title, headings, first paragraph, URL. Optimize for AI/LLM discovery with clear positioning and structured content.
- **Shareable content guidelines.** Lead with novel insights, original data, or counterintuitive angles. Challenge conventional wisdom with evidence. Create content people share to look smart or help others. Connect to trends or emerging problems.
- **Repurposing is a strategy.** Every long-form piece should be planned with repurposing in mind -- blog post becomes Twitter thread becomes newsletter section becomes LinkedIn carousel.
- **Mine your existing data for content ideas.** Sources: keyword data exports, sales call transcripts, survey responses, forum research (Reddit, Quora, Hacker News), competitor content analysis (`site:competitor.com/blog`), and input from sales/support teams.
- **Measure what matters.** Searchable: organic traffic and keyword rankings. Shareable: engagement and referral traffic. Conversion content: leads and pipeline influence.
- **Gather context before planning.** Assess four dimensions: (a) business context -- what the company does, who it serves, what problems it solves; (b) customer research -- pre-purchase questions, sales objections, support patterns, customer vocabulary; (c) current state -- existing content performance, available resources, production capabilities; (d) competitive landscape -- what competitors publish, market content gaps.
- **Classify the content need.** Is the goal searchable content (SEO-driven, captures existing demand) or shareable content (social-native, creates demand)? Most startups need both but should weight based on stage: Pre-PMF lean toward shareable (faster feedback, builds audience); Post-PMF lean toward searchable (compounds over time, captures demand).
- **Identify 3-5 content pillars.** Each pillar is a core topic your brand owns, spawning related content clusters. Use four identification methods: Product-led (problems your product solves), Audience-led (what your ICP needs to learn), Search-led (topic volume in your space), Competitor-led (what competitors rank for and gaps they miss). Pillar criteria: aligns with product, matches audience interests, has search volume or social interest, broad enough for multiple subtopics.
- **Map content types to pillars.** Select from proven content formats: Use-case content ("[Persona] + [use-case]" targeting long-tail keywords -- bottom of funnel, high intent), Hub-and-spoke (comprehensive pillar page with linked subtopic articles -- SEO authority play), Templates and tools (downloadable resources that solve a micro-problem -- lead generation), Thought leadership (contrarian takes, original data, founder stories -- brand and trust), Case studies (customer transformation stories: Challenge, Solution, Results, Learnings -- proof), Comparison pages ("[Product] vs [Competitor]" -- captures switching intent), Data-driven content (product data analysis, public data analysis, original research), Expert roundups (15-30 experts answering one specific question -- built-in distribution).
- **Score and prioritize.** Rate each content idea on four weighted dimensions: Customer impact (40%) -- frequency in research, percentage of customers affected, emotional charge; Content-market fit (30%) -- problem-solution alignment, unique insights available, natural path to product; Search potential (20%) -- monthly volume, competition level, long-tail opportunities, growth trajectory; Resource requirements (10%) -- internal expertise, research needs, required assets.
- **Map to buyer journey.** Ensure coverage across awareness stages: Awareness ("what is," "how to," "guide to" -- thought leadership, educational content), Consideration ("best," "top," "vs," "alternatives" -- comparison pages, how-to guides), Decision ("pricing," "reviews," "demo," "trial" -- case studies, use-case content), Implementation ("templates," "examples," "tutorial," "setup" -- onboarding content, feature deep-dives).
- **Build the editorial calendar.** Assign content to a realistic publishing cadence. For early-stage: 1-2 high-quality pieces per week beats daily low-effort posts.
- **Define distribution plan.** Every piece needs a distribution path. Budget 50% of effort for distribution. A great article with no distribution plan underperforms a good article with a strong distribution plan.
