<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg?v=2">
  <img alt="Denis Șeremet, Senior Frontend Developer and UI/UX Designer" src="./assets/hero-light.svg?v=2" width="100%">
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/label-about-dark.svg?v=2">
  <img alt="01 About" src="./assets/label-about-light.svg?v=2" width="100%">
</picture>

I design and build interfaces, usually both at once. At **Urchin Systems** I work on **Plextera**, a document-intelligence and automation platform: its studio, its document-insights tools, its forms and its OCR gateway.

Outside of that I'm building **[MovesFlow](https://movesflow.it)** end to end, from product design and the React front end to the Spring Boot API and the mobile app.

I care about three things: interfaces that *feel* fast, design systems that keep a product honest, and type-safe contracts between the UI and the API.

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/label-work-dark.svg?v=2">
  <img alt="02 Selected work" src="./assets/label-work-light.svg?v=2" width="100%">
</picture>

#### [movesflow.it](https://movesflow.it) — operations SaaS for moving companies

Requests, surveys, quotes, orders, crews, vehicles, payments and invoices in one system. It replaces the spreadsheets and WhatsApp threads moving companies run on today. It's a multi-tenant React + Spring Boot monorepo, rebuilt from scratch to replace the first Odoo version.

<a href="https://movesflow.it">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/movesflow-board-dark.svg?v=2">
  <img alt="Illustration of the MovesFlow dispatch board" src="./assets/movesflow-board-light.svg?v=2" width="100%">
</picture>
</a>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/movesflow-stats-dark.svg?v=2">
  <img alt="465 commits, 21 API modules, 280+ TSX files, 86 database migrations" src="./assets/movesflow-stats-light.svg?v=2" width="100%">
</picture>

**Front end** React 19, TypeScript, Vite, TanStack Router + Query, React Hook Form + Zod, MUI, i18next<br/>
**Back end** Java, Spring Boot (modular monolith), jOOQ, Flyway, PostgreSQL, WebSocket + STOMP chat<br/>
**Quality** Vitest, Testing Library, MSW, Playwright, JUnit, Testcontainers, OpenAPI-generated client

<details>
<summary><b>How it's put together</b></summary>
<br/>

```mermaid
flowchart LR
    subgraph web["apps/web · React SPA"]
      F[features/*] --> UI["@movesflow/ui<br/>design system"]
    end
    F -->|"generated TS client"| API
    subgraph api["apps/api · Spring Boot"]
      API[REST + STOMP] --> MOD["orders · scheduling · fleet · chat<br/>pricing · billing · accounting · surveys"]
    end
    MOD -->|jOOQ| DB[(PostgreSQL)]
    MOB[Expo mobile app] --> API
```

- **Contract-first.** The OpenAPI spec generates the TypeScript client, so UI and API types can't drift apart.
- **Layered modules.** Each backend module splits into `api / application / domain / infrastructure`.
- **One design system.** Shared components live in `packages/ui`, so features never build their own buttons.

</details>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/movesflow-ecosystem-dark.svg?v=2">
  <img alt="Around the platform: a mobile app for crews, the movesflow.it website, and the legacy Odoo v1" src="./assets/movesflow-ecosystem-light.svg?v=2" width="100%">
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/label-toolkit-dark.svg?v=2">
  <img alt="03 Toolkit" src="./assets/label-toolkit-light.svg?v=2" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/toolkit-dark.svg?v=2">
  <img alt="Toolkit: React, Next.js, Angular, Vue, TypeScript, Redux, TanStack Query, Zustand, Zod, MUI, Ant Design, Tailwind, SCSS, React Native, Expo, Spring Boot, Node.js, NestJS, PostgreSQL, MySQL, MongoDB, Vitest, Jest, Playwright, Figma, Photoshop, Illustrator, After Effects, Blender, Docker, Nginx, GitLab CI" src="./assets/toolkit-light.svg?v=2" width="100%">
</picture>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/label-contact-dark.svg?v=2">
  <img alt="04 Elsewhere" src="./assets/label-contact-light.svg?v=2" width="100%">
</picture>

**[movesflow.it](https://movesflow.it)** &nbsp;·&nbsp; **[LinkedIn](https://www.linkedin.com/in/%C8%99eremet-denis-530893250/)** &nbsp;·&nbsp; Open to talking about UI, design systems and product engineering.

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/footer-dark.svg?v=2">
  <img alt="" src="./assets/footer-light.svg?v=2" width="100%">
</picture>
