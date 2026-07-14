import Navbar from "./Navbar";
import Hero from "./Hero";
import UploadZone from "./UploadZone";
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { submitScreeningRequest } from "./parser"

function App() {
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleAnalyze = async () => {
    console.log("Job Description:", jobDescription);
    console.log("Resumes:", resumes);
    try {
      setIsSubmitting(true);

      const response = await submitScreeningRequest(jobDescription, resumes);

      const data = await response.json();

      console.log(data);
    } catch (error) {
      console.error("Failed to submit screening request:", error);
    }
      finally {
        setIsSubmitting(false);
      }
  };
  const [jobDescription, setJobDescription] = useState<File[]>([]);
  const [resumes, setResumes] = useState<File[]>([]);

  const canAnalyze =
    jobDescription.length === 1 && resumes.length >= 1;

  return (
    <div className="min-h-screen bg-background">
      <Navbar />
      <Hero />
      <UploadZone
        title="Job Description"
        description="Upload a single PDF job description."
        value={jobDescription}
        multiple={false}
        onChange={setJobDescription}
        accept={{
          "application/pdf": [".pdf"],
        }}
      />

    <UploadZone
      title="Candidate Resumes"
      description="Upload one or more resume PDFs."
      value={resumes}
      onChange={setResumes}
      accept={{
        "application/pdf": [".pdf"],
      }}
      multiple={true}
      maxFiles={20}
    />

    {canAnalyze && (
      <div className="mx-auto flex max-w-7xl justify-center px-6 pb-2">
        <Button size="lg" className="h-auto w-50 py-2" onClick={handleAnalyze} disabled={isSubmitting}>
        {isSubmitting ? "Analyzing..." : "Analyze Candidates"}
        </Button>
      </div>
    )}
    </div>
  );
}

export default App;