# The exact process

How each skill runs, step by step, with the decision points drawn out. The skill files are the source of truth; this page is the map.

- [0. End to end](#0-end-to-end)
- [1. audience-research](#1-audience-research)
- [2. hooks](#2-hooks)
- [3. ad-matrix](#3-ad-matrix)
- [4. video-ads](#4-video-ads)
- [5. The lab loop](#5-the-lab-loop)
- [6. Studying reels in bulk](#6-studying-reels-in-bulk)

---

## 0. End to end

```mermaid
sequenceDiagram
    actor U as Seller
    participant A as audience-research
    participant H as hooks
    participant M as ad-matrix
    participant V as video-ads
    participant X as Higgsfield
    U->>A: product + customer messages
    A-->>U: audience.md, top 3 problems or objections, angles, questions to ask
    U->>H: "hooks for a reel"
    H->>A: reads audience.md (seller facts, unknowns, draft notice)
    H-->>U: top 5 hooks, scored, with what the next 5 s must deliver
    U->>M: "ads, ₹500 a day, I can make 8"
    M->>A: reads and updates audience.md
    M-->>U: ad-matrix.csv, ad-brief.md, break-even, cut rule
    U->>V: "make the reel"
    V-->>U: beat sheet + shot list (what to film)
    V->>X: balance + quote (free)
    V-->>U: cost and the cheapest first draft
    U->>V: explicit yes
    V->>X: generate one draft
    V-->>U: reviewed draft, what's left to do
    U->>A: real results and new customer messages
```

| Stage | Input | Output file | Gate before moving on |
|---|---|---|---|
| Research | Product, seller facts, customer messages | `marketing/<slug>/audience.md` | A best first segment and three problems or objections are chosen, with counts |
| Hooks | `audience.md`, platform, goal | (in chat) top 5 | Every hook ≥ 8/12, no fatal flag, nothing from the Unknown list claimed |
| Matrix | Audience, hooks, capacity, budget | `ad-matrix.csv`, `ad-brief.md` | Made set covers every concept and ≥ 3 formats; break-even stated |
| Video | One hook or matrix row, footage on hand | Beat sheet, clips | Proof beats are real; cost approved before any generation |
| Learn | Results from the platform and from the seller's own tally | Sheet result columns, `lab/` | Winners explained by part (concept, hook, body, CTA) |

---

## 1. audience-research

**Use when:** a product has no audience file, the user pastes reviews or DMs, or copy keeps coming out generic.

```mermaid
flowchart TD
    S([Start]) --> B[Step 1 - Ask for basics:<br/>buyers, seller facts,<br/>their own customer material]
    B --> O{Own material<br/>provided?}
    O -->|Yes| R1[Step 2a - Read it all. Keep quotes verbatim.<br/>Mark buyer vs enquirer.]
    O -->|No| R2
    R1 --> R2{Search tool<br/>available?}
    R2 -->|Yes| P[Step 2b - Public voice of customer:<br/>competitor 1-, 3- and 5-star reviews,<br/>Q&A, forums]
    R2 -->|No| I
    P --> I[Step 2c - Inferences and assumptions,<br/>only to fill gaps]
    I --> C[Count source items<br/>1 DM = 1 review = 1 thread = 1 item]
    C --> E[Step 3 - Sort into the eight parts.<br/>One home per finding. No padding.]
    E --> D[Step 4 - Decide: first segment,<br/>top 3 problems or objections,<br/>3-5 angles, what we don't know]
    D --> T{Fewer than ~30<br/>source items?}
    T -->|Yes| N[Mark every decision provisional.<br/>Give counts. Add draft notice.]
    T -->|No| W
    N --> W[Step 5 - Write audience.md.<br/>Short chat summary.]
```

### Evidence tags

| Tag | Meaning | Trust |
|---|---|---|
| `[own]` / `[own buyer]` | Said by the seller's own prospects / paying customers | Highest |
| `[public: source]` | Said by other sellers' customers in the category | Medium |
| `[inferred: from …]` | An interpretation of a named piece of evidence | Reasoned guess |
| `[assumed]` | No source | Hypothesis |

### The eight parts
1 Problems · 2 Frustrations with current options · 3 Desired outcomes · 4 Repeated questions · 5 Common mistakes ·
6 Objections and limiting beliefs · 7 Emotional reasons underneath · 8 Their words (verbatim only)

**Rules:** quotation marks only for verbatim text · strip names and handles · record who it's *not* for · update the file when facts or
results change.

Example: [drone workshop audience file](../examples/drone-workshop/audience.md).

---

## 2. hooks

**Use when:** writing or rating the first line and first three seconds of anything.

```mermaid
flowchart TD
    S([Request]) --> Q{Hook supplied<br/>by the user?}
    Q -->|Yes, score mode| F[State the format assumed]
    F --> SC[Score on 6 criteria, 0-2 each]
    SC --> TG[Name failure tags in plain words]
    TG --> HI{Score ≥ 10?}
    HI -->|Yes| KEEP[Say it's strong. Don't rewrite.]
    HI -->|No| RW[3 rewrites, each a different type]
    Q -->|No, write mode| IN[Step 1 - Inputs: what, who, where,<br/>goal, real proof]
    IN --> AU{audience.md<br/>exists?}
    AU -->|Yes| RD[Read top problems, angles, verbatim,<br/>seller facts, Unknown list]
    AU -->|No| QK[Quick sketch, 2-3 per category,<br/>marked as assumptions]
    RD --> GO[Step 1b - Let the goal shape the hook]
    QK --> GO
    GO --> GEN[Step 2 - Draft 15+ across 6+ types.<br/>Three layers each: visual, text, spoken.]
    GEN --> CUT[Step 3 - Score all. Drop below 8/12<br/>or any fatal flag.]
    CUT --> RK[Rank survivors by which you'd bet on.<br/>Keep 5 of different types;<br/>≥ 2 led by desire or result.]
    RK --> DEL[Step 4 - Deliver top 5 +<br/>which two to test first]
```

### Scoring (0-2 each, 12 total)

| Criterion | 2 means |
|---|---|
| Specific | A number, named situation or concrete object carries the line |
| For the viewer | Names their situation, or shows the result they want happening |
| Opens a loop | A question they need answered, and the piece answers it |
| Clear in one read | Lands in under two seconds |
| Works muted | Movement or an odd image in frame one, plus readable text |
| Not swappable | Rests on something only this offer has |

**Fatal flags:** can't pay off · invented proof · overstated product · banned opener · misleading native format.

### How the goal changes the hook

| Goal | The hook should |
|---|---|
| Sales, DMs, leads | Show the product or result and the buyer's situation; price can be in the hook |
| Reach | Be broad and visual; curiosity anyone gets |
| Comments | Imply a question with an easy answer |
| Saves | Promise a list, steps or settings |
| Shares | Name a person the viewer knows |
| Followers | Promise a series |

Examples: [keychain hooks and a scored bad hook](../examples/keychain/hooks.md) ·
[drone workshop hooks](../examples/drone-workshop/hooks.md).

---

## 3. ad-matrix

**Use when:** planning ad creatives, a creative test, or variations of a winner.

```mermaid
flowchart TD
    S([Request]) --> A1[Read audience.md. Update it if the<br/>request settles an Unknown.]
    A1 --> CK[Sanity-check dates, prices, deadlines.<br/>'Still true?' for carried-over facts.]
    CK --> IN[Step 1 - Inputs: objective, offer, proof,<br/>assets, capacity, budget, margin]
    IN --> BE[Break-even = total spend ÷ profit per sale]
    BE --> CO[Step 2 - Choose 3-5 concepts<br/>≥ 1 led by desire]
    CO --> BO[Step 3 - Write 3-5 bodies,<br/>each a different format]
    BO --> HK[Step 4 - Write hooks by the hooks rules;<br/>mark which bodies each can open]
    HK --> CT[Step 5 - Write 1-3 CTAs]
    CT --> AS[Step 6 - Assemble compatible sets.<br/>ID = C-H-B-A]
    AS --> SZ{Sizing}
    SZ --> MK[Make ≤ capacity]
    SZ --> LV[Live = what the budget can test]
    SZ --> HD[Held = made, swapped in later]
    MK --> DV{Would two ads look the same<br/>muted with the text blurred?}
    LV --> DV
    HD --> DV
    DV -->|Yes| RP[Replace one]
    RP --> DV
    DV -->|No| OUT[Step 7 - ad-matrix.csv + ad-brief.md<br/>+ chat summary]
    OUT --> TP[Step 8 - Test plan: cut rule,<br/>judge by results, record]
```

### Reading the results

```mermaid
flowchart LR
    R[An ad underperforms] --> H{Low hook rate?}
    H -->|Yes| FH[Fix the hook]
    H -->|No| C{Watched but<br/>not clicked?}
    C -->|Yes| FB[Fix the body or CTA]
    C -->|No| B{Clicked but<br/>not bought?}
    B -->|Yes| FO[Fix the offer or landing page]
    B -->|No| W[It's working: make variations<br/>of that concept, one part at a time]
```

**Scope:** creatives and how to read the test. Campaign setup is not covered. Platform numbers are rules of thumb.

Example: [drone workshop matrix](../examples/drone-workshop/ad-matrix.csv) and [brief](../examples/drone-workshop/ad-brief.md);
[the chat reply that came with them](../examples/drone-workshop/ad-matrix-reply.md).

---

## 4. video-ads

**Use when:** a hook, script or ad needs to become a finished short video.

```mermaid
flowchart TD
    S([Hook + goal]) --> CH[Step 1 - Score a supplied hook.<br/>Check every claim against seller facts.]
    CH --> BS[Step 2 - Beat sheet: time, job, visual,<br/>text, sound, source]
    BS --> EACH{For each beat:<br/>is it proof?}
    EACH -->|Yes| REAL{Real footage or<br/>photo available?}
    REAL -->|have| USE[Use it]
    REAL -->|can film| FILM[Shot instruction]
    REAL -->|can't film now| LAD[Proof ladder]
    LAD --> L1[Step 1 - Real substitute: maker on camera,<br/>physical test, raw-vs-finished cut]
    L1 --> L2[Step 2 - Other real evidence:<br/>old clips, customer message, counts]
    L2 --> L3[Step 3 - Ship without the beat;<br/>plan a second version]
    EACH -->|No| GEN[May be generated]
    GEN --> ANY{Anything left<br/>to generate?}
    USE --> ANY
    FILM --> ANY
    L3 --> ANY
    ANY -->|No| FIN[Go to finishing.<br/>Generating nothing is a good outcome.]
    ANY -->|Yes| RT[Step 3 - List connector workflows. Route.]
    RT --> SRC[Inspect every source image<br/>at full size for brand marks]
    SRC --> MG[Step 4 - Money gate]
```

### The money gate

```mermaid
flowchart TD
    A[Collect the files the generation will use] --> B[Check balance — free]
    B --> C[Quote exactly what will run — free]
    C --> D[Show: what, credits vs balance,<br/>cheapest first draft]
    D --> E{Explicit yes?}
    E -->|No| STOP([Stop. Nothing spent.])
    E -->|Yes| F[Re-quote with real inputs attached]
    F --> G{Same or lower?}
    G -->|No| D
    G -->|Yes| H[Generate ONE draft]
    H --> I[Step 5 - Review: honesty, artifacts,<br/>hook, format. Say how it was reviewed.]
    I --> J{Usable?}
    J -->|Yes| K[Ask before the full-quality pass]
    J -->|No, 1st fail| L[Change prompt or reference.<br/>Ask before retrying.]
    L --> D
    J -->|No, 2nd fail| M[Stop. Offer the fallback:<br/>film it, still with motion, restructure.]
```

### Beat sheet format

| # | Time | Job | Visual | On-screen text | Voice / sound | Source |
|---|---|---|---|---|---|---|
| 1 | 0-3 | Hook | … | … | … | have / film / generate / screen / graphic |

Jobs in order: hook → proof or demo → what it is and what you get → objection → CTA.

Examples: [keychain reel when the process can't be filmed](../examples/keychain/video-plan.md) ·
[wallet reel 01](../lab/products/magsafe-wallet-reel-01.md) ·
[first generated draft and its review](../lab/video-tests/0001-drone-draft/notes.md).

---

## 5. The lab loop

```mermaid
flowchart LR
    B[Product brief] --> G[Run the skill]
    G --> S[Score against rubric]
    S --> T[Tag every miss]
    T --> L[Log the run]
    L --> C{Same tag on<br/>3+ products?}
    C -->|Yes| P[Promote to a rule<br/>in the skill]
    C -->|No| N[Keep counting]
    P --> RT[Re-test the products that failed]
    RT --> F{Error rate<br/>dropped?}
    F -->|Yes| K[Keep the rule]
    F -->|No| X[Revise or drop it]
```

Real numbers (CTR, cost per result, sales) override rubric scores. Files: [`lab/README.md`](../lab/README.md),
[`lab/rubric.md`](../lab/rubric.md), [`lab/error-taxonomy.md`](../lab/error-taxonomy.md).

### Two kinds of test, don't mix them up

| | Blind skill test | Lab run |
|---|---|---|
| Question | Do the instructions work? | Does the output perform? |
| Product | Invented | Real |
| Judge | A fresh agent's critique | Rubric, then real results |
| Log | [`lab/skill-tests.md`](../lab/skill-tests.md) | `lab/runs/`, `lab/scoreboard.csv` |
| Done so far | 5 | 0 scored |

---

## 6. Studying reels in bulk

How the source material was gathered; reuse it for the next batch.

```mermaid
flowchart LR
    U[URL list] --> R[tools/reel.py --file]
    R --> D[yt-dlp download]
    D --> F[ffmpeg: hook.jpg, sheet.jpg]
    D --> W[Whisper transcript]
    F --> RP[report.md per reel]
    W --> RP
    RP --> DG[tools/digest.py --todo --board]
    DG --> LG[Ledger entry per reel]
    LG --> TP[Lessons into topic files]
```

```mermaid
pie showData title 122 items collected in the first batch
    "Videos transcribed and studied" : 105
    "Image posts read in the browser" : 14
    "Not accessible" : 3
```

Limits: Whisper drops chunks of Hindi and Hinglish audio, so on-screen text and captions were the dependable source; image carousels
and login-gated reels need the browser.
