from typing import List

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.extractor.document_extractor import extract_text
from app.llm.structure import structure_documents
from app.embeddings.scorer import calculate_embedding_scores
from app.scoring.fusion import calculate_final_score

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/v1/screening")
async def screening(
    jobDescription: List[UploadFile] = File(...),
    resumes: List[UploadFile] = File(...),
):
    # Extract the Job Description once
    jd_text = await extract_text(jobDescription[0])

    results = []

    # Process every uploaded resume
    for resume in resumes:

        # Extract resume text
        resume_text = await extract_text(resume)

        # LLM: Structure + evaluate
        structured_result = structure_documents(
            job_description=jd_text,
            resume=resume_text,
        )

        # Embedding similarity
        embedding_scores = calculate_embedding_scores(
            structured_result
        )

        # Fusion score
        final_result = calculate_final_score(
            structured_result,
            embedding_scores,
        )
        print("\n" + "=" * 80)
        print(f"Candidate: {resume.filename}")
        print(f"Overall Score: {final_result['overall_score']}")
        print(f"Recommendation: {final_result['recommendation']}")
        print("=" * 80 + "\n")

        results.append(
            {
                "filename": resume.filename,
                "analysis": final_result,
            }
        )

    return {
        "status": "success",
        "candidate_count": len(results),
        "results": results,
    }