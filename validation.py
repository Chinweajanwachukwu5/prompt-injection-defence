from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def validate_output(task, tool_output, threshold=0.5):
    task_embedding = model.encode(task)

    # Split the output into sentences (simple split on full stops)
    sentences = [s.strip() for s in tool_output.split(".") if s.strip()]

    # If there are no real sentences, fall back to checking the whole output
    if not sentences:
        sentences = [tool_output]

    # Check each sentence against the task; track the lowest score
    lowest_score = 1.0
    for sentence in sentences:
        sentence_embedding = model.encode(sentence)
        score = util.cos_sim(task_embedding, sentence_embedding).item()
        if score < lowest_score:
            lowest_score = score

    # If ANY sentence drifts below the threshold, block the whole output
    if lowest_score >= threshold:
        return {"allowed": True, "score": lowest_score}
    else:
        return {"allowed": False, "score": lowest_score}