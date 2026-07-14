import { Button } from "@/components/ui/button";

export default function Hero() {
  return (
    <section className="mx-auto flex max-w-7xl flex-col items-center px-6 py-24 text-center">

      <span className="rounded-full border px-4 py-2 text-sm text-muted-foreground">
        AI Powered Resume Screening
      </span>

      <h1 className="mt-8 max-w-4xl text-5xl font-bold tracking-tight">
        Find the Best Candidates
        <br />
        in Minutes
      </h1>

      <p className="mt-6 max-w-2xl text-lg text-muted-foreground">
        Upload a job description and candidate resumes.
        Our AI analyzes every application,
        ranks candidates,
        and explains every recommendation.
      </p>

      <Button size="lg" className="mt-10">
        Start Screening
      </Button>

    </section>
  );
}