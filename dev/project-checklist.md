# Project Scoping Checklist

Template for AI-Raadgivning client scoping. Use at kickoff and update as new needs are identified.

---

## 1. People & Access

<input type="checkbox" /> Who is the project manager / POC on each side? (Client and AI-Raadgivning)  
<input type="checkbox" /> Who are the end users of the product? (Roles, how many, technical level)  
<input type="checkbox" /> Who manages their IT? (Internal team, outsourced MSP, specific company/person)  
&nbsp;&nbsp;&nbsp;&nbsp;- Who has Azure/cloud admin access and can create resources?  
&nbsp;&nbsp;&nbsp;&nbsp;- What is their availability and response time?  
<input type="checkbox" /> What is the budget range? (Project fee + recurring cloud/API costs)  
<input type="checkbox" /> Where should things be hosted, and who pays for hosting/API costs?

## 2. Problem & Scope

<input type="checkbox" /> Problem statement (concise, actionable — what are we solving?)  
<input type="checkbox" /> Definition of done — be specific:  
&nbsp;&nbsp;&nbsp;&nbsp;- Where does the user access the solution?  
&nbsp;&nbsp;&nbsp;&nbsp;- What does it look like?  
&nbsp;&nbsp;&nbsp;&nbsp;- How do they interact with it?  
&nbsp;&nbsp;&nbsp;&nbsp;- What output do they get?  
&nbsp;&nbsp;&nbsp;&nbsp;- What does a successful interaction look like?  
<input type="checkbox" /> What is explicitly in scope?  
<input type="checkbox" /> What is explicitly out of scope? (Can be added later as add-ons, but not part of this engagement)  
<input type="checkbox" /> Agreed product name  

## 3. Delivery Channel

<input type="checkbox" /> **Web App** — standalone website  
&nbsp;&nbsp;&nbsp;&nbsp;- Public (external) or internal only? Or both with different access levels?  
&nbsp;&nbsp;&nbsp;&nbsp;- Where is it hosted? (Azure, Render, Vercel, client infra)  
&nbsp;&nbsp;&nbsp;&nbsp;- Authentication: Microsoft SSO (per-user login) or shared credentials?  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- If shared credentials: how do you handle offboarding (password rotation)?  
<input type="checkbox" /> **Microsoft Teams** — Teams bot/app  
&nbsp;&nbsp;&nbsp;&nbsp;- Does it live inside Teams?  
&nbsp;&nbsp;&nbsp;&nbsp;- Note: requires admin approval to deploy  
<input type="checkbox" /> **Copilot Agent** — Microsoft 365 Copilot plugin  
&nbsp;&nbsp;&nbsp;&nbsp;- Do they have Copilot licenses?  
&nbsp;&nbsp;&nbsp;&nbsp;- Do they have Copilot Studio?  
&nbsp;&nbsp;&nbsp;&nbsp;- If no Copilot licenses: a Teams app achieves similar functionality  
&nbsp;&nbsp;&nbsp;&nbsp;- If they already use Copilot daily: agent is the better experience  
<input type="checkbox" /> **Embedded widget** — inside existing app, website, or intranet  
&nbsp;&nbsp;&nbsp;&nbsp;- Where exactly? (SharePoint page, internal portal, public site)  
<input type="checkbox" /> Is it one of the above, or a combination of multiple?

## 4. Access & Users

<input type="checkbox" /> Access control: who has access? (Everyone, specific departments, specific roles)  
<input type="checkbox" /> Who is the testing group? How will testing commence?  
<input type="checkbox" /> Who is the final user group? (Few employees, a department, multiple teams)  
<input type="checkbox" /> Do users know how to prompt effectively? (If not, plan for training on how to get good results from a RAG chatbot)  
<input type="checkbox" /> Do they want analytics or feedback collection?  
&nbsp;&nbsp;&nbsp;&nbsp;- Usage stats, popular questions, chat history  
&nbsp;&nbsp;&nbsp;&nbsp;- Feedback mechanism on the bot (thumbs up/down, comments)  
&nbsp;&nbsp;&nbsp;&nbsp;- Collect feedback for a period then make updates based on it

## 5. Data & Documents (RAG Projects)

<input type="checkbox" /> File types and formats? (PDF, Word, scanned images, tables)  
<input type="checkbox" /> Is the data multimodal? (Text only, or does it include images/diagrams that the bot needs to understand?)  
<input type="checkbox" /> Where are the documents stored? (SharePoint, local drive, S3, other)  
<input type="checkbox" /> Volume: how many documents, how large?  
<input type="checkbox" /> Do documents need to be updated? How frequently?  
&nbsp;&nbsp;&nbsp;&nbsp;- Is there a naming convention? (Revision numbers, versioning)  
&nbsp;&nbsp;&nbsp;&nbsp;- Delay tolerance: how quickly do updates need to be reflected? (Real-time, same day, 24 hours)  
<input type="checkbox" /> Do they need visibility into what the bot is trained on? (Admin view of indexed documents)  
<input type="checkbox" /> Confidentiality levels:  
&nbsp;&nbsp;&nbsp;&nbsp;- Do different user groups have access to different parts of the bot? (Separate bots per group — more complex)  
&nbsp;&nbsp;&nbsp;&nbsp;- Or do different groups have access to different document folders? (Simpler — same bot, filtered data)

## 6. AI & Model

<input type="checkbox" /> Do they have a specific model in mind, or no preference?  
&nbsp;&nbsp;&nbsp;&nbsp;- Do they already have models hosted in Azure or elsewhere?  
&nbsp;&nbsp;&nbsp;&nbsp;- Do they have a ChatGPT business account or existing API keys?  
<input type="checkbox" /> Language, tone, and persona:  
&nbsp;&nbsp;&nbsp;&nbsp;- What language(s)? (Danish, English, both)  
&nbsp;&nbsp;&nbsp;&nbsp;- What tone of voice? (Formal, casual, technical)  
&nbsp;&nbsp;&nbsp;&nbsp;- What persona should the bot have?  
&nbsp;&nbsp;&nbsp;&nbsp;- Any topics it should or should not engage with?  
<input type="checkbox" /> Does it need to cite sources? In what way?  
&nbsp;&nbsp;&nbsp;&nbsp;- Just a document name?  
&nbsp;&nbsp;&nbsp;&nbsp;- A link to the actual document?  
&nbsp;&nbsp;&nbsp;&nbsp;- Show images inline, or link to them?  
&nbsp;&nbsp;&nbsp;&nbsp;- How important is image display vs text-only answers?

## 7. Infrastructure & Deployment

<input type="checkbox" /> What cloud provider and subscription do they have? (Azure, AWS, GCP — existing or new?)  
<input type="checkbox" /> Data residency requirements? (What region? How strict?)  
<input type="checkbox" /> Compliance requirements? (GDPR, ISO 27001, other legal/regulatory constraints)

## 8. Maintenance & Handover

<input type="checkbox" /> How does maintenance work? (Done after delivery, ongoing support, or shared responsibility?)  
<input type="checkbox" /> What documentation do they need? (User guide, admin guide, technical architecture map)  
<input type="checkbox" /> Do end users need training? (Walkthrough session, written guide, prompting training on how to get best results)  
<input type="checkbox" /> Production credentials and service accounts:  
&nbsp;&nbsp;&nbsp;&nbsp;- Set up under a shared/company account (not personal emails)  
&nbsp;&nbsp;&nbsp;&nbsp;- All API keys, hosting accounts, etc. tied to that account for clean handover  
<input type="checkbox" /> Escalation path: if something breaks, how do they contact us?

---

## Usage

1. Go through at **kickoff meeting** — skip sections that don't apply
2. Flag blockers immediately (especially People & Access items)
3. Share relevant sections with client IT before technical calls

---

## Usage

1. Go through at **kickoff meeting** — skip sections that don't apply
2. Flag blockers immediately (especially People & Access items)
3. Share relevant sections with client IT before technical calls
