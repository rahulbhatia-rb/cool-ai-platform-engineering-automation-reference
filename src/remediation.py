from dataclasses import dataclass
@dataclass(frozen=True)
class Signal:
 service_owner:str; runbook_approved:bool; actionable:bool; reversible:bool
def recommend(s:Signal)->tuple[bool,tuple[str,...]]:
 r=[]
 if not s.service_owner.strip():r.append("service owner required")
 if not s.runbook_approved:r.append("approved runbook required")
 if not s.actionable:r.append("signal requires human triage")
 if not s.reversible:r.append("rollback path required")
 return (not r,tuple(r))
