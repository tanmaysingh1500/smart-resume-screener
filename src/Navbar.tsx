import { BriefcaseBusiness } from "lucide-react";

export default function Navbar() {
  return (
    <header className="border-b">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <BriefcaseBusiness className="h-6 w-6" />
          <h1 className="text-lg font-semibold">
            AI Resume Screener
          </h1>
        </div>

        <p className="text-sm text-muted-foreground">
          Recruiter Dashboard
        </p>
      </div>
    </header>
  );
}