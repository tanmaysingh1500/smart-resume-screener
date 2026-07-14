export async function submitScreeningRequest(
    jobDescription: File[],
    resumes: File[]
  ) {
    const formData = new FormData();
  
    jobDescription.forEach(file => {
      formData.append("jobDescription", file);
    });
  
    resumes.forEach(file => {
      formData.append("resumes", file);
    });
  
    return fetch("http://localhost:8000/api/v1/screening", {
      method: "POST",
      body: formData,
    });
  }