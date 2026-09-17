# Platform Automation & Remediation Reference

Application reference for the Uplers / Cool AI Senior Platform Engineer role. It demonstrates a safe automation primitive for infrastructure operations: turn an observable signal into a proposed remediation, but require explicit safety conditions before execution.

## Design

`recommend()` models a golden path for agent-assisted operations. A remediation is eligible only when the service has an owner, the runbook is approved, the signal is actionable, and the change is reversible. This keeps AI-assisted monitoring and remediation accountable rather than allowing opaque, unrestricted automation.

The component is deliberately dependency-free and tested. In production it would consume Prometheus/Datadog alerts, look up Terraform/Ansible/Helm change evidence, open an auditable GitOps change, and attach traces and rollback instructions.

```bash
python3 -m unittest discover -s tests -v
```

## Role alignment

- Terraform, Ansible, Helm and Kubernetes-ready remediation policy
- observability-first automation and operator-safe guardrails
- a natural bridge to agentic RCA, internal APIs/CLIs, and self-service platforms
- explicit rollback and ownership requirements

## Scope

Personal demonstration only; it does not claim access to Uplers or Cool AI systems. It is informed by my AWS-hosted GenAI/RAG deployment and infrastructure automation work.

[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
